# Cadence Hooks

Purpose: define how VCOS HQ wakes up, reviews state, and routes work without flooding context.

## Daily Heartbeat

Default cadence:

- Time: 8:00 AM America/Toronto
- Owner: Sentinel
- Output: Daily Briefing
- Destination: Slack, Telegram, ClickUp, or current thread

## Office Hours Router

Before weekly office hours, GBrain grills, or activation plan reviews, read:

`1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/session-briefs/README.md`

Dual-laptop Hermes activation: `session-briefs/dual-laptop-hermes/plan.md`

## Daily Heartbeat Inputs

Read only:

1. `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/state.md`
2. `1_Command_Brain_Core/1.2_Headquarters_Memory/active-context.md`
3. `1_Command_Brain_Core/1.2_Headquarters_Memory/key-workspaces.md`
4. Latest weekly plan when running 7pm work-start brief: `session-briefs/weekly-office-hours-plan-*.md` (see `session-briefs/README.md`)
5. Relevant command-room task summaries from ClickUp, if connector access is available

Do not read raw references or domain implementation files during the heartbeat unless a blocker explicitly requires it.

## Daily Briefing Format

```text
Active outcomes:
- ...

Blockers:
- ...

Human decisions needed:
- ...

Agent-executable next actions:
- ...

Approval queue:
- ...
```

## Weekly Level-Up

Once per week:

- Review repeated bugs and hallucinations.
- Update `AGENTS.md` or domain READMEs with negative constraints.
- Promote SOP candidates used successfully 3+ times.
- Archive stale context from active memory.
- Update `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/roadmap.md`.

## Automation Options

- Claude Code `/loop` for local recurring checks.
- OpenClaw cron jobs for scheduled agent tasks.
- Codex automations for thread or workspace reminders.
- ClickUp recurring tasks for human-visible cadence.

## Guardrail

Heartbeat agents may draft and summarize. They must not send external messages, mutate CRM data, publish content, or spend budget without approval.

