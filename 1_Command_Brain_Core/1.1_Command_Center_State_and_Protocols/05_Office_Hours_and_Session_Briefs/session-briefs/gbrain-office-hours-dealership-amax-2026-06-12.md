# GBrain Office Hours - Dealership + AMAX

Date: 2026-06-12  
Status: Internal critique packet  
Mode: Solution Grill + Office Hours  
Scope: Dealership Sales Lead Manager / Morning Brief and AMAX Finance Control Tower

## Verdict

Build, but narrow both lanes harder.

- Dealership: build the sales lead manager around one fake/demo day and one owner morning brief. Do not widen into a full social-media intelligence product yet.
- AMAX: build the QuickBooks -> Hermes -> DB -> ToolJet path around one CFO-approved control view. Do not pull Odoo, Airtable, or n8n back into this v1 finance-control task.

## Hard Truth

Both lanes are close to looking impressive, but the risk is demo sprawl.

The dealership demo already has a real wow moment: Hermes takes vehicle intake and gets to a Marketplace posting. The sales demo will get weaker if it tries to prove every future capability. It gets stronger if it proves one owner pain: "what leads, listings, and follow-ups need my approval this morning?"

AMAX has a strong finance proof asset in the COA rebuild, but the team could easily blur the architecture again. The buyer/user will not care about every integration. They will care whether QuickBooks cleanup, AR/AP exceptions, and WhatsApp updates are visible and approval-safe from one dashboard.

## Sharper Version

### Dealership

Position it as:

```text
Hermes is the dealership's morning sales manager: it watches Marketplace leads, stale conversations, listing gaps, and competitor/content signals, then tells the owner what to approve today.
```

Do not sell it as "social media daily audit + ICP research + sales CRM + lead manager" in one breath. For the demo, all of that collapses into one owner brief with five bullets.

### AMAX

Position it as:

```text
Hermes turns QuickBooks into a finance control room: pull the latest finance state, flag AR/AP/cash exceptions, show them in ToolJet, and draft WhatsApp updates from the dashboard with approval.
```

Do not describe this as a broad finance/sales/marketing/travel ops integration yet. It is a CFO control wedge first.

## Proof Test

### Dealership 48-Hour Test

Create one demo run from `sales-demo-sanitized-day-packet-2026-06-12.md`:

1. Seed 3 Marketplace lead messages.
2. Link them to 2 demo inventory records.
3. Have Hermes classify intent and temperature.
4. Have Hermes draft approval-gated replies.
5. Generate one owner morning brief.
6. Rehearse the flow in under 4 minutes:
   - "listing is live"
   - "leads came in"
   - "Hermes prioritized them"
   - "replies are waiting for approval"
   - "here is what to post/fix today"

Pass condition: Sameer/Uzair can explain the value back as "we won't miss leads after posting cars."

### AMAX 48-Hour Test

Create one QuickBooks-control dry run with sanitized data:

1. Pick 6 finance records: 2 AR, 2 AP, 1 cash/reconciliation issue, 1 COA cleanup item.
2. Map each record to DB fields.
3. Define the ToolJet card/table fields.
4. Write Hermes output:
   - daily finance brief,
   - exception explanation,
   - recommended action,
   - WhatsApp update draft.
5. Mark each action as approval-required.

Pass condition: Maaz/CFO can say, "This is the dashboard I would check before asking Sara what needs cleanup."

## Approval Gates

### Dealership

- Real lead/customer data requires approval.
- Outbound replies require approval.
- Marketplace/social posting requires approval.
- Pricing, financing, warranty, trade-in, and guarantee language require approval.
- Client-facing pilot terms require approval.

### AMAX

- QuickBooks mutation requires CFO/human approval.
- ToolJet production deployment or live data connection requires approval.
- WhatsApp sends require approval.
- Public proof story requires AMAX approval.
- Customer, booking, payment, passport, visa, or finance data storage requires approved data-handling scope.

## Next Actions

1. Dealership: turn `sales-demo-sanitized-day-packet-2026-06-12.md` into the actual Hermes/Airtable test path for task `86e1v9b3t`.
2. Dealership: keep `Morning brief based on their videos and their Competitor` (`86e1v95km`) as the owner-brief output, not a separate research rabbit hole.
3. AMAX: create a one-page `QuickBooks -> DB -> ToolJet field map` for task `86e1d5kyj`.
4. AMAX: create one mock ToolJet dashboard layout with AR/AP/cleanup/WhatsApp approval columns before touching live QuickBooks.
5. After both demo packets run, record pass/fail notes in project handoffs and only then consider broader automation.

## Capture

Save this packet to:

- HQ session brief: this file.
- Dealership workspace handoff after test run.
- AMAX workspace handoff after field map/dry run.
- GBrain only after source scopes are cleaned; today GBrain search did not return fresh indexed results for the new artifacts.

## Do Not Build Yet

- Dealership: full competitor scraper, social-media intelligence engine, ICP research automation, or live reply sender.
- AMAX: Odoo, Airtable, n8n, public proof story, or production QuickBooks mutation.

## Office Hours Skill Validation

Result: useful. It forced the session away from tool sprawl and toward one proof packet per lane.

Next validation: after the Dealership sales demo and AMAX ToolJet dry run, compare whether this critique improved demo clarity or reduced scope drift.
