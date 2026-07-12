# Hermes Dispatch — Direct GCM Helper Test

```text
GOAL: VCOS-GOAL-20260711-001
ENVIRONMENT: Windows L2 Git Bash
MODE: read-only command-scoped helper test

Preserve:
- branch feature/vcos-stab-03-init-docs
- commit bd3bf12c2c85e6034e4b69780d46dce69f9a81b0
- origin https://github.com/WEB3X100/vcos-hq.git

Do not edit Git configuration, credentials, remotes, repository files, branches, or commits. Do not open an interactive login, push, reset, clean, stash, rebase, force-push, install, or update anything.

Run from the repository root:

pwd
git branch --show-current
git rev-parse HEAD
git config --show-origin --get-all credential.helper

echo "DIRECT_MANAGER_NONINTERACTIVE_TEST"
test_output=$(timeout 30s env \
  GIT_TERMINAL_PROMPT=0 \
  GCM_INTERACTIVE=0 \
  git \
    -c credential.helper= \
    -c credential.helper=manager \
    -c credential.interactive=false \
    ls-remote origin 2>&1)
test_exit=$?

if [ "$test_exit" -eq 0 ]; then
  echo "direct_manager_result=PASS"
elif [ "$test_exit" -eq 124 ]; then
  echo "direct_manager_result=TIMEOUT"
elif printf '%s' "$test_output" | grep -Eqi 'authentication failed|could not read Username|terminal prompts disabled|403|access denied|repository not found'; then
  echo "direct_manager_result=AUTH_OR_ACCESS_FAILED"
else
  echo "direct_manager_result=UNKNOWN_FAILURE"
fi
echo "direct_manager_exit=$test_exit"

echo "PERSISTENT_HELPER_AFTER_TEST"
git config --show-origin --get-all credential.helper

Safety:
- The empty `credential.helper=` and `credential.helper=manager` values apply only to this single command.
- Do not print `test_output`, credential values, Windows Credential Manager contents, tokens, usernames, passwords, or trace secrets.
- Do not run with interactive authentication.
- Do not persist `manager` yet.
- Do not push.

Return only:

GCM_DIRECT_HELPER_TEST
goal_id: VCOS-GOAL-20260711-001
repository:
branch:
local_head_full:
persistent_helper_before:
direct_manager_result: PASS|TIMEOUT|AUTH_OR_ACCESS_FAILED|UNKNOWN_FAILURE
direct_manager_exit:
persistent_helper_after:
persistent_config_unchanged: YES|NO
diagnosis: HELPER_SELECTOR_HANG|CREDENTIAL_MISSING_OR_ACCESS_DENIED|GCM_OR_NETWORK_HANG|UNKNOWN
smallest_proposed_fix:
approval_required: YES
configuration_changed: NO
credentials_changed: NO
destructive_actions: NONE
next_action:

Then stop.
```

