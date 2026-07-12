# Hermes Dispatch — Read-Only SSH Identity Audit

```text
GOAL: VCOS-GOAL-20260711-001
ENVIRONMENT: Windows L2 Git Bash
MODE: read-only identity audit

Preserve branch feature/vcos-stab-03-init-docs and commit bd3bf12c2c85e6034e4b69780d46dce69f9a81b0.

Do not edit files, load or create keys, run ssh-add, change SSH/Git configuration, change the remote, open credential managers, print private-key contents, push, reset, clean, stash, rebase, or force anything.

Preferred execution when the goal artifact is available locally:

bash 1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/04_Mission_Control_Dashboard/mission-control/goals/VCOS-GOAL-20260711-001/artifacts/ssh-identity-audit-git-bash.sh

If the artifact cannot be fetched because transport is blocked, run these equivalent commands from the repository root:

pwd
git branch --show-current
git rev-parse HEAD
git config --show-origin --get remote.origin.url

echo "SSH_DIRECTORY_FILENAMES"
find ~/.ssh -maxdepth 1 -type f -printf '%f\n' 2>/dev/null | sort

echo "SSH_AGENT_IDENTITIES"
ssh-add -l 2>&1

echo "EFFECTIVE_GITHUB_SSH_CONFIG"
ssh -G github.com 2>/dev/null | grep -Ei '^(hostname|user|port|identityfile|identitiesonly) '

echo "PUBLIC_KEY_FINGERPRINTS"
for key in ~/.ssh/*.pub; do
  [ -f "$key" ] || continue
  ssh-keygen -lf "$key"
done

echo "SANITIZED_SSH_AUTH_TRACE"
ssh -Tv -o BatchMode=yes -o ConnectTimeout=10 -o ConnectionAttempts=1 git@github.com 2>&1 \
  | grep -Ei 'connecting to|connection established|identity file|offering public key|server accepts key|authentications that can continue|permission denied|successfully authenticated'

Safety rules:
- Public key fingerprints and public-key filenames are allowed.
- Do not print public-key bodies, private-key contents, tokens, passphrases, credential-helper contents, environment secrets, or full verbose logs.
- `ssh-add -l` is inspection only. Do not run `ssh-add` without `-l`.
- Do not apply a fix in this mission.

Return only:

SSH_IDENTITY_AUDIT
goal_id: VCOS-GOAL-20260711-001
repository:
branch:
local_head_full:
origin_url:
ssh_files:
agent_status: RUNNING_WITH_IDENTITIES|RUNNING_NO_IDENTITIES|NOT_RUNNING|UNKNOWN
agent_fingerprints:
effective_hostname:
effective_port:
effective_user:
effective_identity_files:
identities_only:
public_key_fingerprints:
keys_offered_to_github:
github_accepted_key: YES|NO|UNKNOWN
diagnosis: KEY_NOT_PRESENT|AGENT_NOT_RUNNING|KEY_NOT_LOADED|WRONG_KEY_SELECTED|KEY_NOT_REGISTERED_WITH_GITHUB|SSH_CONFIG_CONFLICT|UNKNOWN
smallest_proposed_fix:
approval_required: YES
configuration_changed: NO
credentials_changed: NO
destructive_actions: NONE
next_action:

Then stop.
```
