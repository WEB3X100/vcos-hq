# Skill Leverage Stack

Purpose: define which Claude Code/gstack skills VCOS HQ and `gstack-Travel` should leverage, in what order, and why.

Source signal: Nate Herk video, "I Tried 100+ Claude Code Skills. These 6 Are The Best."

## Core Principle

Do not install or use every skill everywhere. Use a stack:

- VCOS HQ standardizes the operating protocol.
- `gstack-Travel` pilots client-facing execution workflows.
- Skills are framed as business outcomes, not technical toys.

## Recommended Stack

| Skill / capability | Use for us | Priority |
| --- | --- | --- |
| Skill Creator | Turn repeated SOPs into reusable VCOS/travel skills after 3+ uses | High |
| Review / Ultra Review | Quality gate before shipping code, automations, client-facing workflows | High |
| Context Mode | Keep long Claude Code sessions cheaper/cleaner, especially in client repos | High |
| Superpowers | Strong build discipline: plan, test, review for production automations | Medium-high |
| GSD | Larger implementation projects where sub-agents need clean context | Medium |
| ClaudeMem | Evaluate only if it complements gbrain/VCOS reference memory | Medium |
| Front-end Design | Landing pages, proposal visuals, dashboards, client demos | Medium-high |

## Adoption Order

1. Skill Creator
2. Review / Ultra Review
3. Context Mode
4. Superpowers
5. Front-end Design
6. GSD for larger builds
7. ClaudeMem only after deciding how it fits with gbrain

## VCOS HQ Usage

VCOS HQ should leverage:

- Skill Creator for `clickup-command-review`, `drive-clickup-sync`, `client-delivery-triage`, and future command-room SOPs.
- Context Mode or gbrain-style memory to reduce repeated context cost.
- Review / Ultra Review as the standard quality gate before shipping important code, automations, or client-facing workflows.
- Front-end Design for internal dashboards, command surfaces, proposal visuals, and demo assets.

## gstack-Travel Usage

`gstack-Travel` should leverage:

- Skill Creator for travel-specific SOPs.
- Superpowers for Odoo, CRM, workflow, and automation implementation discipline.
- GSD for larger travel automation builds where clean sub-agent context matters.
- Review / Ultra Review before client delivery.
- Front-end Design for travel proposal decks, landing pages, and demos.

## Outcome Language

Do not sell or position these as "skills." Sell outcomes:

- Save 10 hours/week.
- Reduce lead wastage.
- Avoid CRM mistakes.
- Speed up proposal creation.
- Make client delivery repeatable.
- Reduce rework before demos.

## Permanent Skill Rule

A SOP becomes a permanent skill only after it is reused and valuable.

Default threshold:

- Reused at least 3 times.
- Has a clear owner or recurring use case.
- Produces a repeatable output.
- Reduces time, cost, mistakes, or context load.

## Memory Rule

Avoid duplicate memory systems unless there is a clear token or retrieval benefit.

Current default:

- VCOS references + `key-workspaces.md` + gbrain-style memory are the baseline.
- ClaudeMem is an evaluation candidate, not a default installation.
- Context Mode is favored first for session hygiene and context compression.

## Quality Gate Rule

Use `/review` or equivalent review flow for routine changes.

Use `/ultra review` or multi-agent review only for high-risk work:

- Client-facing delivery.
- Payments/auth/data migrations.
- Automations that touch production systems.
- Major refactors.
- Workflows that clients will depend on operationally.

## Installation Policy

Do not install globally by default from a video recommendation. First decide:

- Is this for VCOS HQ, a client domain pack, or a one-off task?
- Is it already covered by gstack or existing VCOS SOPs?
- Will it reduce repeated work or add tool overhead?
- Is there a ClickUp task tracking the adoption?

## ClickUp Home

All skill-stack adoption work belongs in:

- `00 - Production Control Room`
- Parent bucket: `Q3 #3 — Production Infrastructure`

