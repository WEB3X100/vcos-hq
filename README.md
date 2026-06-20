# VCOS Headquarters

VCOS Headquarters is the command brain for multi-project, multi-agent work across NeuralSync, client delivery, domain packs, and reusable AI production systems.

## Operating Model

```text
VCOS HQ
  -> command brain, memory, routing, protocols

Domain packs
  -> specialized limbs such as gstack-Travel, dealerships, clinics, content

Tools
  -> Claude, Codex, gstack, GSD, ClickUp, Drive, MCPs
```

## Folder Structure

The HQ workspace uses purpose-described chronological numbering:

```text
_VCOS_Headquarters/
├── AGENTS.md
├── CLAUDE.md
├── Home.md
├── README.md
├── 1_Command_Brain_Core/
│   ├── 1.1_Command_Center_State_and_Protocols/
│   └── 1.2_Headquarters_Memory/
├── 2_Domain_Packs/
│   ├── 2.1_Dealerships_Domain_Pack/
│   ├── 2.2_Travel_Domain_Pack/
│   ├── 2.3_Clinics_Domain_Pack/
│   └── 2.4_Content_Domain_Pack/
├── 3_Project_Workspaces/
│   ├── 3.1_AgentOSync_Revenue_Pipeline/
│   └── 3.2_Project_Briefs/
├── 4_Reusable_Systems_and_Skills/
│   ├── 4.1_VCOS_Employee_OS_Template/
│   └── 4.2_Skill_Governance_and_Candidates/
├── 5_Legacy_Reference_Archive/
│   ├── 5.1_Legacy_Reference_Singular/
│   └── 5.2_Legacy_References_Plural/
├── 6_Arsenal/
└── 7_VCOS_Interns/
    └── 7.1_NeuralSync_Marketing_Intern/
```

Root files and hidden/tooling folders stay at root because agents, Obsidian, and local skill tooling expect them there.

## Fast Start For Agents

Read these first, in order:

1. `AGENTS.md`
2. `1_Command_Brain_Core/1.2_Headquarters_Memory/ubiquitous_language.md`
3. `1_Command_Brain_Core/1.2_Headquarters_Memory/active-context.md`
4. `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/00_Live_State_and_GSD/state.md`
5. `1_Command_Brain_Core/1.2_Headquarters_Memory/key-workspaces.md`

Only read deeper files when the router or the task requires them.

## Source Of Truth

| Area | Source |
| --- | --- |
| Work ownership, deadlines, blockers | ClickUp |
| Working files, decks, sheets, docs | Google Drive |
| Operating rules and memory | VCOS HQ |
| Client/domain execution | Domain packs |
| Code and skill implementation | GitHub repos |

## Core Principle

Keep the main agent context small. Load interfaces first. Load implementation details only when needed.

## Key Protocols

- Operating system: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/01_Operating_Protocols_and_Guardrails/operating-system.md`
- Approval gates: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/01_Operating_Protocols_and_Guardrails/approval-gates.md`
- Adversarial review: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/01_Operating_Protocols_and_Guardrails/adversarial-review.md`
- Context Mode routing: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/01_Operating_Protocols_and_Guardrails/context-mode-routing.md`
- Cadence hooks: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/01_Operating_Protocols_and_Guardrails/cadence-hooks.md`
- Connections map: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/03_Execution_Surfaces_and_Integrations/connections-map.md`
- Four C audit: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/01_Operating_Protocols_and_Guardrails/four-c-audit.md`
- Obsidian second brain: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/02_AI_OS_Architecture_and_Runtime/obsidian-second-brain.md`
- VCOS Employee template strategy: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/06_Activation_Audits_and_Strategy/vcos-employee-template-strategy.md`
- Task-skill map: `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/vcos-task-skill-map.md`
- Dealership Inception Demo: `2_Domain_Packs/2.1_Dealerships_Domain_Pack/inception-demo.md`
