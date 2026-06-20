# ClickUp Daily Input — TEMPLATE v1.1

**Date:** YYYY-MM-DD  
**Extracted at:** ISO timestamp (America/Toronto)  
**Extractor:** Codex + ClickUp MCP  
**Space/view:** AgentOSync `90175689274`  
**Read-only:** yes — no ClickUp mutations

## MCP health

| Check | Result |
| --- | --- |
| Priority field visible | yes / no |
| Assignee filter ok (Umair) | yes / no |
| Assignee filter ok (Trysoft) | yes / no |
| Keyword lane search ok | yes / no |
| Fallback used | none / broad_scan / manual_classification / assignee_retry |
| Pass 1 (active broad scan) | ok / partial / failed |
| Pass 2 (lane targeted + completed 24h) | ok / partial / failed |

**Degrade rule:** When fields are missing or unreliable, record confidence — do not infer certainty.

## Hygiene

| Metric | Count |
| --- | --- |
| Active tasks scanned (pass 1) | |
| Stale/overdue (active) | |
| Stale due-date pressure (not true urgency) | |
| Due ≤48h (real dates) | |
| Due ≤7d (real dates) | |
| Unassigned / no owner | |
| Umair-assigned (with confidence) | |
| Trysoft-assigned (with confidence) | |
| `stale_sweep_required` (>10 stale) | true / false |

## Lane classification source

Primary: **folder → list → parent task → subtask** hierarchy.  
Secondary: task name keywords only when hierarchy is ambiguous.

| Lane | List/folder signals (examples) |
| --- | --- |
| P0 | `03 Dealership MVP Sameer & Uzair`, dealership parents |
| P1 | `01 · Amax Travel`, AMAX control tower parents |
| P2 | Production, Hermes, GTM — only if unlocks P0/P1 this week |
| P3 | trading, barber, auto-posting, ethnic apparel, weekly review |

## Tonight queue (max 5 — P0/P1 only)

Real work for 7pm–12am. **Exclude** stale P2/P3 unless P0/P1 have zero actionable items.

| Lane | Task | Status | due_date | due_bucket | Owner | confidence | task_id | url | Blocker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | YYYY-MM-DD / none / unknown | optional label | | direct / broad_scan / unassigned | | | |

`due_date` = ISO date or `none` or `unknown` — never use bucket text as due_date.

## Cleanup queue (max 10 — do not promote to TOP 3)

Stale P2/P3, unassigned, duplicate parents, old due dates, mis-laned tasks.

| Lane | Task | Why cleanup | due_date | Owner | confidence |
| --- | --- | --- | --- | --- | --- |
| | | stale P2 / unassigned / duplicate parent / … | | | |

## Duplicate parent detection (per lane)

| Lane | Parent tasks (3+ active in lane) | Recommendation |
| --- | --- | --- |
| P1 AMAX | e.g. AMAX Tasks, AMAX AI Native ORG, Finance + Sales Control Tower | merge / park reference |

## Parent → subtask rollup (P0/P1 parents only)

| Parent | Open subtasks | Unassigned subs | Newest activity |
| --- | --- | --- | --- |
| | | | |

## Completed last 24h (pass 2)

| Task | Completed at | Owner | confidence | url |
| --- | --- | --- | --- | --- |
| | | | | |

## Lane summary

### P0 Dealership

- **Active parent tasks:**
- **Blockers:**
- **Next 72h critical:**

### P1 AMAX

- **Active parent tasks:**
- **Blockers:**
- **Next 7d critical:**

### P2 GTM / Build

- **Active (max 5):**

### P3 Parked / weekly review

- **Candidates to park (max 5):**

## Trysoft delta (since yesterday brief or last 24h)

- **Completed:**
- **In progress:**
- **Delayed:**
- **Newly assigned to Umair:**

## Consolidation recommendations (read-only — max 3)

1. **Action:** merge | park | rename | date-fix — **Target:** — **Why:**

## Suggested TOP 3 for tonight (Hermes may adjust)

Must favor P0 then P1. Never P2/P3 unless both lanes have zero tonight-queue items.

1. **Lane:** | **Task:** | **due_date:** | **Owner:** 👤/🤝/🤖 | **confidence:** | **why tonight:** revenue proof | unblocks Trysoft | client/demo readiness | stale cleanup | **Done means:**
2.
3.

## Raw notes

- Assignee IDs used: Umair `...` / Trysoft `...` / fallback
- MCP errors:
- Folders/lists scanned: Q3 `901713630962`, Delivery `901713630958`, Production `901711785684`, async `90178817003`/`004`
- Keyword searches that returned 0 despite broad scan matches: