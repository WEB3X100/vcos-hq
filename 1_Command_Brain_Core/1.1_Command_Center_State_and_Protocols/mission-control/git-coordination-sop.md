# Git Coordination SOP — Dual-Hermes Mission Control

**Status:** Week 1 active  
**Coordination repo:** VCOS HQ (`/Users/umairkhalid/_VCOS_Headquarters`)

## Branch rules

| Actor | Branch pattern | Merge |
| --- | --- | --- |
| L1 (Chief of Staff) | `l1/*` | Umair approves → merge to `main` |
| L2 (NeuralSync Intern) | `l2/*` | Umair approves → merge to `main` |
| Either | `feature/*` for client repos | Same approval gate |

**Never:** force-push `main`, silent merge, or direct commits to `main` from L2.

## Mission loop

```text
L1 encodes plan in HQ → git push main (or PR)
    → L2 pulls main → creates l2/mission-name → works → pushes
    → L2 writes handoff packet → updates state.json → opens PR
    → L1 reviews PR + handoff → Umair merges
    → L1 harvests skill candidate if pattern repeats 3x
```

## Handoff packet (required)

Path: `session-briefs/handoffs/YYYY-MM-DD-mission-name.md`

```markdown
# Handoff — [mission name]

**Date:** YYYY-MM-DD  
**Branch:** l2/...  
**PR:** [link or "draft local"]

## What shipped
- ...

## Test evidence
- Command: ...
- Result: pass/fail

## Decisions needed from Umair
- [ ] ...

## state.json updates
- cubicle_l2.active_mission: cleared / next
- cubicle_l2.last_push: [timestamp]
```

## state.json update (both cubicles)

After every session, update `mission-control/state.json`:

- `updated_at` (ISO 8601)
- Relevant cubicle `last_session` / `last_push` / `pending_decisions_for_umair`
- `client_lanes` bullets when client work moved
- `tonight_chunk` when 7pm brief sets tonight's focus

## Client repos

Dealership implementation: `3_Project_Workspaces/3.1_AgentOSync_Revenue_Pipeline/dealership-ai-command-layer-mvp/`  
Planning/specs: `3_Project_Workspaces/3.6_Sameer_Uzair_Dealership_Operating_System/`

L2 works in client repo branches; HQ gets pointer updates and handoffs only unless mission says otherwise.