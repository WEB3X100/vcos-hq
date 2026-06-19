# Claude Project Context Shelf

Purpose: easy, organized Markdown shelf for files Umair can add to a Claude Project so Claude has the right VCOS context before giving feedback, reviews, or weekly operating advice.

Claude should not be given the entire HQ folder as a raw dump. Add the smallest packet for the job.

## Add These To The Main VCOS Claude Project

Always include:

1. `CLAUDE.md`
2. `1_Command_Brain_Core/1.4_Agent_Context_Packets/claude-project/packets/vcos-weekly-review-context.md`
3. `1_Command_Brain_Core/1.4_Agent_Context_Packets/claude-project/automation-prompts/weekly-work-review-and-skill-harvest.md`

Optional, when working on automations:

4. `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/automation-registry.md`
5. `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/managed-agent-runtime-evaluation.md`
6. `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/hermes-supergrok-vcos-playbook.md`

Optional, when working on skill packaging:

7. `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/weekly-skill-harvest.md`
8. `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/vcos-task-skill-map.md`

## Claude Code Command

Inside this repo, Claude Code can run the project command:

```text
/vcos-weekly-review
```

Command file:

`.claude/commands/vcos-weekly-review.md`

Use it for a manual run or as the command body for a future Claude Code cron wrapper.

## Context Hygiene

- Use this folder as a curated shelf, not as a mirror of HQ.
- If a Claude answer is stale, add or update one packet here instead of attaching more random files.
- Latest Sunday Office Hours brief outranks older project docs for weekly status.
- Current `state.md` and `active-context.md` outrank stale project plans.
- Human approval gates remain active even inside Claude Projects.

## Suggested Claude Project Instructions

```text
You are helping with VCOS HQ. Treat uploaded files as curated context packets, not as the whole source of truth.

Before reviewing weekly work, read the weekly-review context packet first. The latest Sunday Office Hours/session brief and current state outrank older project docs. If context conflicts, name the conflict and ask which source should win.

Default mode is Draft-Only. Do not recommend external sends, client-facing publishing, CRM mutation, ClickUp mutation, production deployment, spending, or irreversible changes without explicit human approval.

When asked for weekly feedback, produce:
1. what actually shipped or advanced,
2. what missed or stalled,
3. decisions/blockers requiring Umair,
4. next 3 actions,
5. repeated workflows that should become templates or skill candidates.
```

## Intake Rule For New Markdown

When adding a new `.md` file for Claude context, create or update an index entry with:

- packet name
- task it supports
- source-of-truth files it points to
- when to refresh it
- whether it is safe for public/client use
