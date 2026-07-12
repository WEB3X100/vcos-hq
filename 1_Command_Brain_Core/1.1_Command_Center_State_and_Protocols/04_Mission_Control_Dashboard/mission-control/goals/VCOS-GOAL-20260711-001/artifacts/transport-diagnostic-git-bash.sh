#!/usr/bin/env bash

# Read-only VCOS L2 transport diagnostic for Git Bash on Windows.
# It does not push, edit configuration, expose keys, or modify repository files.

set +e

echo "TRANSPORT_DIAGNOSTIC_RAW"
echo "repository=$(pwd)"
echo "branch=$(git branch --show-current 2>/dev/null)"
echo "local_head_full=$(git rev-parse HEAD 2>/dev/null)"
echo "tracked_state_begin"
git status --short --branch
echo "tracked_state_end"

if nslookup github.com >/dev/null 2>&1; then
  echo "dns=PASS"
else
  echo "dns=FAIL"
fi

if curl -I --connect-timeout 10 --max-time 20 https://github.com >/dev/null 2>&1; then
  echo "https_443=PASS"
else
  echo "https_443=FAIL"
fi

ssh22_output=$(ssh -T -o BatchMode=yes -o ConnectTimeout=10 -o ConnectionAttempts=1 git@github.com 2>&1)
if printf '%s' "$ssh22_output" | grep -qi "successfully authenticated"; then
  echo "ssh_22=PASS"
elif printf '%s' "$ssh22_output" | grep -Eqi "permission denied|publickey"; then
  echo "ssh_22=AUTH_FAILED"
else
  echo "ssh_22=BLOCKED_OR_UNKNOWN"
fi

ssh443_output=$(ssh -T -p 443 -o BatchMode=yes -o ConnectTimeout=10 -o ConnectionAttempts=1 git@ssh.github.com 2>&1)
if printf '%s' "$ssh443_output" | grep -qi "successfully authenticated"; then
  echo "ssh_443_fallback=PASS"
elif printf '%s' "$ssh443_output" | grep -Eqi "permission denied|publickey"; then
  echo "ssh_443_fallback=AUTH_FAILED"
else
  echo "ssh_443_fallback=BLOCKED_OR_UNKNOWN"
fi

GIT_SSH_COMMAND="ssh -o BatchMode=yes -o ConnectTimeout=10 -o ConnectionAttempts=1 -o ServerAliveInterval=5 -o ServerAliveCountMax=1" git ls-remote origin >/dev/null 2>&1
ls_remote_code=$?
if [ "$ls_remote_code" -eq 0 ]; then
  echo "ls_remote=PASS"
else
  echo "ls_remote=FAIL_EXIT_${ls_remote_code}"
fi

echo "configuration_changed=NO"
echo "destructive_actions=NONE"
echo "diagnostic_complete=YES"

