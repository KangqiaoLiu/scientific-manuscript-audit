#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_NAMES = {".DS_Store", "Thumbs.db"}
FORBIDDEN_PARTS = {"__MACOSX", ".idea", ".vscode", ".pytest_cache", "__pycache__"}
TEXT_SUFFIXES = {".md", ".txt", ".json", ".jsonl", ".yml", ".yaml", ".py", ".cff"}
SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]
LOCAL_PATH_PATTERNS = [
    re.compile(r"/Users/[A-Za-z0-9._-]+/"),
    re.compile(r"/home/[A-Za-z0-9._-]+/"),
    re.compile(r"[A-Za-z]:\\Users\\[A-Za-z0-9._-]+\\"),
]
EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def validate_paths() -> None:
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if path.name in FORBIDDEN_NAMES or path.name.startswith("._"):
            fail(f"forbidden artifact: {rel}")
        if any(part in FORBIDDEN_PARTS for part in rel.parts):
            fail(f"forbidden directory: {rel}")


def validate_text() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(f"possible secret in {path.relative_to(ROOT)}")
        for pattern in LOCAL_PATH_PATTERNS:
            if pattern.search(text):
                fail(f"local user path in {path.relative_to(ROOT)}")
        if EMAIL_PATTERN.search(text):
            fail(f"email address in {path.relative_to(ROOT)}")


def validate_skill() -> None:
    path = ROOT / "skills" / "scientific-manuscript-audit" / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md lacks YAML frontmatter")
    if "name: scientific-manuscript-audit" not in text:
        fail("SKILL.md name mismatch")
    if "description:" not in text:
        fail("SKILL.md lacks description")


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            fail(f"invalid JSONL at {path.relative_to(ROOT)}:{line_no}: {exc}")
    return rows


def validate_evals() -> None:
    triggers = load_jsonl(ROOT / "evals" / "trigger_cases.jsonl")
    synthetic = load_jsonl(ROOT / "evals" / "synthetic_cases.jsonl")
    composite = [json.loads(path.read_text(encoding="utf-8")) for path in sorted((ROOT / "evals" / "composite").glob("*.json"))]
    if len(triggers) != 60:
        fail(f"expected 60 trigger cases, found {len(triggers)}")
    if len(synthetic) != 12:
        fail(f"expected 12 atomic synthetic cases, found {len(synthetic)}")
    if len(composite) != 6:
        fail(f"expected 6 composite synthetic cases, found {len(composite)}")
    ids = [row["id"] for row in triggers + synthetic + composite]
    if len(ids) != len(set(ids)):
        fail("duplicate evaluation case id")
    labels = {row["label"] for row in triggers}
    if labels != {"trigger", "no_trigger"}:
        fail(f"unexpected trigger labels: {labels}")
    allowed_severities = {"fatal", "major-blocking", "major-fixable", "minor"}
    for case in synthetic + composite:
        required = {"id", "domain", "title", "advertised_claim", "manuscript", "defects", "expected_recommendation"}
        missing = required - set(case)
        if missing:
            fail(f"synthetic case {case.get('id', '<unknown>')} lacks fields: {sorted(missing)}")
        if not case.get("defects"):
            fail(f"synthetic case lacks defects: {case['id']}")
        defect_ids = [defect.get("id") for defect in case["defects"]]
        if len(defect_ids) != len(set(defect_ids)):
            fail(f"duplicate defect id in {case['id']}")
        for defect in case["defects"]:
            if set(defect) != {"id", "type", "severity", "expected"}:
                fail(f"invalid defect schema in {case['id']}: {defect.get('id')}")
            if defect["severity"] not in allowed_severities:
                fail(f"invalid severity in {case['id']}: {defect['severity']}")
        if case in composite:
            word_count = len(re.findall(r"\b\w+[\w'-]*\b", case["manuscript"]))
            if not 380 <= word_count <= 900:
                fail(f"composite case {case['id']} has {word_count} words; expected 380-900")
            if not 3 <= len(case["defects"]) <= 6:
                fail(f"composite case {case['id']} must contain 3-6 defects")
            if not 1 <= len(case.get("decoys", [])) <= 3:
                fail(f"composite case {case['id']} must contain 1-3 decoys")
            unsafe_markers = ("http://", "https://", "doi:", "arxiv:", "\\cite{", "@")
            lower_text = (case["manuscript"] + " " + case["advertised_claim"]).lower()
            if any(marker in lower_text for marker in unsafe_markers):
                fail(f"composite case contains source-identifying marker: {case['id']}")


def validate_dist() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_dist.py"), "--check"],
        cwd=ROOT,
        check=False,
    )
    if result.returncode:
        fail("generated distributions are out of sync")


def main() -> int:
    validate_paths()
    validate_text()
    validate_skill()
    validate_evals()
    validate_dist()
    print("repository validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
