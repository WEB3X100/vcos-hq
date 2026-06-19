# ClickUp Operating Protocol

Purpose: keep ClickUp usable as an execution cockpit, not a task dump.

## Fast Lookup

1. Read `/Users/umairkhalid/_VCOS_Headquarters/references/key-workspaces.md`.
2. Use preferred list IDs directly.
3. Only call ClickUp hierarchy/search when a list is missing, ambiguous, or stale.

## Core References

- Skill leverage stack: `/Users/umairkhalid/_VCOS_Headquarters/references/skill-leverage-stack.md`
- VCOS + gstack architecture: `/Users/umairkhalid/_VCOS_Headquarters/references/vcos-gstack-architecture.md`
- Domain pack router: `/Users/umairkhalid/_VCOS_Headquarters/references/domain-pack-router.md`
- VCOS skill pack manifest: `/Users/umairkhalid/_VCOS_Headquarters/references/vcos-skill-pack-manifest.md`
- Drive sync SOP: `/Users/umairkhalid/_VCOS_Headquarters/references/drive-clickup-sync-sop.md`

## Default Routing

| Work type | List |
| --- | --- |
| 90-day priorities, personal logistics, day-job operating system, investments, tools | `00 - Q3 Command Center` |
| Client delivery, proposals, demos, blockers, close paths | `00 - Delivery Control Room` |
| Agent systems, MCP, n8n, reusable templates, AI production infrastructure | `00 - Production Control Room` |

## Task Shape

Use top-level tasks only for outcomes or operating lanes. Use subtasks for teammate-sized work.

Every agent-ready task should include:

- Outcome
- Definition of done
- Owner or owner placeholder
- Due date
- Links/assets needed
- Human approval checkpoint

## Anti-Overwhelm Rules

- Keep command rooms small.
- Consolidate related bullets into one task with a checklist.
- Promote a checklist item to a subtask only when another person or agent can own it.
- Archive or park stale tasks monthly; do not delete by default.
- Use weekly review tasks instead of creating new status-update tasks.

