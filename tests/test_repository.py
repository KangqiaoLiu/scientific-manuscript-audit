from __future__ import annotations

import json
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

    def test_synthetic_count(self) -> None:
        rows = [json.loads(line) for line in (ROOT / "evals/synthetic_cases.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual(12, len(rows))
        self.assertTrue(all(row["defects"] for row in rows))

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


if __name__ == "__main__":
    unittest.main()
