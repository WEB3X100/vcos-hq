# Hermes Dispatch — Read-Only HTTPS Credential Audit

```text
GOAL: VCOS-GOAL-20260711-001
ENVIRONMENT: Windows L2 Git Bash
MODE: read-only HTTPS credential/helper audit

Preserve branch feature/vcos-stab-03-init-docs and commit bd3bf12c2c85e6034e4b69780d46dce69f9a81b0.

The remote is HTTPS. Do not create SSH keys, start ssh-agent, change transports, change the remote, erase/store credentials, open credential-manager UI, push, or edit repository/configuration files.

Run from the repository root:

pwd
git branch --show-current
git rev-parse HEAD
git config --show-origin --get remote.origin.url
git --version

echo "CREDENTIAL_HELPERS"
git config --show-origin --get-all credential.helper 2>&1

echo "CREDENTIAL_USE_HTTP_PATH"
git config --show-origin --get credential.useHttpPath 2>&1

echo "GCM_AVAILABILITY"
if command -v git-credential-manager >/dev/null 2>&1; then
  git-credential-manager --version 2>&1
elif command -v git-credential-manager-core >/dev/null 2>&1; then
  git-credential-manager-core --version 2>&1
else
  echo "GCM_NOT_FOUND"
fi

echo "PROXY_PRESENCE"
if git config --get http.proxy >/dev/null 2>&1; then
  echo "git_http_proxy=CONFIGURED"
else
  echo "git_http_proxy=NOT_CONFIGURED"
fi
if [ -n "${HTTPS_PROXY:-}" ] || [ -n "${https_proxy:-}" ]; then
  echo "https_proxy_env=PRESENT"
else
  echo "https_proxy_env=ABSENT"
fi

echo "NONINTERACTIVE_LS_REMOTE"
GIT_TERMINAL_PROMPT=0 GCM_INTERACTIVE=Never \
  git -c credential.interactive=never ls-remote origin 2>&1
echo "ls_remote_exit=$?"

Safety:
- Do not run `git credential fill`, `approve`, `reject`, `erase`, or `store`.
- Do not print tokens, passwords, Windows Credential Manager entries, proxy values, or environment secrets.
- Do not apply a fix or retry push.
- If `ls-remote` outputs repository refs, report PASS but do not reproduce the entire ref list.
- If it returns an error, report only the error class and a short sanitized message.

Return only:

HTTPS_CREDENTIAL_AUDIT
goal_id: VCOS-GOAL-20260711-001
repository:
branch:
local_head_full:
origin_url:
git_version:
credential_helpers:
credential_use_http_path:
gcm_status: AVAILABLE|NOT_FOUND|ERROR
gcm_version:
git_http_proxy: CONFIGURED|NOT_CONFIGURED
https_proxy_env: PRESENT|ABSENT
noninteractive_ls_remote: PASS|AUTH_FAILED|TIMEOUT|NETWORK_FAILED|HELPER_FAILED|UNKNOWN
ls_remote_exit:
sanitized_error:
diagnosis: HTTPS_CREDENTIAL_MISSING|GCM_NOT_AVAILABLE|GCM_HELPER_HANG|PROXY_CONFLICT|HTTPS_REPOSITORY_ACCESS_DENIED|UNKNOWN
smallest_proposed_fix:
approval_required: YES
configuration_changed: NO
credentials_changed: NO
destructive_actions: NONE
next_action:

Then stop.
```

