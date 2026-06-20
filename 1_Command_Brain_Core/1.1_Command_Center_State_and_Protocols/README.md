# Command Center State and Protocols

Purpose: this is the VCOS HQ operating control room. Read this file first when a task touches current state, approvals, cadence, ClickUp, Hermes, Mission Control, runtime architecture, or command-center strategy.

## Fast Router

| Task / question | Go to |
| --- | --- |
| What is alive, blocked, decided, or next? | `00_Live_State_and_GSD/state.md` |
| What is the vision, hard spec, or roadmap? | `00_Live_State_and_GSD/` |
| What requires human approval? | `01_Operating_Protocols_and_Guardrails/approval-gates.md` |
| What is the daily/weekly operating rhythm? | `01_Operating_Protocols_and_Guardrails/cadence-hooks.md` |
| What if a session is too noisy or long? | `01_Operating_Protocols_and_Guardrails/session-context-discipline.md` |
| Where do repeated failures or reusable wins go? | `01_Operating_Protocols_and_Guardrails/recursive-self-improvement-loop.md` |
| How should AI OS, Second Brain, Hermes, Grok, Graphify, or Obsidian work? | `02_AI_OS_Architecture_and_Runtime/` |
| Which runtime should own a workflow? | `02_AI_OS_Architecture_and_Runtime/managed-agent-runtime-evaluation.md` |
| Where are ClickUp, Drive, automation, GitHub, and connection notes? | `03_Execution_Surfaces_and_Integrations/` |
| Where is the live Mission Control dashboard and L1/L2 Hermes coordination? | `04_Mission_Control_Dashboard/mission-control/` |
| Where are office-hours briefs, critiques, weekly plans, and handoffs? | `05_Office_Hours_and_Session_Briefs/session-briefs/` |
| Where are revenue readiness, Arsenal activation, and strategic audit packets? | `06_Activation_Audits_and_Strategy/` |

## Numbered Rooms

| Room | Purpose | Default read |
| --- | --- | --- |
| `00_Live_State_and_GSD/` | Live GSD state: project, requirements, roadmap, blockers, decisions, next actions. | `state.md` |
| `01_Operating_Protocols_and_Guardrails/` | Approval gates, cadence, QA, context hygiene, secret handling, recursive improvement. | `approval-gates.md` or `operating-system.md` |
| `02_AI_OS_Architecture_and_Runtime/` | System architecture, Hermes/SuperGrok, managed runtimes, Obsidian, Graphify, Claude/Grok playbooks. | `ai-os-second-brain-architecture.md` |
| `03_Execution_Surfaces_and_Integrations/` | ClickUp, Drive, automations, integrations, connection maps, GitHub backup/audit notes. | `connections-map.md` |
| `04_Mission_Control_Dashboard/` | Dual-Hermes Mission Control, dashboard state, L1/L2 prompts, git coordination. | `mission-control/README.md` |
| `05_Office_Hours_and_Session_Briefs/` | Office-hours router, critiques, weekly plans, clickup payloads, handoff queue. | `session-briefs/README.md` |
| `06_Activation_Audits_and_Strategy/` | Revenue readiness, AI-native activation, Arsenal activation, business-service patterns, template strategy. | `revenue-readiness-audit.md` |

## Human Navigation

1. Start with `00_Live_State_and_GSD/state.md` if you need the current picture.
2. Use the router table above to enter exactly one numbered room.
3. Read that room's `README.md` when present.
4. Open only the smallest file that answers the task.
5. Do not dive into raw payloads, exports, or handoff archives unless the router points there.

## Agent Routing Rule

Read the HQ fast path from `AGENTS.md`, then this README, then the smallest matching room interface. Do not start with broad search. If a task asks for office hours, read `05_Office_Hours_and_Session_Briefs/session-briefs/README.md` before opening any brief. If a task asks about ClickUp, start in `03_Execution_Surfaces_and_Integrations/clickup/protocol.md` and respect the Airtable preservation gate.

## File Placement Rules

| New material | Save in |
| --- | --- |
| Live blocker, decision, next action, current state | `00_Live_State_and_GSD/state.md` |
| Durable command-center requirement | `00_Live_State_and_GSD/requirements.md` |
| Approval, QA, cadence, context, secret, or safety rule | `01_Operating_Protocols_and_Guardrails/` |
| Runtime architecture, AI OS design, memory/retrieval architecture | `02_AI_OS_Architecture_and_Runtime/` |
| ClickUp, Drive, GitHub, automation, connector, workspace ID | `03_Execution_Surfaces_and_Integrations/` |
| Mission Control dashboard state, L1/L2 prompt, dual-Hermes handoff surface | `04_Mission_Control_Dashboard/mission-control/` |
| Office-hours critique, weekly plan, handoff packet, ClickUp paste payload | `05_Office_Hours_and_Session_Briefs/session-briefs/` |
| Strategic activation packet, revenue readiness audit, reusable business pattern | `06_Activation_Audits_and_Strategy/` |

## Non-Negotiables

- Keep this folder token-friendly: route first, read narrowly, summarize noisy outputs.
- Preserve human approval gates before external sends, publishing, CRM mutation, spending, deletion, or production changes.
- Keep raw exports inside their owning subfolder; promote only decisions, blockers, IDs, links, and next actions into live state.
- If a file moves again, update `AGENTS.md`, `CLAUDE.md`, `HEADQUARTERS_MAP.md`, `Home.md`, `active-context.md`, and `key-workspaces.md` in the same pass.

