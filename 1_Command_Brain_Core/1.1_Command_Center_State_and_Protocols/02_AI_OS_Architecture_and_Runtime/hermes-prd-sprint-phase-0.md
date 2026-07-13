# Sprint Contract — Hermes PRD-to-Sprint Delivery Factory Phase 0

**Source PRD:** `hermes-prd-sprint-delivery-factory.md`

**GitHub issue:** Pending — the private-repo connector returned 404 and this host lacks `gh`; create it with the draft PR.

**Owner:** Umair / L1

**Conductor:** Codex for bootstrap; Hermes after approval

**Base ref:** `origin/main`

**Feature branch:** `codex/hermes-prd-sprint-factory`

**Worktree:** isolated temporary worktree

**Time/cycle cap:** one bootstrap sprint; stop after two status-only turns or one repeated evidence failure

## Sprint Outcome

Deliver a runnable VCOS skill candidate that converts an approved outcome into a validator-backed PRD, bounded sprint, reviewed implementation, and evidence-backed draft PR. This sprint establishes the contract and deterministic quality gate; it does not grant Hermes autonomous merge or deployment authority.

## Non-Goals

- Install gstack into Hermes.
- Enable unattended GitHub issue scanning or repository writes.
- Merge, deploy, publish, send externally, or mutate client systems.
- Rebuild gstack inside VCOS.

## Allowed Files and Ownership

| Path or glob | Exclusive owner | Change |
| --- | --- | --- |
| `AGENTS.md` | Bootstrap conductor | Add the delivery fast path and evidence rule. |
| `CLAUDE.md` | Bootstrap conductor | Add runtime routing. |
| `.github/ISSUE_TEMPLATE/hermes-sprint.yml`, `.github/pull_request_template.md`, `.github/workflows/hermes-prd-quality.yml` | Bootstrap conductor | Enforce the sprint contract and PRD quality in GitHub. |
| `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/02_AI_OS_Architecture_and_Runtime/hermes-*` | Bootstrap conductor | Add canonical PRD and sprint; update Hermes playbook. |
| `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/00_Live_State_and_GSD/state.md` | Bootstrap conductor | Record the validation blocker. |
| `1_Command_Brain_Core/1.2_Headquarters_Memory/decisions.md` | Bootstrap conductor | Record durable trust and authority decisions. |
| `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/candidates/hermes-prd-sprint-conductor/**` | Bootstrap conductor | Implement the skill, templates, reference, validator, and proof log. |
| `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/{candidates/README.md,skill-registry.md,vcos-task-skill-map.md}` | Bootstrap conductor | Register and route the candidate. |

No two builders may own the same path concurrently.

## Dependency Order

```text
Failure evidence -> gstack adaptation -> PRD contract -> skill and validator
                 -> HQ routing -> deterministic checks -> adversarial review
                 -> commit -> draft PR
```

## Work Items

| ID | PRD requirement | Deliverable | Owner | Test first | Status |
| --- | --- | --- | --- | --- | --- |
| S-1 | FR-1, FR-2 | Canonical PRD and bounded Office Hours rules | Bootstrap conductor | PRD validator | DONE |
| S-2 | FR-3, FR-4, FR-5 | Sprint template, file ownership, work-item and acceptance mapping | Bootstrap conductor | Template inspection | DONE |
| S-3 | FR-6, FR-7, FR-8 | Completion audit, review, and fresh-verification gates | Bootstrap conductor | Skill validation | DONE |
| S-4 | FR-9, FR-10, FR-11 | PR body, evidence rules, and circuit breaker | Bootstrap conductor | Positive/negative validator cases | DONE |
| S-5 | FR-12 | HQ router, registry, decisions, and Hermes playbook updates | Bootstrap conductor | Link/path review | DONE |
| S-5b | FR-13 | GitHub issue form, PR template, and PRD quality workflow | Bootstrap conductor | YAML parse and local workflow-command replay | PARTIAL — local PASS; remote CI pending draft PR |
| S-6 | NFR-1 through NFR-6 | Final QA, local commit, and draft PR | Bootstrap conductor | `git diff --check` and adversarial review | BLOCKED — branch pushed; issue/draft PR tooling unavailable |

## Acceptance-to-Evidence Matrix

| Acceptance criterion | Status | Evidence required | Verification command/procedure |
| --- | --- | --- | --- |
| AC-1 | DONE | Real PRD passes deterministic validation. | `python3 .../scripts/validate_prd.py .../hermes-prd-sprint-delivery-factory.md` |
| AC-2 | DONE | This contract names one outcome, ownership, tests, stops, and gates. | Human/readback review of this file. |
| AC-3 | DONE | Skill contains acceptance-status taxonomy and audit packet. | Search `SKILL.md` for DONE, CHANGED, PARTIAL, NOT DONE, and UNVERIFIABLE. |
| AC-4 | PARTIAL | Evidence policy requires raw local and remote SHA output. | Policy exists; verify raw equality during publish. |
| AC-5 | DONE | Circuit breaker is present in the skill and HQ instructions. | Search for `two consecutive status-only turns`. |
| AC-6 | DONE | Checks run after the final edit. | Record commands and results in `validation-log.md`. |
| AC-7 | PARTIAL | Draft PR contains outcome, evidence, risk, rollback, and gates. | Template passes readback; verify the created PR during publish. |
| AC-8 | DONE | Human approval boundaries are explicit. | Readback of skill, PRD, playbook, and this contract. |
| AC-9 | PARTIAL | GitHub validates the PRD, negative template, and diff hygiene. | YAML and commands pass locally; remote Actions run requires the draft PR. |

## Risks and Approval Gates

| Risk/action | Mitigation | Human approval required |
| --- | --- | --- |
| False completion evidence | Fresh raw commands and exact SHA comparison | No for read-only verification; yes before merge |
| Scope creep | Frozen file table and diff audit | Yes to expand the file boundary |
| gstack browser helper affects live browser | Pointer-only use; browser safety rule remains active | Yes before browser-control scripts |
| Autonomous remote mutation | Bootstrap stops at a draft PR | Yes for merge, deploy, issue automation, or expanded authority |

## Stop Conditions

- Missing approved decision or credential.
- File ownership collision.
- Test or build failure after the defined correction cap.
- Evidence mismatch between local and remote.
- Scope no longer advances the PRD outcome.

## Evidence Ledger

| Time | Work item | Artifact/evidence | Result |
| --- | --- | --- | --- |
| 2026-07-13 | S-1 through S-5 | PRD, skill, validator, templates, routing changes | Created; deterministic validation pending final edit |
| 2026-07-13 | S-6 | Positive/negative validation, path audit, diff check, adversarial review | PASS; two findings corrected; commit/PR pending |
| 2026-07-13 | S-6 | Commit and SSH branch push | PASS; issue and draft PR blocked by connector 404 plus missing `gh` |
| 2026-07-13 | S-5b | GitHub issue form, PR template, workflow YAML, and local command replay | PASS locally; remote Actions pending draft PR |

## Sprint Exit Gate

- [x] Requested artifact exists and is usable.
- [ ] Every acceptance criterion is DONE, CHANGED with equivalent value, or explicitly dropped by Umair.
- [x] Tests/build ran after the final behavioral change.
- [x] Diff contains only approved scope.
- [x] Adversarial review has no unresolved P0/P1 findings.
- [ ] Draft PR and raw evidence packet exist.
- [x] Merge/deploy/publication remains human-gated.
