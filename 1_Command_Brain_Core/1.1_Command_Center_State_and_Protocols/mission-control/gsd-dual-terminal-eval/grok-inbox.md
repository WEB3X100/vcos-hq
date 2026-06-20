# Grok Inbox — GSD Dual-Terminal Eval

**Actor:** Grok Build (L2)  
**Turn:** 1  
**Timestamp:** 2026-06-20T23:45:00-04:00

---

## E1 — Path hygiene audit (submitted)

**Method:** `rg -l "mission-control/|session-briefs/" --glob "*.md"` on repo root (excl. `6_Arsenal`).

**Rule:** Bare `mission-control/` or `session-briefs/` in agent-facing instructions are wrong when Hermes `--workdir` = repo root. Correct pattern: `MC=` / `HANDOFFS=` aliases per `MISSION_CONTROL_PATHS.md` and `l2-collab-test-prompt.md`.

### Exempt (do not patch)

| File | Reason |
| --- | --- |
| `MISSION_CONTROL_PATHS.md` | Canonical path constants doc |
| `mission-control/hermes/l2-collab-test-prompt.md` | Already uses `MC=` / `HANDOFFS=` |
| `mission-control/hermes/l2-path-fix-recovery-prompt.md` | Recovery doc; mentions wrong paths intentionally |

### P0 — Hermes prompts + MC ops (fix first)

| File | Sample wrong refs |
| --- | --- |
| `mission-control/dual-hermes-collaboration-protocol.md` | `mission-control/state.json`, `session-briefs/handoffs/` throughout diagram + tables |
| `mission-control/l2-setup-guide.md` | `mission-control/`, `session-briefs/handoffs/`, `mission-control/state.json` |
| `mission-control/git-coordination-sop.md` | `session-briefs/handoffs/`, `mission-control/state.json` |
| `mission-control/README.md` | `session-briefs/handoffs/MISSION-QUEUE.md` |
| `mission-control/hermes/l2-soul-seed.md` | `session-briefs/handoffs/`, `mission-control/` (mixed — item 2 uses full path) |
| `mission-control/hermes/l1-post-push-prompt.md` | `session-briefs/handoffs/`, `mission-control/state.json` |
| `mission-control/hermes/7pm-cron-prompt.md` | `mission-control/state.json` (line 66 bare short path) |
| `mission-control/hermes/dream-cycle-lite.md` | `mission-control/briefs/`, `session-briefs/handoffs/` |
| `session-briefs/handoffs/MISSION-QUEUE.md` | `mission-control/state.json` |
| `session-briefs/handoffs/l1-week1-git-collab-test-2026-06-20.md` | `mission-control/state.json`, `session-briefs/handoffs/` |

### P1 — Routers + entry docs

| File | Notes |
| --- | --- |
| `AGENTS.md` | `session-briefs/` paths without HQ prefix |
| `session-briefs/README.md` | `mission-control/state.json`, `session-briefs/` self-refs |
| `cadence-hooks.md` | `session-briefs/` short paths |
| `HEADQUARTERS_MAP.md` | `session-briefs/README.md` short path |

### P2 — Memory / historical (lower urgency)

| File | Notes |
| --- | --- |
| `1.2_Headquarters_Memory/active-context.md` | `session-briefs/`, `mission-control/` |
| `1.2_Headquarters_Memory/decisions.md` | `mission-control/`, `session-briefs/` |
| `1.2_Headquarters_Memory/key-workspaces.md` | mixed `.../mission-control/` and `.../session-briefs/` (partially qualified) |
| `session-briefs/dual-laptop-hermes/plan.md` | historical plan refs |
| `session-briefs/interactive-office-hours-dual-laptop-hermes-2026-06-19.md` | OH artifact |
| `session-briefs/gbrain-office-hours-dual-laptop-hermes-2026-06-19.md` | OH artifact |
| `session-briefs/clickup-payloads-dual-laptop-hermes-2026-06-19.md` | mixed full + short |
| `session-briefs/handoffs/l2-collab-test-response-2026-06-20.md` | handoff path in Telegram draft only |

### E1 counts

- **Total files with matches:** 31
- **P0:** 10
- **P1:** 4
- **P2:** 7
- **Exempt:** 3

---

## → Hermes: skeptic-review request (Turn 2)

**@neuralsync-intern-builder** — please execute E2 on branch `l2/gsd-dual-terminal-eval-2026-06-20`:

1. **Skeptic-review E1** above. Challenge false positives; add any missed files; confirm P0/P1/P2 ranking.
2. Write your verdict to `hermes-inbox.md` (append below the header).
3. Update `mission-control/state.json` → `cubicle_l2`:
   - `active_mission`: `gsd-dual-terminal-eval`
   - `active_branch`: `l2/gsd-dual-terminal-eval-2026-06-20`
   - `last_session`: one-line summary of E2 skeptic review
   - `last_push`: ISO timestamp after your commit
4. Increment `SESSION.json` → `turn: 2`, `next_actor: grok`.
5. Commit + push branch. Do **not** merge to main.

**Read first:** `EVAL-MATRIX.md`, this file, `MISSION_CONTROL_PATHS.md`, `HANDOFFS/l1-gsd-dual-terminal-eval-2026-06-20.md`.