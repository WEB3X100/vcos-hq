# Hermes Dispatch — Post-Authentication Verify and Push

This dispatch is inactive until L1 supplies a completed `HTTPS_FIX_APPROVAL` and the approved human authentication action finishes.

```text
GOAL: VCOS-GOAL-20260711-001
ENVIRONMENT: Windows L2 Git Bash
MODE: verify approved authentication fix, push once, and prove remote SHA

REQUIRED INPUT:
<PASTE COMPLETED HTTPS_FIX_APPROVAL HERE>

Preserve:
- branch feature/vcos-stab-03-init-docs
- commit bd3bf12c2c85e6034e4b69780d46dce69f9a81b0
- origin https://github.com/WEB3X100/vcos-hq.git

Do not amend, rebase, reset, clean, stash, force-push, edit files, change the remote, expose credentials, merge, install, publish, deploy, or mutate external business systems.

1. Verify preflight:

git branch --show-current
git rev-parse HEAD
git status --short --branch
git config --get remote.origin.url

Stop unless branch, full HEAD, and origin exactly match the preserved values. Protected untracked paths are allowed only when unchanged and outside mission scope.

2. Verify repository access noninteractively:

timeout 30s env GIT_TERMINAL_PROMPT=0 GCM_INTERACTIVE=Never \
  git -c credential.interactive=never ls-remote origin

Stop if this does not pass. Do not push.

3. Push exactly once:

git push -u origin feature/vcos-stab-03-init-docs

Stop after any failure or timeout. Do not retry.

4. Verify exact remote SHA:

git rev-parse HEAD
git ls-remote --heads origin refs/heads/feature/vcos-stab-03-init-docs

The two full SHAs must exactly equal bd3bf12c2c85e6034e4b69780d46dce69f9a81b0.

5. If and only if SHA match passes, return the comparison URL:

https://github.com/WEB3X100/vcos-hq/compare/main...feature/vcos-stab-03-init-docs

Create a draft PR only if an available authorized tool returns a PR URL/number. Do not merge.

Return only:

POST_AUTH_DELIVERY
goal_id: VCOS-GOAL-20260711-001
approval_diagnosis:
approved_action_observed_complete: YES|NO
branch:
local_head_full:
origin_url:
tracked_state:
protected_untracked:
noninteractive_ls_remote: PASS|FAIL|TIMEOUT
push: PASS|FAIL|TIMEOUT|NOT_ATTEMPTED
remote_head_full:
sha_match: PASS|FAIL|NOT_VERIFIED
draft_pr:
comparison_url:
configuration_changed_beyond_approval: NO
credential_values_exposed: NO
destructive_actions: NONE
mission_status: READY_FOR_L1_REVIEW|BLOCKED_TRANSPORT|BLOCKED_PREFLIGHT
next_action:

Then stop.
```

