# Department Capability Map

Purpose: show which Mini Intern owns which capabilities, tools, memories, and approval gates.

## Rule

Every capability has exactly one owning department. Other departments can consume its output through handoff packets, but they do not inherit its tools, secrets, or full context by default.

## Departments

| Department | Primary Job | Example Capabilities | Tools / Systems | Approval Gates |
| --- | --- | --- | --- | --- |
| Marketing | Create demand, proof, content, websites, and campaign assets | LinkedIn scripts, Higgsfield media, Seedance website hero loops, Nano Banana visuals, ICP/content strategy, campaign briefs | Higgsfield, Claude/Codex, Figma/Canva, GitHub/Vercel for demo sites | Public publishing, client proof, paid generation, public claims |
| Sales Ops | Convert qualified attention into conversations and proposals | LinkedIn DM drafts, Upwork proposal drafts, lead qualification, call handoff packets, Trojan Horse partner outreach | ClickUp, CRM, email/WhatsApp drafts, calendar links | External messages, calendar links, proposal terms, CRM mutation |
| Operations | Keep workflows, data, dashboards, and systems clean | n8n maps, Airtable/CRM logging, dashboard signals, testimonial/site updates, reporting | n8n, Airtable, ClickUp, CMS/webhooks, forms | CRM/customer data changes, website publishing, client reporting claims |
| Finance | Own revenue/admin finance automations | QuickBooks workflows, invoice/payment reconciliation, spend tracking, finance reports | QuickBooks, accounting exports, bank/payment systems where approved | Credential access, financial mutations, spend, invoice/customer finance actions |
| Reviewer QA | Reduce hallucination, claim risk, and context bias | Hook scoring, factual review, brand-fit review, handoff review, approval readiness checks | Claude/Codex review, rubrics, source packets | None for internal review; cannot override human approval |
| Infrastructure | Maintain deployable skeletons and runtime choices | `memory.md`, `skills.md`, `soul.md`, env templates, GitHub sync, Trigger.dev/Modal/n8n runtime notes | GitHub, Docker/VPS, Trigger.dev, Modal, n8n, CI/deploy tooling | Deployment, credential setup, destructive changes |
| Marketplace | Package validated workflows for reuse | Skill packaging, install notes, client-safe examples, versioning | GitHub, docs, demo assets | Marketplace/public release, pricing, client-facing claims |

## Cross-Agent Handoff Packet

Use short packets instead of raw chat history:

```markdown
## Handoff Packet

- Source department:
- Receiving department:
- Outcome:
- Funnel / workflow stage:
- Input data:
- Output requested:
- Source links:
- Claims requiring proof:
- Approval status:
- Deadline:
```

