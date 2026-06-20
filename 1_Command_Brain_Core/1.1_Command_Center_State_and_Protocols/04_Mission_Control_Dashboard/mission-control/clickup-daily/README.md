# ClickUp Daily Input — Codex → Hermes Pipeline

**Purpose:** Codex (ClickUp MCP) extracts today's operating picture **read-only** into a dated file. Hermes 7pm cron reads this file — it does **not** call ClickUp.

## Flow

```text
6:30pm America/Toronto — Codex ground job (ClickUp MCP)
  → writes clickup-daily/YYYY-MM-DD-clickup-daily-input.md

7:00pm America/Toronto — Hermes cron (vcos-brain-grok)
  → reads today's clickup-daily-input.md + state.json + HQ fast path
  → composes 7pm brief v2.1 → WhatsApp
  → writes briefs/YYYY-MM-DD-7pm-brief.md
```

## Files

| File | Writer | Reader |
| --- | --- | --- |
| `YYYY-MM-DD-clickup-daily-input.md` | Codex daily job | Hermes 7pm cron |
| `briefs/YYYY-MM-DD-7pm-brief.md` | Hermes 7pm cron | Umair + tomorrow delta |

## Codex prompt

`../hermes/codex-clickup-daily-ground-job-prompt.md` — **v1.1** (API-aware, two-pass, confidence)

## Assignee IDs

`assignee-ids.json` — populate ClickUp user ID strings when known (MCP member list).

## Hermes cron

`../hermes/cron-prompt-body-v2.3-clickup-prefetch.txt` (reads v1.1 daily input)

## v1.1 changes (2026-06-21)

- Two-pass extraction (broad active + lane-targeted + completed 24h)
- Hierarchy-based lane classification (list/parent > task title)
- Split **Tonight queue** vs **Cleanup queue**
- MCP health block + degrade gracefully (no inferred certainty)
- Owner confidence: direct | broad_scan | unassigned | co_owned
- TOP 3 requires `why tonight` + real `due_date`
- Duplicate parent detection (AMAX pattern)
- Priority: P0/P1 lane > real due > ClickUp priority > stale cleanup

## Rules

- Codex: **read-only** ClickUp — no rename, move, archive, delete (per clickup/protocol.md)
- Lane order: P0 Dealership → P1 AMAX → P2 GTM/Build → P3 Parked
- Stale overdue P2/P3 must not rank above P0/P1 in TOP 3 recommendations
- If Codex job fails, Hermes uses `⚠️ ClickUp daily input missing` and HQ files only

## Schedule (L1 personal laptop)

```bash
# Codex ~6:30pm (adjust path to your codex CLI)
30 18 * * * cd /Users/umairkhalid/_VCOS_Headquarters && codex -p "$(cat .../codex-clickup-daily-ground-job-prompt.md)" >> .../clickup-daily/logs/codex-$(date +\%F).log 2>&1

# Hermes 7pm — existing cron 1cc5917442de with v2.2 body
0 19 * * * America/Toronto
```

Manual test: run Codex prompt first, verify today's `*-clickup-daily-input.md` exists, then trigger Hermes once.