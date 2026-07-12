---
goal_id: VCOS-GOAL-20260711-001
status: active
cycle: 3
project: WEB3X100/vcos-hq
owner: Sentinel (Codex)
created: 2026-07-11 America/Toronto
updated: 2026-07-11 America/Toronto
max_cycles: 3
cycle_minutes: 30
draft_only: true
lanes: [codex, hermes-l2, skeptic, evidence]
---

# Goal — Deliver VCOS-STAB-03 to a reviewable GitHub draft PR

## Done means

1. L2 produces a complete Git Bash transport diagnostic with DNS, HTTPS 443, SSH 22, SSH 443 fallback, and `git ls-remote` results.
2. The failure is classified from evidence and only the smallest non-destructive fix is applied with any required human approval.
3. Remote branch `feature/vcos-stab-03-init-docs` exists and its remote SHA equals local commit `bd3bf12`.
4. A draft PR or verifiable GitHub comparison URL exists, and the handoff truthfully links the artifact, commit, validation, and remaining blockers.
5. A next bounded mission draft exists but is not activated, merged, installed, published, or sent externally.

## Machine checks

| Check | Command or method | Required result | Status | Evidence |
| --- | --- | --- | --- | --- |
| Remote branch exists | `git ls-remote --heads origin refs/heads/feature/vcos-stab-03-init-docs` | one row returned | FAIL | `artifacts/machine-checks.md` |
| Remote/local SHA agree | compare remote SHA with `bd3bf12` | exact match | BLOCKED | `artifacts/machine-checks.md` |
| Draft review surface exists | PR URL or GitHub comparison URL opens | URL recorded | BLOCKED | `artifacts/evidence-ledger.md` |
| Goal packet integrity | required files exist, script parses, and `git diff --check` exits 0 | PASS | PASS | `artifacts/machine-checks.md` |

## Non-goals

- Merge to `main`.
- Amend, rebase, reset, clean, delete, stash, or recreate `bd3bf12`.
- Install or modify the Hermes profile.
- Fix Castle or edit the documentation artifact during transport recovery.
- Mutate ClickUp, publish content, deploy, spend, or send client-facing messages.
- Enable SSH-over-443 or change remotes without an evidence-backed need and explicit human approval.

## Approval gates

- Human approval is required before changing SSH configuration, changing the Git remote, copying credentials, or using a different authentication method.
- Human review is required before merging any PR.
- Draft-only: no publish, spend, external send, install, deploy, or business-system mutation.

## Budgets

| Budget | Limit | Stop action |
| --- | --- | --- |
| Max cycles | 3 | stop and summarize remaining truths |
| Cycle wall-clock | 30 minutes | preserve evidence and return blocked handoff |
| Push retries | 1 after `ls-remote` passes | stop as `BLOCKED_TRANSPORT` |
| Destructive commands | 0 | abort mission |
| Files L2 may modify | handoff only, and only after transport result | stop on any other diff |

## Preflight

| Capability | Result | Evidence |
| --- | --- | --- |
| Native goal tooling | active | goal registered in current Codex task |
| L1 repository inspection | available | remote branch absent during last check |
| L2 Windows execution | cross-host dispatch required | `dispatches/HERMES-NEXT-5-STEPS.md` |
| Sandbox / approval posture | supervised, Draft-Only | this goal contract |

## Known blockers

| Blocker | Owner | Unblocks |
| --- | --- | --- |
| L2 `git ls-remote` and push timeout | Hermes L2 / Umair for auth changes | remote branch and PR |
| Commit `bd3bf12` exists only on L2 | Hermes L2 | L1 diff inspection |

## File ownership manifest

| Cycle | Lane | Writable paths | Reviewer-only paths | Forbidden paths |
| --- | --- | --- | --- | --- |
| 1 | codex/evidence | this goal directory | repository outside goal directory | dirty L1 main worktree |
| 1 | hermes-l2 | existing mission handoff only if update is required | committed artifact and local branch | all other repository files; `.hermes`; credentials |
| 2 | skeptic | none | diagnostic, remote readback, PR, handoff | all writes |

## Five-step lane plan

| Step | Owner | Deliverable | Gate |
| --- | --- | --- | --- |
| 1 | Hermes L2 | Git Bash diagnostic | all six transport fields reported |
| 2 | Sentinel + human if needed | failure classification and smallest fix | no configuration change without approval |
| 3 | Hermes L2 | one push attempt | `ls-remote` must pass first |
| 4 | Hermes L2 + L1 | remote SHA readback, draft PR/comparison URL, handoff | remote SHA equals `bd3bf12` |
| 5 | Sentinel | next documentation mission draft | no activation before review |

## Truth tracker

| # | Truth | Status | Evidence | Last cycle |
| --- | --- | --- | --- | --- |
| 1 | complete diagnostic | PASS | L2 returned complete `TRANSPORT_DIAGNOSTIC_V2`: DNS/HTTPS pass, SSH 22 auth fails, SSH 443 blocked | 3 |
| 2 | evidence-backed fix | UNKNOWN | read-only SSH identity audit required before proposing a change | 3 |
| 3 | remote SHA agreement | FAIL | GitHub still has no feature branch ref | 2 |
| 4 | draft review surface and handoff | BLOCKED | no remote branch or PR can exist | 2 |
| 5 | next mission draft prepared | PASS | verified one-file router-path mission in `artifacts/NEXT-MISSION-DRAFT.md` | 1 |

## Stop conditions

- All truths and machine checks pass.
- Transport remains blocked after the bounded diagnostic and one authorized fix.
- Any request for secrets, destructive recovery, remote/auth change, merge, or external action.
- Cycle or time budget reached.
