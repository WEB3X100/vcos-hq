#!/usr/bin/env bash

# Read-only HTTPS/Git Credential Manager audit for Windows Git Bash.
# Does not display credentials, change config/remotes, or push.

set +e

echo "HTTPS_CREDENTIAL_AUDIT_RAW"
echo "repository=$(pwd)"
echo "branch=$(git branch --show-current 2>/dev/null)"
echo "local_head_full=$(git rev-parse HEAD 2>/dev/null)"
echo "origin_url=$(git config --get remote.origin.url 2>/dev/null)"
echo "git_version=$(git --version 2>/dev/null)"

echo "credential_helpers_begin"
git config --show-origin --get-all credential.helper 2>&1
echo "credential_helpers_end"

use_http_path=$(git config --show-origin --get credential.useHttpPath 2>/dev/null)
if [ -n "$use_http_path" ]; then
  echo "credential_use_http_path=$use_http_path"
else
  echo "credential_use_http_path=UNSET"
fi

if command -v git-credential-manager >/dev/null 2>&1; then
  echo "gcm_command=git-credential-manager"
  git-credential-manager --version 2>&1
elif command -v git-credential-manager-core >/dev/null 2>&1; then
  echo "gcm_command=git-credential-manager-core"
  git-credential-manager-core --version 2>&1
else
  echo "gcm_command=NOT_FOUND"
fi

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

if ! command -v timeout >/dev/null 2>&1; then
  echo "noninteractive_ls_remote=NOT_RUN"
  echo "ls_remote_exit=TIMEOUT_COMMAND_NOT_FOUND"
else
  ls_output=$(timeout 30s env \
    GIT_TERMINAL_PROMPT=0 \
    GCM_INTERACTIVE=Never \
    git -c credential.interactive=never ls-remote origin 2>&1)
  ls_code=$?

  if [ "$ls_code" -eq 0 ]; then
    echo "noninteractive_ls_remote=PASS"
    echo "ls_remote_exit=0"
  elif [ "$ls_code" -eq 124 ]; then
    echo "noninteractive_ls_remote=TIMEOUT"
    echo "ls_remote_exit=124"
  elif printf '%s' "$ls_output" | grep -Eqi 'authentication failed|could not read Username|terminal prompts disabled|403|access denied|repository not found'; then
    echo "noninteractive_ls_remote=AUTH_OR_ACCESS_FAILED"
    echo "ls_remote_exit=$ls_code"
  elif printf '%s' "$ls_output" | grep -Eqi 'could not resolve host|failed to connect|connection.*timed out|network is unreachable'; then
    echo "noninteractive_ls_remote=NETWORK_FAILED"
    echo "ls_remote_exit=$ls_code"
  else
    echo "noninteractive_ls_remote=UNKNOWN_FAILURE"
    echo "ls_remote_exit=$ls_code"
  fi
fi

echo "configuration_changed=NO"
echo "credentials_changed=NO"
echo "destructive_actions=NONE"
echo "audit_complete=YES"

