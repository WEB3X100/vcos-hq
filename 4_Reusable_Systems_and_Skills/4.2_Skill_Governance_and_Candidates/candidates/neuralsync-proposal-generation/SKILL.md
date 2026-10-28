---
name: neuralsync-proposal-generation
description: Use when generating or reviewing a NeuralSync client proposal, scope-of-work PDF, pricing proposal, audit proposal, or sales document from a client brief. Produces an approval packet and client-ready PDF only after validating sources, pricing, claims, confidentiality, and the approved NeuralSync brand kit.
---

# NeuralSync Proposal Generation

## Required inputs

- client and opportunity name;
- problem, desired outcome, and approved scope;
- source-backed capabilities and proof;
- approved pricing source and commercial owner;
- timeline, exclusions, assumptions, owner, CTA, and review deadline;
- approved brand packet from `neuralsync-brand-kit`.

Missing fields become explicit blockers or `[HUMAN INPUT REQUIRED]` placeholders. Never fill them by inference.

## Workflow

1. Read `references/proposal-contract.md` and the Drive manifest.
2. Create a source ledger: claim/pricing field, exact source, owner, approval state, and last-reviewed date.
3. Run the preflight. Reject unsupported claims, ambiguous pricing, conflicting scope, missing confidentiality rules, and unapproved brand assets.
4. Draft the narrative: context, diagnosis, proposed outcome, scope, delivery approach, timeline, investment, responsibilities, assumptions/exclusions, proof, and next step.
5. Mark the asset `DRAFT — NOT FOR CLIENT` until the responsible human approves facts, pricing, and scope.
6. Render a PDF only from approved inputs and the shared brand packet.
7. Inspect every page for clipping, overflow, illegible type, broken links, incorrect totals, inconsistent terminology, orphan headings, and confidential notes.
8. Return the PDF, editable source, source ledger, QA result, and explicit approval request. Do not send it.

## Non-negotiable checks

- totals reconcile with the approved pricing source;
- no invented capability, outcome, customer, testimonial, date, or price;
- NeuralSync naming is consistent;
- scope and exclusions are unambiguous;
- client data is handled only for the named engagement;
- output remains human-gated.

## Completion

A draft is complete when it passes structural and factual preflight. The skill is production-accepted only after a real proposal PDF opens correctly, passes visual inspection, and receives human approval.
