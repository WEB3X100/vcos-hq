# Product Requirements — Hermes Marketing Mini Intern

**Document ID:** `VCOS-MMI-001`
**Version:** 0.1
**Status:** Draft-Only
**Date:** 2026-07-11

## 1. Outcome

Umair can activate Hermes through Telegram with a reference post, transcript, screenshot, URL, notes, or rough idea. Hermes works asynchronously and returns five genuinely different LinkedIn campaign concepts. Castle presents them for comparison, feedback, combination, revision, and exact-version approval.

The first release succeeds when one real overnight mission produces a reviewable artifact packet by morning without publishing, external messaging, CRM/QBO mutation, spending, or invented evidence.

## 2. User story

> As Umair, I send Hermes a bounded content mission at night. By morning, Castle shows five experimental LinkedIn concepts in my tone, each with a visual direction and lead-magnet pairing. I select useful elements, reject weak elements, request a combined revision, and explicitly approve the exact final version before I post it.

## 3. Required workflow

1. Umair sends `CONTENT START` in Telegram with source material or local artifact references.
2. Hermes replies with a mission receipt: mission ID, understood objective, inputs, constraints, output directory, hard cap, and Draft-Only boundary.
3. Hermes validates inputs. Missing or inaccessible inputs produce `BLOCKED`, not invented content.
4. Hermes creates five strategically distinct concepts.
5. Hermes saves a structured handoff packet and artifacts under the approved L2 handoff root.
6. The handoff reaches L1 through the approved Git/GitHub coordination path; Castle never claims direct L2 connectivity unless verified.
7. Castle shows the mission in the morning review queue.
8. Umair records feedback per concept and per element.
9. Hermes creates one combined final candidate from selected elements.
10. Umair may approve the exact immutable revision.
11. Any edit after approval invalidates approval and returns the item to `REVIEW`.
12. Publishing remains manual and outside this release.

## 4. Five required concept strategies

| Concept | Intent |
| --- | --- |
| A — Authority | Teach a sharp operator insight and demonstrate credible expertise. |
| B — Founder story | Use a real experience, tension, lesson, and earned conclusion. |
| C — Contrarian | Challenge a familiar assumption with evidence and a useful alternative. |
| D — Tactical | Deliver a framework, checklist, teardown, or step-by-step operating method. |
| E — Experimental | Test a bolder hook, unusual structure, visual inversion, or emerging format. |

These must differ in thesis, narrative structure, hook mechanism, and visual treatment—not merely wording.

## 5. Every concept must include

- Concept thesis and intended audience.
- Primary hook plus two alternates.
- Full LinkedIn post in Umair's calibrated tone.
- Visual choice: infographic, carousel, or single image, with rationale.
- Slide-by-slide carousel copy or complete image/infographic brief.
- Lead-magnet pairing, CTA, and link-placement recommendation.
- Suggested first comment.
- Claims/evidence table: supported, inference, needs verification, prohibited.
- Risks: confidentiality, private client data, fabricated metrics, brand confusion.
- Confidence and what Hermes would improve with better input.

## 6. Castle morning review queue

Each mission card must show:

- Mission ID and status.
- Requested time, completed time, and observed source/freshness.
- Input references and output path.
- Five candidate summaries with preview links.
- Evidence/claims status and blockers.
- Feedback controls: `Like`, `Dislike`, `Keep element`, `Combine`, `Request revision`, `Reject`.
- Final revision checksum/version.
- Approval state and immutable audit entry.

Castle labels must distinguish `queued`, `received`, `working`, `artifact returned`, `reviewed`, and `approved`. No state may be inferred from elapsed time alone.

## 7. Approval contract

- Concept feedback is not publishing approval.
- `Approve exact version` records the mission ID, revision, checksum, approver, and time.
- Approval never triggers LinkedIn or another external service.
- Any content or visual change invalidates approval automatically.
- Only Umair can approve external use.
- No agent may transform “looks good,” a reaction emoji, or `READY` into approval.

## 8. Tone-learning contract

Feedback creates **candidate preferences**, not permanent laws. A preference is promoted only after repeated evidence or explicit confirmation from Umair. The ledger records:

- Source mission and concept.
- Exact liked/disliked element.
- Context where the preference applies.
- Confidence and occurrence count.
- Status: candidate, confirmed, rejected, superseded.

Raw private source material is not copied into general memory. Store reviewed summaries and pointers only.

## 9. Non-goals

- Autonomous LinkedIn publishing or scheduling.
- LinkedIn credentials, browser session reuse, or cookie/CDP automation.
- Automatic DMs, comments, CRM updates, lead outreach, or email.
- Scraping reference URLs without an approved, disclosed retrieval path.
- Training or fine-tuning a model.
- Multi-client content production.
- Additional Castle rooms unrelated to this one workflow.

## 9.1 Brand isolation

Each brand has its own audience, offer, voice references, approved proof, prohibited claims, visual direction, and lead-magnet inventory. A mission names exactly one brand. Preferences learned for one brand cannot silently affect another.

MMI-1 validates one brand first. Multi-brand support means reusable schemas and isolated profiles—not launching every brand simultaneously.

## 9.2 Supervised-week promotion gate

For at least seven reviewed daily outputs/posts:

- Umair selects and approves the exact final version each day.
- Publishing is manual.
- Voice/tone corrections and visual/lead-magnet quality feedback are logged.
- Factual, privacy, approval, and brand errors are counted explicitly.
- The system remains Draft-Only regardless of apparent quality.

Afterward, Umair reviews the evidence. A passing review authorizes writing a separate autopost PRD; it does not authorize posting. Autopost requires explicit written approval, narrow brand/account/cadence scope, monitoring, rollback, and a kill switch.

## 10. Release acceptance

- One Telegram activation produces one traceable mission.
- Five meaningfully distinct complete kits exist on disk.
- Castle imports the handoff without claiming a live bridge.
- Feedback survives restart and generates a combined revision request.
- Approval is exact-version, auditable, and invalidated after editing.
- No publish/send/CRM/QBO/spend/deploy path exists.
- Failure cases are tested: missing source, invalid handoff, duplicate mission, partial output, stale status, failed write, and altered approved revision.
