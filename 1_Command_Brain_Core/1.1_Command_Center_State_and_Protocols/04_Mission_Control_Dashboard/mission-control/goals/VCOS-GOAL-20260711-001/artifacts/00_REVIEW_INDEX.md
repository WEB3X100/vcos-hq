# Review Index — VCOS-GOAL-20260711-001

## Verdict

Status: active  
Judge call: RESHAPE  
Confidence: high

## What changed

- Converted an ambiguous transport retry into five gated steps.
- Added a read-only Git Bash diagnostic.
- Added exact remote SHA and draft-review acceptance checks.
- Prepared the next mission as a draft without activating it.

## How to review in five minutes

| Step | Open or run | What good looks like |
| --- | --- | --- |
| 1 | `dispatches/HERMES-NEXT-5-STEPS.md` | no destructive or unauthorized actions |
| 2 | `artifacts/transport-diagnostic-git-bash.sh` | read-only tests; no push/config writes |
| 3 | L2 diagnostic result | every field populated from evidence |
| 4 | remote readback | remote SHA equals local `bd3bf12` full SHA |
| 5 | PR/comparison URL | L1 can inspect actual diff |

## Important risks

- L2 may not have this goal packet until the stabilization branch is available.
- SSH port 22 may be blocked while HTTPS remains healthy.
- Any authentication change requires human approval.

## Cheapest next test

Run the read-only diagnostic on L2 and return `TRANSPORT_DIAGNOSTIC_V2`.

