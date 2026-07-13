# VCOS HQ Claude Code Guide

VCOS HQ is the headquarters operating system for agency, project, and domain-pack work.

Claude Code should treat this repo as the command brain, not as a raw document dump.

## Fast Path

Before doing work, read these files in order:

1. `AGENTS.md`
2. `1_Command_Brain_Core/1.2_Headquarters_Memory/ubiquitous_language.md`
3. `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/state.md`
4. `1_Command_Brain_Core/1.2_Headquarters_Memory/active-context.md`
5. `1_Command_Brain_Core/1.2_Headquarters_Memory/key-workspaces.md`

Then load the smallest relevant interface:

- HQ operations: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/operating-system.md`
- Power AI usage: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/claude-power-user-playbook.md`
- Session/context discipline: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/session-context-discipline.md`
- Recursive self-improvement: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/recursive-self-improvement-loop.md`
- Strategic prompting: `1_Command_Brain_Core/1.2_Headquarters_Memory/prompting-principles.md`
- Workflow architecture: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/business-service-broker-pattern.md`
- Managed/runtime evaluation: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/managed-agent-runtime-evaluation.md`
- Hermes + SuperGrok persistent agent playbook (profiles, sessions, crons, scanner, memory seeding, Imagine/TTS): `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/hermes-supergrok-vcos-playbook.md`
- Approval gates: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/approval-gates.md`
- Automations: `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/automation-registry.md`
- Skills: `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/vcos-task-skill-map.md`
- Claude Project context packets: `1_Command_Brain_Core/1.4_Agent_Context_Packets/claude-project/README.md`
- Domain work: `2_Domain_Packs/<domain>/README.md`
- Arsenal (stuck on a task / "what do I have for X"): `6_Arsenal/README.md` → `6_Arsenal/arsenal-index.md`

Do not start with broad repository scans. Do not load `5_Legacy_Reference_Archive/5.1_Legacy_Reference_Singular/`, `5_Legacy_Reference_Archive/5.2_Legacy_References_Plural/`, raw captures, logs, or implementation folders unless the fast path points there.

## Operating Contract

Every session should answer internally:

- What outcome is requested?
- Which command room or domain owns it?
- What is the smallest context file needed next?
- Does this require human approval?
- Where should outputs be saved or linked?

## Default Behavior

- Use progressive context loading.
- Draft before acting externally.
- Keep active memory small.
- Save raw/noisy material outside active memory.
- Promote SOPs into skills only after repeated value.
- Record durable decisions in `1_Command_Brain_Core/1.2_Headquarters_Memory/decisions.md`.
- Update `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/state.md` when blockers or next actions change.

## Revenue-First Execution

Do not let VCOS architecture work replace revenue motion.

Current compounding loops:

1. Dealership OS Delivery Loop: real client/team build, scraper, Airtable schema, Marketplace posting, QuickBooks cleanup, dashboard/control output.
2. Amax Internal Proof Loop: real sales-team usage and one structured before/after proof asset.
3. Content Intel Loop: monitor trusted AI/SME signals and draft approval-gated content in Umair's voice.
4. Employee Repo + Skill Loop: workflows proven 3+ times become packaged employee repos/skills.

Claude Code is the primary builder for these loops. Arsenal tools are parked unless they remove a blocker from the active sprint.

Before expanding tools or routines, read `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/revenue-readiness-audit.md`. If shipped output, daily bottleneck, paid-pilot terms, Amax feedback, or variance risk is unknown, surface that as the blocker.

## Core Routines

Build and run these one at a time:

- `content-intel-routine`: source sweep, signal summary, and 3 approval-gated draft posts in Umair's voice.
- `morning-cockpit`: start-of-session brief with outcomes, blockers, approvals, next actions, and avoid list.
- `sprint-closer`: end-of-session handoff plus ClickUp-ready update held for approval.
- `skeptic-review`: QA pass before content, claims, proposals, workflow approvals, or public proof.
- `skill-packager`: package a workflow only after 3+ successful internal runs.
- `proof-packager`: turn approved internal proof into draft-only social/content assets.
- `employee-repo-updater`: improve employee repos from feedback, failed runs, or new use cases.

Current routine priority: build `content-intel-routine` first, then `sprint-closer`, then `skeptic-review`. Defer `morning-cockpit` until one focused lane needs a daily brief.

## Hermes PRD-to-Sprint Routing

For an approved engineering or product-delivery mission, use `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/candidates/hermes-prd-sprint-conductor/SKILL.md`. The required flow is outcome clarification, bounded Office Hours, code-grounded PRD, acceptance criteria, sprint contract, isolated worktree, implementation, completion audit, adversarial review, fresh verification, and draft PR. Status messages do not count as progress unless they link to a durable artifact or name a precise blocker.

## Claude Project Context

When using Claude Projects, add curated Markdown packets from `1_Command_Brain_Core/1.4_Agent_Context_Packets/claude-project/` instead of attaching broad folders or stale project dumps.

For weekly reviews, Claude must read `1_Command_Brain_Core/1.4_Agent_Context_Packets/claude-project/packets/vcos-weekly-review-context.md` before project-specific files. Latest Sunday Office Hours/session briefs and current `state.md` outrank old project plans, stale scoreboards, and historical execution packets.

If Claude's review anchors on a parked or stale lane, it should name the source conflict instead of pretending the older file is current truth.

## Power User Protocol

Claude/Codex should help Umair become a stronger AI operator over time, not just complete isolated tasks.

- Start substantial work by clarifying outcome, constraints, definition of done, and approval gates.
- Ask focused questions when context is missing; do not let vague requests produce vague work.
- Keep context lean. Prefer short summaries, links, IDs, schemas, and decisions over raw dumps.
- Treat long context as a liability. Use rewind for wrong turns, clear between missions, handoff before clearing, and sidecar agents for noisy research when available.
- Use plan-first execution for ambiguous, high-risk, client-facing, or architecture-sensitive work.
- Bake self-checks into the task list: tests, screenshots, readbacks, ClickUp verification, or review gates.
- Challenge weak prompts and outputs. Suggest a sharper question or framing when the current ask will waste time.
- Preserve durable lessons in the right file after repeated mistakes or repeated value.
- Treat VCOS HQ as the control plane. Raw data, logs, chats, and customer records live in ClickUp, Drive, Airtable, n8n, or client systems.
- Treat Claude Code as an agent runtime with commands, tools, memory, permissions, MCP, tasks, reviews, and context controls.
- For persistent memory, proactive cadence (cron/heartbeat), multi-session hygiene, profile/role specialization, artifacts second-brain, and messaging reach: use Hermes + SuperGrok (via Desktop for best UX). Seed with VCOS fast-path + ubiquitous language once; use dedicated sessions per lane; prune skills; apply reverse prompting for high-quality crons/routines. Follow the hermes-supergrok-vcos-playbook.md and managed-agent-runtime-evaluation.md (multi-channel + scheduled fits Hermes-style). Always respect Phase gates and human approval for anything beyond read-only/draft.
- Before adopting a hosted/managed agent runtime, validate current API docs and decide what owns scheduling, memory, permissions, observability, and approvals.

## Approval Gates

Stop for human approval before:

- Sending external or client-facing messages.
- Publishing public content or proposals.
- Mutating CRM/customer records.
- Spending money or increasing budgets.
- Deleting, overwriting, or making irreversible changes.
- Deploying capital or production-sensitive actions.

## Four C Lens

Use the VCOS AIOS sequence:

1. Context: what the agent knows.
2. Connections: what it can reach.
3. Capabilities: what it can produce or execute.
4. Cadence: when it acts without being manually prompted.

Never add cadence before context, connections, capabilities, and approval gates are clear.
