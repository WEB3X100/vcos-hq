# PRD — Hermes PRD-to-Sprint Delivery Factory

**Status:** Draft for one supervised proof run
**Owner:** Umair / L1 Sentinel
**Conductor:** Hermes on L2
**Source outcome:** Replace status-heavy Git coordination with useful PRDs, product artifacts, tests, and reviewable pull requests
**Last verified:** 2026-07-13

## Executive Summary

Hermes must become a delivery conductor, not a status-report generator. Given one approved VCOS outcome, it should create a code-grounded PRD, convert the PRD into a bounded GitHub sprint, supervise an isolated builder, audit every acceptance criterion, run fresh verification, and return a draft pull request plus no more than three human decisions. The first release is an internal, supervised workflow. It does not grant autonomous merge, deployment, external communication, CRM/QBO mutation, spending, or publishing authority.

## User and Problem Evidence

- **Primary user:** Umair, operating VCOS across two laptops and multiple AI runtimes.
- **Supporting users:** L1 Sentinel/reviewer, L2 Hermes conductor, and bounded Builder/Skeptic agents.
- **Current job:** Turn business or product intent into complete, independently reviewable engineering work without repeatedly reconstructing context.
- **Observed pain:** PR #2 required four commits (`42e98a6`, `13ac17b`, `7885993`, `ac0dae6`) to deliver roughly sixty lines of documentation. The exchange included transport reports, repeated PR metadata, an invented SHA, an incomplete wording correction, and a false final-newline claim. The original Hermes Co-Founder PRD was not produced during that loop.
- **Evidence source:** The 2026-07-13 VCOS-STAB-04 task conversation and GitHub PR `WEB3X100/vcos-hq#2`.
- **Why now:** Git transport is working. The next bottleneck is product and engineering throughput. Continuing status-first behavior would automate coordination cost rather than artifact creation.

## Current State

VCOS has strong but disconnected ingredients: Office Hours, approval gates, a build cockpit, handoff packets, GitHub branches, adversarial reviews, and the pointer-first gstack Arsenal clone. The missing contract is a single workflow that forces Hermes to chain them into a product result.

The current operating model also says Hermes is a cadence agent that may never execute builds. That boundary is safe for unsupervised cron work but too broad for supervised engineering. The corrected model is: Hermes conducts an approved sprint, may dispatch isolated builders, and may implement only files explicitly assigned to it in the sprint contract. It still cannot merge, deploy, publish, send externally, mutate client systems, spend, or expand permissions without approval.

Gstack upstream `v1.60.1.0` was reviewed from commit `7c9df1c568a9ea745508f679a329332b2c338063`. Its useful pattern is the artifact chain—Office Hours, spec, plan review, implementation, plan-completion audit, adversarial review, fresh verification, and ship—not the wholesale copying of its generated prompt surface.

## Desired Outcome and Success Metrics

| Metric | Baseline | Target | Measurement source |
| --- | --- | --- | --- |
| Durable artifact before status churn | No PRD produced in the STAB-04 loop | First PRD draft within two non-blocked Hermes turns | Session transcript and artifact path |
| Acceptance-criterion traceability | No requirement-to-evidence matrix | 100% of Must criteria mapped to evidence before PR | Sprint contract and PR body |
| False completion evidence | Invented SHA and incorrect newline claim observed | Zero false or manually fabricated evidence claims | Raw Git/test output and L1 reproduction |
| Documentation-only correction commits | Three correction commits after initial delivery | At most one correction commit before circuit breaker | Git log |
| Human repair time | Multiple review-and-reprompt rounds | Under 15 minutes for each of three supervised missions | Sprint scorecard |
| Useful sprint completion | Transport proof only | Three consecutive accepted missions: PRD, small build, revenue-support artifact | GitHub PRs and human acceptance |

## Scope

### In Scope

- One reusable `hermes-prd-sprint-conductor` skill candidate in VCOS HQ.
- Backlog-ready PRD, sprint contract, and PR body templates.
- A deterministic PRD structure validator.
- Routing rules in `AGENTS.md` and `CLAUDE.md`.
- Skill registry and task-map entries.
- Raw-evidence rules and a circuit breaker for repeated non-delivery.
- A phased path to install current gstack skills for the Hermes host after human approval.
- Three supervised proof missions before any recurring issue scanner.

### Out of Scope

- Installing software or credentials on Laptop 2 during this PR.
- Automatic GitHub issue creation, merge, deployment, or release.
- Automatic ClickUp mutation or task closure.
- Autonomous external messages, customer/vendor communication, publishing, CRM/QBO changes, or spending.
- A new dashboard, Castle room, generalized multi-agent swarm, or second project-management database.
- Replacing ClickUp, GitHub, VCOS HQ, GBrain, or Graphify as existing sources of truth.

## User Journeys

### Primary journey

1. Umair supplies or approves one outcome.
2. Hermes reads the VCOS fast path and the owning project interface.
3. Hermes runs Office Hours only if the outcome is vague; otherwise it begins the PRD.
4. Hermes inspects current repository evidence, writes the PRD, and runs the validator.
5. Umair approves or reshapes the PRD.
6. Hermes creates a sprint contract with one branch, one worktree, exact file ownership, acceptance-to-test mapping, and stop conditions.
7. Hermes dispatches or acts as the bounded builder for one vertical slice at a time.
8. Hermes audits plan completion, runs adversarial review and fresh tests, and prepares a draft PR.
9. Umair receives a reviewable artifact, raw evidence, risks, and no more than three decisions.
10. Umair alone decides whether to merge or authorize any later external action.

### Failure and recovery journeys

1. If the outcome is ambiguous, Hermes stops implementation and returns a decision packet rather than guessing.
2. If authentication or transport fails, Hermes returns one diagnostic blocker and preserves the artifact; it does not repeat status-only attempts indefinitely.
3. If the same finding recurs after one correction, Hermes triggers the circuit breaker and asks for a reset or human edit.
4. If evidence is inconsistent, Hermes reports `BLOCKED — EVIDENCE_MISMATCH` and returns raw commands.
5. If a builder crosses file ownership, Hermes stops both edits and reconciles ownership before continuing.

## Functional Requirements

| ID | Requirement | Priority | Evidence when complete |
| --- | --- | --- | --- |
| FR-1 | Route vague outcomes through Office Hours and accepted outcomes directly to PRD creation. | Must | Decision packet or PRD path |
| FR-2 | Inspect repository evidence before technical PRD questions or architecture choices. | Must | Cited files/current-state section |
| FR-3 | Generate every required PRD section and pass the deterministic validator. | Must | Validator PASS output |
| FR-4 | Require explicit human PRD approval before implementation. | Must | Approval recorded in active task/thread |
| FR-5 | Generate one sprint contract per reviewable outcome with file ownership and stop conditions. | Must | Sprint contract path |
| FR-6 | Use one isolated worktree and feature branch for implementation. | Must | Raw branch/worktree evidence |
| FR-7 | Map every acceptance criterion to test or observable evidence. | Must | Completion audit matrix |
| FR-8 | Run scope-drift, plan-completion, and adversarial reviews before ship readiness. | Must | Review packet with resolved findings |
| FR-9 | Run fresh tests/build checks after the final behavioral change. | Must | Raw command output |
| FR-10 | Prepare a draft PR with risks, rollback, approval boundaries, and raw SHAs. | Must | Draft PR URL and body |
| FR-11 | Reject status-only completion and fabricated/transcribed evidence. | Must | Circuit-breaker behavior and raw evidence |
| FR-12 | Retain human authority for merge, deployment, external action, client mutation, spending, and skill installation. | Must | Approval section and no unauthorized action |

## Non-Functional Requirements

| ID | Requirement | Target | Verification |
| --- | --- | --- | --- |
| NFR-1 | Context efficiency | Load fast path, project interface, PRD, and current diff only | Handoff context inventory |
| NFR-2 | Correction efficiency | One correction attempt per repeated review finding | Git log and circuit-breaker output |
| NFR-3 | Evidence integrity | Machine-generated identifiers returned verbatim | Local/remote SHA equality |
| NFR-4 | Reviewability | One outcome and no overlapping file owners per sprint | Sprint contract audit |
| NFR-5 | Reversibility | No force-push; logical commits; rollback documented | Git history and PR body |
| NFR-6 | Platform compatibility | Templates and validator run on macOS and Windows Python 3 | Supervised L1/L2 dry run |

## Data, Interfaces, and Architecture

```text
Umair outcome / ClickUp business task
                 |
                 v
       Hermes Conductor on L2
        |        |         |
        v        v         v
   PRD/spec   Sprint     Evidence ledger
        |        |         |
        +--------+---------+
                 |
                 v
       isolated Builder worktree
                 |
         code + tests + artifact
                 |
                 v
   completion audit + Skeptic review
                 |
                 v
           draft GitHub PR
                 |
                 v
       Umair/L1 merge decision
```

ClickUp owns the business outcome, priority, owner, and approval. GitHub Issues own repository requirements. GitHub PRs own proposed changes and engineering evidence. VCOS HQ owns durable policy and skill routing. Hermes owns orchestration state only for the active sprint and must not become another task database.

## Security and Approval Gates

- **Data classification:** HQ policy and internal engineering evidence; no client raw data is required for the first proof run.
- **Permissions:** Read repository context; write only the approved worktree and file allowlist; push only the sprint branch after verification.
- **Human approvals:** PRD direction, main merge, installation on Hermes, deployment, external communication, CRM/QBO changes, spending, publishing, and permission expansion.
- **Prohibited actions:** Force-push, silent remote switching, credential copying, browser-session hijacking, client-system mutation, or declaring approval by inference.

## Failure Modes and Recovery

| Failure | Detection | User/system response | Recovery |
| --- | --- | --- | --- |
| Status loop without artifact | Two consecutive reports with no artifact diff | Trigger circuit breaker | Return current artifact, root cause, and reset options |
| Fabricated SHA or test result | Independent command differs from report | Block ship readiness | Return raw output and log a prevention rule |
| Incomplete PRD | Validator fails or reviewer score is below threshold | Do not file/implement | Correct the named gaps and rerun once |
| Scope drift | Diff contains work not mapped to PRD/sprint | Block or split work | Remove unrelated change or create follow-up issue |
| Missing requirement | Completion audit reports PARTIAL/NOT DONE | Block draft-ready status | Implement, explicitly drop, or create approved follow-up |
| Conflicting edits | Two agents own the same path | Stop affected builders | Reassign exclusive ownership and resume from clean state |
| Stale test evidence | Code changed after test output | Reject evidence | Rerun test/build after final change |
| Dirty base checkout | Unrelated changes exist in working tree | Do not build there | Create an isolated worktree from approved base |

## Acceptance Criteria

- [ ] AC-1: Given an approved outcome, Hermes creates a validator-passing PRD before any implementation edit.
- [ ] AC-2: Given an approved PRD, Hermes creates a sprint contract with one artifact, exact file ownership, tests, stop conditions, and approval gates.
- [ ] AC-3: Given a completed implementation, every acceptance criterion is classified as DONE, CHANGED, PARTIAL, NOT DONE, or UNVERIFIABLE with evidence.
- [ ] AC-4: Given any final completion claim, local and remote SHAs are returned as raw command output and match independently.
- [ ] AC-5: Given two status-only turns or one repeated correction finding, Hermes stops and returns the circuit-breaker packet instead of continuing token-heavy coordination.
- [ ] AC-6: Given a small supervised build, fresh tests and build checks pass after the final behavioral change.
- [ ] AC-7: Given a ship-ready sprint, the draft PR contains the outcome, source PRD/issue, acceptance evidence, risks, rollback, and approval boundaries.
- [ ] AC-8: Given no explicit human authorization, Hermes does not merge, deploy, publish, send externally, mutate client systems, spend, or install capabilities.

## Test Plan

| Layer | Scenario | Command or procedure | Expected result |
| --- | --- | --- | --- |
| Unit | Complete PRD validates | Run validator against this file | Exit 0 and PASS summary |
| Unit | Template with placeholders fails | Run validator against untouched PRD template | Non-zero exit and named placeholders |
| Integration | Skill creates PRD and sprint from one outcome | Supervised Hermes dry run | Both artifacts exist and map to each other |
| Integration | Evidence mismatch | Supply a deliberately incorrect reported SHA | Hermes blocks and returns raw evidence |
| End-to-end | Documentation mission | Issue through branch, review, draft PR | Accepted with under 15 minutes human correction |
| End-to-end | Small tested build | PRD through test and draft PR | Requested behavior works and tests pass |
| End-to-end | Revenue-support artifact | Draft-only AMAX or AgentOSync-safe artifact | Useful artifact exists; no external action occurs |

```bash
python3 4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/candidates/hermes-prd-sprint-conductor/scripts/validate_prd.py 1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/02_AI_OS_Architecture_and_Runtime/hermes-prd-sprint-delivery-factory.md
python3 4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/candidates/hermes-prd-sprint-conductor/scripts/validate_prd.py 4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/candidates/hermes-prd-sprint-conductor/assets/PRD-TEMPLATE.md
git diff --check
```

The first command must pass. The untouched template must fail because it intentionally contains placeholders.

## Rollout and Rollback

- **Rollout sequence:** Merge the candidate artifacts; manually load the skill on Laptop 2; run the PRD mission; run a small build; run a draft-only revenue-support mission.
- **Feature gate:** Manual invocation only until three consecutive accepted missions.
- **Rollback trigger:** Repeated false evidence, scope violations, unauthorized action, or more than 15 minutes average human repair across the proof missions.
- **Rollback procedure:** Disable the candidate in Hermes, retain the artifacts for review, revert the candidate commit through a normal Git revert, and return Hermes to read-only cadence mode.

## Delivery Phases

| Phase | User-visible deliverable | Dependencies | Exit gate |
| --- | --- | --- | --- |
| 0 | Candidate skill, templates, validator, and this PRD in VCOS HQ | L1 review | Draft PR accepted |
| 1 | Complete Hermes Co-Founder PRD | Umair product decisions | Validator passes and Umair approves scope |
| 2 | One documentation sprint | GitHub auth and isolated worktree | Accepted PR with no false completion claims |
| 3 | One small tested product slice | Phase 2 pass | Working behavior, tests, and under 15 minutes correction |
| 4 | One draft-only revenue-support artifact | Approved AMAX/AgentOSync-safe inputs | Useful artifact accepted; no external mutation |
| 5 | Optional recurring issue scan | Three consecutive accepted missions | Separate human approval and calibrated limits |

## Open Decisions

| Decision | Owner | Deadline | Blocks phase |
| --- | --- | --- | --- |
| Choose the Phase 1 product wedge inside the Hermes Co-Founder PRD interview | Umair | Before Phase 1 implementation | Phase 1 |
| Approve installing current gstack Hermes-host skills on Laptop 2 | Umair | After Phase 0 PR review | Automated gstack invocation only |

## Definition of Done

- [ ] All Must requirements have evidence.
- [ ] This PRD passes the deterministic validator.
- [ ] The skill passes Skill Creator validation.
- [ ] Acceptance criteria are mapped to passing verification.
- [ ] No high-impact plan item is PARTIAL or NOT DONE.
- [ ] Documentation reflects the delivered workflow.
- [ ] Three supervised missions meet correction and evidence targets.
- [ ] Draft PRs contain risks, approvals, and raw evidence.
- [ ] Human merge, installation, deployment, and external-action decisions remain explicit.
