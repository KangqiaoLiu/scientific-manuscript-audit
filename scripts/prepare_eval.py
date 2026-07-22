#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Export synthetic audit prompts for a model run.")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cases = load_jsonl(ROOT / "evals" / "synthetic_cases.jsonl")
    args.output.mkdir(parents=True, exist_ok=True)
    for case in cases:
        prompt = (
            "Use a rigorous referee-style manuscript audit. Identify decision-relevant defects, "
            "classify severity, give bounded resolutions, and provide an advisory recommendation.\n\n"
            f"Title: {case['title']}\n"
            f"Advertised claim: {case['advertised_claim']}\n\n"
            f"Manuscript material:\n{case['manuscript']}\n"
        )
        (args.output / f"{case['id']}.txt").write_text(prompt, encoding="utf-8")
    print(f"wrote {len(cases)} prompts to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
