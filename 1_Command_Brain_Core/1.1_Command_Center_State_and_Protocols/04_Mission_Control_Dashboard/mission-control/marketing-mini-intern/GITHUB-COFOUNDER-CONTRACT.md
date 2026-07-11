# GitHub Co-Founder Memory and Shipping Contract

**Status:** Draft-Only operating authority for Castle/Hermes project work
**Coordination bus:** `WEB3X100/vcos-hq`
**Human authority:** Umair

## 1. Purpose

GitHub is the durable cross-laptop memory and coordination bus. Telegram activates and discusses missions; Castle visualizes missions and review state; ClickUp remains execution truth; repository artifacts tell every new agent what has shipped, what is active, what is blocked, and what the north star is.

Chat memory alone never counts as project state.

## 2. Required project memory packet

Every active build project must expose these Markdown interfaces from a stable README:

| File | Required answer |
| --- | --- |
| `PROJECT-STATE.md` | What shipped, what is being built, blockers, approvals, branch/commit, and next action. |
| `PRODUCT-REQUIREMENTS.md` | What outcome the product must deliver and how it will be accepted. |
| `IMPLEMENTATION-PHASE.md` | Current bounded slice, entry/exit gates, ownership, and tests. |
| `DECISIONS.md` | Durable choices and rejected alternatives. |
| `HANDOFF.md` or dated handoffs | Exact artifacts, evidence, failures, and instructions for the next agent. |

The project README links these files in reading order. Missing or stale interfaces block implementation.

## 3. Project-state contract

`PROJECT-STATE.md` must name its observed branch/commit, north star, current validated workflow, truly shipped artifacts with evidence, current bounded phase, blockers, approvals, and one next action.

“Shipped” requires a commit and verification evidence. Drafted, locally present, mocked, or planned are separate states.

## 4. Agent start protocol

Before touching a project, Hermes/Grok/Codex must:

1. Fetch remote refs without deleting or resetting local work.
2. Report branch, commit, dirty/untracked files, and whether the expected remote branch exists.
3. Read the project README and memory packet.
4. Restate north star, shipped state, current phase, blockers, approval boundary, and proposed done-means.
5. Ask only the questions whose answers materially change the PRD or build.
6. Stop if paths, authority, source branch, or runtime truth are ambiguous.

## 5. PRD grilling protocol

Before planning a live site or end-to-end workflow, the co-founder asks Umair one focused question at a time until these are unambiguous:

- Exact user and painful job.
- Offer, promise, and measurable outcome.
- Input source and owner.
- End-to-end happy path.
- Failure and recovery paths.
- System of record.
- Artifact or live surface that proves completion.
- Brand voice, proof, claims, and privacy boundaries.
- Human approvals and prohibited actions.
- Acceptance tests and first real UAT.
- What is explicitly not being built.

The agent reflects each confirmed answer into the PRD. It never silently invents commercial, brand, safety, or publishing decisions.

## 6. Mission and branch lifecycle

1. L1 identifies the approved base/integration branch.
2. L2 fetches and creates an `l2/<mission-slug>` feature branch.
3. L2 works only within declared file ownership.
4. L2 commits artifacts plus a handoff; it never commits `.hermes/`, secrets, raw private memory, or unrelated untracked files.
5. L2 pushes the feature branch, never `main`.
6. L1 reviews the diff, tests, safety, and truthfulness.
7. L1 merges only after required approval.
8. The merge updates `PROJECT-STATE.md` and links the shipped commit/evidence.
9. Both laptops pull with fast-forward-safe behavior; neither uses destructive reset as synchronization.

## 7. Castle behavior

Castle may read repository-backed state and handoffs. It must show observed branch/commit and freshness, north star, validated workflow, shipped/current/blocked/approval state, mission receipts, artifact paths, review evidence, and exact-version approval.

Castle never infers that GitHub, L2, Telegram, ClickUp, a deployment, or a published post is live merely because a record exists.

## 8. Marketing maturity ladder

| Stage | Minimum evidence | Permission |
| --- | --- | --- |
| M0 — Design | PRD and test mission | No runtime activation. |
| M1 — Draft | One complete five-concept kit | Draft generation only. |
| M2 — Supervised week | At least seven reviewed daily outputs, corrections logged, lead magnets inspected | Human approves every exact post and publishes manually. |
| M3 — Scheduled candidate | Voice/tone and asset-quality review passes; zero unresolved safety incidents; rollback and kill switch tested | May propose a separately reviewed scheduling/publishing PRD. |
| M4 — Governed autopost | Explicit written authorization naming brand, account, cadence, allowed content, monitoring, and revocation | Only the separately approved narrow autopost workflow may execute. |

Seven days never automatically unlocks publishing. Promotion depends on reviewed evidence and a new explicit approval. Any voice drift, factual error, confidentiality incident, low-value lead magnet, or approval mismatch returns the system to M2.

## 9. Multi-brand boundary

Each brand has an isolated profile containing audience, offer, voice references, approved proof, prohibited claims, visual rules, lead magnets, and account/cadence permissions. Feedback from one brand never silently trains another brand.

Select and validate the first brand explicitly. Onboard additional brands only after the first end-to-end workflow passes UAT.
