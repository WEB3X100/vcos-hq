# Mission Control — Path Constants (L1 + L2)

**Repo root:** `vcos-hq` clone (e.g. `~/VCOS-Coordination/vcos-hq` or `C:\Users\...\VCOS-Coordination\vcos-hq`)

Mission Control is **not** at repo root. Use these paths:

| Alias | Full path from repo root |
| --- | --- |
| `HQ_MC` | `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/04_Mission_Control_Dashboard/mission-control/` |
| `HQ_SB` | `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/05_Office_Hours_and_Session_Briefs/session-briefs/` |
| `HQ_HANDOFFS` | `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/05_Office_Hours_and_Session_Briefs/session-briefs/handoffs/` |

(A leftover flat `1.1_Command_Center_State_and_Protocols/mission-control/` folder still holds `gsd-dual-terminal-eval/` only — pending the flat→numbered reorg completion. The numbered paths above are canonical.)

**Key files:**

- State: `HQ_MC/state.json`
- Mission queue: `HQ_HANDOFFS/MISSION-QUEUE.md`
- Git SOP: `HQ_MC/git-coordination-sop.md`
- Collaboration protocol: `HQ_MC/dual-hermes-collaboration-protocol.md`
- L1 mission: `HQ_HANDOFFS/l1-week1-git-collab-test-2026-06-20.md`
- L2 response: `HQ_HANDOFFS/l2-collab-test-response-2026-06-20.md`

Hermes `--workdir` = repo root (not `mission-control/` subfolder).