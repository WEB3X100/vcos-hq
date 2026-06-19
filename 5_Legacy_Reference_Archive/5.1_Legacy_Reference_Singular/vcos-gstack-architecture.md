# VCOS + gstack Architecture

Decision date: 2026-05-10

## Core Decision

VCOS HQ is the command brain. `gstack-Travel` is one specialized limb.

Do not let the travel fork become headquarters. Keep the travel fork connected to VCOS through SOPs, ClickUp, Drive, and repo links.

## Layer Model

```text
Upstream gstack
  -> generic AI-assisted work engine

VCOS HQ
  -> command brain, operating memory, cross-client orchestration

gstack-Travel
  -> travel-agency domain pack / specialized implementation limb
```

## Responsibilities

### Upstream gstack

Use for generic methodology and tooling:

- office-hours
- autoplan
- review
- qa
- ship
- investigate
- cso
- browser QA
- gbrain/setup primitives

### VCOS HQ

Use for headquarters-level orchestration:

- ClickUp command rooms
- Drive + ClickUp file sync
- Q3 priorities
- production systems
- active client delivery
- cross-client SOPs
- team operating protocols
- reusable agent workflows
- skill routing and memory shortcuts

### gstack-Travel

Use for the travel-agency operating limb:

- travel CRM workflows
- Odoo/Amax workflows
- travel lead intake and follow-up
- travel content calendar
- proposal/deck generation for travel prospects
- client-specific SOPs
- travel-specific agent prompts and automations

## Connection Points

| Connection | Source of truth |
| --- | --- |
| Work ownership/status | ClickUp |
| Working files/assets | Google Drive |
| Code and skills | GitHub repos |
| Operating protocols | VCOS HQ references |
| Client-specific execution | client domain pack, e.g. `gstack-Travel` |

## ClickUp Rule

VCOS HQ command rooms stay primary:

- Production Control Room
- Delivery Control Room
- Q3 Command Center

Client/domain forks should be referenced from these rooms, not used as the main operating brain.

## First VCOS HQ Skill/SOP Candidates

Installed local skill:

- `vcos-command-router`: `/Users/umairkhalid/_VCOS_Headquarters/.agents/skills/vcos-command-router/SKILL.md`

Skill/SOP manifest:

- `/Users/umairkhalid/_VCOS_Headquarters/references/vcos-skill-pack-manifest.md`

First candidates:

1. `vcos-command-router`
2. `clickup-command-review`
3. `drive-clickup-sync`
4. `production-control-room`
5. `client-delivery-triage`
6. `q3-command-center`
7. `repo-domain-pack-router`

## First gstack-Travel Skill/SOP Candidates

1. `travel-crm-intake`
2. `travel-lead-followup`
3. `travel-proposal-deck`
4. `amax-odoo-crm`
5. `travel-content-calendar`
6. `travel-client-weekly-brief`

## Guardrails

- Do not customize upstream gstack directly for a client.
- Do not put VCOS HQ protocols only inside a client repo.
- Do not create one fork per idea.
- Prefer small domain packs and SOP files over large divergent forks.
- Every domain pack should link back to VCOS HQ command rooms.

## Active ClickUp Task

`VCOS HQ command brain + gstack-Travel specialized limb architecture`

Task URL: `https://app.clickup.com/t/86e1acj09`

## Completion State

Completed deliverables:

- Base/shared/client-specific architecture documented.
- Upstream gstack vs VCOS HQ vs gstack-Travel responsibilities defined.
- First VCOS HQ skill/SOP list created.
- First gstack-Travel skill/SOP list created.
- `gstack-Travel` repo link recorded.
- ClickUp command room and Drive folder rules connected through SOP references.
- Local VCOS HQ command-router skill installed.
