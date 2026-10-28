# Email marketing activation

Status: `AUDIT_AND_DESIGN_ONLY`

## Readiness gates

No sending until all are recorded:

- campaign type: lifecycle/nurture or cold outbound;
- one ICP, one workflow, one offer, one CTA;
- list source, lawful basis, jurisdiction, and suppression process;
- sending domains/inboxes, authentication, warm-up, and reputation owner;
- approved sender identity, reply owner, booking link, and response SLA;
- proof asset and claim ledger;
- sequence, stop rules, unsubscribe handling, and complaint process;
- baseline, success metrics, sample size, and review date;
- explicit launch approval.

## First deliverable

Nova produces an activation packet, not a live campaign:

1. existing-stack audit;
2. recommended first segment with alternatives rejected;
3. message map using buyer language;
4. proof-safe 3–5 touch draft sequence;
5. subject-line and CTA hypotheses;
6. compliance/deliverability checklist;
7. measurement design;
8. launch blockers and human decisions.

## Metrics

Primary: qualified positive replies and booked qualified demos.

Guardrails: bounce rate, spam complaints, unsubscribes, negative replies, domain reputation, reply SLA, and list-quality failures. Opens are diagnostic only and can be unreliable.

## Stop rules

Pause and escalate if provenance is unclear, authentication is incomplete, bounce/complaint signals exceed the approved threshold, a claim lacks evidence, replies are unowned, or requested actions exceed Nova's permissions.
