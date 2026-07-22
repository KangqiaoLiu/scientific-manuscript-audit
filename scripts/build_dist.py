#!/usr/bin/env python3
from __future__ import annotations

import argparse
import filecmp
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "scientific-manuscript-audit"
TARGETS = [
    ROOT / "dist" / "codex" / "scientific-manuscript-audit",
    ROOT / "dist" / "claude-code" / "scientific-manuscript-audit",
]
FILES = ["SKILL.md", "TESTS.md"]


def sync() -> None:
    for target in TARGETS:
        target.mkdir(parents=True, exist_ok=True)
        for name in FILES:
            shutil.copy2(SOURCE / name, target / name)


def check() -> bool:
    ok = True
    for target in TARGETS:
        for name in FILES:
            src = SOURCE / name
            dst = target / name
            if not dst.exists() or not filecmp.cmp(src, dst, shallow=False):
                print(f"out of sync: {dst.relative_to(ROOT)}")
                ok = False
    return ok


def main() -> int:
    parser = argparse.ArgumentParser(description="Build or check generated host distributions.")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        return 0 if check() else 1
    sync()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
