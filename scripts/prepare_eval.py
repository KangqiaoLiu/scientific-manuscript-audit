#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUITES = {
    "atomic": ROOT / "evals" / "synthetic_cases.jsonl",
    "composite": ROOT / "evals" / "composite",
}


def load_cases(path: Path) -> list[dict]:
    if path.is_dir():
        return [json.loads(item.read_text(encoding="utf-8")) for item in sorted(path.glob("*.json"))]
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Export synthetic audit prompts for a model run.")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--suite", choices=("atomic", "composite", "all"), default="all")
    args = parser.parse_args()
    suite_names = tuple(SUITES) if args.suite == "all" else (args.suite,)
    args.output.mkdir(parents=True, exist_ok=True)
    count = 0
    for suite_name in suite_names:
        for case in load_cases(SUITES[suite_name]):
            prompt = (
                "Use a rigorous referee-style manuscript audit. Identify decision-relevant defects, "
                "classify severity, preserve valid sub-results, give bounded resolutions, and provide "
                "an advisory recommendation.\n\n"
                f"Title: {case['title']}\n"
                f"Advertised claim: {case['advertised_claim']}\n\n"
                f"Manuscript material:\n{case['manuscript']}\n"
            )
            (args.output / f"{suite_name}_{case['id']}.txt").write_text(prompt, encoding="utf-8")
            count += 1
    print(f"wrote {count} prompts to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
