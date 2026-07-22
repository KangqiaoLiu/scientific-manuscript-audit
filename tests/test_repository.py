from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RepositoryTests(unittest.TestCase):
    def test_skill_frontmatter(self) -> None:
        text = (ROOT / "skills/scientific-manuscript-audit/SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        self.assertIn("name: scientific-manuscript-audit", text)
        self.assertIn("description:", text)

    def test_trigger_count_and_labels(self) -> None:
        rows = [json.loads(line) for line in (ROOT / "evals/trigger_cases.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual(60, len(rows))
        self.assertEqual(40, sum(row["label"] == "trigger" for row in rows))
        self.assertEqual(20, sum(row["label"] == "no_trigger" for row in rows))

    def test_synthetic_counts(self) -> None:
        rows = [json.loads(line) for line in (ROOT / "evals/synthetic_cases.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual(12, len(rows))
        self.assertTrue(all(row["defects"] for row in rows))
        composite = [json.loads(path.read_text(encoding="utf-8")) for path in sorted((ROOT / "evals/composite").glob("*.json"))]
        self.assertEqual(6, len(composite))
        self.assertTrue(all(3 <= len(row["defects"]) <= 6 for row in composite))
        self.assertTrue(all(1 <= len(row["decoys"]) <= 3 for row in composite))
        for row in composite:
            word_count = len(row["manuscript"].split())
            self.assertGreaterEqual(word_count, 380)
            self.assertLessEqual(word_count, 900)

    def test_distributions_match(self) -> None:
        canonical = ROOT / "skills/scientific-manuscript-audit"
        for host in ("codex", "claude-code"):
            target = ROOT / "dist" / host / "scientific-manuscript-audit"
            for name in ("SKILL.md", "TESTS.md"):
                self.assertEqual(
                    (canonical / name).read_bytes(),
                    (target / name).read_bytes(),
                )

    def test_no_macos_artifacts(self) -> None:
        bad = []
        for path in ROOT.rglob("*"):
            rel = path.relative_to(ROOT)
            if "__MACOSX" in rel.parts or path.name == ".DS_Store" or path.name.startswith("._"):
                bad.append(str(rel))
        self.assertEqual([], bad)

    def test_workflow_is_hardened(self) -> None:
        text = (ROOT / ".github/workflows/validate.yml").read_text(encoding="utf-8")
        self.assertIn("permissions:\n  contents: read", text)
        self.assertIn("persist-credentials: false", text)
        self.assertIn("timeout-minutes:", text)
        self.assertIn("cancel-in-progress: true", text)
        refs = re.findall(r"^\s*-\s+uses:\s+([^#\s]+)", text, flags=re.MULTILINE)
        self.assertTrue(refs)
        for action_ref in refs:
            if action_ref.startswith("./"):
                continue
            self.assertIn("@", action_ref)
            self.assertRegex(action_ref.rsplit("@", 1)[1], r"^[0-9a-f]{40}$")

    def test_repository_protection_files(self) -> None:
        for path in (
            ".github/CODEOWNERS",
            ".github/dependabot.yml",
            "SECURITY.md",
            "RESPONSIBLE_USE.md",
            "TRADEMARKS.md",
        ):
            self.assertTrue((ROOT / path).is_file(), path)
        pr_template = (ROOT / ".github/pull_request_template.md").read_text(encoding="utf-8")
        self.assertIn("I have the right to submit", pr_template)
        self.assertIn("submitted under the Apache License 2.0", pr_template)


if __name__ == "__main__":
    unittest.main()
