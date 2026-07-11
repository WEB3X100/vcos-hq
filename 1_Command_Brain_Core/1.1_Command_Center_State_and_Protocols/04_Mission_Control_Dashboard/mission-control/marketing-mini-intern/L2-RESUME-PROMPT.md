# L2 Hermes Resume Prompt — Fetch MMI Coordination Branch

Send this to the existing approved Hermes co-founder Telegram surface.

```text
MISSION: Resume MMI-1 preflight from the newly published GitHub coordination branch.

TRUTH UPDATE
- Your previous stop was correct: the required Castle/MMI files were absent from your local main.
- L1 has now published branch: codex/hermes-marketing-mini-intern
- Expected first packet commit: a96b3fd
- This branch is based on Castle commit 40253c5.
- The branch is design/review state only. Nothing is merged, implemented, live,
  connected, scheduled, or approved for publishing.

SAFETY
- Preserve untracked .hermes/, cofounder-handoffs/, and the dealership file.
- Do not reset --hard, clean, delete, move, merge, or push main.
- Do not create publishing, LinkedIn auth, Telegram bot, CRM/QBO, spend,
  deployment, browser takeover, or autopost behavior.
- This turn is read-only fetch + verification + PRD interrogation/preflight.

GIT
1. Report `git status --short --branch` and current HEAD.
2. Run `git fetch origin codex/hermes-marketing-mini-intern`.
3. Verify `origin/codex/hermes-marketing-mini-intern` exists and report its SHA.
4. Do not switch the dirty/current checkout if switching risks untracked files.
   Read files with `git show origin/codex/hermes-marketing-mini-intern:<path>`
   or create a separate safe worktree only if your environment permits it.
5. If expected branch/commit is absent, STOP and report observed refs.

READ FROM THAT EXACT REMOTE REF
Base directory:
1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/04_Mission_Control_Dashboard/mission-control/

Read in order:
1. README.md
2. marketing-mini-intern/README.md
3. marketing-mini-intern/GITHUB-COFOUNDER-CONTRACT.md
4. marketing-mini-intern/PROJECT-STATE.md
5. marketing-mini-intern/PRODUCT-REQUIREMENTS.md
6. marketing-mini-intern/CAPABILITY-SPEC.md
7. marketing-mini-intern/IMPLEMENTATION-PHASE.md
8. marketing-mini-intern/FIRST-OVERNIGHT-TEST.md
9. marketing-mini-intern/GROK-BUILD-PROMPT.md
10. COFOUNDER-CASTLE-OS-PRD.md
11. CORE_WORKFLOWS.md

RESPONSE CONTRACT
First restate:
- observed branch/commit;
- north star;
- truly shipped vs designed/unimplemented work;
- current bounded phase;
- blockers and approval boundaries;
- the single next action.

Then re-run Phase 0 preflight against this remote ref. Do not implement.

If requirements still need human decisions, begin the PRD grilling protocol:
ask Umair ONE focused question at a time. Start with the highest-leverage open
decision: which single brand will be the first seven-day supervised marketing
workflow. Wait for his answer before asking the next question.

Return:
READINESS: n/12 | Approval: Draft-Only; no publish/autopost | Next: exact action
```
