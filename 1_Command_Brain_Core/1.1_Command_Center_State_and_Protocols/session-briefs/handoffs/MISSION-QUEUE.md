# Mission Queue — L2 NeuralSync Intern

**Updated:** 2026-06-20  
**Poll:** Read this file + `mission-control/state.json` before every L2 session.

## Active mission

| Field | Value |
| --- | --- |
| **ID** | `week1-git-collab-test` |
| **Priority** | P0 — Week 1 proof |
| **Assignment** | `l1-week1-git-collab-test-2026-06-20.md` |
| **Branch** | `l2/collab-test-2026-06-20` |
| **Status** | `complete` — L2 pushed `l2/collab-test-2026-06-20`; awaiting Umair merge |
| **Assigned by** | L1 Chief of Staff |

## Queue (after active mission)

| # | Mission | Status |
| --- | --- | --- |
| 2 | VCOS HQ hygiene: verify all `mission-control/` files present | pending |
| 3 | Read `dual-hermes-collaboration-protocol.md`; confirm workdir path | pending |

## Idle rule

If `state.json` → `cubicle_l2.active_mission` is `null` and this queue is empty, report idle on Telegram. Do not invent greenfield work.