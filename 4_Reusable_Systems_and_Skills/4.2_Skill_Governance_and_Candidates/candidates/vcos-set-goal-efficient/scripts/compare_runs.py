#!/usr/bin/env python3
"""Compare control and efficient run metrics without inventing quality scores."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path


def load(path: str) -> dict:
    return json.loads(Path(path).read_text())


def proxy(run: dict) -> int:
    derived = math.ceil((int(run.get("prompt_chars", 0)) + int(run.get("output_chars", 0))) / 4)
    recorded = run.get("token_proxy")
    if recorded is None:
        return derived
    if int(recorded) != derived:
        raise ValueError(f"token_proxy {recorded} does not match character-derived value {derived}")
    return int(recorded)


def quality_pass(run: dict) -> bool:
    total = int(run.get("machine_checks_total", 0))
    passed = int(run.get("machine_checks_passed", 0))
    return (
        run.get("final_verdict") in {"pass", "complete", "pass_with_non_blocking_findings"}
        and int(run.get("critical_findings", 0)) == 0
        and int(run.get("major_findings", 0)) == 0
        and total > 0
        and passed == total
        and int(run.get("done_truths_total", 0)) >= 3
        and int(run.get("done_truths_passed", 0)) == int(run.get("done_truths_total", 0))
        and run.get("independent_skeptic_complete") is True
        and run.get("binder_ready") is True
        and run.get("ownership_reconciled") is True
        and run.get("approval_gates_satisfied") is True
        and run.get("council_gate_satisfied") is True
    )


def main() -> None:
    if len(sys.argv) != 4:
        raise SystemExit("usage: compare_runs.py CONTROL.json EFFICIENT.json PAIR_REVIEW.json")
    control, efficient = load(sys.argv[1]), load(sys.argv[2])
    pair_review = load(sys.argv[3])
    control_proxy, efficient_proxy = proxy(control), proxy(efficient)
    reduction = 0.0 if control_proxy == 0 else (control_proxy - efficient_proxy) / control_proxy * 100
    preference = pair_review.get("blind_reviewer_preference")
    quality_parity_pass = quality_pass(control) and quality_pass(efficient) and pair_review.get("isolation_confirmed") is True and preference in {"tie", "efficient"}
    efficiency_pass = reduction >= 25
    pair_eligible = quality_parity_pass and efficiency_pass
    result = {
        "control": {"skill": control.get("skill"), "token_proxy": control_proxy, "quality_pass": quality_pass(control)},
        "efficient": {"skill": efficient.get("skill"), "token_proxy": efficient_proxy, "quality_pass": quality_pass(efficient)},
        "token_proxy_reduction_percent": round(reduction, 2),
        "blind_reviewer_preference": preference,
        "quality_parity_pass": quality_parity_pass,
        "efficiency_pass": efficiency_pass,
        "pair_eligible": pair_eligible,
        "promotion_eligible": False,
        "promotion_note": "One pair cannot qualify a skill; aggregate at least three representative pairs.",
        "warning": "Token proxy is ceil(characters/4), not provider usage or billing data.",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
