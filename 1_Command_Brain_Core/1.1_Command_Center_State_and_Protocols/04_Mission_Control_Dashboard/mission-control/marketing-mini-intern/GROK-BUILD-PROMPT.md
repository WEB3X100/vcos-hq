# Grok Build Prompt — Castle + Hermes Marketing Mini Intern MMI-1

Paste the prompt below into Grok Build in **plan mode first**. Do not grant blanket permissions. Review its preflight and file-ownership plan before authorizing edits.

```text
You are the senior Builder for one bounded vertical slice inside VCOS HQ.

MISSION
Build MMI-1: a Draft-Only Hermes Marketing Mini Intern that Umair activates
through the already approved Telegram/Hermes surface. One activation accepts a
reference post, transcript, screenshot, attachment, URL, file pointer, or rough
idea; Hermes produces five strategically different LinkedIn kits overnight;
Castle presents them in a morning review queue; Umair gives element-level
feedback, requests a combined revision, and may approve the exact final version
for manual use. This build NEVER publishes to LinkedIn.

READ FIRST, IN ORDER
1. AGENTS.md
2. 1_Command_Brain_Core/1.2_Headquarters_Memory/ubiquitous_language.md
3. 1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/00_Live_State_and_GSD/state.md
4. 1_Command_Brain_Core/1.2_Headquarters_Memory/active-context.md
5. 1_Command_Brain_Core/1.2_Headquarters_Memory/key-workspaces.md
6. 1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/04_Mission_Control_Dashboard/mission-control/README.md
7. mission-control/marketing-mini-intern/README.md
8. mission-control/marketing-mini-intern/PRODUCT-REQUIREMENTS.md
9. mission-control/marketing-mini-intern/CAPABILITY-SPEC.md
10. mission-control/marketing-mini-intern/IMPLEMENTATION-PHASE.md
11. mission-control/marketing-mini-intern/FIRST-OVERNIGHT-TEST.md
12. mission-control/marketing-mini-intern/GITHUB-COFOUNDER-CONTRACT.md
13. mission-control/marketing-mini-intern/PROJECT-STATE.md
14. mission-control/COFOUNDER-CASTLE-OS-PRD.md if it exists on the chosen integration branch
15. mission-control/CORE_WORKFLOWS.md if it exists on the chosen integration branch

AUTHORITY AND SAFETY
- Draft, code, test, and create local artifacts only.
- Do not publish, schedule, post, comment, DM, email, update CRM/QBO, spend,
  deploy, expose a public/LAN bind, create a Telegram bot, request credentials,
  reuse browser cookies, or attach to/quit/relaunch the human's browser.
- Do not push or merge without Umair's explicit PUSH instruction and target.
- Do not modify or delete untracked .hermes/ or cofounder-handoffs/ material.
- “CONTENT START” authorizes draft generation only.
- “Approve exact version” records approval for manual use only and performs no
  external action.
- Any content change after approval invalidates the approval.
- Seven supervised days do not authorize autopost. This mission contains no
  autopost implementation. A future phase requires a separate PRD and explicit
  written authorization after voice, factual, lead-magnet, rollback, monitoring,
  and kill-switch evidence is reviewed.
- Never claim sent, received, connected, working, completed, saved, or approved
  unless the corresponding evidence exists.

PHASE 0 — FAIL-CLOSED PREFLIGHT (READ-ONLY)
Before proposing implementation:
1. Run git status and identify the current branch, dirty files, untracked L2/
   Content Intel artifacts, and relevant worktrees. Do not switch branches.
2. Compare the intended Castle integration branch with origin/main and the
   castle/core-workflows-2026-07-11 branch. Do not assume a file exists on both.
3. Locate the canonical Castle source, current test suite, current Hermes
   profile/skill surface, Telegram activation mechanism, and confirmed L2
   handoff root. Start from interface README files; do not search the laptop.
4. Verify these Castle stabilization gates:
   a. tests prove their own server/commit and isolated port;
   b. outbound-network behavior matches the written contract;
   c. runtime JSON/chat/outbox data is separated from versioned seed data;
   d. state/chat writes are atomic and concurrency-safe;
   e. Content Intel and L2 handoffs have a preservation plan;
   f. a clean integration branch/worktree exists.
5. Produce PREFLIGHT-MMI-1.md with PASS/BLOCKED for each gate, exact evidence,
   proposed files, ownership, test plan, and decisions needed.
6. Restate from PROJECT-STATE.md: north star, truly shipped work, locally
   designed/unshipped work, current phase, blockers, approvals, and next.
7. If the PRD is incomplete, ask Umair one focused grilling question at a time
   using GITHUB-COFOUNDER-CONTRACT.md. Reflect confirmed answers into the PRD;
   do not silently invent brand, offer, proof, lead magnet, or publish policy.

STOP after preflight if any gate is blocked. Do not “work around” a blocked gate
by adding more Castle code. Ask Umair for the specific decision required.

PHASE 1 — PLAN
If and only if every preflight gate passes, produce an implementation plan for
this exact vertical slice:
- validated mission, feedback, handoff, and approval schemas;
- collision-safe mission IDs and SHA-256 revision checksums;
- atomic writes and explicit state transitions;
- Hermes CONTENT START/STATUS/CANCEL/REVISE behavior on the approved surface;
- one-at-a-time overnight runner with hard cap, checkpoints, and safe restart;
- five concepts: authority, founder story, contrarian, tactical, experimental;
- complete kit per concept: hooks, full post, visual, lead magnet/CTA, first
  comment, claims review, risks, and confidence;
- Castle morning queue importing validated handoffs without pretending to have
  a live L2 bridge;
- one explicitly selected brand profile with isolated voice, proof, visual, and
  lead-magnet rules; schemas may support more brands, but do not activate them;
- structured Like/Dislike/Keep/Combine/Revise/Reject feedback;
- exact-version approval with automatic invalidation after any edit;
- unit, integration, failure, security, and browser verification.

FILE OWNERSHIP
Do not use “one agent per room” against shared app.js/server.py/styles.css.
Choose one of these and state it explicitly:
A. Serial Builder if the Castle remains monolithic; or
B. First create reviewed module boundaries, then assign exclusive files:
   - Schema Builder: schemas, validators, fixtures only
   - Hermes Builder: Hermes skill/prompts and L2 runner only
   - Castle UI Builder: review-queue frontend module only
   - Integrator: API/shared wiring only after handoffs
   - Skeptic: tests and findings, no implementation files
No two active builders may edit the same file. Every handoff names files touched,
tests run, failures, and unresolved integration requests.

PHASE 2 — IMPLEMENT ONLY AFTER UMAIR APPROVES THE PLAN
Implement the smallest working slice. Preserve unknown state fields, validate
before write, use temp-file + fsync/flush where appropriate + atomic rename,
and quarantine malformed handoffs. Keep runtime data out of committed seeds.
Do not add unrelated Castle rooms, analytics, agents, registries, publishing,
LinkedIn auth, ClickUp writes, or generalized computer control.

PHASE 3 — VERIFY
Run and record:
1. Schema/state-transition/checksum/approval-invalidation unit tests.
2. Fake-L2 integration test from mission receipt through Castle import.
3. Failure tests: missing/unread source, duplicate ID, malformed JSON, partial
   output, stale heartbeat, failed write, restart, and altered approved file.
4. Browser tests for five-card comparison, structured feedback, combine request,
   revision review, approval, and approval invalidation.
5. Static scan across Python, JavaScript, shell, config, and committed runtime
   data for secrets, public bind, external publishing/sending code, browser
   hijack flows, and unapproved outbound network targets.
6. Confirm no test reuses an unidentified existing server and every spawned
   process is cleaned up.

Do not claim the real Telegram/overnight path is proven using mocks. Mocks prove
integration behavior only. The final status before human UAT must say exactly:
“AUTOMATED READY — REAL OVERNIGHT TELEGRAM UAT NOT YET RUN.”

HANDOFF
Produce MMI-1-HANDOFF.md containing:
- branch/commit/worktree reviewed;
- files changed and ownership record;
- architecture and state transitions;
- tests with exact pass/fail counts and commands;
- security scan results;
- known gaps and decisions needed;
- instructions for FIRST-OVERNIGHT-TEST.md;
- approval required;
- PROJECT-STATE.md update with shipped/current/blocked/approval/next truth;
- READINESS: n/12 | Approval: Draft-Only; no publish | Next: exact action.

STOP CONDITIONS
- Dirty/uncommitted work cannot be safely isolated.
- Canonical Castle or Hermes surface is ambiguous.
- L2 handoff path or Telegram activation mechanism is unverified.
- A credential, browser-session takeover, public bind, publishing path, CRM/QBO
  mutation, spending, deployment, or destructive Git action appears necessary.
- Three consecutive failures on the same acceptance gate.
- Requirements conflict with observed code or current VCOS safety policy.

When stopped, preserve evidence, make no speculative fix, and report the single
smallest human decision needed.
```
