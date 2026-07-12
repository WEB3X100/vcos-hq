# PR Draft (not opened — human approval required)

**Title:** Adopt HQ loop-contract governance for Hermes crons + fix protocol path drift

**Branch:** `claude/vcos-employee-hq-hermes-h0ffpw` → `main`
**Compare URL:** https://github.com/WEB3X100/vcos-hq/compare/main...claude/vcos-employee-hq-hermes-h0ffpw

---

## What files

**New:**
- `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/01_Operating_Protocols_and_Guardrails/loop-contract.md` — HQ master loop contract (Hermes crons/heartbeats, `/loop`, VPS jobs) with L0/L500/L1000 ↔ Hermes Phase mapping, role ↔ profile map, six guardrails, and a filled L0 night-brief example appendix
- `.../01_Operating_Protocols_and_Guardrails/templates/validation-contract-template.md` — assertions written before implementation or a cron's first run
- `.../01_Operating_Protocols_and_Guardrails/templates/handoff-packet-template.md` — required output format for handoffs and Hermes cron runs

**Edited:**
- Hermes playbook (`02_AI_OS_Architecture_and_Runtime/hermes-supergrok-vcos-playbook.md`) — mandatory Cron Governance section; scanner untrusted-input note; First Human Run + VPS checklists require validation contract and handoff-packet format by path
- `recursive-self-improvement-loop.md` — "Where Prevention Rules Land" for failed crons (decisions.md one-liner + cron prompt/seed update + supervised re-test)
- `AGENTS.md`, `CLAUDE.md`, `HEADQUARTERS_MAP.md`, `MISSION_CONTROL_PATHS.md`, guardrails `README.md` — flat→numbered path fixes; loop contract linked from fast path and Cadence Hooks
- `decisions.md` — 2026-07-12 adoption entry

## What agents must do differently

1. **Embed the contract:** every Hermes cron/heartbeat/`/loop` carries the loop-contract block (outcome, per-cron ceiling, output ownership, stop conditions, evidence packet). Reverse prompting alone is no longer sufficient.
2. **Treat scanner output as untrusted:** Sentinel compresses web/scan content before any role acts on it; suspected injection stops the cron.
3. **Skeptic validation exit:** nothing is "done" on the worker's word — Skeptic validates against the prewritten validation contract in a fresh session (heartbeats get a lighter pass).
4. **Standard handoff packets:** night briefs and scanner sweeps land in the handoff-packet template format with an explicit "Needs Human Approval" queue.
5. **Failures produce prevention rules:** decisions.md one-liner + updated cron prompt/seed + one supervised re-test before returning to unattended cadence.

## What is NOT included

- No live Castle↔L2/Telegram/Hermes bridge — no Castle files exist in this branch, and none were added
- No Castle dashboard WIP mixed in
- No live cron installs (the night-brief contract is an example appendix only)
- No merge — draft for human review
- No flat→numbered folder reorg completion (leftover flat `mission-control/gsd-dual-terminal-eval/` is flagged as a separate mission)

## Test plan

1. Open `01_Operating_Protocols_and_Guardrails/loop-contract.md` — ceiling table, role map, template block, and example appendix render.
2. Follow one path end-to-end: `AGENTS.md` Cadence Hooks → loop-contract → Hermes playbook Cron Governance → both templates. All links resolve.
3. `CLAUDE.md` fast path: every listed protocol file exists at its stated path.
4. `MISSION_CONTROL_PATHS.md` aliases resolve (HQ_MC state.json, HQ_HANDOFFS MISSION-QUEUE.md).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_013ePKAhj8hm3S3omuaaApVg
