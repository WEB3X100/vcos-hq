# Dealership + AMAX Working Session - 2026-06-12

Status: Internal operating brief. Draft-only for external/client-facing use.

## Session Objective

Move two active proof lanes forward without adding new infrastructure:

1. Dealership OS: turn the working operations/listing demo into a stronger sales lead manager and daily intelligence demo.
2. AMAX / Travel OS: convert completed QuickBooks COA cleanup work into CFO-approved implementation next steps.

## Lane 1: Dealership OS

Primary ClickUp list: `03 Dealership MVP Sameer & Uzair` (`901714231386`)  
Primary MVP task: `Operationalize Dealership AI Command Layer MVP` (`86e1p1gqj`)  
Sales demo task: `Sales Demo` (`86e1v95hu`)

### Current Proof

The demo is no longer theoretical. Screenshots in `3_Project_Workspaces/3.6_Sameer_Uzair_Dealership_Operating_System/Demo/` show:

- HermesBot receives WhatsApp vehicle intake.
- Hermes parses a 2020 Toyota Corolla LE listing.
- Inventory is saved as `Pending Review`.
- Marketplace draft fields are generated.
- Photos are attached.
- Facebook Marketplace returns a posted/selling URL.

This is enough for an operations/listing manager demo and a CEO "talk to Hermes, see posted listings" moment.

### Sales Demo Gap

The next demo should not re-prove listing creation. It should prove lead/revenue control after listings go live.

Current empty Sales Demo subtasks:

- `Morning brief based on their videos and their Competitor` (`86e1v95km`)
- `Sales lead manager from marketplace` (`86e1v9b3t`)

### Recommended Sales Demo Shape

Show the dealership owner:

1. Posted or ready listing exists.
2. Marketplace/social lead arrives.
3. Hermes turns the inquiry into a lead record.
4. Hermes tags intent: hot, warm, low intent, duplicate, spam, financing question, appointment request.
5. Hermes drafts a reply but does not send without approval.
6. Morning brief summarizes:
   - yesterday's new leads,
   - unanswered messages,
   - stale leads,
   - best vehicle to push today,
   - competitor pricing/posting signals,
   - one suggested content/listing idea.

### Build Next

1. Define `Marketplace Lead` schema in Airtable:
   - source, vehicle, buyer name, message, intent, lead temperature, next action, owner, status, last touch, approval needed.
2. Create Hermes parser examples:
   - "Is this still available?"
   - "What's your best price?"
   - "Can I finance?"
   - "Can I come today?"
   - "Trade-in possible?"
3. Create morning brief prompt:
   - inputs: new Marketplace leads, stale leads, active inventory, recently posted videos, competitor examples.
   - output: owner-ready daily brief, 5 bullets max, with approval-gated suggested replies.
4. Create a fake/sanitized demo packet for one day:
   - 3 marketplace leads,
   - 2 competitor examples,
   - 1 video/post idea,
   - 1 stale lead alert.

### Demo Script

```text
We already proved the listing manager: Hermes can take a WhatsApp vehicle intake, draft the listing, attach photos, and get it posted.

The next part is the sales manager:
Every morning, the owner asks Hermes what happened yesterday.
Hermes shows which listings got leads, who needs follow-up, which buyer is hot, what reply is waiting for approval, and what competitor signal matters today.

Nothing sends without approval. The point is not automation for its own sake. The point is that no lead or listing goes invisible.
```

### Approval Gates

- No real customer lead data in local files without approval.
- No live outbound replies without approval.
- No public posts or marketplace publishing beyond approved/demo scope.
- No pricing, financing, warranty, or guarantee language without human approval.

## Lane 2: AMAX / Travel OS

Primary ClickUp task: `[Amax] Finance + Sales Control Tower v1 — DB | Hermes | GBrain | Tooljet | Quickbooks` (`86e1d5ky4`)  
Current focus task: `00_Clean Quickbooks` (`86e1t6n5w`)  
Critical next task: `[Amax] 1. Define DB + QuickBooks data map for Hermes/ToolJet` (`86e1d5kyj`)

Integration boundary: do not mix Odoo, Airtable, or n8n into this v1 finance-control path.

Clean architecture:

`QuickBooks -> Hermes -> DB/Postgres -> ToolJet dashboard -> WhatsApp response control`

### Current Proof

The QuickBooks COA audit/rebuild is complete according to ClickUp comments:

- 87 existing accounts audited.
- 74-account upgraded COA produced.
- 23 Systrix integration questions documented.
- 27-step weekly AR/AP/Cash close checklist created.
- Critical issues identified/fixed in the model:
  - Amax USA AP sub-accounts.
  - Hajj/Umrah deferred revenue.
  - Distributor commission accounts.
  - AR split by product line.

### CFO Meeting Objective

Use the completed workbook and `docs/cfo-quickbooks-cleanup-brief-2026-06-12.md` to get approval on:

1. Upgraded COA direction.
2. Deferred revenue treatment for Hajj deposits.
3. TICO Trust Account restriction.
4. Which flagged accounts Sara may rename/split/delete.
5. Whether TrySoft/Sohaib can proceed to QuickBooks -> DB -> Hermes -> ToolJet mapping.

### AMAX Next Build

1. Extract Sheet 3 priority Systrix questions:
   - Q1 sync method.
   - Q18 QB sync format.
   - Q19 Class/Department tagging.
   - Q20 COA mapping UI.
2. Build a mapping table for:
   - ticket invoice,
   - service fee,
   - BSP cost,
   - Umrah invoice,
   - Hajj deposit/installment,
   - Amax USA vendor bill.
3. Map each transaction type to:
   - QB account number,
   - DB table and field name,
   - Hermes fetch/command path,
   - ToolJet dashboard field,
   - approval owner,
   - exception rule.

### Draft Before / After Proof

Before: AMAX had a QuickBooks structure that could not cleanly support Systrix, weekly AR/AP visibility, product-line P&L, or reliable deferred revenue handling.

After: the finance OS now has a CFO-reviewable upgraded COA, Systrix question set, class/department design, and weekly close checklist that can become the finance control tower foundation after Maaz approval.

Result to validate: AMAX can move from manual finance cleanup to a weekly control process with clear ownership, exception review, and dashboard-ready data.

## Session Priority

1. Dealership: write the Sales Lead Manager + Morning Brief spec/demo packet.
2. AMAX: use CFO feedback to approve or revise the QuickBooks cleanup path.
3. Do not start new tools or dashboards until these two artifacts are reviewable.

## Suggested ClickUp Comment Payloads

Hold for Umair approval before posting.

### Dealership Sales Demo

```text
Working-session recommendation:

Operations/listing demo is now strong enough: Hermes can intake vehicle info, save inventory, generate Marketplace fields, attach photos, and return a posting URL.

Next sales demo should focus on lead/revenue control after listings go live:
1. Marketplace lead intake.
2. Lead temperature / intent classification.
3. Approval-gated reply draft.
4. Morning brief from leads + videos + competitor signals.
5. Stale lead/listing delay alert.

Suggested next artifact: sanitized one-day sales demo packet with 3 Marketplace leads, 2 competitor examples, 1 video/post idea, and 1 owner morning brief.
```

### AMAX Finance Control Tower

```text
Working-session recommendation:

QuickBooks COA audit/rebuild is complete. Next critical path is CFO approval + Systrix mapping.

Need Maaz/CFO approval on:
1. Upgraded COA direction.
2. Deferred Revenue approach for Hajj/Umrah deposits.
3. TICO Trust Account restriction.
4. Which flagged accounts Sara may rename/split/delete.

Next TrySoft/Sohaib action:
Build QuickBooks -> DB -> Hermes -> ToolJet mapping for ticket invoices, service fees, BSP cost, Umrah invoices, Hajj deposits/installments, and Amax USA vendor bills.
```
