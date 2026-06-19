# Dealership Inception Demo

Purpose: first internal demo build for `Employee 01: Front Desk`.

## Prompt

```text
Read AGENTS.md. Enter 2_Domain_Packs/2.1_Dealerships_Domain_Pack/. Execute the Inception Demo build in Plan Approval Mode.
```

## Demo Scenario

Your Choice Autos receives a missed call at 9:00 PM on Saturday from a lead interested in a vehicle.

The agent must recover the lead without violating approval gates.

## Five-Minute Journey

```text
Minute 0:
Lead calls after hours and reaches voicemail or missed-call capture.

Minute 1:
Agent drafts immediate response, qualifies intent, and asks for vehicle preference, budget, trade-in, and availability.

Minute 3:
Agent proposes a test-drive slot using dealership appointment rules.

Minute 5:
Agent drafts GM summary with lead details, urgency, requested vehicle, recommended next action, and approval request.
```

## Required Outputs

- Lead qualification summary
- Draft SMS/email response
- Draft test-drive booking request
- GM Monday summary
- Approval request payload for Slack/Telegram/ClickUp
- CRM update draft, not executed

## Approval Gates

Human approval required before:

- Sending customer message
- Confirming booking
- Updating CRM
- Mentioning pricing, financing, trade-in value, or guarantees

## Build Boundary

Plan Approval Mode means:

- Do not send external messages.
- Do not mutate CRM.
- Do not publish.
- Do not deploy.
- Prepare plan and draft artifacts only.

## Acceptance Criteria

- A dealership owner can understand the workflow in under 2 minutes.
- The approval gate is obvious and cannot be bypassed accidentally.
- The GM summary is useful on Monday morning.
- The workflow can be triggered from a phone approval surface.

