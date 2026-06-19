# Claude-Visible Weekly Review

Purpose: turn VCOS weekly work review context into a Claude/team-visible packet when local filesystem access is unavailable.

## Trigger Phrases

- "Claude doesn't have local context"
- "prepare Claude Project context"
- "make this visible for Claude review"
- "publish the weekly review context to ClickUp"
- "run weekly work review and skill harvest"

## Owner

Infrastructure / Sentinel.

## When To Use

Use when a Claude agent or team member needs to review weekly VCOS work but cannot read local files in `_VCOS_Headquarters`.

This skill does not replace local fast-path files. It distills the current fast-path and weekly truth into a ClickUp task or comment.

## Inputs

- VCOS fast path:
  - `1_Command_Brain_Core/1.2_Headquarters_Memory/ubiquitous_language.md`
  - `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/state.md`
  - `1_Command_Brain_Core/1.2_Headquarters_Memory/active-context.md`
  - `1_Command_Brain_Core/1.2_Headquarters_Memory/key-workspaces.md`
- Latest Sunday Office Hours/session brief.
- Weekly skill harvest rubric.
- Current ClickUp routing target.
- Any local prompt/packet that Claude cannot access.

## Output

A ClickUp task or comment containing:

- purpose
- current source-of-truth summary
- source priority rules
- weekly review prompt
- latest weekly status summary
- skill-harvest rubric
- candidate workflow table
- approval gates
- definition of done

## Current ClickUp Proof Task

- Task: `86e1w6343`
- URL: https://app.clickup.com/t/86e1w6343
- Created: 2026-06-15
- Purpose: Claude/team-visible weekly review + skill harvest handoff.

## Source Priority Rules

1. Latest Sunday Office Hours/session brief wins for weekly status.
2. Current `state.md` wins for active blockers and next actions.
3. Current `active-context.md` wins for active project priority.
4. Project README/handoff files win for project-specific details.
5. Older plans and stale checklists are historical evidence only.

## Approval Gates

Human approval is required before:

- notifying all assignees/team members
- sending external messages
- mutating CRM/customer records
- publishing public content or proof claims
- editing live QuickBooks/client systems
- packaging this as a public/client-ready skill
- changing ClickUp structure, statuses, or assignments beyond the approved task/comment

## Validation Log

| Date | Use | Result | Next Action |
| --- | --- | --- | --- |
| 2026-06-15 | Created local packet shelf and ClickUp task `86e1w6343` after Claude produced stale local-context review | Useful first run; Claude-visible task now contains enough context for review without local files | Ask Claude/team to review the task; update after feedback; promote after 3 successful uses |

