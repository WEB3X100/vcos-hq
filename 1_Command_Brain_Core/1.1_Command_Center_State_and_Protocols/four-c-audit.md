# VCOS Four C Audit

Purpose: evaluate VCOS HQ as an AI operating system across context, connections, capabilities, and cadence.

Run this weekly or before adding a major automation.

## Scorecard

| Pillar | Score | Current evidence | Gap | Next action |
| --- | --- | --- | --- | --- |
| Context | 18/25 | Fast-path memory, state, decisions, domain READMEs, approval gates | Legacy references still overlap | Finish reference migration index |
| Connections | 8/25 | ClickUp workspace/list IDs documented; Drive named as file truth | Connectors/API paths not fully verified | Create read-first GitHub/ClickUp/Drive setup tasks |
| Capabilities | 12/25 | Command router skill, skill governance, task-skill map, candidate skills | Few packaged repeatable skills tested 3+ times | Run Daily Briefing and Employee 01 mock test as candidates |
| Cadence | 8/25 | Daily heartbeat defined; automation registry created | No tested recurring run yet | Configure one current-thread Daily Briefing heartbeat |

Current baseline: 46/100.

## Audit Questions

Context:

- Does a new agent answer like a teammate or a stranger?
- Are priorities, blockers, decisions, approval gates, and domain interfaces easy to find?
- Is active memory compact enough to load every session?

Connections:

- Can VCOS reach the systems that hold tasks, files, meetings, approvals, and customer context?
- Are credentials least-privilege and stored outside chat?
- Are write actions gated?

Capabilities:

- Which SOPs were used 3+ times?
- Which repeated prompts should become skill candidates?
- Which tasks need deterministic scripts instead of agent autonomy?
- Which skills need endpoint IDs, templates, or reference files to save tokens?

Cadence:

- Which routines should run daily, weekly, or on demand?
- Which routines must remain manual because approval or judgment is required?
- What should notify the human, and where?
- What happens on failure?

## Level-Up Interview

Use these questions to find the next improvement:

1. What did we do three or more times this week?
2. What felt manual, boring, or copy/paste?
3. What did a smart assistant need too much explanation to do?
4. If lead volume doubled next week, what would break first?
5. What would create more revenue or delivery speed if it ran reliably on autopilot?

Record outputs as:

- New decision: `1_Command_Brain_Core/1.2_Headquarters_Memory/decisions.md`
- Blocker: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/state.md`
- Skill candidate: `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/vcos-task-skill-map.md`
- Automation candidate: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/automation-registry.md`
- Domain-specific rule: `2_Domain_Packs/<domain>/README.md`

