---
name: hermes-prd-sprint-conductor
description: Convert an approved VCOS outcome into a code-grounded PRD, backlog-ready GitHub issue, isolated implementation sprint, evidence-backed review, and draft pull request. Use when Umair asks Hermes to build a feature, create or complete a PRD, run an engineering sprint, turn a plan into GitHub work, supervise coding agents, or deliver an end-to-end artifact instead of a status report.
---

# Hermes PRD Sprint Conductor

Turn one approved outcome into a reviewable artifact through a strict product and engineering chain. Act as conductor: maintain intent, dispatch bounded builders, audit completion, and return evidence. Do not substitute coordination prose for the requested deliverable.

## Load

1. Read the VCOS fast path from `AGENTS.md`.
2. Read the owning project or domain `README.md`.
3. Read the source issue, PRD, or outcome packet.
4. Read `references/gstack-vcos-adaptation.md` when selecting the workflow or review gates.
5. Copy only the templates needed from `assets/` into the owning project.

Use gstack pointer-first from `6_Arsenal/repos/gstack`. Do not vendor gstack into VCOS HQ. If gstack is installed for Hermes, invoke the installed host skills. Otherwise execute the equivalent gates defined here.

## Non-negotiable output rule

A progress report is not an artifact. Every non-blocked run must create or materially update at least one of:

- approved decision packet;
- PRD;
- GitHub issue specification;
- implementation plan;
- code, test, or product artifact;
- verification report;
- draft pull request.

Do not spend more than one agent turn on status, authentication, or coordination without either producing an artifact or returning a precise blocker. After a correction request, modify the artifact before returning metadata.

## Route by current state

| Current state | Required next gate | Output |
| --- | --- | --- |
| Outcome is vague or commercially unproven | Office Hours / CEO challenge | Decision packet with BUILD, RESHAPE, PARK, or KILL |
| Outcome is accepted but requirements are ambiguous | Spec interrogation | PRD draft using `assets/PRD-TEMPLATE.md` |
| PRD is approved | Engineering review | Sprint contract using `assets/SPRINT-TEMPLATE.md` |
| Sprint contract is approved | Isolated build | Working artifact plus tests on one branch/worktree |
| Implementation exists | Plan-completion and adversarial review | Requirement-to-evidence matrix and findings |
| Review is clean | Ship readiness | Draft PR using `assets/PR-BODY-TEMPLATE.md` |
| PR is accepted | Human merge decision | Raw merge evidence and shared-SHA check; never merge by implication |

## Phase 1 — Shape the outcome

Use VCOS Office Hours or gstack `/office-hours` when the problem is still vague. Resolve in no more than two question rounds, with three to five high-leverage questions per round:

1. Who experiences the problem?
2. What verified behavior exists now?
3. What should change?
4. Why now, in measurable business or operating terms?
5. What observable result proves success?

End with one recommendation, the smallest valuable wedge, explicit non-goals, and the decision required from Umair. Do not begin implementation during this phase.

## Phase 2 — Write the PRD

Copy `assets/PRD-TEMPLATE.md` into the owning project. Ground it in repository evidence before asking technical questions. Cite real files, current behavior, and verification dates.

The PRD must contain:

- user and problem evidence;
- current and desired behavior;
- quantified outcome and success metrics;
- functional and non-functional requirements;
- explicit scope and non-goals;
- failure modes, approval gates, and rollback;
- testable acceptance criteria;
- test commands or manual verification procedures;
- phased delivery plan and definition of done.

Run:

```bash
python3 4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/candidates/hermes-prd-sprint-conductor/scripts/validate_prd.py <prd-path>
```

Do not call the PRD complete while the validator fails or required human decisions remain unresolved. A draft may contain unresolved decisions only when each has an owner and blocks the correct later phase.

## Phase 3 — Create the sprint contract

After PRD approval, copy `assets/SPRINT-TEMPLATE.md`. Create one sprint per independently reviewable outcome. Define:

- source PRD and GitHub issue;
- exact deliverable and user-visible value;
- allowed files and exclusive ownership;
- dependency order;
- acceptance-criterion-to-test mapping;
- stop conditions, time budget, and escalation rule;
- approval boundaries;
- PR and handoff requirements.

Use one isolated worktree and one feature branch. Never let two builders edit the same files. Hermes may conduct the sprint and dispatch specialized builders; it may implement only when explicitly assigned file ownership by the sprint contract.

## Phase 4 — Build in vertical slices

Implement the smallest end-to-end slice that satisfies an acceptance criterion. For each slice:

1. Inspect existing code before editing.
2. Add or identify the failing test or observable check.
3. Implement the slice.
4. Run the narrow check.
5. Commit one coherent, bisectable change.
6. Update the sprint evidence ledger.

Do not create architecture-only documentation when the sprint requests a product artifact. Do not expand scope with unrelated cleanup. Capture worthwhile discoveries as follow-up issues rather than hiding them in the current diff.

## Phase 5 — Audit completion before review

Map every acceptance criterion to evidence:

| Criterion | Status | Evidence | Verification |
| --- | --- | --- | --- |
| Exact criterion | DONE, PARTIAL, NOT DONE, CHANGED, or UNVERIFIABLE | File, test, screenshot, or external check | Raw command or human check |

Treat touched files as insufficient evidence. Require the requested behavior. Any high-impact PARTIAL or NOT DONE item blocks shipping unless Umair explicitly drops it or creates an approved follow-up.

Then run a pre-landing review equivalent to gstack `/review`:

- scope drift and missing requirements;
- correctness, data safety, concurrency, and security;
- error and empty-state handling;
- test sufficiency;
- documentation staleness;
- adversarial second opinion for consequential changes.

Quote the motivating file and line for every finding. Suppress speculation from the main report.

## Phase 6 — Verify and prepare the draft PR

Run fresh verification after the final code change. Never rely on tests from before a fix. Use `assets/PR-BODY-TEMPLATE.md` for the PR.

Required raw evidence:

```bash
git diff --check <base>...HEAD
git diff --name-status <base>...HEAD
git rev-parse HEAD
git status --short
```

Also run the project test and build commands named in the sprint contract. For UI changes, include safe browser or screenshot evidence without attaching to or restarting Umair's live browser.

Never transcribe or invent a SHA. Return the raw command output. If local and remote evidence disagree, report `BLOCKED — EVIDENCE_MISMATCH`.

Open a draft PR only after verification passes. Never merge, deploy, publish, send externally, mutate CRM/QBO, spend, or expand permissions without explicit human approval.

## Evidence-backed completion packet

Return:

```text
OUTCOME:
ARTIFACTS:
ACCEPTANCE: <done>/<total>
TESTS: <raw command + result>
DIFF: <raw name-status>
LOCAL_HEAD: <raw git rev-parse output>
REMOTE_HEAD: <raw ls-remote output or NOT_PUSHED>
RISKS:
APPROVAL_NEEDED:
NEXT_ACTION:
```

Mark status as only one of:

- `DONE — REVIEWABLE_ARTIFACT_EXISTS`
- `BLOCKED — <specific unmet dependency>`
- `CAPPED — <time/cycle cap reached, artifact and continuation supplied>`

Never use `DONE` for authentication, branch creation, a status report, or a handoff alone when the requested PRD, code, test, or product artifact does not exist.

## Anti-loop circuit breaker

Stop and escalate when any of these occurs:

- two consecutive reports contain no artifact change;
- the same reviewer finding recurs after one correction;
- reported evidence cannot be reproduced;
- more than three correction commits are required for a documentation-only sprint;
- the sprint no longer advances the PRD outcome.

Return the root cause, current artifact, safest options, and recommended reset. Do not keep polishing the courier.
