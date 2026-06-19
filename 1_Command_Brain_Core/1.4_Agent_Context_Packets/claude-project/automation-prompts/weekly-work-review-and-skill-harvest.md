# Claude Code Automation Prompt: Weekly Work Review + Skill Harvest

Purpose: reusable Claude Code prompt for the weekly review automation. This is the Claude-side companion to the Codex scheduled automation `weekly-work-review-skill-harvest`.

## Suggested Schedule

Weekly, Sunday evening after Sunday Office Hours.

Recommended local schedule: Sunday 6:30 PM America/Toronto.

## Claude Code Prompt

```text
Run the VCOS weekly work review and skill harvest in Draft-Only mode.

First read:
1. CLAUDE.md
2. 1_Command_Brain_Core/1.4_Agent_Context_Packets/claude-project/packets/vcos-weekly-review-context.md
3. 1_Command_Brain_Core/1.2_Headquarters_Memory/ubiquitous_language.md
4. 1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/state.md
5. 1_Command_Brain_Core/1.2_Headquarters_Memory/active-context.md
6. 1_Command_Brain_Core/1.2_Headquarters_Memory/key-workspaces.md
7. the latest 1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/session-briefs/sunday-office-hours-*.md
8. 4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/weekly-skill-harvest.md

Review the week using the smallest relevant sources only. Prioritize the latest Sunday Office Hours brief and current state over stale project docs.

Draft:
- top outcomes shipped or advanced
- misses, blockers, and human decisions needed
- next week's 3 highest-leverage actions
- active approval gates
- repeated workflows that should become templates, protocols, skill candidates, or automations

For each skill/workflow candidate, include:
- trigger phrase
- owning department/domain
- validation count
- smallest input packet
- output packet
- approval gate
- recommendation

Do not send external messages, mutate ClickUp/CRM/client data, publish, spend, deploy, or make destructive changes. Draft only.
```

## Expected Output

Save or return a short Markdown draft titled:

`VCOS Weekly Work Review - YYYY-MM-DD`

If saving locally, use:

`1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/session-briefs/weekly-work-review-YYYY-MM-DD.md`

## Setup Notes

Actual scheduling should be done through the chosen runtime:

- Codex app automation: already active as `weekly-work-review-skill-harvest`.
- Claude Code local cron: only configure after confirming the local Claude CLI command and desired output path.
- Hermes/SuperGrok: preferred for persistent read-only sensor cadence after Phase 0 source scopes are approved.

Do not create a new scheduler if one already exists. Prefer updating the automation registry.

