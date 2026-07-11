# Dual-Hermes Mission Control

**Status:** Castle OS Phase 1+2 on L1 · Core workflows solidified 2026-07-11  
**Purpose:** Single visibility surface for Laptop 1 (Chief of Staff) and Laptop 2 (Hermes co-founder / Telegram).

## Start here (operator)

| Doc | Role |
| --- | --- |
| **`CORE_WORKFLOWS.md`** | **Solidified daily workflows — read before inventing loops** |
| `COFOUNDER-CASTLE-OS-PRD.md` | Build authority (Castle UI / phases) |
| `local-dashboard/` | Run: `python3 server.py` → http://127.0.0.1:8765/ |
| `marketing-mini-intern/README.md` | Draft-Only Telegram → Hermes → five LinkedIn kits → Castle review/approval packet |

**Branch truth:** Castle is available on its reviewed feature branch; it is not merged to `main`. Read `marketing-mini-intern/PROJECT-STATE.md` for current shipped/designed/blocked truth.

## Two Cubicles

| Cubicle | Device | Channel | Role |
| --- | --- | --- | --- |
| L1 | Personal laptop | WhatsApp | Strategist, 7pm brief, approvals |
| L2 | Second laptop | Telegram | 24/7 builder, VCOS HQ sync, feature branches |

## Coordination Bus

GitHub is the coordination layer:

- L2 pushes feature branches only
- L1 pulls, reviews, merges
- Every mission ends with handoff packet in `../../05_Office_Hours_and_Session_Briefs/session-briefs/handoffs/`
- `state.json` in this folder is the live dashboard state

## Update Protocol

After every L1 or L2 session:

1. Update `state.json` (agent or human)
2. Write handoff packet if mission complete
3. Post draft ClickUp comment on list https://app.clickup.com/9017760195/v/li/901713786845

## Files

| File | Purpose |
| --- | --- |
| `state.json` | Live L1/L2 cubicle state |
| `dashboard.md` | Human-readable live dashboard |
| `git-coordination-sop.md` | Branch/PR rules |
| `l2-setup-guide.md` | Second laptop provisioning steps |
| `dual-hermes-collaboration-protocol.md` | How L1 + L2 share work via GitHub |
| `six-loop-l2-operating-model.md` | Bounded setup for running the VCOS six loops on L2 |
| `hermes/l2-six-loop-cron-prompts.md` | L2 cron and queue-driven prompt templates for the six loops |
| `../../05_Office_Hours_and_Session_Briefs/session-briefs/handoffs/MISSION-QUEUE.md` | L2 mission queue (poll every session) |
| `briefs/` | Daily 7pm brief archive |
| `hermes/` | Cron prompts, dream cycle, L2 soul seed, AI SDR daily brief |
| `hermes/ai-sdr-daily-brief-setup.md` | Enable checklist for AI SDR Telegram monitoring cron |
| `replit-launch/` | Replit dashboard PRD, build prompt, UI spec, QA plan, and retrieval safety |
| `replit-launch/flywheel-enhancements-spec.md` | Labyrinth observability, skill pipeline, QA gates, CodeBurn, and Kanban read-only spec |
| `marketing-mini-intern/README.md` | MMI requirements, GitHub memory contract, build prompt, and first overnight UAT |
| `README.md` | This file |

See `../../05_Office_Hours_and_Session_Briefs/session-briefs/interactive-office-hours-dual-laptop-hermes-2026-06-19.md` for locked 7pm brief template.
