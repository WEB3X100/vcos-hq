# Dealerships Domain Pack

Dealerships is a specialized limb for auto dealership offers, demos, appraisals, voice AI, and lead management.

First commercial product: `Employee 01: Front Desk`.

## Interface

Use this domain for:

- Missed-call recovery
- After-hours lead qualification
- Test-drive booking
- Dealership appraisal MVPs
- Meta / Auto Trader ad-source workflows
- Voice AI dealership systems
- Dealer lead capture and follow-up
- Dealership proposal assets

## Inputs

- Dealer/client name
- Lead source
- Inventory/appraisal data
- CRM or sheet link
- Demo deadline
- Owner
- ClickUp task link

## Outputs

- Scoped MVP
- Demo script
- Lead workflow
- Follow-up automation
- Proposal or close path
- GM summary brief
- Approval-ready customer response draft

## First Wedge

Read:

1. `employee-01-front-desk.md` for the dealership MVP.
2. `inception-demo.md` for the first internal demo build.
3. `../../1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/approval-gates.md` before any client-facing action.
4. `../../1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/adversarial-review.md` before Gate 3 Human Approval.

Default approval mode is Draft-Only until the client authorizes automation.

## Sunday Ghost Town Interface

This domain's first production interface is:

```text
Missed weekend call
-> qualify lead
-> draft response
-> propose test-drive slot
-> request human approval
-> draft CRM update
-> GM summary
```

Inputs:

- Missed-call timestamp
- Caller name and phone
- Vehicle of interest
- Lead source
- Appointment availability
- Approval surface

Outputs:

- Approval-ready customer response
- Booking draft
- GM summary
- CRM update draft

## Prevention Rules

- Do not send customer messages without approval.
- Do not confirm bookings without approval.
- Do not mutate CRM without approval.
- Do not discuss pricing, financing, trade-in values, or guarantees unless approved by a human.
- Client-facing dealership decks must use trusted-partner language, not sales-coaching language. Avoid `Positioning`, `Sales framing`, `wow moment`, `pitch`, `close`, and conversion claims on slides.
- Do not use blurry screenshots or unreadable phone captures in dealership presentations. Replace them with clean diagrams, tables, queues, or workflow maps unless the screenshot is crisp at final slide size.
- Before sharing dealership PPT/PDF assets, render and inspect all slides for text overflow, cramped boxes, clipping, and client-facing final CTA quality.
- Do not read `implementation/` unless the task explicitly requires implementation details.

## Hidden Implementation

Do not read `implementation/` by default. Use the README interface first.
