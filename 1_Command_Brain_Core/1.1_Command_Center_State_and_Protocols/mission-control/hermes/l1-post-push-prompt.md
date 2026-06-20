# L1 Hermes Prompt — After L2 Pushes Collaboration Test

**Profile:** `vcos-brain-grok`  
**Workdir:** `~/VCOS-Coordination/vcos-hq` or `/Users/umairkhalid/_VCOS_Headquarters`

Paste after L2 reports complete on Telegram:

---

L1 review: L2 week1-git-collab-test.

Workdir: [your VCOS HQ path]

PATH PREFIX:
MC=1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/mission-control
HANDOFFS=1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/session-briefs/handoffs

1. git pull origin main
2. git fetch origin l2/collab-test-2026-06-20
3. Read HANDOFFS/l2-collab-test-response-2026-06-20.md
4. Verify test contract in HANDOFFS/l1-week1-git-collab-test-2026-06-20.md (all checks pass?)
5. Update MC/state.json:
   - cubicle_l1.last_session: L2 collab test reviewed
   - cubicle_l2: confirm active_mission status
   - github.open_branches: include l2/collab-test-2026-06-20
   - flywheel.delegation_level: L0 → L1 if test passed
6. Draft 3-line summary for Umair: merge branch Y/N?

Do not merge to main without Umair approval.