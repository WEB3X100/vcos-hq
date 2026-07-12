# Hermes Dispatch — VCOS-STAB-04 Clean Documentation Proof

**Status:** Ready for Umair to send on Telegram

**Base:** `origin/main@189b66be730cd54ee06b35b1417733858eecfda2`

**Owner:** L2 Hermes (`neuralsync-intern-builder`)

**Timebox:** 45 minutes; stop after three failed transport/auth attempts

## Telegram prompt

```text
ACTIVATE VCOS-STAB-04 — CLEAN DOCUMENTATION PROOF

You are the L2 Hermes Co-Founder operating as a bounded Builder. This is a supervised GitHub issue-to-PR proof, not an open-ended goal.

OUTCOME
Create one clean VCOS dual-laptop architecture document and one evidence handoff on a new branch from the latest origin/main. Prove scope control, Git transport, validation, and handoff quality.

REPOSITORY
C:\Users\92324\VCOS-Coordination\vcos-hq

MANDATORY START
1. Run `git fetch origin --prune`.
2. Confirm `git rev-parse origin/main` equals `189b66be730cd54ee06b35b1417733858eecfda2`.
3. If it does not match, STOP and report `BLOCKED — BASE SHA MISMATCH` with the observed SHA.
4. Protect any untracked runtime/private files. Do not delete, stash, reset, or overwrite them.
5. Create a fresh worktree or clean feature branch from that exact `origin/main`:
   `l2/vcos-stab-04-clean-doc-proof`

ALLOWED WRITES — EXACTLY TWO FILES
1. `docs/vcos-architecture-overview.md`
2. `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/05_Office_Hours_and_Session_Briefs/session-briefs/handoffs/vcos-stab-04-handoff.md`

Do not modify `state.json`, AGENTS.md, skills, profiles, marketing files, project workspaces, credentials, runtime files, or any other path.

DOCUMENT REQUIREMENTS
`docs/vcos-architecture-overview.md` must concisely document:
- VCOS HQ as canonical brain and GitHub as the coordination bus.
- L1 Mac as Sentinel with exclusive `main` merge authority.
- L2 Windows as bounded Builder using feature branches and draft PRs.
- ClickUp as business/outcome truth; GitHub as engineering evidence truth.
- Agents do not share memory directly; they exchange versioned artifacts and handoff packets.
- Telegram is the human relay; no autonomous external sends.
- Tailscale is optional private networking, never a public Git service.
- Secrets stay outside the repo; Draft-Only and human approval gates remain active.

VALIDATION
- Run `git diff --check`.
- Run `git status --short` and confirm only the two allowed files are changed.
- Run the repository STAB-03 secret-scan/check command if present; otherwise inspect the staged diff for `.env`, tokens, secrets, credentials, client PII, or private runtime content.
- Stage only the two allowed files.
- Before commit, run `git diff --cached --name-only`; it must list exactly those two paths.

HANDOFF FILE REQUIREMENTS
Record:
- Mission ID: VCOS-STAB-04
- Full base SHA
- Branch
- Full commit SHA
- Push status
- Exact files touched
- Commands/checks run and results
- Secrets result
- Dirty/untracked items protected, if any, without exposing their contents
- Blockers or `none`
- `READINESS: DRAFT_PR_REVIEW`
- Decision requested: `Umair/L1: review diff and approve or reject; do not infer merge approval.`

DELIVERY
1. Commit message: `docs(stab-04): prove clean L2 documentation delivery`
2. Push only `l2/vcos-stab-04-clean-doc-proof`.
3. Open a draft PR if your authenticated GitHub tooling supports it. Otherwise return the compare URL; do not improvise credentials.
4. Never push to `main`, merge, install a profile, send externally, publish, deploy, or mutate ClickUp.

STOP CONDITIONS
- Base SHA mismatch.
- Dirty tracked tree before edits.
- Any required write outside the two-file allowlist.
- Secret/PII suspicion.
- Three failed transport/auth attempts.
- 45-minute cap.

FINAL TELEGRAM RESPONSE — EXACT FORMAT
SHIP — VCOS-STAB-04
Status: DONE | BLOCKED | CAPPED
Base: [full SHA]
Branch: l2/vcos-stab-04-clean-doc-proof
Commit: [full SHA or none]
Push: [success or exact blocker]
Draft PR: [URL or not opened]
Files: [exact two paths or actual paths if blocked]
Checks: [concise evidence]
Secrets: CLEAN | BLOCKED
READINESS: DRAFT_PR_REVIEW | NOT_READY
Decision: Umair/L1 review required; no merge implied.
HP: VCOS-STAB-04 | [done/blocked/capped] | evidence: [branch/commit/checks] | needs: L1 review | next: review bounded diff
```

## L1 review note

Do not merge the existing `feature/vcos-stab-03-init-docs` branch as-is. Compared with `origin/main`, it contains the architecture document plus unrelated Marketing Mini Intern and cofounder-skill files, and therefore fails the original allowed-file boundary.
