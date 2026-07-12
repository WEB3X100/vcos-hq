# HTTPS Credential Remediation Matrix — Approval Required

Use only after `HTTPS_CREDENTIAL_AUDIT` returns. This matrix proposes the smallest next action; it does not authorize credential or configuration changes.

| Audit diagnosis | Required evidence | Smallest proposed action | Human approval/action | Verification after action |
| --- | --- | --- | --- | --- |
| `HTTPS_CREDENTIAL_MISSING` | GCM available; noninteractive access reports missing/disabled credentials | human completes one GitHub authentication using the installed GCM command confirmed by its local help output | explicit approval; human completes browser/device authentication | noninteractive `ls-remote`, one push, remote SHA readback |
| `GCM_NOT_AVAILABLE` | no configured/available credential helper | human chooses either repair/install Git Credential Manager or deliberately migrate this repo to SSH with a dedicated L2 key | explicit tooling/transport decision | helper/version check or SSH auth, then `ls-remote` |
| `GCM_HELPER_HANG` | helper exists; bounded noninteractive request times out; network is healthy | inspect GCM version/help and Windows process state; human chooses interactive reauthentication or credential repair | explicit approval before UI, credential deletion, repair, or update | bounded `ls-remote` before push |
| `PROXY_CONFLICT` | Git or environment proxy is present and request fails while direct HTTPS is healthy | human/network owner validates the proxy; propose session-only proxy bypass only if policy allows | explicit network-policy approval | bounded `ls-remote` with approved route |
| `HTTPS_REPOSITORY_ACCESS_DENIED` | authentication completes but repository returns denial/not found | human verifies the authenticated GitHub account and its access to `WEB3X100/vcos-hq` | human account/repository access check | `ls-remote` under confirmed account |
| `UNKNOWN` | incomplete, contradictory, or unclassified output | make no change; run one narrower evidence query | no mutation | new evidence packet |

## Hard constraints

- Never display, paste, store in repo, or transmit a token/password.
- Never run credential `erase`, `reject`, or delete Windows Credential Manager entries without separate explicit approval and a recovery plan.
- Never install/update Git or GCM implicitly.
- Never change `remote.origin.url` merely because another transport is familiar.
- Never generate an SSH key unless Umair explicitly selects an SSH migration after reviewing the HTTPS diagnosis.
- Authentication is performed by the human in the provider/browser/device flow; Hermes may verify status afterward.
- After a fix: one noninteractive `ls-remote`; if PASS, one push attempt; then exact remote SHA readback.
- Approval expires after the first failure or successful remote SHA readback.

## Approval format

```text
HTTPS_FIX_APPROVAL
goal_id: VCOS-GOAL-20260711-001
diagnosis: <exact audit diagnosis>
approved_action: <one matrix action>
authentication_human_present: YES|NOT_REQUIRED
remote_change_allowed: NO
credential_value_exposure_allowed: NO
push_attempts_after_ls_remote_pass: 1
destructive_actions: 0
expires: first failure or successful remote SHA readback
```

