#!/usr/bin/env python3
"""Deterministically recommend a VCOS model tier and token envelope."""

from __future__ import annotations

import argparse
import json


def nonnegative(value: str) -> int:
    parsed = int(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError("must be nonnegative")
    return parsed


def positive(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be positive")
    return parsed


PRICES = {
    "gpt-5.6-sol": {"input": 5.0, "output": 30.0},
    "gpt-5.6-terra": {"input": 2.5, "output": 15.0},
    "gpt-5.6-luna": {"input": 1.0, "output": 6.0},
}

ROLE_DEFAULTS = {
    "curator": ("gpt-5.6-luna", "low", 12000, 1500),
    "architect": ("gpt-5.6-terra", "medium", 24000, 4000),
    "core-builder": ("gpt-5.6-terra", "medium", 36000, 7000),
    "production-builder": ("gpt-5.6-terra", "medium", 40000, 7000),
    "qa-runner": ("gpt-5.6-luna", "low", 16000, 1800),
    "evidence": ("gpt-5.6-luna", "low", 12000, 1500),
    "semantic-skeptic": ("gpt-5.6-terra", "medium", 24000, 3500),
    "final-judge": ("gpt-5.6-terra", "medium", 16000, 2200),
    "documenter": ("gpt-5.6-luna", "low", 16000, 2200),
}


def choose(args: argparse.Namespace) -> dict:
    risk = args.consequence + args.ambiguity + args.novelty + args.quality_leverage + args.verification_difficulty
    model, effort, input_budget, output_budget = ROLE_DEFAULTS[args.role]
    reasons: list[str] = []

    if args.role in {"architect", "core-builder"} and args.quality == "flagship":
        model, effort = "gpt-5.6-sol", "high"
        reasons.append("flagship quality kernel")
    elif args.role == "final-judge" and (args.quality == "flagship" or risk >= 8):
        model, effort = "gpt-5.6-sol", "high"
        reasons.append("flagship or high-risk final judgment")

    if risk >= 8 and args.role in {"architect", "core-builder", "final-judge"}:
        model, effort = "gpt-5.6-sol", "high"
        reasons.append("risk score >= 8")
    elif risk >= 4 and model == "gpt-5.6-luna" and args.role not in {"curator", "qa-runner", "evidence", "documenter"}:
        model, effort = "gpt-5.6-terra", "medium"
        reasons.append("semantic judgment requires Terra")

    if args.ambiguity == 2 and risk >= 8 and args.role in {"architect", "core-builder", "final-judge"}:
        model, effort = "gpt-5.6-sol", "high"
        reasons.append("high ambiguity in quality-defining role")

    if args.quality == "economy" and args.role in {"production-builder", "core-builder"} and risk <= 3:
        model, effort = "gpt-5.6-luna", "low"
        reasons.append("economy mode and reversible low-risk work")

    if not args.reversible and model == "gpt-5.6-luna" and args.role not in {"curator", "evidence", "documenter"}:
        model, effort = "gpt-5.6-terra", "medium"
        reasons.append("irreversible work cannot rely on Luna judgment")

    if model == "gpt-5.6-sol" and args.sol_calls_used >= args.max_sol_calls:
        raise SystemExit("Sol routing required but max-sol-calls is exhausted; stop for approval or change quality mode")

    input_tokens = args.input_tokens if args.input_tokens is not None else input_budget
    output_tokens = args.output_tokens if args.output_tokens is not None else output_budget
    price = PRICES[model]
    estimated_cost = input_tokens / 1_000_000 * price["input"] + output_tokens / 1_000_000 * price["output"]

    return {
        "role": args.role,
        "quality": args.quality,
        "risk_score": risk,
        "risk_components": {
            "consequence": args.consequence,
            "ambiguity": args.ambiguity,
            "novelty": args.novelty,
            "quality_leverage": args.quality_leverage,
            "verification_difficulty": args.verification_difficulty,
        },
        "recommended_model": model,
        "reasoning_effort": effort,
        "input_budget": input_tokens,
        "output_budget": output_tokens,
        "estimated_cost_usd_at_budget": round(estimated_cost, 4),
        "routing_claim": "recommendation_only_unless_runtime_enforces_model",
        "reasons": reasons or ["role default"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--role", choices=sorted(ROLE_DEFAULTS), required=True)
    parser.add_argument("--quality", choices=["flagship", "balanced", "economy"], default="balanced")
    parser.add_argument("--consequence", type=int, choices=range(0, 3), default=1)
    parser.add_argument("--ambiguity", type=int, choices=range(0, 3), default=1)
    parser.add_argument("--novelty", type=int, choices=range(0, 3), default=1)
    parser.add_argument("--quality-leverage", type=int, choices=range(0, 3), default=1)
    parser.add_argument("--verification-difficulty", type=int, choices=range(0, 3), default=1)
    parser.add_argument("--max-sol-calls", type=nonnegative, default=1)
    parser.add_argument("--sol-calls-used", type=nonnegative, default=0)
    parser.add_argument("--reversible", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--input-tokens", type=positive)
    parser.add_argument("--output-tokens", type=positive)
    args = parser.parse_args()
    print(json.dumps(choose(args), indent=2))


if __name__ == "__main__":
    main()
