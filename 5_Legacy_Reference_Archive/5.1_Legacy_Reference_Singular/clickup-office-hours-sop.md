# ClickUp Office Hours SOP

Date: 2026-05-10

## Goal

Make ClickUp the operating cockpit for NeuralSync without turning it into another overloaded inbox. The system should let Umair speak messy context to Codex, have Codex route it through `key-workspaces.md`, and keep the team focused on a small number of active outcomes.

## What I Understand

The agency has three live operating layers:

- Production: reusable systems, templates, AI workflows, MCP/n8n infrastructure.
- Delivery: active client outcomes, proposals, demos, blockers, close paths.
- Q3 Command Center: Umair's personal/day-job/family/investment load so it does not leak into agency execution.

The problem is not lack of tasks. The problem is task entropy: too many lists, too many half-shaped tasks, and unclear distinctions between idea, priority, active work, and completed asset.

## Premises

1. A top-level task should represent an outcome, not a thought.
2. A subtask should exist only when a person or agent can own it.
3. A task without owner, due date, and next action is not active work; it is triage or backlog.
4. Production and Delivery must stay separate: Production builds the machine; Delivery runs the machine for clients.
5. Completed production tasks are portfolio assets, not clutter.
6. Codex should use `references/key-workspaces.md` first and ClickUp search second.

## Recommended Operating Model

### Command Rooms

Use only three default command rooms for daily orchestration:

| Command room | Use for | Active top-level cap |
| --- | --- | --- |
| `00 - Production Control Room` | reusable systems, templates, AI/MCP/n8n infrastructure | 5 |
| `00 - Delivery Control Room` | client work, proposals, demos, blockers, close paths | 3 active outcomes |
| `00 - Q3 Command Center` | Umair bandwidth: day job, personal logistics, investments, tools | 2 active personal/work lanes |

### Status Meaning

| Status | Meaning |
| --- | --- |
| Open | parked, triage, or scheduled but not being worked today |
| In Progress | active commitment with owner, due date, next action |
| Completed | shipped asset, finished outcome, or closed loop |

Do not use `In Progress` for "important someday." It means someone is actively moving it.

## Task SOP

Every top-level task must have:

- Outcome: what changes when this is done.
- Owner: one accountable person.
- Due date: real date, not vague urgency.
- Definition of done: checklist or subtasks.
- Decision point: what happens after completion.

Every subtask must have:

- Single owner.
- Due date when sequence matters.
- Clear deliverable.
- Parent task that explains why it exists.

## Routing SOP

When Umair gives messy context:

1. Read `/Users/umairkhalid/_VCOS_Headquarters/references/key-workspaces.md`.
2. Pick the default command room:
   - client/proposal/demo/blocker -> Delivery Control Room
   - reusable system/template/MCP/n8n/agent workflow -> Production Control Room
   - day job/personal/family/investment/tool-spend -> Q3 Command Center
3. If it is a new outcome, create one top-level task.
4. If it supports an existing outcome, create a subtask.
5. If unclear, create or update a triage task; do not create a new list.

## Weekly Review SOP

Run this once per week.

1. Production:
   - Is anything in progress without a deadline?
   - Did any completed task become a reusable portfolio asset?
   - Are there more than 5 top-level tasks in progress?

2. Delivery:
   - Which client outcomes move cash, demo, or close date this week?
   - Which open opportunities need owner/date or should be parked?
   - Are there more than 3 active delivery outcomes?

3. Q3:
   - What is actively using Umair's brain this week?
   - What should stay open but not active?
   - What can be delegated to Codex/Claude/team?

## Daily Codex Prompt

Use this when starting a work session:

```text
Read key-workspaces.md and review the three command rooms. Tell me:
1. what is active,
2. what is blocked,
3. what needs my decision,
4. what Codex/Claude/team can execute next.
Do not create new tasks unless I approve.
```

## Add-New-Work Prompt

Use this when capturing chaos:

```text
Route this into ClickUp using key-workspaces.md. Consolidate into existing outcomes where possible. Create a top-level task only if it is a new outcome; otherwise create subtasks/checklists. Add owner, due date, next action, and definition of done.
```

## Office Hours Advice

The failure mode is not under-planning. The failure mode is letting every idea become its own object. The discipline is: outcomes at the top, execution underneath, and only three rooms for daily attention.

The narrowest useful wedge is this: for the next two weeks, only manage work through the three command rooms. If something cannot fit into Production, Delivery, or Q3, it is probably not ready to become active work.

## Assignment

For the next 7 days, run one daily review:

- Keep Production at no more than 5 in-progress top-level tasks.
- Keep Delivery at no more than 3 in-progress client outcomes.
- Keep Q3 at no more than 2 in-progress personal/day-job lanes.
- Anything else becomes Open, a subtask, or a checklist item.

