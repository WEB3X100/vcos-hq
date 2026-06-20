# Dual-Hermes Collaboration Protocol — Week 1

**Status:** Active  
**Coordination repo:** https://github.com/WEB3X100/vcos-hq  
**Local path (both laptops):** `~/VCOS-Coordination/vcos-hq` (recommended — same path on both machines)

**Path constants** (Hermes `--workdir` = repo root — not root-level `mission-control/`):

- `MC=` `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/mission-control`
- `HANDOFFS=` `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/session-briefs/handoffs`

## Architecture (how the two agents share work)

```text
┌─────────────────────────────────────────────────────────────────┐
│  VCOS HQ repo (GitHub) = single coordination bus                │
│  MC/state.json               ← live dashboard                   │
│  HANDOFFS/                   ← mission queue + completion packets │
└─────────────────────────────────────────────────────────────────┘
         ▲ pull/push                    ▲ pull/push
         │                              │
┌────────┴────────┐            ┌────────┴────────┐
│ L1 Personal     │            │ L2 Second       │
│ vcos-brain-grok │            │ neuralsync-     │
│ WhatsApp        │            │ intern-builder  │
│ 7pm brief       │            │ Telegram        │
│ workdir → HQ    │            │ workdir → HQ    │
└─────────────────┘            └─────────────────┘
```

**Rule:** Hermes agents do **not** share memory directly. They share **files in git**:

| Artifact | Purpose | Who writes first |
| --- | --- | --- |
| `MC/state.json` | Live cubicle status, active mission, client lanes | L1 seeds; both update after sessions |
| `HANDOFFS/MISSION-QUEUE.md` | L2 polls for next mission | L1 |
| `HANDOFFS/l1-*.md` | L1 → L2 mission assignment | L1 |
| `HANDOFFS/l2-*.md` | L2 → L1 completion packet | L2 |
| Feature branches `l1/*`, `l2/*` | Isolated work | Either |

**Do not** clone the repo inside `~/.hermes/`. Keep the repo in `~/VCOS-Coordination/vcos-hq` and set Hermes `--workdir` to that path (cron, manual sessions, L2 missions).

## Folder layout (both laptops)

```bash
mkdir -p ~/VCOS-Coordination
cd ~/VCOS-Coordination
git clone https://github.com/WEB3X100/vcos-hq.git vcos-hq
cd vcos-hq
```

| Laptop | Hermes profile | Channel | Workdir |
| --- | --- | --- | --- |
| L1 Personal | `vcos-brain-grok` | WhatsApp | `~/VCOS-Coordination/vcos-hq` |
| L2 Second | `neuralsync-intern-builder` | Telegram | `~/VCOS-Coordination/vcos-hq` |

## Mission loop (every collaboration)

```text
1. L1 writes mission → HANDOFFS/l1-<mission>.md
2. L1 updates MC/state.json (cubicle_l2.active_mission, active_branch)
3. L1 commits + pushes (main or l1/* branch)
4. L2: git pull
5. L2: git checkout -b l2/<mission>
6. L2 executes mission (read-only or bounded writes per handoff)
7. L2 writes HANDOFFS/l2-<mission>.md + updates MC/state.json cubicle_l2
8. L2 commits + pushes branch
9. L1 pulls, reviews handoff, Umair merges (never silent-merge)
10. L1 updates cubicle_l1 + flywheel metrics
```

## Context sharing (what each agent reads every session)

**Both read (in order):**

1. `AGENTS.md`
2. `MC/state.json`
3. `HANDOFFS/MISSION-QUEUE.md`
4. Latest `HANDOFFS/l1-*.md` or `HANDOFFS/l2-*.md` for active mission
5. `MC/git-coordination-sop.md`

**L1 only:** `active-context.md`, 7pm brief template, client lane files  
**L2 only:** Mission spec in the `l1-*.md` handoff; never invent work outside queue

## Channels (human relay)

| Event | L1 (WhatsApp) | L2 (Telegram) |
| --- | --- | --- |
| New mission queued | Optional ping | L2 posts when pull complete |
| Mission complete | L1 summarizes in 7pm brief | L2 posts branch + handoff path |
| Blocked | L1 escalates to Umair | L2 updates `pending_decisions_for_umair` in `MC/state.json` |

## Week 1 test mission

See `HANDOFFS/l1-week1-git-collab-test-2026-06-20.md`

**Pass criteria:**

- [ ] L1 pushed mission to GitHub
- [ ] L2 cloned same repo path and pulled
- [ ] L2 branch `l2/collab-test-2026-06-20` exists on GitHub
- [ ] L2 handoff file exists with test evidence
- [ ] `state.json` cubicle_l2.status = `active`, last_push set
- [ ] Umair reviewed; no silent merge to main

## AMAX / Rooshan (parallel track — not L2 Week 1)

Rooshan reclassifies COA history → Umair loads QBO exports to `01_Finance_Control_Tower_QB_Hermes_DB/data/` → L1 runs diagnostic using `qbo-report-inventory-matrix.md`.

That lane stays on L1 (`amax-finance-sentinel`) until reports land. L2 does **not** touch AMAX data folder in Week 1.

## Parking lot

- Shared Hermes memory / soul merge across devices
- Auto-merge PRs
- L2 writing to client repos without TDD handoff
- ClickUp API sync (paste payloads manually for now)