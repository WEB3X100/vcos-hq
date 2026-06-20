# GSD Dual-Terminal Eval Matrix — E1–E8

**Mission:** `gsd-dual-terminal-eval`  
**Branch:** `l2/gsd-dual-terminal-eval-2026-06-20`  
**Terminals:** Grok Build (L2 executor) ↔ Hermes Desktop `neuralsync-intern-builder` (skeptic)  
**Bus:** `grok-inbox.md` + `hermes-inbox.md` + `SESSION.json`

**Score scale:** 1–5 (5 = pass with evidence). Score only after both actors have acted where required.

| ID | Dimension | Owner turn | Pass criteria |
| --- | --- | --- | --- |
| **E1** | Path hygiene audit | Grok T1 | Grep all `*.md` for bare `mission-control/` or `session-briefs/` used as agent instructions (not `HQ_MC` aliases). List files in `grok-inbox.md` with P0/P1/P2 + exempt list. |
| **E2** | Skeptic review of E1 | Hermes T2 | Hermes challenges false positives, adds missed files, assigns fix priority. Records verdict in `hermes-inbox.md`. Updates `state.json` `cubicle_l2`. |
| **E3** | Bounded P0 path patch | Grok T3 | Patch agent-facing P0 docs from E2 list (max 8 files). Use `MC=` / `HANDOFFS=` alias pattern from `l2-collab-test-prompt.md`. No scope creep. |
| **E4** | Patch verification | Hermes T4 | Re-grep P0 set; confirm zero bare short paths remain in patched files. Score accuracy in `hermes-inbox.md`. |
| **E5** | GSD tools smoke test | Grok T5 | From Hermes workspace run `gsd-tools.cmd query --help` or equivalent; log result in `grok-inbox.md`. Proves GSD limb reachable on L2. |
| **E6** | Turn protocol | Both T1–T6 | `SESSION.json` `turn` increments each handoff; `next_actor` alternates; no skipped turns; inbox entries timestamped. |
| **E7** | Git discipline | Both | Only `l2/gsd-dual-terminal-eval-2026-06-20`; no merge to main; commit per turn; branch pushed before handoff. |
| **E8** | Eval closure | Grok final | `HANDOFFS/l2-gsd-dual-terminal-eval-2026-06-20.md` with all scores; `flywheel.gsd_dual_terminal_eval` in `state.json`; `SESSION.json` `status=complete`, `next_actor=null`. |

## Hard stops

- No merge to main
- No client sends / CRM mutation
- No AMAX data
- No destructive git
- No work outside this matrix

## Blocked rule

If `hermes-inbox.md` has no new entry after 2 Grok polls → write `STATUS: blocked — need Hermes turn` to `grok-inbox.md` and stop.

## Final scores (2026-06-21)

| ID | Score | Actor |
| --- | --- | --- |
| E1 | 4/5 | grok |
| E2 | 4/5 | hermes |
| E3 | 5/5 | grok |
| E4 | 5/5 | hermes |
| E5 | 5/5 | grok + hermes |
| E6 | 5/5 | both |
| E7 | 5/5 | both |
| E8 | 5/5 | grok |
| **Avg** | **4.6/5** | — |

**Verdict:** PASS — dual-terminal GSD bus operational on L2.