# VCOS Headquarters Map

> Main foundation map for `_VCOS_Headquarters`.
> Last Updated: 2026-05-20

This file is the first navigation layer for VCOS HQ. It tells an agent what the headquarters is, how to load context without flooding itself, and where to allocate new information so it becomes reusable.

VCOS HQ is an Obsidian-style neural network for cross-client work, Mini Intern development, reusable skills, and operating memory. The goal is not to store everything everywhere. The goal is to route each piece of information to the smallest durable home where future agents can find it again.

## Prime Directive

When new information arrives, classify it before storing it:

1. Is it live state, a decision, a blocker, a project brief, a client artifact, a reusable workflow, a skill candidate, a domain pattern, or raw reference?
2. Which command room or domain owns it?
3. Does it belong in durable memory, active project context, a domain pack, a reusable skill system, the arsenal, or the legacy archive?
4. Does it require human approval before external action?
5. What is the smallest file that should be updated so future agents can reuse the information?

Do not dump raw context into memory. Compress first. Store decisions, facts, links, IDs, owners, next actions, and reusable patterns.

## Mandatory Fast Path

Before doing HQ work, read these files in order:

1. `AGENTS.md`
2. `1_Command_Brain_Core/1.2_Headquarters_Memory/ubiquitous_language.md`
3. `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/state.md`
4. `1_Command_Brain_Core/1.2_Headquarters_Memory/active-context.md`
5. `1_Command_Brain_Core/1.2_Headquarters_Memory/key-workspaces.md`

Then load only the domain or project interface needed for the request.

## System Shape

```text
_VCOS_Headquarters/
|
├── AGENTS.md
├── CLAUDE.md
├── HEADQUARTERS_MAP.md
├── Home.md
├── README.md
|
├── 1_Command_Brain_Core/
│   ├── 1.1_Command_Center_State_and_Protocols/
│   ├── 1.2_Headquarters_Memory/
│   ├── 1.3_Knowledge_Graphs/
│   └── 1.4_Agent_Context_Packets/
|
├── 2_Domain_Packs/
│   ├── 2.1_Dealerships_Domain_Pack/
│   ├── 2.2_Travel_Domain_Pack/
│   ├── 2.3_Clinics_Domain_Pack/
│   └── 2.4_Content_Domain_Pack/
|
├── 3_Project_Workspaces/
│   ├── 3.1_AgentOSync_Revenue_Pipeline/
│   ├── 3.2_Project_Briefs/
│   ├── 3.3_Ethnic_Apparel_Gem_Client_Workspace/
│   ├── 3.4_Workplace_AI_Trading_Coach/
│   ├── 3.5_YC_Startup_Intelligence_Tracker/
│   ├── 3.6_Sameer_Uzair_Dealership_Operating_System/
│   ├── 3.7_AMAX_Travel_Operating_System/
│   ├── 3.8_Premium_FDE_Applied_AI_Target/
│   └── 3.9_King_of_the_Glass_Padel_Tournament/
|
├── 4_Reusable_Systems_and_Skills/
│   ├── 4.1_VCOS_Employee_OS_Template/
│   ├── 4.2_Skill_Governance_and_Candidates/
│   ├── 4.3_Department_Skill_Packs/
│   ├── 4.4_Validated_Marketplace_Skills/
│   └── seedance-loop-prompt/
|
├── 5_Legacy_Reference_Archive/
│   ├── 5.1_Legacy_Reference_Singular/
│   └── 5.2_Legacy_References_Plural/
|
└── 6_Arsenal/
    └── arsenal-index.md
```

## Root Files

| File | Purpose | When To Read Or Update |
| --- | --- | --- |
| `AGENTS.md` | Hard operating instructions for agents inside HQ. | Read first. Update only for durable agent behavior rules and negative constraints. |
| `CLAUDE.md` | Claude/Codex operating context and route map. | Read when using Claude Code or improving agent behavior. Keep lean. |
| `HEADQUARTERS_MAP.md` | Neural navigation and allocation map. | Read before routing data. Update when folders, allocation rules, or Mini Intern surfaces change. |
| `Home.md` | Obsidian home note and human navigation entry. | Use for human-friendly navigation. |
| `README.md` | Public-ish explanation of the HQ structure. | Use for onboarding or broad repo orientation. |

## Folder Map

| Folder | Role | Main Goal | What Belongs Here | What Does Not Belong Here |
| --- | --- | --- | --- | --- |
| `1_Command_Brain_Core/` | Headquarters brain | Keep VCOS coherent across clients, domains, agents, tools, and approvals. | State, decisions, protocols, routes, workspace IDs, approval rules, current operating context. | Raw research dumps, client files, implementation details, reusable skill packages. |
| `2_Domain_Packs/` | Vertical limbs | Store reusable industry/domain knowledge and execution interfaces. | Dealership, travel, clinic, and content domain patterns, SOPs, schemas, workflows, constraints. | One-off client files unless they are generalized into a domain pattern. |
| `3_Project_Workspaces/` | Active project context | Keep active projects moving with compact briefs and deliverables. | AgentOSync, Amax, Ethnic Apparel Gem, project briefs, execution notes, demo assets. | Reusable cross-client systems after they mature. Move those to `4_*`. |
| `4_Reusable_Systems_and_Skills/` | Skill foundry | Turn repeated workflows into Mini Intern capabilities and marketplace assets. | Employee OS template, skill candidates, department skill packs, reusable SOPs, validated marketplace skills. | Raw client-specific context or unvalidated one-off experiments. |
| `5_Legacy_Reference_Archive/` | Historical archive | Preserve old material until reviewed and migrated. | Legacy files, duplicated references, historical exports. | Active context. Do not load by default. |
| `6_Arsenal/` | Swiss Army Knife | Curated tools, repos, APIs, frameworks, prompts, and gems. | Resource index with URLs, problem tags, and reusable tool references. | Full raw docs unless intentionally archived elsewhere. |

## Command Brain Core

### `1.1_Command_Center_State_and_Protocols/`

Live operational control layer.

| File Or Area | Purpose | Allocation Rule |
| --- | --- | --- |
| `project.md` | HQ vision and durable strategic north star. | Put long-lived “what VCOS is becoming” statements here. |
| `requirements.md` | Hard requirements and constraints. | Put non-negotiable system requirements here. |
| `state.md` | Current state, decisions, blockers, next actions. | Update when something changes the live operating picture. |
| `roadmap.md` | Sequencing and progress. | Use for ordered build plans and milestone movement. |
| `approval-gates.md` | Human approval rules. | Put rules for sends, publishing, CRM mutation, budgets, deployment, and risk. |
| `cadence-hooks.md` | Daily/weekly heartbeat patterns. | Put recurring briefing, review, and check-in routines here. |
| `ai-os-second-brain-architecture.md` | Two-layer VCOS architecture: Second Brain remembers, AI OS acts. | Read when designing GBrain, Obsidian, skills, automations, routines, or an operator console. |
| `automation-registry.md` | Automation inventory. | Put active/suggested automations, cron jobs, and scheduled work here. |
| `connections-map.md` | Tool and integration map. | Put connector/API/system relationship notes here. |
| `session-context-discipline.md` | Token/context operating discipline. | Use when sessions get long, polluted, expensive, or need a handoff. |
| `managed-agent-runtime-evaluation.md` | Runtime selection rubric. | Use before choosing local Claude, managed agents, Trigger.dev, OpenClaw/Hermes, n8n, etc. |
| `clickup/` | ClickUp planning and preservation material. | Store ClickUp restructure plans, IDs, import snapshots, and task-system decisions. |
| `drive/` | Drive routing notes. | Store Drive folder/file routing notes, not full Drive exports. |

### `1.3_Knowledge_Graphs/`

Graphify and lightweight graph/RAG control layer.

| File Or Area | Purpose | Allocation Rule |
| --- | --- | --- |
| `README.md` | Knowledge graph folder interface. | Read before adding generated graph/wiki/Obsidian files. |
| `registry.md` | Approved graph sources, graph paths, import paths, owners, and query rules. | Update whenever a project/domain graph is built, refreshed, or retired. |
| `imports/` | Quarantined Graphify wiki/Obsidian exports. | One removable subfolder per source. Do not redistribute generated node files across HQ by default. |
| `summaries/` | Curated summaries promoted from graph imports. | Store durable summaries only, not raw graph JSON dumps. |

### `1.4_Agent_Context_Packets/`

Curated Markdown packets for Claude Projects, Claude Code, Hermes profiles, and other agent runtimes.

| File Or Area | Purpose | Allocation Rule |
| --- | --- | --- |
| `README.md` | Packet shelf interface. | Read before adding agent-facing context packets. |
| `claude-project/` | Claude Project and Claude Code context packets, automation prompts, and templates. | Store small curated files Umair can attach to Claude Projects; prefer source links over copied context. |

### `1.2_Headquarters_Memory/`

Compact durable memory.

| File | Purpose | Allocation Rule |
| --- | --- | --- |
| `ubiquitous_language.md` | Shared vocabulary. | Add terms only when they will be reused across agents/projects. |
| `active-context.md` | Compact current focus. | Update with only the current focus, architecture, and risk. |
| `decisions.md` | Durable decision log. | Add decisions that should shape future work. Include date and reason. |
| `key-workspaces.md` | IDs, repos, folders, command rooms. | Add stable workspace IDs, URLs, repo paths, and routing anchors. |
| `prompting-principles.md` | How Umair should prompt and guide agents. | Add reusable prompt habits and question patterns. |

## Domain Packs

Domain packs are deep modules. Read the domain `README.md` first. Only enter `implementation/` if the request requires deeper context.

| Domain | Folder | Goal | Route Here When |
| --- | --- | --- | --- |
| Dealerships | `2_Domain_Packs/2.1_Dealerships_Domain_Pack/` | Build Employee 01: Front Desk and dealership automation workflows. | The work involves missed calls, test drives, CRM follow-up, dealership leads, appointment booking, or AVAPI dealership use cases. |
| Travel | `2_Domain_Packs/2.2_Travel_Domain_Pack/` | Support Amax/travel agency systems and travel workflows. | The work involves Amax, forms, WhatsApp collection, travel CRM, itineraries, customer insights, Odoo, dashboards, or travel operations. |
| Clinics | `2_Domain_Packs/2.3_Clinics_Domain_Pack/` | Prepare healthcare/clinic workflows. | The work involves clinic intake, appointment workflows, patient communications, or healthcare SMB automation. |
| Content | `2_Domain_Packs/2.4_Content_Domain_Pack/` | Store content strategy and production patterns. | The work involves LinkedIn video, YouTube SME research, short-form hooks, content calendars, scripts, proof assets, or creative systems. |

## Project Workspaces

Project workspaces are active execution areas. Use them when the work is specific to a current initiative, client, or demo.

| Workspace | Goal | Route Here When |
| --- | --- | --- |
| `3.1_AgentOSync_Revenue_Pipeline/` | AgentOSync sales, GTM, demos, and revenue pipeline execution. | The work is for AgentOSync acquisition, demos, outbound, public funnel, website proof, or client pipeline. |
| `3.2_Project_Briefs/` | Compact briefs for active projects. | A project needs a clean top-level brief that future agents can read quickly. |
| `3.3_Ethnic_Apparel_Gem_Client_Workspace/` | Active client workspace for Ethnic Apparel Gem / PakTextile. | The work is client-specific to this account, marketplace build, manufacturer feedback drip, brand context, or demo handoff. |
| `3.4_Workplace_AI_Trading_Coach/` | Trading coach and personal trading performance systems. | The work involves trading behavior, coach mode, strategy bot design, watchlists, alerts, or trading workflow instrumentation. |
| `3.5_YC_Startup_Intelligence_Tracker/` | YC/startup research and intelligence tracking. | The work involves YC cohorts, startup scoring, early-company research, brief generation, or venture thesis tracking. |
| `3.6_Sameer_Uzair_Dealership_Operating_System/` | Sameer & Uzair dealership operating system. | The work involves their dealership MVP, appraisal workflow, sales/ops coordination, lead handling, pilot packaging, or demo-to-client handoff. |
| `3.7_AMAX_Travel_Operating_System/` | AMAX/Maaz travel operating system. | The work involves AMAX finance control tower, QuickBooks cleanup, travel ops, dashboards, forms, distribution leads, or Maaz executive visibility. |
| `3.8_Premium_FDE_Applied_AI_Target/` | Umair career, AI-Native ERP Consultant OS, Lattice evidence, and FDE brand. | The work involves Senior Consultant proof, John review, ERP implementation evidence, public-safe professional content, resume, or FDE target assets. |
| `3.9_King_of_the_Glass_Padel_Tournament/` | Padel tournament and sponsor assets. | The work involves King of the Glass event planning, sponsor decks, tournament materials, or related event execution. |

## Reusable Systems And Skills

Use this area when a workflow is becoming repeatable beyond one client.

| Area | Goal | Route Here When |
| --- | --- | --- |
| `4.1_VCOS_Employee_OS_Template/` | Generic deployable Mini Intern / Employee OS template. | The work improves the reusable employee skeleton, memory, skills, approvals, deployment assets, or GitHub-backed employee repo. |
| `4.2_Skill_Governance_and_Candidates/` | Skill foundry control system. | A repeated workflow needs registration, evaluation, owner assignment, promotion rules, or marketplace readiness tracking. |
| `4.3_Department_Skill_Packs/` | Department capability libraries. | A capability belongs to Marketing, Sales, Ops, Finance, Reviewer QA, Infrastructure, Marketplace, or Approval/Future. |
| `4.4_Validated_Marketplace_Skills/` | Packaged/validated reusable skills. | A workflow has been tested and is ready to package as “install this repo/skill and your Mini Intern can do X.” |
| `seedance-loop-prompt/` | Current reusable Seedance loop prompt skill. | The work involves seamless website background loops or Seedance prompt patterns. Eventually fold into Marketing pack governance if promoted. |

## Mini Intern Department Map

Every task should have exactly one owning intern, even if it hands off to another intern.

| Intern | Department Field | Owns | Default Folder |
| --- | --- | --- | --- |
| Marketing Mini Intern | `Marketing` | LinkedIn video, YouTube SME research, content hooks, Higgsfield prompts, Nano Banana images, Seedance clips, website creative, social campaigns, static artworks. | `4_Reusable_Systems_and_Skills/4.3_Department_Skill_Packs/marketing/` |
| Ops Mini Intern | `Operations` | n8n maps, website/testimonial updates, CMS/webhook specs, CRM-safe logging, reporting, data quality, dashboards, WhatsApp/forms insights. | `4_Reusable_Systems_and_Skills/4.3_Department_Skill_Packs/ops/` |
| Sales Mini Intern | `Sales Ops` | Lead qualification, Upwork proposals, LinkedIn DM drafts, call handoff packets, Trojan Horse partner outreach, AVAPI booking demo sales flow. | `4_Reusable_Systems_and_Skills/4.3_Department_Skill_Packs/sales/` |
| Infrastructure Intern | `Infrastructure` | Employee OS skeleton, repo templates, deployment notes, `.env.example`, API setup notes, runtime selection, GitHub sync. | `4_Reusable_Systems_and_Skills/4.3_Department_Skill_Packs/infrastructure/` |
| Reviewer / QA Intern | `Reviewer QA` | Claim checks, script scoring, handoff review, factual accuracy, risk review, quality gates. | `4_Reusable_Systems_and_Skills/4.3_Department_Skill_Packs/reviewer-qa/` |
| Marketplace Intern | `Marketplace` | Packaging successful workflows into reusable installable skills and templates. | `4_Reusable_Systems_and_Skills/4.3_Department_Skill_Packs/marketplace/` |
| Approval / Decisions Layer | `Approval` | Human approval gates, final execution authority, high-risk decisions. | `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/approval-gates.md` |
| Future Systems | `Future` | TV Network/R&D Pod, Trojan Horse partnerships, future wedge experiments. | `3_Project_Workspaces/3.2_Project_Briefs/` until validated, then move to domain/skill area. |

## Data Allocation Router

Use this table when new material is thrown into HQ.

| Incoming Material | Put It Here | Also Update |
| --- | --- | --- |
| New live priority, blocker, or operating status | `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/state.md` | `active-context.md` if it changes current focus. |
| Durable strategic decision | `1_Command_Brain_Core/1.2_Headquarters_Memory/decisions.md` | `state.md` if it affects active work. |
| New term/framework used across VCOS | `1_Command_Brain_Core/1.2_Headquarters_Memory/ubiquitous_language.md` | Relevant skill/domain README if operational. |
| Workspace ID, repo URL, ClickUp ID, Drive folder | `1_Command_Brain_Core/1.2_Headquarters_Memory/key-workspaces.md` | Relevant project/domain file. |
| Human approval rule | `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/approval-gates.md` | `AGENTS.md` if it becomes mandatory behavior. |
| Prompting or Claude Code power-user habit | `1_Command_Brain_Core/1.2_Headquarters_Memory/prompting-principles.md` | `claude-power-user-playbook.md` or Employee template if reusable. |
| Graphify graph, wiki, Obsidian export, or graph report | `1_Command_Brain_Core/1.3_Knowledge_Graphs/` | Update `registry.md` and the owning project/domain README source capsule. |
| Curated Markdown context for Claude Projects, Claude Code, Hermes, or other agent runtimes | `1_Command_Brain_Core/1.4_Agent_Context_Packets/` | Link canonical files and update `CLAUDE.md` or `automation-registry.md` when relevant. |
| Long session handoff/context reset guidance | `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/session-context-discipline.md` | Employee template session discipline if it applies to Mini Interns. |
| Repeated failure, repeated correction, or reusable win | `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/recursive-self-improvement-loop.md` | Update the relevant skill, domain README, project manifest, tracker, or decision log. |
| New client-specific file/context | Relevant folder under `3_Project_Workspaces/` | Link from ClickUp where applicable. |
| New industry/vertical insight | Relevant `2_Domain_Packs/<domain>/README.md` | Implementation folder only if detailed. |
| Raw transcript, PDF notes, copied article, or dump | Summarize first; store raw only in `5_Legacy_Reference_Archive/` or project implementation folder if needed. | Add compact summary to the active project/domain/skill file. |
| New tool, repo, API, framework, prompt pack, or gem | `6_Arsenal/arsenal-index.md` | Skill candidate map if used 3+ times. |
| Repeated workflow discovered in work | `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/skill-registry.md` | Department skill pack and `weekly-skill-harvest.md`. |
| Department capability for a Mini Intern | `4_Reusable_Systems_and_Skills/4.3_Department_Skill_Packs/<department>/capabilities.md` | `department-capability-map.md`. |
| Validated repeatable skill | `4_Reusable_Systems_and_Skills/4.4_Validated_Marketplace_Skills/ready-to-package/` | `promotion-rules.md` and skill registry. |
| GitHub-backed Employee OS improvement | `4_Reusable_Systems_and_Skills/4.1_VCOS_Employee_OS_Template/` | HQ skill governance if reusable across employees. |

## Project Routing Examples

| Request Type | Correct Route |
| --- | --- |
| “Update Amax forms and WhatsApp data collection insights” | Travel domain pack plus active project brief; Ops Mini Intern owns dashboards/logging. |
| “Prepare AVAPI barber shop demo” | AgentOSync revenue pipeline for sales/demo context; Sales Mini Intern owns booking flow; Ops owns workflow map if built. |
| “Create LinkedIn video using Higgsfield/Seedance/Nano Banana” | Marketing department skill pack and Content domain; Reviewer QA gates claims and quality. |
| “Package this as a reusable workflow” | Skill Governance first, then Department Skill Pack, then Marketplace Skills after validation. |
| “Show prospects what Mini Intern capabilities we have built/tested” | `3_Project_Workspaces/3.1_AgentOSync_Revenue_Pipeline/mini-intern-dashboard/`; keep client-safe and approval-gated. |
| “Make this intern/workflow improve itself over time” | `recursive-self-improvement-loop.md`; define sensors, policy, tools, QA, feedback, learning update, and re-test. |
| “Add a new useful repo/tool to my Swiss Army Knife” | `6_Arsenal/arsenal-index.md`; add problem tags and later promote if used repeatedly. |
| “Clean up or migrate old references” | `5_Legacy_Reference_Archive/`; do not delete without migration index and approval. |
| “Change ClickUp structure” | `1.1_Command_Center_State_and_Protocols/clickup/`; obey Airtable preservation snapshot gate first. |

## Obsidian Linking Rules

Use Obsidian links when they make navigation easier:

- Link root maps: `[[HEADQUARTERS_MAP]]`, `[[Home]]`, `[[README]]`.
- Link core state: `[[state]]`, `[[active-context]]`, `[[decisions]]`, `[[key-workspaces]]`.
- Link project briefs from `Home.md` and related domain READMEs.
- Do not create duplicate notes for the same concept. Update the canonical note instead.
- If a note becomes too large, split by ownership and leave a route link in the parent file.

## Context Loading Rules

- Start with the fast path.
- Load one domain/project README before reading implementation files.
- Prefer summaries over raw transcripts or copied articles.
- Use `rg` or `rg --files` before broad scans.
- Use sidecar/sub-agent/context-mode patterns for noisy research, large logs, repo audits, screenshots, and raw web data.
- If a session feels long, repetitive, or polluted, create a handoff using `session-context-discipline.md`, then clear or restart.

## Approval Rules

Agents may draft, analyze, summarize, and prepare. Human approval is required before:

- Sending external email, SMS, WhatsApp, Slack, Telegram, LinkedIn DMs, or client-facing messages.
- Publishing content, ads, landing pages, videos, or public assets.
- Mutating CRM/customer data.
- Spending money or increasing API/ad budgets.
- Deploying client-facing production workflows.
- Making destructive repo, filesystem, database, or ClickUp changes.
- Finalizing client-facing strategy, pricing, proposal terms, or claims.

Default mode is Draft-Only until approval is explicit.

## Numbering Rule

Use decimal sequence numbers that describe order and ownership:

- `1_*` is the command brain core.
- `1.1_*`, `1.2_*`, and deeper decimals are ordered subsystems.
- `2_*` is domain-pack execution.
- `3_*` is project workspace context.
- `4_*` is reusable systems and skill governance.
- `5_*` is legacy reference material awaiting migration.
- `6_*` is curated arsenal/tooling memory.

Every folder name should explain its purpose. Avoid metaphor-only names unless paired with a plain-language description.
