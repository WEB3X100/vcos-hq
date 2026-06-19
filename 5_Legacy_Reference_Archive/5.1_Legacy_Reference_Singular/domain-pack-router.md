# Domain Pack Router

Purpose: decide whether work belongs in VCOS HQ or a specialized domain pack.

## Routing Question

Ask: "Is this reusable headquarters capability, or client/domain execution?"

## VCOS HQ

Route to VCOS HQ when work is:

- Cross-client
- Strategic
- Operating-system related
- ClickUp/Drive/SOP orchestration
- Team workflow design
- Reusable across multiple clients
- About memory, routing, command rooms, or agent behavior

Default files:

- `/Users/umairkhalid/_VCOS_Headquarters/references/key-workspaces.md`
- `/Users/umairkhalid/_VCOS_Headquarters/references/clickup-operating-protocol.md`
- `/Users/umairkhalid/_VCOS_Headquarters/references/vcos-gstack-architecture.md`
- `/Users/umairkhalid/_VCOS_Headquarters/references/vcos-skill-pack-manifest.md`

## gstack-Travel

Route to `gstack-Travel` when work is:

- Specific to travel agency delivery
- Specific to Amax/Odoo/travel CRM
- Travel proposal/deck/itinerary related
- Travel lead follow-up
- Travel content calendar
- Travel client weekly reporting

Repo:

- `https://github.com/WEB3X100/gstack-Travel`

## ClickUp Bridge

Even when work is routed to a domain pack, ClickUp remains the execution record:

- Owner
- Status
- Due date
- Blockers
- Drive file links
- Decision history

## Anti-Drift Rule

If a domain-pack SOP becomes useful across multiple clients, promote the pattern back to VCOS HQ. If a VCOS HQ SOP becomes client-specific, copy a narrow version into the domain pack.

