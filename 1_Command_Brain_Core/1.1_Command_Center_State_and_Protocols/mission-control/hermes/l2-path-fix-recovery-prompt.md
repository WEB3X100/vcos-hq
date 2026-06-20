# L2 Recovery Prompt — Path Fix + Re-validate Collab Test

**Use when:** Prompt 1 reported `mission-control/state.json` missing but git remote is correct.

**Root cause:** Files live under `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/` — not repo root.

**Profile:** `neuralsync-intern-builder`  
**Workdir:** repo root (`C:\Users\92324\VCOS-Coordination\vcos-hq` on Windows)

---

```text
L2 PATH RECOVERY — week1-git-collab-test

Workdir: C:\Users\92324\VCOS-Coordination\vcos-hq
Profile: neuralsync-intern-builder

PATH PREFIX (use for ALL reads/writes):
MC=1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/mission-control
HANDOFFS=1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/session-briefs/handoffs

Step 1 — Sync main
git fetch origin
git checkout main
git pull origin main

Step 2 — Verify files (must all succeed)
ls MC/state.json
ls HANDOFFS/MISSION-QUEUE.md
ls HANDOFFS/l1-week1-git-collab-test-2026-06-20.md
ls MC/dual-hermes-collaboration-protocol.md

Step 3 — Reconcile branch
git checkout l2/collab-test-2026-06-20
git merge main
(If conflicts: keep main versions of MC/* and HANDOFFS/*, preserve l2 response file)

Step 4 — Fix or create response handoff at CORRECT path
HANDOFFS/l2-collab-test-response-2026-06-20.md
Include: hostname, git hash, pull verification checkboxes, Windows path note.

Step 5 — Update MC/state.json cubicle_l2:
status=active, active_mission=week1-git-collab-test, active_branch=l2/collab-test-2026-06-20, last_push=ISO now

Step 6 — Commit and push
git add MC/state.json HANDOFFS/l2-collab-test-response-2026-06-20.md
git commit -m "L2: path-corrected collab test response (HQ_MC prefix)"
git push origin l2/collab-test-2026-06-20

Do NOT merge to main.

Final output:
## L2 Recovery Complete
- Files found at HQ_MC: Y/N
- Branch: 
- Commit:
- Push:
- Wrong-path files at repo root mission-control/: [list if any — should delete]
```