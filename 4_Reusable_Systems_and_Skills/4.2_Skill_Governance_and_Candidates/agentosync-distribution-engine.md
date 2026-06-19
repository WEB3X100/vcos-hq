# AgentOSync Distribution Engine

Status: reusable SOP candidate  
First proof lane: AMAX Umrah inquiry desk  
Created: 2026-06-12

## Purpose

Create AI-native distribution desks for existing businesses that already have services, inventory, fulfillment, and sales capacity. AgentOSync operates a measurable acquisition and qualification channel, routes qualified leads to the partner business, and earns commission or rev-share on tracked closed revenue.

## Pattern

```text
Existing business supply
  -> AgentOSync market signal capture
  -> offer/funnel/intake
  -> qualified lead packet
  -> partner sales or fulfillment team
  -> tracked close
  -> commission / rev-share
  -> feedback loop
```

## When To Use

Use this when a client has:

- a real service or inventory already being sold.
- a sales or fulfillment team that can handle qualified demand.
- clear buyer intent in the market.
- willingness to track source and outcome.
- willingness to define commission, bounty, or rev-share terms.

Do not use this when:

- fulfillment is unclear or unreliable.
- the client cannot respond to leads quickly.
- attribution cannot be tracked.
- the offer is regulated and the approval/compliance owner is unknown.
- the client expects AgentOSync to absorb all sales risk without data access, response SLA, or commission agreement.

## Required Inputs

- Partner business and offer lane.
- Approved services or inventory.
- Lead qualification fields.
- Handoff owner.
- Response SLA.
- Attribution rules.
- Commission model.
- Approval owner for external messages and public assets.
- Data handling boundary.

## Standard Outputs

- Distribution desk spec.
- Lead packet template.
- Lead ledger schema.
- Commission agreement inputs.
- Fictional dry-run results.
- Partner review packet.
- Weekly signal and feedback note.

## First Implementation: AMAX

AMAX proof lane:

- Service: Umrah inquiry desk.
- Partner: AMAX Travel.
- AgentOSync job: find demand, qualify inquiries, prepare handoff packets, track source/outcome.
- AMAX job: approve offer language, contact leads, quote, book, fulfill, confirm close status.
- Source spec: `3_Project_Workspaces/3.7_AMAX_Travel_Operating_System/specs/amax-distribution-desk-v0.md`

## Promotion Criteria

Promote this SOP into a packaged VCOS skill only after:

- 3 qualified-lead pilots across AMAX or another client.
- attribution is tested without disputes.
- at least one handoff reaches partner sales successfully.
- approval gates are stable.
- the lead packet template saves meaningful time or prevents mistakes.

## Approval Gates

Human approval is required before:

- external email, WhatsApp, SMS, DM, or customer message.
- public landing page, post, ad, video, or proof story.
- use of partner brand/name in public.
- CRM, booking, accounting, or customer record mutation.
- paid ad/API/phone/WhatsApp/provider spend.
- final pricing, package, travel-policy, legal, refund, cancellation, finance, or commission terms.
- storing sensitive customer, payment, passport, visa, booking, or raw conversation records.

## Reusable Mini Interns

| Mini Intern | Role |
| --- | --- |
| Market Signal Scout | Finds demand signals and pain language from approved channels |
| Offer Builder | Turns approved service lanes into draft funnel/CTA/intake copy |
| Lead Qualifier | Scores and structures inquiries |
| Handoff Agent | Prepares partner-ready lead packets |
| Attribution Clerk | Tracks source, state, close, and commission |
| Feedback Analyst | Converts wins/losses/objections into next experiments |
| Skeptic | Reviews compliance, privacy, claims, and approval gates |

