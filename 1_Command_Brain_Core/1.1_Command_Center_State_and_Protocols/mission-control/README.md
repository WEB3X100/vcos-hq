# Dual-Hermes Mission Control

**Status:** Week 1 scaffold — created by Interactive OH 2026-06-19  
**Purpose:** Single visibility surface for Laptop 1 (Chief of Staff / WhatsApp) and Laptop 2 (NeuralSync Intern / Telegram).

## Two Cubicles

| Cubicle | Device | Channel | Role |
| --- | --- | --- | --- |
| L1 | Personal laptop | WhatsApp | Strategist, 7pm brief, approvals |
| L2 | Second laptop | Telegram | 24/7 builder, VCOS HQ sync, feature branches |

## Coordination Bus

GitHub is the coordination layer:

- L2 pushes feature branches only
- L1 pulls, reviews, merges
- Every mission ends with handoff packet in `session-briefs/handoffs/`
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
| `session-briefs/handoffs/MISSION-QUEUE.md` | L2 mission queue (poll every session) |
| `briefs/` | Daily 7pm brief archive |
| `hermes/` | Cron prompts, dream cycle, L2 soul seed |
| `README.md` | This file |

See `session-briefs/interactive-office-hours-dual-laptop-hermes-2026-06-19.md` for locked 7pm brief template.