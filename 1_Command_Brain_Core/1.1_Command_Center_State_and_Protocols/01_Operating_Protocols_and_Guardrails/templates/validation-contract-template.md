# Validation Contract Template (HQ Master)

Write this before implementation or before a cron's first run. Correctness must be defined independently of the output that will be produced. Downstream copy: VCOS Employee `1_Employee_OS_Core/1.3_Mission_Operations_Library/1.3.2_Mission_Lifecycle_Templates/validation-contract-template.md`.

## Mission / Loop

- Mission or cron name:
- Owner / Sentinel:
- Worker (role + Hermes profile or session):
- Validator (Skeptic):
- Approval surface:
- Ceiling (L0 / L500 / L1000):
- Human approval required before:

## Goal

- Requested outcome:
- Audience or user:
- In scope:
- Out of scope:
- Constraints:

## Assertions

| ID | Assertion | Feature/Milestone | Validation Method | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| A1 |  |  | Scrutiny / User Testing / Human Review |  | Not Started |
| A2 |  |  | Scrutiny / User Testing / Human Review |  | Not Started |
| A3 |  |  | Scrutiny / User Testing / Human Review |  | Not Started |

For recurring loops, include at minimum: output lands in the owned path, format matches the handoff packet, sources are linked, no approval-gated action was taken, and ceiling was not exceeded.

## Scrutiny Validation

- Tests to run:
- Lint/typecheck/build commands:
- Static review focus:
- Spec coverage checks:

## User Testing Validation

- Live workflow to exercise:
- Viewports/devices:
- Forms/buttons/navigation:
- Error states:
- Data persistence or side effects:

## Acceptance

A milestone or loop cycle can close only when:

- All assigned assertions pass, or blockers are logged.
- Worker handoff is complete.
- Validator report is complete.
- Sentinel has scoped corrective work for failed assertions.
- Human approval is recorded when required.
