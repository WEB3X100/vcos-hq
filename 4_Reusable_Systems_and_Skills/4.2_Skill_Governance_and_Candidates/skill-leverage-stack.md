# Skill Leverage Stack

Purpose: define which Claude Code/gstack skills VCOS HQ and domain packs should leverage, in what order, and why.

## Core Principle

Do not install or use every skill everywhere. Use a stack:

- VCOS HQ standardizes the operating protocol.
- Domain packs pilot client-facing execution workflows.
- Skills are framed as business outcomes, not technical toys.
- A workflow becomes a skill only after it has repeated value, a clear input/output packet, and approval gates.

## Recommended Stack

| Skill / capability | Use for us | Priority | Install & Activation | Reference |
| --- | --- | --- | --- | --- |
| Skill Creator | Turn repeated SOPs into reusable VCOS/domain skills after 3+ uses | High | `/plugin install skill creator` (official Anthropic) | Skill foundry framework; promote after 3+ uses |
| Review / Ultra Review | Quality gate before shipping code, automations, client-facing workflows | High | Built-in Claude Code 2.1.86+ (no install) | Use before Gate 3 approval; ultra for architecture/auth/payments |
| Context Mode | Keep long Claude Code sessions cleaner and cheaper | High | Plugin marketplace → restart Claude Code → `/contextmode:ctx-stats` to verify | Token-saving best practice; monitor savings |
| Superpowers | End-to-end build discipline for medium/complex coding: clarify, design, plan, execute, verify, review, finish | Medium-high | Plugin marketplace | Website workflow included (Nano Banana 2 + Kling hero-video recipe) |
| GSD | Larger builds where sub-agents need clean context | Medium | Plugin marketplace → `/gsd-help` after install | Sub-agent task decomposition; parallel work streams |
| ClaudeMem | Evaluate only if it complements existing memory | Medium | Plugin marketplace ONLY (do NOT run npm install) | Session handoff may supersede this; evaluate after 2 handoff uses |
| Front-end Design | Landing pages, proposal visuals, dashboards, client demos | Medium-high | Official (global install) OR Claude Design at claude.ai | B.R.A.N.D. framework for consistency; brand system + pitch deck + mobile + video |

## Adoption Order

1. Skill Creator
2. Review / Ultra Review
3. Context Mode
4. Superpowers
5. Front-end Design
6. GSD for larger builds
7. ClaudeMem only after deciding how it fits with current memory

## Superpowers Usage Rule

Use Superpowers for medium/complex code, automation, or client-delivery builds where wrong direction would be expensive.

Prefer it when the task needs:

- clarification before implementation
- design tradeoffs
- a written implementation plan
- test-driven development
- systematic debugging
- fresh verification before completion
- code review before merge/deploy
- worktree isolation

Skip or downshift it for:

- tiny one-file edits
- quick markdown updates
- low-risk note capture
- simple command output
- tasks where the 10-20 minute planning overhead is larger than the risk

Priority order remains:

1. Human instructions and approval gates
2. VCOS `AGENTS.md` / domain rules
3. Superpowers discipline
4. Default Claude behavior

Superpowers complements GSD and gstack:

- Superpowers constrains development process.
- GSD constrains context and execution isolation.
- gstack constrains role-based decision making.
- VCOS HQ constrains business routing, memory, departments, and approval gates.

## Outcome Language

Do not sell or position these as "skills." Sell outcomes:

- Save 10 hours/week.
- Reduce lead wastage.
- Avoid CRM mistakes.
- Speed up proposal creation.
- Make client delivery repeatable.
- Reduce rework before demos.

## Promotion Criteria

Promote a workflow into a permanent skill only when it meets most of these:

- Used successfully at least 3 times, or clearly needed across multiple clients.
- Has a named trigger and a narrow job.
- Has a structured input packet and output packet.
- Has explicit approval gates for external action, customer data, spend, and deployment.
- Saves time, reduces mistakes, improves quality, or reduces context load.
- Can be tested in isolation.
- Has a failure mode and fallback.

Do not promote raw ideas, one-off experiments, or tools that only seem interesting.
