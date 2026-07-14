#!/usr/bin/env python3
"""Enforce the three-pair promotion gate for the experimental skill."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: evaluate_benchmark.py MANIFEST.json")
    manifest = json.loads(Path(sys.argv[1]).read_text())
    pairs = manifest.get("pairs", [])
    if len(pairs) < 3:
        raise SystemExit("benchmark requires at least three representative pair results")
    quality_pairs = [p for p in pairs if p.get("quality_parity_pass") is True]
    efficient_pairs = [p for p in pairs if p.get("efficiency_pass") is True]
    task_types = {p.get("task_type") for p in pairs}
    required_types = {"small", "medium", "flagship"}
    result = {
        "pairs_total": len(pairs),
        "quality_pairs_passed": len(quality_pairs),
        "efficiency_pairs_passed": len(efficient_pairs),
        "representative_task_types_present": required_types.issubset(task_types),
        "promotion_eligible": len(quality_pairs) == len(pairs) and len(efficient_pairs) >= 2 and required_types.issubset(task_types),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
