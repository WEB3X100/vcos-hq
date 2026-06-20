# VCOS Automation Registry

Purpose: track routines that can become buttons, cron jobs, heartbeats, or ClickUp-controlled workflows.

Buttons and automations may draft, summarize, analyze, test, or prepare. They must not send external messages, mutate CRM/customer data, publish content, spend money, deploy capital, or delete production data without explicit approval.

| Routine | Interface | Frequency | Owner | Inputs | Outputs | Approval needed before action | Last tested | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Daily Briefing | heartbeat or ClickUp recurring task | Daily, 8:00 AM America/Toronto | Sentinel | `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/state.md`; `1_Command_Brain_Core/1.2_Headquarters_Memory/active-context.md`; `1_Command_Brain_Core/1.2_Headquarters_Memory/key-workspaces.md`; ClickUp blockers if available | Active outcomes, blockers, human decisions, next actions, approval queue | Yes, if posting to external/client-visible surfaces | Not tested | candidate |
| Daily Command Brief | manual, then heartbeat candidate | Daily start of work | Sentinel | Fast path; `1.3_Knowledge_Graphs/registry.md`; relevant project README/source capsule; Graphify query if graph exists; GBrain search if cross-HQ memory needed; ClickUp read path when verified | Today mode, active outcomes, best first action, blockers, approvals, agent-executable next actions | Yes before external/client-visible posting or task mutation | Tested manually for AgentOSync on 2026-06-10 | candidate |
| Hermes read-only night brief | Hermes cron or manual dry run | Nightly candidate | Sentinel / Night Operator | Fast path; approved project source capsules; Graphify/GBrain approved sources; Git/ClickUp read-only state when configured | Overnight findings, draft next actions, blockers, review queue, touched files/tasks | Yes before any write, external send, CRM mutation, publishing, spending, deletion, or deployment | Not tested | blocked: Hermes source scopes and read-only runner not configured |
| Active blocker sweep | dashboard button or heartbeat | Daily or on demand | Sentinel | `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/state.md`; ClickUp blockers if available | Blocker summary and recommended owner/action | Yes, before changing ClickUp/client-visible statuses | Not tested | candidate |
| Approval queue sweep | dashboard button or heartbeat | Daily or on demand | Sentinel | `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/approval-gates.md`; active ClickUp/Slack/Telegram approvals if available | List of waiting approvals and recommended decisions | Yes, before executing any gated action | Not tested | candidate |
| Employee 01 mock missed-call test | manual command or dashboard button | On demand during dealership demo prep | Builder with Sentinel gate | `2_Domain_Packs/2.1_Dealerships_Domain_Pack/README.md`; `2_Domain_Packs/2.1_Dealerships_Domain_Pack/employee-01-front-desk.md`; mock lead data | Draft recovery response, booking path, and QA notes | Yes, before external communication or CRM mutation | Not tested | candidate |
| Reference migration index check | manual command | Weekly until migration completes | Sentinel | `5_Legacy_Reference_Archive/5.1_Legacy_Reference_Singular/`; `5_Legacy_Reference_Archive/5.2_Legacy_References_Plural/`; existing 1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/1_Command_Brain_Core/1.2_Headquarters_Memory/domain files | Migration index and archive recommendations | Yes, before deletion, overwrite, or archive moves | Not tested | candidate |
| Four C audit | manual, then weekly heartbeat candidate | Weekly | Sentinel | `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/four-c-audit.md`; `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/connections-map.md`; `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/vcos-task-skill-map.md`; `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/automation-registry.md` | Scorecard updates, gaps, next actions | Yes, before creating external tasks or changing integrations | Not tested | candidate |
| Weekly level-up interview | manual | Weekly | Sentinel | `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/operating-system.md`; recent work summaries | Skill candidates, automation candidates, repeated pain points | Yes, before packaging/deploying new automations | Not tested | candidate |
| Weekly work review + skill harvest | Codex cron automation `weekly-work-review-skill-harvest`; Claude Code companion prompt at `1_Command_Brain_Core/1.4_Agent_Context_Packets/claude-project/automation-prompts/weekly-work-review-and-skill-harvest.md`; Claude/team ClickUp task `86e1w6343` | Weekly, Sunday 6:30 PM America/Toronto | Sentinel | Fast path; Claude weekly-review context packet; latest Sunday Office Hours/session brief; recent session briefs and project handoffs; `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/weekly-skill-harvest.md`; ClickUp task `86e1w6343` when local file access is unavailable | Short weekly status update; misses/blockers/decisions; next 3 actions; repeated workflow and skill-candidate recommendations | Yes, before posting externally, mutating ClickUp/CRM/client data, publishing, packaging, or deploying automations | Scheduled 2026-06-15; Claude context packet added 2026-06-15; ClickUp task created 2026-06-15 | active |
| GitHub issue triage | manual or dashboard button | On demand | Sentinel | Private VCOS HQ repo issues once created | Issue routing, labels, recommended next changes | Approval before closing issues or pushing changes | Not tested | blocked: GitHub repo not initialized |
| VCOS Employee template cleanup | manual GitHub issue/PR workflow | On demand | Sentinel + Builder | `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/vcos-employee-template-strategy.md`; `https://github.com/WEB3X100/VCOS-Employee` | Refactor plan, template files, reviewable PR | Approval before pushing repo changes or changing template contract | Repo inspected 2026-05-13 | candidate |

## Interface Definitions

- `button`: user-triggered from mission-control or future dashboard.
- `cron`: detached scheduled job.
- `heartbeat`: current-thread follow-up or briefing.
- `ClickUp`: human-visible task or recurring task.
- `manual`: no automation yet.

## Status Definitions

- `candidate`: plausible but not fully tested.
- `active`: tested and approved for routine use.
- `paused`: intentionally disabled.
- `blocked`: cannot run until an integration, approval path, or dependency is resolved.
- `retired`: no longer needed.
