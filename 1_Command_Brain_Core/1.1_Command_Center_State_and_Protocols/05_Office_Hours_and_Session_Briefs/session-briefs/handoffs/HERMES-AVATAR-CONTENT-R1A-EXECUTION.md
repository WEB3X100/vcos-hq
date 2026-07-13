# Hermes Execution Dispatch — Avatar Content System R1A

**Mission ID:** `AVATAR-CONTENT-R1A`

**Status:** Ready for Telegram activation after L2 confirms the approved base SHA

**PRD:** `docs/prds/hermes-supervised-avatar-content-inbound-system-v1.md`

**Approved base branch:** `origin/codex/vcos-hq-canonical-r1`

**Approved base SHA:** `f945b64a36075f9aa56209798d05cfff0e78adf6`

**Timebox:** 120 minutes maximum; checkpoint at 45 and 90 minutes

## Outcome

Implement the Release 1A contract scaffold from the PRD: shared data envelope, Mini Intern registry/permissions, and three candidate skills (`content-router`, `source-ledger`, `content-intelligence`) with schemas, sanitized fixtures, deterministic eval scaffolding, documentation, and evidence.

This mission builds internal contracts only. It does not access social accounts, generate media, use identity assets, send messages, publish, spend credits, mutate CRM, install profiles, or deploy.

## Required start sequence

1. Run `git fetch origin --prune`.
2. Record the full `origin/codex/vcos-hq-canonical-r1` SHA.
3. Confirm it equals `f945b64a36075f9aa56209798d05cfff0e78adf6`.
4. If it differs, stop with `BLOCKED — BASE SHA MISMATCH`.
5. Confirm tracked worktree is clean. Protect untracked/private runtime files; do not delete or overwrite them.
6. Create a fresh branch `l2/avatar-content-r1a-contracts` from the exact approved integration SHA—not from local `main`.
7. Read `AGENTS.md`, the HQ fast path, and the PRD. Do not broad-load project or legacy folders.

## Allowed writes

```text
4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/candidates/agentosync-avatar-content-system/
1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/05_Office_Hours_and_Session_Briefs/session-briefs/handoffs/avatar-content-r1a-handoff.md
```
No other paths may be changed.

## Required package structure

```text
agentosync-avatar-content-system/
├── README.md
├── capability-registry.yaml
├── shared/
│   ├── record-envelope.schema.json
│   ├── permissions-matrix.yaml
│   └── fixtures/
├── agentosync-content-router/
│   ├── SKILL.md
│   ├── README.md
│   ├── input.schema.json
│   ├── output.schema.json
│   ├── permissions.yaml
│   ├── fixtures/
│   ├── evals/
│   └── CHANGELOG.md
├── agentosync-source-ledger/
│   └── [same package contract]
└── agentosync-content-intelligence/
    └── [same package contract]
```

## Implementation rules

- Status is `candidate` and maturity is `designed` until fixture/eval evidence justifies `fixture-proven`.
- The router selects the smallest workflow and enforces separation of duties; it does not reproduce specialist instructions.
- All schemas use explicit required fields and reject unknown fields where practical.
- Every output uses the shared record envelope: stable ID, timestamps, parent/source IDs, owner, approval state, sensitivity, evidence, version/checksum, allowed next actions, blockers, and audit events.
- Permissions must default deny external messaging, publishing, browsing private accounts, scraping, CRM writes, identity assets, media generation, credential access, spend, deployment, profile installation, and durable memory mutation.
- Fixtures are synthetic and contain no real client, creator, DM, testimonial, likeness, or voice data.
- Include at least six fixtures: valid public evidence, missing provenance, private/client data, copied-language risk, unsupported claim, and ambiguous approval.
- Evals must return deterministic pass/block outcomes and name the blocking rule.
- No skill may claim installed, live, production-ready, or autonomous.

## Verification

Run and record:

1. `git diff --check`
2. Exact allowed-path check using `git status --short`
3. JSON parsing/schema validation using an available local tool
4. YAML parsing when a local parser exists; otherwise document manual structural verification
5. Fixture/eval command and results
6. Repository secret scan command used by STAB-03, if available
7. `git diff --cached --name-only` before commit

If a required verifier is unavailable, do not install dependencies or use the network. Record the limitation and provide a portable follow-up command.

## Review requirement

Use a separate Reviewer/QA session or Mini Intern after implementation. It owns review notes only and must challenge:

- missing deny rules;
- schemas that allow evidence-free completion;
- producer/self-approval;
- copied-language leakage;
- private/client data leakage;
- ambiguous approval treated as authorization;
- false maturity or completion claims;
- scope outside the three R1A skills.

Fix blocking findings before delivery, then rerun verification.

## Git delivery

- Commit message: `feat(content-system): scaffold supervised R1A contracts`
- Push only `l2/avatar-content-r1a-contracts`.
- Open a draft PR if authenticated tooling supports it; otherwise provide the GitHub compare URL.
- Never merge or push directly to `main`.

## Handoff contract

Create `avatar-content-r1a-handoff.md` with:

- mission and status (`done`, `blocked`, or `capped`);
- approved base SHA, branch, and full commit SHA;
- exact file manifest;
- verification commands/results;
- fixture/eval summary;
- Reviewer/QA findings and fixes;
- maturity of each capability with evidence;
- blockers and open risks;
- no more than three decisions for Umair;
- exact recommended next mission;
- one-line HP.

## Stop conditions

- Base SHA mismatch.
- Dirty tracked tree before mission work.
- Any required edit outside the allowlist.
- Real client, creator, identity, private-message, or credential data encountered.
- A request for network access, install, permission expansion, external action, or spend.
- Three repeated failures on the same step.
- 120-minute hard cap.

## Final response format

```text
SHIP — AVATAR-CONTENT-R1A
Status: DONE | BLOCKED | CAPPED
Base: [full SHA]
Branch: l2/avatar-content-r1a-contracts
Commit: [full SHA or none]
Push: [success or exact blocker]
Draft PR: [URL or not opened]
Artifacts: [root path + handoff]
Checks: [pass/fail summary]
Maturity: [three skill statuses]
External actions: NONE
Decisions: [maximum three]
HP: AVATAR-CONTENT-R1A | [done/blocked/capped] | evidence: [commit/checks] | needs: L1 review | next: [mission]
```
