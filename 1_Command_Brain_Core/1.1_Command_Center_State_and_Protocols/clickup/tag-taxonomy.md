# NeuralSync ClickUp Tag Taxonomy

Status: additive-only during restructure.

Purpose: make ClickUp searchable across folders so an agent can trace one business motion from build work to client proof to content to leads.

## Rules

- Add canonical tags without deleting existing tags.
- Never use tags as a substitute for the correct folder/list.
- Use lowercase kebab-case.
- Do not create duplicate spelling variants.
- If a task fits multiple tags, use all relevant tags.

## Client Tags

| Tag | Use |
| --- | --- |
| `amax` | Amax Travel work, internal proof lab, travel CRM/finance ops |
| `agentosync` | AgentOSync GTM, public proof engine, brand/revenue pipeline |
| `sameer` | Sameer dealership/client work |
| `usman` | Usman business development/proposal work |
| `cellmart` | Cellmart-related work |
| `alex-reed` | Alex Reed-related work |

## Vertical Tags

| Tag | Use |
| --- | --- |
| `dealership` | Dealership workflows, Employee 01 wedge, vehicle/service leads |
| `clinic` | Clinics, receptionist workflows, medical/dental lead ops |
| `restaurant` | Restaurant workflows and later vertical tests |
| `travel` | Travel agency, GDS, Systrix, Amax workflows |
| `real-estate` | Realtor, Zillow, property video, real estate workflows |

## Type Tags

| Tag | Use |
| --- | --- |
| `build` | Build task for systems, software, templates, automations |
| `automation` | n8n, Vapi, Make, workflows, trigger systems |
| `client-delivery` | Named client delivery work |
| `lead` | Prospect, lead, deal, outreach, proposal |
| `content` | Post, video, proof asset, social calendar |
| `ops` | Internal ops, team, finance, admin |
| `approval` | Waiting for or recording human approval |
| `blocked` | Cannot move without blocker resolution |

## Agent Tags

| Tag | Use |
| --- | --- |
| `sentinel` | Routing, approvals, handoffs, decision logs |
| `builder` | Implementation task |
| `skeptic` | Review, validation, adversarial QA |
| `kingmaker` | Content, proof, public narrative |

## System Tags

| Tag | Use |
| --- | --- |
| `n8n` | n8n workflows |
| `vapi` | Voice AI / Vapi workflows |
| `odoo` | Odoo CRM/accounting work |
| `airtable` | Airtable base, schema, control table |
| `github` | GitHub repo/issue/PR work |
| `higgsfield` | Higgsfield media generation |
| `claude` | Claude workflows, prompts, projects |
| `gpt` | GPT/OpenAI workflows, prompts, projects |

## Cross-Context Intelligence Prompt

Use this after tags are applied consistently:

```text
Trace Employee 01 from BUILD through any Amax proof work in CLIENTS, related proof/content in CONTENT, and dealership lead work in LEADS. Summarize the business narrative, current blockers, proof assets, and next three actions for AgentOSync.
```

