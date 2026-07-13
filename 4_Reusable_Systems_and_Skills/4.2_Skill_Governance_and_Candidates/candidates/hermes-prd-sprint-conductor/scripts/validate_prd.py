#!/usr/bin/env python3
"""Fail closed on structurally incomplete VCOS PRDs."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_HEADINGS = [
    "Executive Summary",
    "User and Problem Evidence",
    "Current State",
    "Desired Outcome and Success Metrics",
    "Scope",
    "User Journeys",
    "Functional Requirements",
    "Non-Functional Requirements",
    "Data, Interfaces, and Architecture",
    "Security and Approval Gates",
    "Failure Modes and Recovery",
    "Acceptance Criteria",
    "Test Plan",
    "Rollout and Rollback",
    "Delivery Phases",
    "Open Decisions",
    "Definition of Done",
]

PLACEHOLDER_PATTERNS = [
    r"<[^>]+>",
    r"\bTBD\b",
    r"\bTODO\b",
    r"to be filled",
    r"YYYY-MM-DD",
]


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_prd.py <prd.md>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"FAIL: file not found: {path}")
        return 2

    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    headings = set(re.findall(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE))
    for heading in REQUIRED_HEADINGS:
        if heading not in headings:
            errors.append(f"missing heading: ## {heading}")

    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            errors.append(f"unresolved placeholder matching: {pattern}")

    acceptance_checks = re.findall(r"^- \[ \] AC-\d+:\s*\S.+$", text, flags=re.MULTILINE)
    if len(acceptance_checks) < 3:
        errors.append("need at least three concrete unchecked AC-N criteria")

    done_checks = re.findall(r"^- \[ \]\s+.+$", text, flags=re.MULTILINE)
    if len(done_checks) < 6:
        errors.append("need acceptance criteria plus a concrete definition-of-done checklist")

    if "```bash" not in text:
        errors.append("test plan must include an exact bash command block")

    if len(text.split()) < 500:
        errors.append("PRD is too thin: fewer than 500 words")

    if not text.endswith("\n"):
        errors.append("file must end with a newline")

    if errors:
        print(f"FAIL: {path}")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PASS: {path}")
    print(f"- required headings: {len(REQUIRED_HEADINGS)}")
    print(f"- acceptance criteria: {len(acceptance_checks)}")
    print(f"- checklist items: {len(done_checks)}")
    print(f"- words: {len(text.split())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
