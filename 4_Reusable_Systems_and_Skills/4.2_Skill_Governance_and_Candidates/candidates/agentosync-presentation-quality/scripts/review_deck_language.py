#!/usr/bin/env python3
"""Scan AgentOSync deck source/text for client-facing language red flags."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys


BANNED = {
    "positioning": "Use a client-facing claim instead.",
    "sales framing": "Remove internal salesperson coaching labels.",
    "wow moment": "Use professional workflow language.",
    "recommended close": "Final slide must be a client decision path.",
    "close on": "Avoid salesperson close language.",
    "pitch": "Use walkthrough, validation, or client discussion.",
    "conversion": "Avoid unsupported sales-outcome framing.",
    "no-brainer": "Use plain next-step language.",
}


def iter_files(paths: list[Path]) -> list[Path]:
    out: list[Path] = []
    for path in paths:
        if path.is_dir():
            out.extend(p for p in path.rglob("*") if p.is_file() and p.suffix.lower() in {".md", ".txt", ".mjs", ".js", ".jsx", ".ts", ".tsx", ".json"})
        elif path.is_file():
            out.append(path)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="Deck source, extracted text, or folders to scan")
    args = parser.parse_args()

    hits: list[str] = []
    for path in iter_files(args.paths):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError as exc:
            hits.append(f"{path}: unable to read: {exc}")
            continue
        for phrase, guidance in BANNED.items():
            pattern = re.compile(rf"\b{re.escape(phrase)}\b", re.IGNORECASE)
            for match in pattern.finditer(text):
                line_no = text.count("\n", 0, match.start()) + 1
                hits.append(f"{path}:{line_no}: banned phrase '{match.group(0)}' - {guidance}")

    if hits:
        print("\n".join(hits))
        return 1
    print("AgentOSync language review passed: no banned client-facing phrases found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
