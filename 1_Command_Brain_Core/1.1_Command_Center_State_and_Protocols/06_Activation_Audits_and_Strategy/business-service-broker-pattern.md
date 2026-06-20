# Business Service Broker Pattern

Purpose: adapt the platform engineering lesson from internal developer platforms to AgentOSync and VCOS client workflows.

Atlassian-style platform thinking: developers should request capabilities through a broker instead of rebuilding infrastructure each time.

AgentOSync version: SMBs should request business outcomes through reusable workflow services instead of rebuilding automations each time.

## Mental Model

| Platform Engineering Pattern | VCOS / AgentOSync Pattern |
| --- | --- |
| Open Service Broker | Workflow Broker |
| Provisioning request | Business workflow request |
| SQS worker | n8n, Trigger.dev, Modal, or background worker |
| DynamoDB state | Airtable, Supabase, Postgres, or ClickUp state |
| Envoy templates | n8n templates, skill.md files, prompt templates, web templates |
| Envoy control plane | VCOS HQ orchestration layer |
| Proxy sidecars | Mini Intern agents and specialized services |
| CloudFormation/Packer | GitHub-backed deployment templates |
| Access logs/metrics | Dashboard signals, audit logs, and review packets |

## Runtime Options

Choose the execution layer based on the workflow's job:

| Option | Best For | Watchouts |
| --- | --- | --- |
| Claude Code local | Repo work, operator-driven builds, direct debugging | Local session ends when operator stops; context can bloat |
| Managed Agents | API-driven product features, one-off async analysis, low-infra prototypes | Reactive by default; scheduling/heartbeat usually needs another layer |
| Agent SDK + Trigger.dev | Scheduled/proactive workflows with retries and observability | Requires code and deployment discipline |
| OpenClaw/Hermes style self-hosting | Multi-channel personal or business assistants with heartbeat/cron | More DevOps and security ownership |
| n8n | Business workflow routing, webhook glue, approvals, integrations | Should be worker layer, not the whole brain |

VCOS should choose a runtime explicitly. Do not assume every agent needs the same infrastructure.

## Workflow Broker Request

Every reusable workflow should be expressible as:

```text
Service name:
Client / proof lane:
Requested outcome:
Input channels:
State store:
Worker / automation layer:
Agents involved:
Output packet:
Approval gate:
Success metric:
Failure mode:
Rollback / fallback:
```

## Control Plane Rule

VCOS HQ is the control plane. It stores:

- workflow definitions
- routing rules
- approval gates
- reusable templates
- schemas
- runbooks
- decisions
- blockers

VCOS HQ does not store:

- raw WhatsApp exports
- raw CRM/customer records
- full scrape dumps
- long logs
- secrets or API keys
- noisy chat histories

## Amax Application

Service: Amax Forms + WhatsApp Insights Dashboard

- Inputs: forms, WhatsApp messages, call notes, manual updates.
- State store: Airtable or approved client data store.
- Worker: n8n or equivalent workflow layer.
- Agents: Ops Mini Intern, Sales Mini Intern, Reviewer/QA, Infrastructure.
- Outputs: form field map, WhatsApp data map, dashboard signals, sentiment labels, quote/follow-up packets.
- Approval: required before WhatsApp sends, CRM mutation, public/client-facing claims, or external report delivery.
- Success: Thursday-ready review packet and dashboard signal design.

## Barber Shop Application

Service: AI Front Desk Booking Demo

- Inputs: inbound call, services, hours, booking rules, customer name, phone number, preferred time.
- State store: demo sheet, Airtable, or booking-system sandbox.
- Worker: voice agent workflow plus n8n handoff if needed.
- Agents: Sales Mini Intern, Ops Mini Intern, Reviewer/QA.
- Outputs: call script, booking handoff packet, test call scenarios, acceptance criteria.
- Approval: required before calling prospect, using live number, calendar mutation, or presenting pricing.
- Success: prospect-ready demo flow that proves missed-call capture and booking handoff.

## Design Implication

Do not build one-off automations as isolated toys. Build them as services that can become:

- a ClickUp task template
- an Airtable schema
- an n8n workflow template
- a skill.md file
- a demo page
- a deployment checklist

## Maintenance Rule

The first version is easy. Safe change over time is the product.

Every service needs:

- owner
- source of truth
- schema
- logs
- health check
- failure mode
- approval gate
- review cadence
- documentation

## Agent Lifecycle Rule

For hosted or deployable agents, track:

- agent version
- environment version
- session/run ID
- tools/MCP servers enabled
- skills attached
- memory stores or state sources
- permission policy
- last successful run
- known failure modes
- owner and approval surface

If an agent changes tools, prompt, skills, permissions, or memory access, treat that as a new version and record what changed.
