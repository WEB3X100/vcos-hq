# VCOS + gstack Architecture

Decision: VCOS HQ is the command brain. `gstack-Travel` is one specialized travel-agency limb.

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
- Claude/gstack skill leverage policy

### gstack-Travel

Use for the travel-agency operating limb:

- travel CRM workflows
- Odoo/Amax workflows
- travel lead intake and follow-up
- travel content calendar
- proposal/deck generation for travel prospects
- client-specific SOPs
- travel-specific agent prompts and automations

## Guardrails

- Do not customize upstream gstack directly for a client.
- Do not put VCOS HQ protocols only inside a client repo.
- Do not let `gstack-Travel` become the headquarters.
- Prefer small domain packs and SOP files over large divergent forks.
- Every domain pack should link back to VCOS HQ command rooms.

## Skill Leverage

Reference: `/Users/umairkhalid/_VCOS_Headquarters/references/skill-leverage-stack.md`

VCOS HQ standardizes the skill stack. `gstack-Travel` pilots client-facing execution workflows.

