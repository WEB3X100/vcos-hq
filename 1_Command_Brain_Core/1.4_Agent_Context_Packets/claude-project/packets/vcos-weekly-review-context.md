# VCOS Weekly Review Context Packet

Purpose: give Claude enough current VCOS context to review the week accurately, diagnose repeated workflows, and draft a short status update without drifting into stale project plans.

## Trigger

Use this packet when Umair asks:

- "review what I worked on this week"
- "draft my weekly status update"
- "run Sunday office hours"
- "what workflows did I repeat that should become a template or skill?"
- "grill my weekly tasks"

## Read Order

Read these first, in order:

1. `CLAUDE.md`
2. `1_Command_Brain_Core/1.2_Headquarters_Memory/ubiquitous_language.md`
3. `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/state.md`
4. `1_Command_Brain_Core/1.2_Headquarters_Memory/active-context.md`
5. `1_Command_Brain_Core/1.2_Headquarters_Memory/key-workspaces.md`
6. Latest file matching `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/session-briefs/sunday-office-hours-*.md`
7. `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/weekly-skill-harvest.md`
8. `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/automation-registry.md`

Only after that, read the smallest relevant project README or handoff file.

## Source Priority

When sources conflict:

1. Latest Sunday Office Hours/session brief wins for weekly status.
2. Current `state.md` wins for active blockers and next actions.
3. Current `active-context.md` wins for active project priority.
4. Project README/handoff files win for project-specific details.
5. Older plans, old scoreboards, raw dumps, and stale checklists are historical evidence, not current truth.

## Known Context Failure To Avoid

Do not anchor the weekly review on old barbershop documents unless the latest state says barbershop is active. As of the current fast path, barbershop is parked; Dealership OS and AMAX are the active proof lanes, with content-intel blocked on Umair voice calibration.

If a project file says a stale loop is active but the latest Sunday Office Hours says another lane moved, explicitly call out the mismatch instead of producing a confident stale review.

## Weekly Review Output

Produce a concise Draft-Only status update:

1. Top outcomes shipped or advanced.
2. Misses, blockers, and human decisions needed.
3. Next week's 3 highest-leverage actions.
4. Approval gates still active.
5. Skill harvest: repeated workflows that should become a template, protocol, skill candidate, or automation.

## Skill Harvest Rubric

For each repeated workflow, include:

- name
- trigger phrase
- owning department/domain
- validation count
- smallest input packet
- output packet
- approval gate
- recommendation: keep as note, add to registry, promote to candidate, install into department pack, or package later

Use `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/weekly-skill-harvest.md` as the governing rubric.

## Approval Gates

Everything is Draft-Only until Umair approves.

Do not recommend taking direct action on:

- external email, SMS, WhatsApp, Slack, Telegram, or client-facing messages
- public posts, ads, landing pages, videos, or public proof claims
- CRM/customer records
- ClickUp task mutation unless asked and approved
- live QuickBooks/client system changes
- spending, deployment, or irreversible changes

