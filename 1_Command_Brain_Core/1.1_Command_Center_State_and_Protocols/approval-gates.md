# Human Approval Gates

Purpose: protect client brand, customer data, and money while letting agents move quickly.

## Default Mode

Agents operate in Draft-Only Mode unless approval is explicitly recorded.

## Gate 1: External Communication

Approval required before sending:

- Email
- SMS
- WhatsApp
- Telegram
- Slack messages to external/client channels
- CRM/customer messages

Agent may draft the message and recommend send timing.

## Gate 2: Publishing

Approval required before publishing:

- Social posts
- Ads
- Landing pages
- Videos
- Public proposals
- Client-facing strategy docs

Agent may create drafts and previews.

## Gate 3: Taste Gate

Approval required when output affects brand, tone, aesthetics, pricing, positioning, or client trust.

The human reviewer checks:

- Tone
- Visual quality
- Offer clarity
- Brand fit
- Risk of embarrassment

## Gate 4: Destructive / Capital Actions

Approval required before:

- Deleting or overwriting data
- Updating CRM/customer records at scale
- Spending money
- Changing ad/API budgets
- Deploying production changes
- Running irreversible commands

## Approval Surfaces

Preferred approval surfaces:

1. ClickUp comments/status
2. Slack `#approvals`
3. Telegram approval thread
4. Current Claude/Codex thread

Approval should include:

- Approved action
- Scope
- Timestamp
- Approver

