# Handoff — L1 → L2: GSD Dual-Terminal Eval

**Date:** 2026-06-20  
**From:** L1 Chief of Staff (seeded by L2 Grok — self-authored eval spec)  
**To:** L2 NeuralSync Intern (`neuralsync-intern-builder`) + Grok Build  
**Mission ID:** `gsd-dual-terminal-eval`  
**Branch:** `l2/gsd-dual-terminal-eval-2026-06-20`  
**Priority:** P0 — proves GSD + dual-terminal coordination bus

## Objective

Evaluate whether **Grok Build** and **Hermes Desktop** can execute bounded missions via git-backed inbox protocol (GSD discipline) without path failures or main-branch violations.

## Path constants (mandatory)

```
MC=1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/mission-control
HANDOFFS=1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/session-briefs/handoffs
BUS=MC/gsd-dual-terminal-eval
```

See `MISSION_CONTROL_PATHS.md` at repo root.

## BUS layout

| File | Purpose |
| --- | --- |
| `BUS/SESSION.json` | Turn counter, next_actor, eval progress |
| `BUS/EVAL-MATRIX.md` | E1–E8 criteria |
| `BUS/grok-inbox.md` | Grok → Hermes messages |
| `BUS/hermes-inbox.md` | Hermes → Grok responses |

## Turn map

| Turn | Actor | Action |
| --- | --- | --- |
| 1 | Grok | Scaffold BUS, run E1 path audit, hand off |
| 2 | Hermes | E2 skeptic review E1, update state.json |
| 3 | Grok | E3 bounded P0 path patches |
| 4 | Hermes | E4 verify patches |
| 5 | Grok | E5 GSD tools smoke test |
| 6+ | Both | E6 turn protocol, E7 git discipline until scored |
| Final | Grok | E8 eval report → `HANDOFFS/l2-gsd-dual-terminal-eval-2026-06-20.md` |

## Hard stops

- No merge to main
- No client sends / CRM mutation
- No AMAX data
- No destructive git
- No work outside `EVAL-MATRIX.md`

## Exit criteria

Turn ≥ 12 **OR** E1–E8 all scored → write L2 completion handoff, set `flywheel.gsd_dual_terminal_eval`, `SESSION.json status=complete`.

## L2 Turn 1 evidence (Grok)

- Branch created: `l2/gsd-dual-terminal-eval-2026-06-20`
- BUS scaffolded under `BUS/`
- E1 findings in `BUS/grok-inbox.md`
- `SESSION.json`: turn=1, next_actor=hermes

## Decisions needed from Umair

- [ ] Merge `l2/gsd-dual-terminal-eval-2026-06-20` → main after eval complete (Y/N)