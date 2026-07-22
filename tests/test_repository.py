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
        allowed = {"actions/checkout", "actions/setup-python"}
        for action_ref in refs:
            if action_ref.startswith("./"):
                continue
            self.assertIn("@", action_ref)
            action, ref = action_ref.rsplit("@", 1)
            self.assertIn(action, allowed)
            self.assertRegex(ref, r"^[0-9a-f]{40}$")

    def test_repository_protection_files(self) -> None:
        for path in (
            ".github/CODEOWNERS",
            ".github/dependabot.yml",
            "SECURITY.md",
            "RESPONSIBLE_USE.md",
            "TRADEMARKS.md",
            "docs/RELEASE_PROCESS.md",
        ):
            self.assertTrue((ROOT / path).is_file(), path)
        pr_template = (ROOT / ".github/pull_request_template.md").read_text(encoding="utf-8")
        self.assertIn("I have the right to submit", pr_template)
        self.assertIn("submitted under the Apache License 2.0", pr_template)

    def test_version_and_plugin_metadata_are_aligned(self) -> None:
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        entry = marketplace["plugins"][0]

        self.assertEqual("https://json.schemastore.org/claude-code-plugin-manifest.json", plugin["$schema"])
        self.assertEqual(version, plugin["version"])
        self.assertEqual(version, marketplace["version"])
        self.assertEqual(version, entry["version"])
        self.assertEqual("./", entry["source"])
        self.assertIs(entry["strict"], True)
        self.assertNotIn("skills", plugin)
        self.assertNotIn("skills", entry)

        badge_version = "v" + version.replace("-", "--")
        for readme in ("README.md", "README.zh-CN.md", "README.ja.md"):
            text = (ROOT / readme).read_text(encoding="utf-8")
            self.assertIn(badge_version, text)
            self.assertIn("/reload-plugins", text)

    def test_markdown_links_resolve(self) -> None:
        link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
        broken = []
        for path in ROOT.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            for target in link_pattern.findall(text):
                target = target.strip().split("#", 1)[0]
                if not target or target.startswith(("http://", "https://", "mailto:")):
                    continue
                resolved = (path.parent / target).resolve()
                try:
                    resolved.relative_to(ROOT.resolve())
                except ValueError:
                    broken.append(f"{path.relative_to(ROOT)} -> {target}")
                    continue
                if not resolved.exists():
                    broken.append(f"{path.relative_to(ROOT)} -> {target}")
        self.assertEqual([], broken)


if __name__ == "__main__":
    unittest.main()
