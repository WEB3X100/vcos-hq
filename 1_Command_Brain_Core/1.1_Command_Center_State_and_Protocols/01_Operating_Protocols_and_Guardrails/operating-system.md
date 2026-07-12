# VCOS HQ Operating System

Purpose: define how VCOS HQ should function as an AI operating system for agency, project, and multi-agent work.

VCOS is tool-agnostic. Claude Code, Codex, GitHub, Obsidian, ClickUp, Drive, and future agents are interfaces over the same headquarters memory and execution protocol.

Canonical architecture: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/ai-os-second-brain-architecture.md`.

## Model

VCOS HQ is two layers, one system:

- **Second Brain**: remembers.
- **AI OS**: acts.

Those two layers map to four operating steps:

1. Context: compact memory, decisions, active priorities, domain interfaces.
2. Connections: ClickUp, Drive, GitHub, calendar, comms, CRM, revenue systems, meeting transcripts.
3. Capabilities: SOPs, skill candidates, active skills, deterministic scripts, agent workflows.
4. Cadence: daily briefings, blocker sweeps, approval sweeps, recurring routines, dashboard buttons.

Build in that order. Cadence before context creates noisy automation. Capabilities before approval gates create risk. Connections before source-of-truth rules create duplicated memory.

## Mindset Rules

### Default Shift

Before doing repetitive work manually, ask:

- Can an agent do 30% of this?
- Can a deterministic workflow do the boring part?
- Is this a one-time task, a repeated SOP, or an automation candidate?

### Function Breakdown

Break large agency work into reusable chunks:

- Intake.
- Research.
- Triage.
- Draft.
- QA.
- Approval.
- Handoff.
- Follow-up.

Automate chunks before trying to automate the whole workflow.

### Curiosity Rule

Do not accept agent output blindly. Ask why the system chose an approach when risk is high, behavior is unclear, or an automation may repeat.

When a mistake repeats, update:

1. `1_Command_Brain_Core/1.2_Headquarters_Memory/decisions.md`
2. `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/state.md`, if it creates a blocker
3. `AGENTS.md` or the relevant domain README, if it needs a prevention rule

## Seven Connection Buckets

Use these buckets when deciding what VCOS should know or reach:

| Bucket | VCOS default source |
| --- | --- |
| Revenue | Project files first; finance tools only after explicit integration |
| Customers / clients | ClickUp and Drive; CRM only with approval-aware access |
| Calendar | Google Calendar when connected |
| Comms | Current thread, ClickUp comments, Slack/Telegram/Gmail only when connected |
| Tasks | ClickUp command rooms |
| Meetings | Meeting transcripts or summaries, stored as project/domain artifacts |
| Knowledge | VCOS Markdown, Drive, domain READMEs, curated wiki notes |

Do not connect everything at once. Start with the highest-leverage, lowest-risk source.

## Daily Loop

Morning:

- Read active outcomes.
- Check blockers.
- Check approvals waiting.
- Pick agent-executable next actions.
- Decide what needs human taste or approval.

During work:

- Route through the smallest interface.
- Use skills only when the task matches a proven workflow.
- Save outputs where future agents will look.

End of day:

- Capture new decisions.
- Compress raw tool output into facts, IDs, links, blockers, and next actions.
- Update skill candidates if a process repeated.

## Weekly Level-Up

Run a weekly VCOS level-up:

- What did we do 3+ times?
- What felt manual, boring, or copy/paste?
- What did a smart assistant need too much explanation to do?
- What would break if lead volume doubled?
- Which approval bottlenecks slowed delivery?
- Which skill should be promoted, deprecated, or tightened?

Save results to `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/four-c-audit.md` or the relevant skill candidate note.

## GitHub Role

GitHub should provide:

- Version history.
- Issues for enhancement packets.
- Pull requests for risky or reviewable changes.
- A remote source for cloud routines.

Do not store secrets in GitHub. Use `.env` locally and cloud environment variables for remote routines.

## Obsidian Role

Obsidian should provide:

- Human-friendly navigation.
- Visual backlinks.
- Second-brain browsing.
- Manual note review.

Obsidian is not a second source of truth. It should open this folder as the vault.
