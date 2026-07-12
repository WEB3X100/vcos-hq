# SSH Remediation Matrix — Approval Required

Use only after `SSH_IDENTITY_AUDIT` returns a supported diagnosis. This file proposes fixes; it does not authorize Hermes to apply them.

## Selection rule

Choose exactly one row matching the audit evidence. If the evidence fits multiple rows or the named key cannot be identified by its public fingerprint, stop as `UNKNOWN`.

| Audit diagnosis | Required evidence | Smallest proposed fix | Persistence | Human action |
| --- | --- | --- | --- | --- |
| `AGENT_NOT_RUNNING` | private/public key pair exists; no agent socket | start an SSH agent for the current Git Bash session, load the explicitly approved existing key, test `ssh -T`, then `git ls-remote` | session only | approve named key fingerprint before loading |
| `KEY_NOT_LOADED` | agent runs; approved key pair exists; fingerprint absent from `ssh-add -l` | load only the approved existing key into the current agent and retest | agent/session dependent | approve named key fingerprint |
| `WRONG_KEY_SELECTED` | trace offers a different key; correct registered public fingerprint is known | use a one-command `GIT_SSH_COMMAND` with the approved identity and `IdentitiesOnly=yes`; do not edit config initially | one command | approve identity selection |
| `KEY_NOT_REGISTERED_WITH_GITHUB` | key is offered; GitHub rejects it; public fingerprint is known | human adds the existing public key to the correct GitHub account, then L2 retests | GitHub account | human performs GitHub key registration |
| `SSH_CONFIG_CONFLICT` | effective host/user/identity differs from intended values | test a one-command override first; propose a minimal config patch only after proof | one command, then optional persistent config | approve override; separately approve config patch |
| `KEY_NOT_PRESENT` | no usable key pair exists | human decides whether to generate a dedicated L2 key or use an approved HTTPS credential flow | persistent credential | explicit credential-creation decision |
| `UNKNOWN` | incomplete or contradictory evidence | no change | none | rerun a narrower audit |

## Guardrails

- Never print or transmit a private key, passphrase, token, or credential-helper content.
- Never copy the L1 private key to L2.
- Never select a key from filename alone; compare its public fingerprint.
- Never add every available key to the agent.
- Never edit `~/.ssh/config`, change the Git remote, or switch to HTTPS as an implicit fallback.
- Never retry push until `ssh -T` authenticates and `git ls-remote origin` succeeds.
- After any approved fix, run one authentication test, one `ls-remote`, one push attempt, and one remote SHA readback.
- Preserve `feature/vcos-stab-03-init-docs` and `bd3bf12c2c85e6034e4b69780d46dce69f9a81b0` throughout.

## Approval response format

After the audit, L1 should authorize a fix using:

```text
SSH_FIX_APPROVAL
goal_id: VCOS-GOAL-20260711-001
diagnosis: <exact audit diagnosis>
approved_public_fingerprint: <fingerprint or NOT_APPLICABLE>
approved_action: <one matrix action>
persistence: session-only|github-account|one-command|persistent-config
push_attempts_after_fix: 1
destructive_actions: 0
expires: after remote SHA readback or first failure
```

