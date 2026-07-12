#!/usr/bin/env bash

# Read-only SSH identity audit for Windows Git Bash.
# This script does not load/create keys, modify configuration, change remotes, or push.

set +e

echo "SSH_IDENTITY_AUDIT_RAW"
echo "repository=$(pwd)"
echo "branch=$(git branch --show-current 2>/dev/null)"
echo "local_head_full=$(git rev-parse HEAD 2>/dev/null)"
echo "origin_url=$(git config --get remote.origin.url 2>/dev/null)"

echo "ssh_files_begin"
find ~/.ssh -maxdepth 1 -type f -printf '%f\n' 2>/dev/null | sort
echo "ssh_files_end"

echo "agent_identities_begin"
ssh-add -l 2>&1
echo "agent_identities_end"

echo "effective_github_config_begin"
ssh -G github.com 2>/dev/null \
  | grep -Ei '^(hostname|user|port|identityfile|identitiesonly) '
echo "effective_github_config_end"

echo "public_key_fingerprints_begin"
for key in ~/.ssh/*.pub; do
  [ -f "$key" ] || continue
  ssh-keygen -lf "$key" 2>/dev/null
done
echo "public_key_fingerprints_end"

echo "sanitized_auth_trace_begin"
ssh -Tv \
  -o BatchMode=yes \
  -o ConnectTimeout=10 \
  -o ConnectionAttempts=1 \
  git@github.com 2>&1 \
  | grep -Ei 'connecting to|connection established|identity file|offering public key|server accepts key|authentications that can continue|permission denied|successfully authenticated'
echo "sanitized_auth_trace_end"

echo "configuration_changed=NO"
echo "credentials_changed=NO"
echo "destructive_actions=NONE"
echo "audit_complete=YES"

