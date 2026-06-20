# L2 Hermes Prompt — Week 1 Git Collaboration Test

**Profile:** `neuralsync-intern-builder`  
**Workdir:** `~/VCOS-Coordination/vcos-hq` (after clone)

Paste as first message on Laptop 2:

---

You are NeuralSync Intern on Laptop 2. Execute mission `week1-git-collab-test`.

Workdir: ~/VCOS-Coordination/vcos-hq

Read in order:
1. mission-control/state.json
2. session-briefs/handoffs/MISSION-QUEUE.md
3. session-briefs/handoffs/l1-week1-git-collab-test-2026-06-20.md
4. mission-control/dual-hermes-collaboration-protocol.md

Execute every task in the L1 handoff exactly:
- git pull origin main
- git checkout -b l2/collab-test-2026-06-20
- Write session-briefs/handoffs/l2-collab-test-response-2026-06-20.md (use template in handoff)
- Update mission-control/state.json cubicle_l2 fields
- git commit and git push -u origin l2/collab-test-2026-06-20
- Do NOT merge to main

Post Telegram summary when done.

If clone does not exist yet, run:
mkdir -p ~/VCOS-Coordination && cd ~/VCOS-Coordination && git clone https://github.com/WEB3X100/vcos-hq.git vcos-hq

Report blockers in state.json pending_decisions_for_umair.