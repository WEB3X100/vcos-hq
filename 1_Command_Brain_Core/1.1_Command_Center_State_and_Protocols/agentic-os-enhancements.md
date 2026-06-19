# VCOS HQ Agentic OS Enhancements

Source: YouTube transcript "Stop Using Claude Code Without an Agentic OS" shared on 2026-05-10.

## Takeaway

VCOS HQ already has the right backbone: fast-path memory, deep-module domains, approval gates, skill governance, and cadence hooks. The main enhancement is to make the operating system more visible and executable:

1. Map domains into a skill and automation registry.
2. Promote repeated SOPs into skill candidates after observed use.
3. Add an observability surface that can trigger approved routines and show system state.
4. Keep memory Markdown-first unless a retrieval problem proves a heavier RAG layer is worth it.

Canonical two-layer architecture: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/ai-os-second-brain-architecture.md`.

## Fit With Current VCOS

| Video concept | VCOS equivalent | Enhancement needed |
| --- | --- | --- |
| Agentic OS architecture | VCOS HQ command brain plus domain packs | Add a single domain-task-skill-automation map. |
| Domains | `2_Domain_Packs/<domain>/README.md` deep modules | Keep README interfaces as the contract. |
| Skills | `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/` and skill candidates | Track repeated SOP usage before promotion. |
| Automations | cadence hooks, cron/heartbeat jobs, ClickUp tasks | Create an automation registry with owner, approval gate, and run surface. |
| Memory layer | `1_Command_Brain_Core/1.2_Headquarters_Memory/`, `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/`, domain READMEs | Keep active memory compact; use raw/wiki/output style only for non-active artifacts. |
| Observability dashboard | mission-control / future command UI | Add buttons for safe routines and state panels for blockers, approvals, and active outcomes. |

## Proposed Architecture Additions

### 1. Domain Task Map

Create a lightweight registry that lists each domain, repeated tasks, candidate skills, and whether automation is justified.

Suggested file:

- `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/vcos-task-skill-map.md`

Minimum columns:

- Domain
- Task
- Trigger phrase
- Current SOP/source file
- Skill status: none, candidate, active, deprecated
- Automation status: manual, local, remote, blocked
- Approval gate
- Output destination

### 2. Skill Candidate Promotion Rule

Current rule says SOPs become skills after repeated value. Make that measurable:

- `1 use`: keep as notes or SOP.
- `2 uses`: mark as a skill candidate.
- `3+ successful uses`: package as a skill if it reduces time, mistakes, or context load.
- Any failed run: record the root cause before promotion.

Candidate skills should live under:

- `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/candidates/`

### 3. Automation Registry

Add a registry for routines that may become buttons, cron jobs, or thread heartbeats.

Suggested file:

- `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/automation-registry.md`

Minimum columns:

- Routine
- Interface: button, cron, heartbeat, ClickUp, manual
- Frequency
- Owner
- Inputs
- Outputs
- Approval needed before action
- Last tested
- Status

Initial routines to register:

- Daily Briefing at 8:00 AM America/Toronto.
- Employee 01 mock missed-call recovery test.
- Reference migration index check.
- Active blocker sweep.
- Approval queue sweep.

### 4. Observability Surface

The dashboard should not be a decorative layer. It should expose operational controls and state:

- Active outcomes.
- Blockers.
- Human approvals waiting.
- Safe runnable routines.
- Recent 1_Command_Brain_Core/1.2_Headquarters_Memory/roadmap changes.
- Skill candidate queue.
- Automation health.
- Domain status for dealerships, travel, clinics, and content.

Button rule:

- Buttons may draft, summarize, analyze, test, or prepare.
- Buttons must not send messages, mutate CRM, publish, spend, deploy capital, or delete production data without an explicit approval step.

### 5. Memory Layout Guardrail

The video recommends raw/wiki/output. VCOS should adopt the principle, not blindly rename the repo:

- `1_Command_Brain_Core/1.2_Headquarters_Memory/` remains compact active memory.
- `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/` remains live HQ operating state.
- `2_Domain_Packs/*/README.md` remains the deep-module interface.
- Raw or noisy artifacts should go to legacy/archive, project folders, or a future `workspace-artifacts/` area only when needed.
- Do not duplicate active state into a second Obsidian-style hierarchy unless it creates a clear retrieval or token benefit.

## Priority Sequence

1. Create `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/vcos-task-skill-map.md`.
2. Create `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/automation-registry.md`.
3. Register the Daily Briefing, blocker sweep, approval sweep, and Employee 01 mock test.
4. Add dashboard requirements to mission-control only after the registries exist.
5. Package the first real skill only after 3 successful observed uses.

## Non-Goals

- Do not install broad skill packs because the video mentions skills.
- Do not add a vector database or RAG layer until Markdown retrieval fails in a specific workflow.
- Do not turn the dashboard into the source of truth. ClickUp remains execution truth, Drive remains file truth, and VCOS memory remains routing truth.
- Do not automate client-facing sends, CRM mutations, publishing, or spending without approval gates.
