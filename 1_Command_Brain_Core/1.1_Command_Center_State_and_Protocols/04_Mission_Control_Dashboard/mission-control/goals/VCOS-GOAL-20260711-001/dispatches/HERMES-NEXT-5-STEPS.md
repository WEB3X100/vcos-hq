# Hermes Dispatch — Next Five Steps

```text
GOAL ID: VCOS-GOAL-20260711-001
MODE: supervised, Draft-Only
OBJECTIVE: deliver existing local commit bd3bf12 to a remotely verifiable draft review surface without modifying its contents.

PRESERVE EXACTLY:
- branch: feature/vcos-stab-03-init-docs
- commit: bd3bf12
- artifact: docs/vcos-architecture-overview.md
- existing handoff path reported by L2

DO NOT edit, amend, rebase, reset, clean, delete, stash, force-push, recreate the commit, change authentication, change the remote, copy credentials, merge, install, publish, deploy, or mutate ClickUp/CRM/QBO.

STEP 1 — Run the bounded Git Bash diagnostic

From the repository root, execute:
bash 1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/04_Mission_Control_Dashboard/mission-control/goals/VCOS-GOAL-20260711-001/artifacts/transport-diagnostic-git-bash.sh

If this goal packet is not yet available on L2 because the stabilization branch cannot be fetched, run the commands embedded in that script from the packet provided by L1. Do not claim the file was read from GitHub unless it was.

STEP 2 — Classify; do not guess

Use only these classes:
- DNS_FAILURE
- HTTPS_443_FAILURE
- PORT_22_BLOCKED
- SSH_AUTH_FAILURE
- REPOSITORY_ACCESS_FAILURE
- PUSH_TIMEOUT
- UNKNOWN_TRANSPORT_FAILURE

Do not call this PUSH_TIMEOUT unless DNS, HTTPS, SSH authentication, and `git ls-remote origin` pass.

If SSH 22 fails but SSH 443 fallback authenticates, STOP and request approval to configure SSH-over-443. Do not change configuration yourself.

STEP 3 — One bounded push attempt

Only when `git ls-remote origin` passes, run exactly once:
git push -u origin feature/vcos-stab-03-init-docs

If it fails or times out, stop. Do not retry and do not change the branch.

STEP 4 — Verify delivery and prepare review

Run:
git ls-remote --heads origin refs/heads/feature/vcos-stab-03-init-docs

READY_FOR_L1_REVIEW requires the returned remote SHA to equal the full SHA resolved from local commit bd3bf12.

If equal, create a draft PR if supported. Otherwise provide this comparison URL:
https://github.com/WEB3X100/vcos-hq/compare/main...feature/vcos-stab-03-init-docs

Update the handoff status truthfully. Do not say PR created without a PR URL or number.

STEP 5 — Return one compact evidence packet

TRANSPORT_DIAGNOSTIC_V2
goal_id: VCOS-GOAL-20260711-001
branch:
local_head_full:
tracked_state:
protected_untracked:
dns: PASS|FAIL|NOT_RUN
https_443: PASS|FAIL|NOT_RUN
ssh_22: PASS|BLOCKED|AUTH_FAILED|NOT_RUN
ssh_443_fallback: PASS|BLOCKED|AUTH_FAILED|NOT_RUN
ls_remote: PASS|TIMEOUT|AUTH_FAILED|NOT_RUN
failure_class:
configuration_changed: NO
destructive_actions: NONE
push: PASS|FAIL|TIMEOUT|NOT_ATTEMPTED
remote_head_full:
sha_match: PASS|FAIL|NOT_VERIFIED
draft_pr:
comparison_url:
handoff_path:
mission_status: READY_FOR_L1_REVIEW|BLOCKED_TRANSPORT
next_action:

Stop after returning this packet.
```

