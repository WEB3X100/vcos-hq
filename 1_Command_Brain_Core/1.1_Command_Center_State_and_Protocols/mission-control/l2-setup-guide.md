# Laptop 2 Setup Guide — NeuralSync Intern

**Time:** ~45–60 min  
**Outcome:** L2 pulls VCOS HQ, runs first handoff-sync mission, posts to Telegram

**Path constants** (Hermes `--workdir` = repo root):

- `MC=` `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/mission-control`
- `HANDOFFS=` `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/session-briefs/handoffs`

## Prerequisites

- [ ] GitHub access to VCOS HQ repo
- [ ] Hermes installed on Laptop 2 (`hermes setup && hermes doctor`)
- [ ] xAI OAuth logged in (`hermes model` → Grok)
- [ ] Telegram bot token (Hermes gateway)

## Step 1 — Install Hermes (Laptop 2)

```bash
hermes setup
hermes doctor
hermes model   # pick xAI Grok OAuth
```

## Step 2 — Create intern profile

```bash
hermes profile create neuralsync-intern-builder --description "24/7 VCOS HQ builder — feature branches only, Telegram channel"
```

Paste soul seed from `MC/hermes/l2-soul-seed.md` as first message. Confirm branch rules.

## Step 3 — Activate Telegram

```bash
hermes gateway   # follow Telegram bot setup
```

L2 posts handoffs here. L1 stays on WhatsApp.

## Step 4 — Clone VCOS HQ

```bash
mkdir -p ~/VCOS-Coordination
cd ~/VCOS-Coordination
git clone https://github.com/WEB3X100/vcos-hq.git vcos-hq
cd vcos-hq
git pull origin main
```

Workdir for all L2 missions: `~/VCOS-Coordination/vcos-hq`

## Step 5 — First mission (handoff sync)

```bash
git checkout -b l2/handoff-sync-2026-06-20
```

1. Verify `MC/` and `HANDOFFS/` exist
2. Read `MC/state.json` + `MC/git-coordination-sop.md`
3. Write `HANDOFFS/l2-vcos-hq-sync-2026-06-20.md`
4. Update `MC/state.json` cubicle_l2 fields
5. Commit, push, open draft PR (do not merge)
6. Post Telegram summary with branch + decisions needed

## Step 6 — Idle behavior

When `MC/state.json` shows no active mission:

- Poll `MC/state.json` every 30 min OR wait for Telegram mission from L1
- Report idle — do not invent greenfield work
- Parking lot items are off-limits

## Verification checklist

- [ ] `hermes profile list` shows `neuralsync-intern-builder`
- [ ] Telegram bot responds to ping
- [ ] Branch `l2/handoff-sync-*` pushed to GitHub
- [ ] Handoff packet exists in `HANDOFFS/`
- [ ] `MC/state.json` cubicle_l2.status = `active`