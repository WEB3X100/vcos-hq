# Implementation Phase — Overnight LinkedIn Kit Vertical Slice

**Phase:** MMI-1
**Status:** Planned; blocked by Castle stabilization gate
**Outcome:** One Telegram-triggered mission returns five complete LinkedIn kits to Castle for human feedback and exact-version approval.

## Entry gates

- Castle integration branch is created from the current committed HQ structure.
- Content Intel and L2 handoff files are preserved and canonical paths confirmed.
- Castle server has atomic runtime-state writes and runtime/source separation.
- Castle tests prove their own server/commit and use one isolated port.
- Phase 1 outbound-network contract is resolved explicitly.
- Umair confirms the L2 Windows handoff root and the permitted Telegram/Hermes activation mechanism.
- The GitHub memory packet and `PROJECT-STATE.md` contract are present on the chosen branch.
- Umair selects one first brand and identifies its voice references, proof boundaries, and lead-magnet inventory.

No feature implementation begins until these gates are evidenced in a preflight report.

## Vertical slice

### Workstream 1 — Mission contract

- Define and validate `mission.json`, `feedback.json`, `approval.json`, and `handoff.md`.
- Add collision-safe mission IDs and checksums.
- Use atomic writes, explicit schema versions, and quarantine for invalid inputs.

### Workstream 2 — Hermes Marketing Mini Intern

- Add `CONTENT START`, `CONTENT STATUS`, `CONTENT CANCEL`, and `CONTENT REVISE` behaviors to the approved Hermes profile/skill surface.
- Accept reference transcript/file/attachment metadata without claiming unread inputs.
- Generate the five required strategies and the complete artifact layout.
- Enforce hard caps and Draft-Only boundaries.

### Workstream 3 — Overnight runner

- Queue only missions explicitly activated by Umair.
- Process one mission at a time in v1.
- Persist heartbeat and checkpoints with timestamps.
- Resume safely after restart or report a partial failure.
- Send Telegram notification summaries only through the already approved Hermes gateway behavior; no new bot/token integration.

### Workstream 4 — Castle morning review queue

- Import validated handoff artifacts from the confirmed coordination path.
- Show observed status and freshness; never infer L2 health.
- Render five comparable concept cards.
- Capture structured feedback and a combine instruction.
- Export a revision mission for Hermes.
- Record exact-version approval without performing publication.

### Workstream 5 — Verification

- Unit tests for schema, state transitions, checksums, approval invalidation, and feedback combination.
- Integration test using a fake L2 handoff directory.
- Failure tests for missing input, stale status, duplicate mission, malformed JSON, partial output, failed write, and changed approved content.
- Browser test for morning queue, feedback, combine, revision, approval, and approval invalidation.
- Static scan for secrets, public bind, external send/publish code, and unapproved outbound calls across Python and JavaScript.

## File ownership rule

Do not repeat “one agent per room” against shared monoliths. Before parallel work, establish modules and exclusive ownership:

| Owner | Exclusive scope |
| --- | --- |
| Builder A | Mission schemas, validators, and fixtures only |
| Builder B | Hermes skill/prompts and L2 runner only |
| Builder C | Castle review-queue frontend module only |
| Integrator | Castle API wiring and shared state after A–C handoff |
| Skeptic | Tests, threat review, and acceptance evidence only |

If the existing Castle remains monolithic, use one Builder serially. Do not claim parallel ownership.

## Acceptance criteria

1. Telegram activation creates exactly one mission receipt.
2. The runner produces five complete, meaningfully distinct concepts.
3. Every concept includes copy, visual direction, lead magnet/CTA, and claims review.
4. Castle imports only valid artifacts and displays their real freshness.
5. Feedback can retain and combine individual elements.
6. Hermes produces a final revision from structured feedback.
7. Approval binds to a checksum and revision.
8. Editing invalidates approval.
9. No external post, message, CRM/QBO mutation, spend, or deploy occurs.
10. Clean restart and all defined failures are proven.
11. One real overnight dogfood mission passes human review.
12. `PROJECT-STATE.md` records the tested commit, evidence, blockers, approvals, and next action for a fresh L2 session.

## Exit decision

After the dogfood mission, Umair chooses one:

- Adopt as the daily Draft-Only Marketing Mini Intern.
- Revise the workflow and repeat MMI-1.
- Stop and archive without adding more capabilities.

Automatic publishing is not an MMI-1 exit option.

The next permitted phase is a seven-day supervised draft-and-manual-publish evaluation. A separate autopost PRD may be proposed only after its evidence is reviewed.
