# Evidence Ledger

| Truth | Claim | Artifact | Reviewer action | Machine check | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | L2 diagnostic is complete and truthful | `artifacts/TRANSPORT-DIAGNOSTIC-V2.md` | open | required fields present | PASS |
| 2 | fix is evidence-gated | `dispatches/HERMES-GCM-DIRECT-HELPER-TEST.md` | inspect | direct helper test pending | UNKNOWN |
| 3 | remote branch matches commit | remote GitHub ref | run | `git ls-remote` | FAIL |
| 4 | draft review surface exists | PR/comparison URL | open | URL pending | FAIL |
| 5 | next mission is fully bounded and not activated | `NEXT-MISSION-DRAFT.md` | open | one allowed file and exact validation contract | PASS |
