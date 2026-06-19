# GBrain Office Hours

Status: Skill Candidate  
Owner department: Infrastructure with Strategy, Marketing, and Reviewer QA hooks  
Created: 2026-06-10

## Purpose

Use GBrain as the memory-backed sparring partner before VCOS project development, solution design, offer positioning, branding, conversion review, and skill promotion.

This skill turns "use GBrain" into a repeatable office-hours loop:

1. Retrieve relevant VCOS/project context.
2. Grill the idea, solution, offer, or build plan.
3. Produce a sharper execution packet.
4. Identify approval gates and proof gaps.
5. Capture reusable lessons back into HQ or GBrain.

## Trigger Phrases

- `GBrain office hours`
- `grill this`
- `use GBrain to improve this`
- `GBrain conversion review`
- `GBrain solution review`
- `GBrain brand review`
- `GBrain skill foundry review`
- `is this worth building`

## Input Packet

Minimum input:

- Project, domain, or offer name.
- What is being reviewed: idea, solution, workflow, copy, landing page, demo, build plan, or skill candidate.
- Desired outcome: build, sell, polish, decide, de-risk, or package.

Optional input:

- Target buyer or user.
- Current draft/copy/spec/link.
- Known constraints.
- Approval-sensitive areas.
- Where the output should be saved.

## Retrieval Protocol

Start with HQ fast path, then run targeted GBrain searches. Use direct file reads when GBrain returns a known source.

Core searches:

```bash
gbrain search "<project/domain> active context decisions blockers"
gbrain search "<project/domain> approval gates proof lane next actions"
gbrain search "<project/domain> offer CTA proof conversion"
gbrain search "<project/domain> skill governance promotion reusable workflow"
```

If search returns noisy Arsenal/vendor docs, manually narrow to the relevant HQ or project workspace files.

## Review Modes

### 1. Office Hours

Use for new ideas or product direction.

Answer:

- Who is this for?
- What painful current workaround exists?
- What is the narrowest sellable wedge?
- What proof would make it undeniable?
- What should not be built yet?
- What is the next 48-hour test?

### 2. Solution Grill

Use for implementation plans, agent workflows, dashboards, demos, and automations.

Answer:

- What is the obvious version?
- What is the sharper version?
- What breaks first?
- What needs a human approval gate?
- What should be mocked before being automated?
- What output packet proves the workflow worked?

### 3. Branding And Conversion Review

Use for landing pages, offers, demos, outreach, proof assets, and scripts.

Score:

- ICP specificity.
- Speed to value.
- Concrete promise.
- Proof quality.
- CTA clarity.
- Trust and claim risk.
- Visual or demo fit.

Output:

- Better headline or offer.
- Stronger proof angle.
- CTA rewrite.
- Objection handling.
- Demo flow improvement.
- Approval-sensitive claims.

### 4. Skill Foundry Review

Use for repeated workflows.

Check:

- Trigger phrase.
- Input packet.
- Output packet.
- Owner department.
- Tools needed.
- Approval gate.
- Proof lane.
- Failure mode.
- Evidence of 1, 2, or 3+ successful uses.

Output:

- `experiment`, `pattern`, `skill candidate`, or `validated skill` recommendation.
- Registry/map update recommendation.
- Next validation run.

## Output Packet

Return a compact packet:

```markdown
## Verdict
[build / pause / sharpen / validate / package]

## Hard Truth
[the thing most likely being avoided]

## Sharper Version
[specific improved solution or offer]

## Proof Test
[48-hour or next-session validation]

## Approval Gates
[external send, publishing, CRM mutation, spend, client-facing strategy, etc.]

## Next Actions
1. ...
2. ...
3. ...

## Capture
[what should be saved to HQ, project workspace, ClickUp, or GBrain]
```

## Approval Gates

Human approval is required before:

- Sending external messages.
- Publishing posts, websites, ads, videos, or public proof assets.
- Updating CRM/customer records.
- Spending money or increasing budget.
- Deploying production workflows.
- Presenting final client-facing strategy, pricing, or proposal terms.

Internal drafts, critiques, and local HQ notes are allowed.

## Validation Log

| Date | Use | Result | Next validation |
| --- | --- | --- | --- |
| 2026-06-10 | Defined the VCOS GBrain Office Hours operating loop after local HQ import | Candidate created; needs live use on AgentOSync, Amax, or dealership work | Run on one real offer/build plan and record whether it improved the output |
| 2026-06-12 | Ran office hours on Dealership Sales Lead Manager / Morning Brief and AMAX Finance Control Tower | Useful; narrowed both lanes to one proof packet each and blocked tool sprawl | After demo/dry run, record whether critique improved clarity or reduced scope drift |
