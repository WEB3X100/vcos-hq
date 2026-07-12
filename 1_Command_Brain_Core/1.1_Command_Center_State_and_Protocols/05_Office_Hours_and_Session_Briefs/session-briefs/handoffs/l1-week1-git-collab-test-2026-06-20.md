# Handoff — L1 → L2: Week 1 Git Collaboration Test

**Date:** 2026-06-20  
**From:** L1 Chief of Staff (`vcos-brain-grok`, personal laptop)  
**To:** L2 NeuralSync Intern (`neuralsync-intern-builder`, second laptop)  
**Mission ID:** `week1-git-collab-test`  
**Priority:** P0 — proves dual-Hermes coordination bus

## Objective

Prove L1 and L2 can share context and collaborate via GitHub + VCOS HQ files — no direct agent-to-agent channel.

## Prerequisites (L2 human — Umair)

1. Hermes installed: `hermes setup && hermes doctor`
2. Profile: `hermes profile create neuralsync-intern-builder` + paste `mission-control/hermes/l2-soul-seed.md`
3. Clone repo (recommended path — **same on both laptops**):

```bash
mkdir -p ~/VCOS-Coordination
cd ~/VCOS-Coordination
git clone https://github.com/WEB3X100/vcos-hq.git vcos-hq
cd vcos-hq
git pull origin main
```

4. Hermes workdir for all L2 missions: `~/VCOS-Coordination/vcos-hq`

## L2 tasks (execute in order)

### Task 1 — Pull and verify

```bash
cd ~/VCOS-Coordination/vcos-hq
git pull origin main
```

Confirm these exist:

- `mission-control/state.json`
- `mission-control/dual-hermes-collaboration-protocol.md`
- `session-briefs/handoffs/MISSION-QUEUE.md`
- `session-briefs/handoffs/l1-week1-git-collab-test-2026-06-20.md` (this file)

### Task 2 — Create branch

```bash
git checkout -b l2/collab-test-2026-06-20
```

### Task 3 — Write L2 response artifact

Create file: `session-briefs/handoffs/l2-collab-test-response-2026-06-20.md`

```markdown
# L2 Response — Git Collaboration Test

**Date:** [timestamp]
**Branch:** l2/collab-test-2026-06-20
**L2 device:** second laptop
**Hermes profile:** neuralsync-intern-builder

## Pull verification
- [ ] git pull succeeded
- [ ] state.json read
- [ ] MISSION-QUEUE.md read

## Test evidence
- git rev-parse HEAD: [hash]
- hostname: [output of hostname]
- hermes profile: neuralsync-intern-builder

## L2 acknowledgment
I confirm: I will only work on l2/* branches, never merge to main, and update state.json after every mission.

## Decisions needed from Umair
- [ ] Merge l2/collab-test-2026-06-20 to main? (Y/N)
```

### Task 4 — Update state.json

Update `mission-control/state.json`:

```json
"cubicle_l2": {
  "status": "active",
  "active_mission": "week1-git-collab-test",
  "active_branch": "l2/collab-test-2026-06-20",
  "last_push": "[ISO timestamp]",
  "last_session": "L2 collab test — pulled HQ, wrote response handoff"
}
```

Also set `github.open_branches` to include `l2/collab-test-2026-06-20`.

### Task 5 — Commit and push

```bash
git add session-briefs/handoffs/l2-collab-test-response-2026-06-20.md
git add mission-control/state.json
git commit -m "L2: Week 1 git collaboration test response"
git push -u origin l2/collab-test-2026-06-20
```

**Do not merge to main.**

### Task 6 — Telegram summary

Post to Telegram:

```text
L2 mission complete: week1-git-collab-test
Branch: l2/collab-test-2026-06-20
Handoff: session-briefs/handoffs/l2-collab-test-response-2026-06-20.md
Decisions: merge to main? (awaiting Umair)
```

## Test contract

| Check | Pass |
| --- | --- |
| L2 branch on GitHub | `l2/collab-test-2026-06-20` exists |
| Response handoff file | `l2-collab-test-response-2026-06-20.md` |
| state.json updated | cubicle_l2.status = active |
| No main merge | L2 did not push to main |

## Out of scope

- AMAX / Rooshan COA work (L1 only until reports loaded)
- Client repo changes
- ClickUp mutations
- Production deploy

## L1 follow-up (after L2 push)

L1 will `git pull`, read `l2-collab-test-response-2026-06-20.md`, update `cubicle_l1.last_session`, and include result in next 7pm brief.