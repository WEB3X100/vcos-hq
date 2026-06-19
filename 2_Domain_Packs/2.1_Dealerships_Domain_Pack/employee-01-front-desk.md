# Employee 01: Front Desk

Purpose: dealership front-desk agent for missed-call recovery, lead qualification, appointment booking, and manager summaries.

## First Wedge

Sunday Ghost Town missed-call recovery and test-drive booking.

## Pain

Dealerships lose gross profit when after-hours or weekend calls go to voicemail. The wedge is mathematically provable and visceral: a lead calls while the team is unavailable, and the system recovers it before Monday.

## MVP Journey

```text
Minute 0: Lead calls after hours.
Minute 1: Agent answers or follows up, qualifies the lead, and captures intent.
Minute 3: Agent books or proposes a test-drive slot.
Minute 5: GM receives summary with lead details, urgency, requested vehicle, and next action.
Monday: Sales team sees booked appointments and recovered leads.
```

## Inputs

- Dealership name
- Phone/SMS provider
- CRM or lead sheet
- Inventory source
- Calendar / appointment rules
- GM or sales manager contact
- Approval surface: Slack or Telegram
- Escalation rules

## Outputs

- Qualified lead summary
- Draft SMS/email response
- Test-drive booking request or calendar event draft
- GM daily/weekly recovery brief
- CRM update draft

## Human Approval Rules

Until the client explicitly authorizes automation:

- Draft-only for external SMS/email.
- Draft-only for CRM record mutation.
- Human approval required before booking confirmation is sent.
- Human approval required before pricing, financing, trade-in, or guarantee language.

## Success Metrics

- Missed calls recovered
- After-hours leads contacted
- Test drives booked
- Response time
- Appointment show rate
- Gross profit recovered estimate

## First Demo Script

1. Show an after-hours missed call.
2. Show the agent qualifying the lead.
3. Show a drafted response and approval gate.
4. Show booked test-drive draft.
5. Show GM Monday summary.

