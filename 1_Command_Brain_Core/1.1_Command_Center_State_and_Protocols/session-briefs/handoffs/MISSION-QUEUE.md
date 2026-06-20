# Mission Queue — L2 NeuralSync Intern

**Updated:** 2026-06-20  
**Poll:** Read this file + `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/mission-control/state.json` before every L2 session.

## Active mission

| ID | Branch | Handoff |
| --- | --- | --- |
| `gsd-dual-terminal-eval` | `l2/gsd-dual-terminal-eval-2026-06-20` | `HANDOFFS/l1-gsd-dual-terminal-eval-2026-06-20.md` |

**Next actor:** Hermes — E5 confirm + E6/E7 check. Poll `MC/gsd-dual-terminal-eval/grok-inbox.md`.

## Completed

| ID | Branch | Merged |
| --- | --- | --- |
| `week1-git-collab-test` | `l2/collab-test-2026-06-20` | 2026-06-20 → `main` @ `3155d04` |

## Queue (awaiting L1 assignment)

| # | Mission | Status |
| --- | --- | --- |
| 2 | VCOS HQ hygiene: verify all `mission-control/` files present | pending |
| 3 | Read `dual-hermes-collaboration-protocol.md`; confirm workdir path | pending |

## Idle rule

If `state.json` → `cubicle_l2.active_mission` is `null` and no mission is promoted above, report idle on Telegram. Do not invent greenfield work.