# PRD — Hermes-Supervised Avatar Content and Inbound System v1

**Status:** Approved for supervised Release 1 implementation; Draft-Only for every external action

**Date:** 2026-07-13

**Product owner and final approver:** Umair

**Operator identity:** Ammar

**Business architecture:** NeuralSync is the company/delivery identity; AgentOSync is the market-facing acquisition and proof brand

**Primary channel:** LinkedIn, manual-first

**Repository:** `WEB3X100/vcos-hq`

## 1. Outcome

Build a Hermes-supervised content-to-conversation system that converts approved SME evidence and manually supplied transcripts into:

1. original AgentOSync content intelligence;
2. approval-ready LinkedIn posts;
3. buyer-friendly lead magnets;
4. private avatar-production packets for validated ideas;
5. evidence-backed media review packets;
6. manual publishing handoffs;
7. draft inbound and discovery handoffs; and
8. weekly market-learning decisions.

Hermes supervises bounded Mini Interns. It does not act as researcher, writer, producer, reviewer, publisher, inbound operator, and analyst in one session.

## 2. Success metrics

### Outcome metrics

- Three approval-ready LinkedIn posts per week by 2026-08-01.
- Two qualified discovery calls per week by 2026-08-31 across inbound and supervised AI SDR activity.
- At least ten inbound conversations per month by 2026-09-30.
- Zero unauthorized publishing, messaging, CRM mutation, client-proof claims, identity use, credential changes, or spend.

### Operating metrics

- Three accepted supervised missions per week.
- Less than 15 minutes of Umair correction per accepted mission.
- Zero false completion claims.
- Every completion linked to artifacts and verification evidence.
- Morning handoffs contain no more than three human decisions.

Impressions, scraping volume, generated videos, and content volume are supporting signals—not success outcomes.

## 3. Product principles

1. Manual-first before automation.
2. Buyer utility before technical novelty.
3. SME content is evidence and inspiration, never copy.
4. One content item has one audience, one painful workaround, one hypothesis, one proof boundary, and one CTA.
5. Written content discovers demand; avatar content scales validated ideas.
6. Lead magnets deliver value without requiring an agent, prompt, or skill installation.
7. Humans approve identity use, claims, publishing, outreach, CRM writes, testimonials, spend, and strategy changes.
8. A producing Mini Intern cannot approve its own output.
9. ClickUp owns business outcomes; GitHub owns engineering evidence; VCOS owns curated memory.
10. The market may change mechanism, format, pain, audience, or CTA through reviewed experiments; it cannot silently change the approved outcome.

## 4. Release 1 boundaries

### In scope

- Manual source, transcript, screenshot, article, post-text, and comment-sample intake.
- Source provenance, permission, attribution, and claim classification.
- Original content-intelligence briefs.
- LinkedIn post and lead-magnet packets.
- Avatar script/render packets without generation.
- Human QA and exact-version approval queues.
- Manual publishing checklists.
- Manually supplied inbound classification and draft replies.
- Weekly market-learning packets.
- Proposed memory and skill changes as reviewable diffs.
- Schemas, fixtures, evals, permissions, install verification, and rollback instructions.

### Explicitly out of scope

- Automatic scraping, following, or monitoring of social profiles.
- Automatic publishing, scheduling, commenting, DMs, email, WhatsApp, or outreach.
- Live LinkedIn browser control.
- Automatic CRM writes.
- Avatar/voice cloning, source-asset upload, generation, distribution, or credit spend.
- Autonomous offer, pricing, ICP, brand, or strategic-memory changes.
- Public claims based on demos, internal work, or unreviewed client evidence.
- Replacing discovery calls or closing deals.
- Installing permanent profiles or expanding permissions without explicit approval.

## 5. Users and first market hypothesis

### Operators

Umair and Ammar need a trustworthy review queue that reduces research and production time without surrendering judgment, identity control, account safety, or commercial focus.

### Initial buyer hypothesis

Owner-led service businesses where leads, follow-up, customer communication, reporting, or administrative coordination still depend on memory and manual work.

### First pain hypothesis

Revenue and customer intent are lost because follow-up and operational context are fragmented across people, inboxes, spreadsheets, and memory.

### First buyer asset hypothesis

An AgentOSync Leak Map/checklist that helps the buyer identify one measurable workflow leak and the smallest AI-assisted intervention. This remains a working internal hypothesis until Umair approves an exact public version.

## 6. Mini Intern registry

| ID | Mini Intern | Owns | Cannot do |
| --- | --- | --- | --- |
| MI-01 | Content Intelligence | Source ledger and intelligence brief | Scrape, copy creator language, access private sources, or invent claims |
| MI-02 | LinkedIn Editorial | Posts, lead magnets, hooks, asset briefs | Publish, fabricate proof, or change offer/ICP |
| MI-03 | Avatar Producer | Spoken scripts and private render packets | Clone identity, upload media, render, spend, or distribute |
| MI-04 | Reviewer/QA | Content/media checks and release recommendation | Approve its own production or publish |
| MI-05 | Inbound Concierge | Supplied-signal classification, draft replies, discovery handoffs | Send, browse inboxes, price, promise, or mutate CRM |
| MI-06 | Growth Analyst | Weekly evidence review and next-test recommendation | Optimize vanity metrics or silently rewrite strategy |

Hermes may create temporary specialist sessions only inside an approved mission with one outcome, exclusive file ownership, minimal context, a hard cap, stop conditions, and a candidate-output label.

## 7. End-to-end workflows

### WF-01 — Source intake and evidence ledger

Input: approved URL, transcript, screenshot, article, post text, or comment sample.

Output: `SourceEvidenceRecord` with provenance, rights/use class, fact/opinion/signal/inference labels, attribution requirement, claim risks, and `usable`, `needs-review`, or `blocked` verdict.

Stop: missing provenance, private/client data, unclear permission, or high-stakes claim without review.

### WF-02 — Content-intelligence brief

Input: approved evidence record.

Output: `ContentIntelligenceBrief` containing painful workaround, source insight, audience signal, original AgentOSync POV, practical workflow, proof boundary, anti-copy constraints, content options, and confidence.

### WF-03 — LinkedIn post packet

Input: approved intelligence brief.

Output: `PostProductionPacket` with one hypothesis, detailed draft, Ammar voice notes, hook, CTA, optional asset brief, evidence links, originality/claim review, and risk label.

### WF-04 — Lead-magnet packet

Input: repeated buyer problem or approved post hypothesis.

Output: a self-contained checklist, diagnostic, worksheet, calculator, or short guide plus an optional separate operator appendix.

Pass: a target buyer can receive value in under ten minutes without installing software.

### WF-05 — Avatar-production packet

Input: exact written content approved by Umair/Ammar and either supported by intent or explicitly approved as calibration.

Output: `AvatarRenderPacket` with exact script, duration/platform, pronunciation, pauses, delivery, framing, captions, B-roll, negative constraints, consent reference, provider preset, cost estimate, output destination, and approval state.

Release 1 stops before provider submission.

### WF-06 — Media QA

Input: manually supplied private render plus exact approved packet.

Output: `MediaReviewPacket` scoring likeness, voice, lip-sync, motion, trust, hook, claims, captions, usefulness, and CTA; verdict is `approve`, `revise`, or `kill`.

Hard cap: two render corrections unless reapproved.

### WF-07 — Manual publishing handoff

Input: exact-version content/media approval.

Output: `PublishingHandoffPacket` verifying version/checksum, profile, timing, CTA, asset destination, attribution, inbound owner, and manual checklist.

Release 1 never publishes.

### WF-08 — Inbound handoff

Input: manually supplied comment, DM, request, workshop interest, or call booking.

Output: `InboundHandoffPacket` classifying attention, utility, intent, qualification, or conversion and including draft reply, missing context, owner, SLA, and recommended next action.

Release 1 never sends or mutates CRM.

### WF-09 — Weekly market-learning loop

Input: approved content, asset, inbound, and call outcomes.

Output: `WeeklyLearningPacket` separating attention from intent/qualification/conversion and recommending exactly one decision per experiment: `continue`, `iterate`, `narrow`, `pivot-mechanism`, or `park`.

Memory, strategy, and task changes remain proposed diffs until approval.

## 8. Hermes supervisor contract

Hermes must:

1. restore the approved repository/project state;
2. select the smallest capable workflow and Mini Intern;
3. validate input readiness before dispatch;
4. declare file ownership, allowed tools, approval boundary, hard cap, and stop conditions;
5. prevent producer/self-review conflicts;
6. preserve evidence and compact handoffs instead of copying full session logs;
7. stop retry loops at their cap;
8. assemble the final review queue;
9. state uncertainty and blocked status without false completion;
10. propose learning as a PR/diff, never silently mutate durable memory or installed skills.

When no approved mission exists, Hermes may propose the highest-leverage next mission. It must not invent a new project or begin an unapproved external workflow.

## 9. Skill packages

The target packages are:

1. `agentosync-content-router`
2. `agentosync-source-ledger`
3. `agentosync-content-intelligence`
4. `agentosync-linkedin-post`
5. `agentosync-lead-magnet`
6. `agentosync-avatar-production-packet`
7. `agentosync-avatar-media-review`
8. `agentosync-publishing-handoff`
9. `agentosync-inbound-handoff`
10. `agentosync-market-learning-loop`

Every package must contain:

```text
SKILL.md
README.md
input.schema.json
output.schema.json
permissions.yaml
fixtures/
evals/
CHANGELOG.md
```

Each package declares its exact trigger, inputs, outputs, allowed files/systems, credentials, approval boundary, stop rules, retry/cost caps, evidence, maturity, and rollback behavior.

The umbrella router orchestrates specialist skills; it does not duplicate every specialist procedure.

## 10. `soul.md` contract

Hermes is Umair and Ammar's commercially grounded content and acquisition co-pilot for AgentOSync. It protects buyer usefulness, identity, trust, focus, proof integrity, and account safety.

### Traits

- Commercially candid, calm, concise, inventive, and evidence-seeking.
- Skeptical of vanity metrics, generic AI hype, and infrastructure without a proven workflow.
- Comfortable saying `not enough evidence`.
- Willing to challenge priorities that do not improve qualified conversations.
- Adaptive about mechanism while loyal to the approved outcome.
- Independent enough to disagree; committed enough to execute after an informed decision.

### Default judgment

- Ask which buyer problem and decision the artifact serves.
- Prefer one clear experiment to a multi-channel factory.
- Separate fact, source opinion, audience signal, inference, and hypothesis.
- Surface the strongest objection before recommending release.
- Never treat preparation as completion or impressions as demand.
- Preserve Ammar's natural voice; never write like a generic AI guru.
- Capture distracting ideas without activating them.
- Propose reversible diffs with evidence.

### Trust-breaking behavior

- False completion or hidden uncertainty.
- Unauthorized publishing, messaging, identity use, spend, or system mutation.
- Invented sources, testimonials, results, or audience signals.
- Cross-brand or client-context leakage.
- Silent strategy, memory, permission, or installed-skill changes.
- Scope expansion or file-ownership violations.
- Agreeing with weak priorities instead of challenging them.

## 11. Data, memory, and state

Required record types:

`SourceEvidenceRecord`, `ContentIntelligenceBrief`, `ContentExperiment`, `PostProductionPacket`, `LeadMagnetPacket`, `AvatarRenderPacket`, `MediaReviewPacket`, `ApprovalRecord`, `PublishingHandoffPacket`, `InboundSignal`, `InboundHandoffPacket`, `WeeklyLearningPacket`, `MemoryChangeProposal`, and `SkillChangeProposal`.

Every record includes stable ID, timestamps, source/parent IDs, owner, approval state, sensitivity, evidence, version/checksum, allowed next actions, blockers, and audit events.

### Memory allowlist

- Approved ICP, exclusions, offer, CTA, voice examples, rejection notes, source registry, proof ledger, experiment outcomes, non-secret provider presets, and current weekly objective/budget.

### Never place in general memory or Git

- Credentials, API keys, private identity footage/audio, raw client data, unapproved testimonials, raw DMs, noisy scraper output, generated-media binaries, or unsupported strategic conclusions.

Only a human-approved `MemoryChangeProposal` becomes durable memory.

## 12. Evaluation and maturity

Maturity labels:

- `designed`
- `fixture-proven`
- `supervised-proven`
- `autonomous-approved`

Start with 15–20 labeled success, rejection, and edge-case examples.

Blocking checks:

- source faithfulness;
- originality;
- claim safety;
- identity consent;
- approval compliance;
- exact-version integrity;
- separation of duties; and
- false-completion resistance.

Fixture promotion requires deterministic checks and the labeled eval set. Supervised promotion requires three consecutive accepted real missions, zero blocking violations, and less than 15 minutes of correction each. Every maturity claim links to evidence.

Automation unlocks progressively:

- Source monitoring after 10 manual source-to-post runs.
- Draft automation after six Ammar-approved posts need only light edits.
- Scheduling after three manual publishing cycles plus explicit standing authorization.
- Avatar distribution only after all core media dimensions score at least 4/5 and two written topics produce real intent.

## 13. Failure recovery

- Every mission has retry and time caps plus a terminal `blocked` state.
- No silent fallback from real inputs to fixtures.
- No more than two automatic regenerations.
- Provider failures return blockers; they do not change provider, permissions, or spend.
- Wrong-version or missing-approval detection invalidates release readiness.
- Every skill/profile install has manifest, checksum, health check, and rollback.
- One kill switch disables scheduled internal jobs without deleting artifacts.

## 14. Release plan

### R0 — Repository truth

L1 and L2 must fetch the same canonical SHA. Permanent profile/skill installation remains blocked until matching check-ins are recorded.

### R1A — Contract scaffold

Build only:

- Mini Intern registry and permissions matrix;
- shared record envelope schema;
- source-ledger schema;
- content-intelligence schema;
- content-router candidate skill;
- source-ledger candidate skill;
- content-intelligence candidate skill;
- fixtures and safety/eval scaffolding;
- implementation handoff and evidence.

No external tools, credentials, media generation, social access, publishing, or live data.

### R1B — Manual written-content proof

Run three manually supplied sources through ledger → intelligence → editorial draft → independent QA → human review.

### R2 — Avatar packet proof

Convert one approved written winner into a provider-ready packet, then stop before generation. Private render and spend require separate approval.

### R3 — Inbound and learning proof

Process manually supplied inbound examples and produce the weekly learning packet.

### R4 — Supervised internal automation

Only after proof gates: approved source monitoring, internal draft queue, scheduled internal runs, and read-only Castle/Harness status. No external publication or messaging without separate authorization.

## 15. First implementation slice acceptance criteria

The first L2 mission is complete only when:

1. It starts from the exact approved base SHA.
2. It uses a new `l2/*` feature branch.
3. It edits only the paths in its mission allowlist.
4. Three candidate skills and the shared contracts exist.
5. JSON schemas parse successfully.
6. Permissions contain explicit deny rules for external action, identity assets, credentials, spend, publishing, messaging, CRM, and durable memory mutation.
7. Fixtures cover at least: valid public source, missing provenance, private/client data, copied language risk, unsupported claim, and ambiguous approval.
8. Evals produce deterministic pass/block results for those fixtures.
9. No secrets, private media, raw client data, generated binaries, or runtime logs enter Git.
10. `git diff --check`, schema validation, secret scan, and exact-file-scope checks pass.
11. A handoff records base, branch, commit, files, checks, blockers, maturity, and no more than three decisions.
12. Output is labeled `candidate`/`designed`; it is not installed or called production-ready.

## 16. Product decisions deferred beyond the first slice

- Exact first public ICP/pain statement and offer language.
- Exact public lead magnet.
- Inbound response owner and SLA.
- Private likeness/voice asset store.
- Avatar provider, presets, and credit budget.
- Standing publication/scheduling authority.
- External orchestration framework.
- Authority advance after the first three accepted missions.

These decisions do not block R1A because R1A uses sanitized fixtures and creates contracts only.
