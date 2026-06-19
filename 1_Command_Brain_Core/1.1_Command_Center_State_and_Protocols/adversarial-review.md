# Adversarial Review Protocol

Purpose: prevent optimistic agent outputs from reaching humans or clients without scrutiny.

## When Required

Run adversarial review before:

- Gate 3 Human Approval
- Client-facing delivery
- Domain implementation submission
- Production-sensitive changes
- CRM mutations
- External communications automation
- Large architecture changes

## Review Stack

Use the strongest available option:

1. Codex adversarial review
2. Claude `/review`
3. Claude `/ultra review` for major architecture, security, database, auth, payments, or irreversible workflow changes
4. Manual Skeptic sub-agent review when tool-specific review is unavailable

## Reviewer Mandate

The reviewer must attack:

- Logic gaps
- Edge cases
- Security/privacy risks
- Brand/taste risks
- Approval gate bypasses
- Missing rollback paths
- Data mutation mistakes
- Overpromising to clients

## If Review Finds A Problem

1. Builder fixes the problem.
2. Sentinel logs root cause in `1_Command_Brain_Core/1.2_Headquarters_Memory/decisions.md`.
3. Relevant domain README gets a new prevention rule.
4. Reviewer re-checks before human approval.

