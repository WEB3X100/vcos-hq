# ClickUp Protocol

ClickUp is the execution ledger and approval surface for NeuralSync Agency. VCOS HQ is the operating brain. Airtable is the preservation and rollback layer for ClickUp restructuring.

## Current Safety Status

Status: restructure gated.

The live ClickUp space still uses the old structure as of the latest read-only check:

- `1. CRM`
- `2. Verticle Playbook`
- `3. Production Systems`
- `4. Client Delivery`
- `2. Client Onboarding`
- `5. Billing & Invoicing`
- `6. Client Feedback & Testimonials`
- `7. Internal Operations`
- `8. SOPs & Documentation`
- `✨ Template Guide`
- `Scope of Work`

Do not rename, move, merge, archive, or delete ClickUp folders/lists/tasks until the Airtable preservation snapshot has been imported and reviewed.

## Canonical Folder Model

After the preservation snapshot is complete, the target NeuralSync Agency structure is:

| Folder | Purpose |
| --- | --- |
| `01 · COMMAND — Strategy, Roadmap, Decisions` | Priorities, roadmap, approvals, decisions |
| `02 · BUILD — Systems, Automations, AI Employees` | Reusable systems, n8n, Vapi, AI employees, templates, skills |
| `03 · CLIENTS — Active Delivery and Accounts` | Named client delivery and active accounts |
| `04 · LEADS — Pipeline and Outreach` | Prospects, deals, proposals, outreach |
| `05 · CONTENT — Social, Media, and Proof` | Posts, videos, proof assets, social calendars |
| `06 · OPS — Team, Finance, and Admin` | Team, finance, tools, internal admin |
| `00 · ARCHIVE — Inactive Folders and Dead Lists` | Hidden inactive material; never delete during restructure |

## Final List Layout

### `01 · COMMAND`

- `00 · Weekly Priorities`
- `01 · Roadmap and Milestones`
- `02 · Decisions and Approvals`

### `02 · BUILD`

- `00 · Build Control Room`
- `01 · AI Employees and Skills`
- `02 · Automations and Workflows`
- `03 · Templates and Reference`

### `03 · CLIENTS`

- `00 · Delivery Control Room`
- `01 · Amax Travel`
- `02 · AgentOSync GTM`
- `03 · Other Active Clients`

### `04 · LEADS`

- `00 · Active Leads`
- `01 · Deals In Progress`
- `02 · Outreach and Proposals`

### `05 · CONTENT`

- `00 · Content Control Room`
- `01 · AgentOSync Social`
- `02 · Amax Social`

### `06 · OPS`

- `00 · Team and Standups`
- `01 · Finance and Tools`

## Preservation Rule

No ClickUp context may be intentionally omitted during restructure. Preserve:

- Full task description.
- Comments and comment history.
- Tags.
- Subtasks and nested subtasks.
- Checklists and completion states.
- Due dates and start dates.
- Assignees.
- Status.
- Priority.
- Time estimates.
- Attachments.
- Links.
- Custom fields.
- Original task name if a rename is needed.

If a ClickUp move risks losing context, stop and use manual migration from the ClickUp UI.

## Airtable Snapshot Gate

The Airtable base is named:

`NeuralSync ClickUp Preservation Snapshot`

Required tables:

- `Folders`
- `Lists`
- `Tasks`
- `Subtasks`
- `Checklists`
- `Tags`
- `Comments Index`
- `Attachments and Links`
- `Migration Map`
- `Verification Log`

Local import package:

`1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/clickup/airtable-preservation-snapshot/`

The restructure can proceed only after:

1. Airtable base is created.
2. All import tables are populated.
3. Sentinel verifies every active ClickUp task appears in Airtable.
4. Umair approves the snapshot as the rollback source.

## Routing Rules

Route by intent:

- Plan, decision, approval, weekly priority -> `01 · COMMAND`
- Reusable build, automation, AI employee, skill, template -> `02 · BUILD`
- Named client delivery -> `03 · CLIENTS`
- Prospect, lead, deal, proposal, outreach -> `04 · LEADS`
- Social, media, proof asset, calendar -> `05 · CONTENT`
- Team, tools, finance, internal admin -> `06 · OPS`

Personal/day-job tasks do not belong in NeuralSync Agency. They should be moved to Umair's private ClickUp space after preservation snapshot.

## Tag Taxonomy

Canonical tags are additive only. Do not remove old tags during migration.

Client tags:

- `amax`
- `agentosync`
- `sameer`
- `usman`
- `cellmart`
- `alex-reed`

Vertical tags:

- `dealership`
- `clinic`
- `restaurant`
- `travel`
- `real-estate`

Type tags:

- `build`
- `automation`
- `client-delivery`
- `lead`
- `content`
- `ops`
- `approval`
- `blocked`

Agent tags:

- `sentinel`
- `builder`
- `skeptic`
- `kingmaker`

System tags:

- `n8n`
- `vapi`
- `odoo`
- `airtable`
- `github`
- `higgsfield`
- `claude`
- `gpt`

## Pinned Context Tasks

Each control room list must have a pinned README/context task:

- `00 · Weekly Priorities`
- `00 · Build Control Room`
- `00 · Delivery Control Room`
- `00 · Active Leads`
- `00 · Content Control Room`
- `00 · Team and Standups`

Each pinned context task must include:

- List purpose.
- What belongs here.
- What does not belong here.
- Current sprint goal.
- Approval gates.
- Routing rules.
- Required task fields.
- Airtable snapshot link.
- VCOS HQ ClickUp protocol link.

Template file:

`1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/clickup/pinned-context-task-templates.md`

## Update Budget

Normal ClickUp usage:

1. Read the task once.
2. Execute work in the right workspace.
3. Add one compact update when a decision, blocker, approval request, or final deliverable exists.

Avoid using ClickUp for every intermediate thought or draft revision.

## Approval Gates

Umair approval is required before:

- External sends.
- Public publishing.
- CRM/customer mutation.
- Folder/list archive.
- Destructive action.
- Budget/tool spend decision.
- Moving personal/day-job tasks out of NeuralSync Agency.
- Finalizing the restructure after Airtable verification.

