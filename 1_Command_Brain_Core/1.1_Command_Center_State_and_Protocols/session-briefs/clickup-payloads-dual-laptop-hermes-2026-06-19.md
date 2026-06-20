# ClickUp Payloads — Dual-Laptop Hermes Activation

**Hermes agent list:** https://app.clickup.com/9017760195/v/li/901713786845  
**AgentOSync view:** https://app.clickup.com/9017760195/v/s/90175689274  
**Source:** Interactive OH 2026-06-19 — `interactive-office-hours-dual-laptop-hermes-2026-06-19.md`

Paste tasks into list `901713786845`. All external sends remain Draft-Only until approved.

---

## Master Task

**Title:**  
[HQ] Dual-Laptop Hermes — Week 1 Mission Control + Coordination Flywheel

**Description:**

Week 1 goal: organize existing Hermes/L2 work into a visible two-cubicle Mission Control dashboard. Laptop 1 (WhatsApp) = Chief of Staff. Laptop 2 (Telegram) = 24/7 intern. Coordination bus = GitHub branches/PRs.

**Done means:**
- 7pm brief cron delivers locked template 7/7 nights (avg ≥3.5)
- Mission Control shows L1 + L2 state and pending decisions
- L2 completes first VCOS HQ sync mission with handoff packet
- Telegram bot active on L2; WhatsApp confirmed on L1

**Canonical docs:**
- `session-briefs/dual-laptop-hermes/plan.md` (Approved)
- `session-briefs/interactive-office-hours-dual-laptop-hermes-2026-06-19.md`
- `session-briefs/README.md`

**Tags:** `hermes`, `dual-laptop`, `week-1`

---

## Subtask 1 — 48h Proof: Manual 7pm Brief

**Title:**  
[HQ] Run manual 7pm brief + score (target ≥3.5)

**Description:**

Use locked template in `interactive-office-hours-dual-laptop-hermes-2026-06-19.md`.

Inputs: ClickUp tasks assigned to Umair + `weekly-office-hours-plan-2026-06-15-draft.md` + latest L2 git activity if available.

Score: accuracy, actionability, brevity (1–5 each). Log in this task comment.

**Due:** Tonight  
**Done means:** Overall avg ≥3.5 OR documented fix list for prompt.

---

## Subtask 2 — Laptop 1: Hermes Chief of Staff

**Title:**  
[L1] Hermes Desktop + VCOS-Brain-Grok seed + WhatsApp template

**Description:**

1. `hermes doctor`
2. Seed from `hermes-vcos-first-seed-brief-2026-06-13.md`
3. Confirm WhatsApp delivers compressed brief template only (Phase 1)
4. Folder allowlist per OH decisions

**Done means:** Agent restates ClickUp rule + P0 lanes; one WhatsApp test message reviewed by Umair.

---

## Subtask 3 — Laptop 2: Hermes Intern + Telegram

**Title:**  
[L2] Provision NeuralSync Intern + Telegram bot

**Description:**

1. Dedicated identity + GitHub branch push access (no main merge)
2. Seed `NeuralSync-Intern-Builder` profile
3. Activate Telegram bot for remote workflow triggers
4. Document bot commands in handoff packet

**Done means:** Telegram receives test status ping from L2; `hermes doctor` clean.

---

## Subtask 4 — Mission Control Dashboard (Week 1 Artifact)

**Title:**  
[HQ] Build dual-cubicle Mission Control (L1 + L2 visibility)

**Description:**

Create `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/mission-control/`:

- `state.json` — L1 cubicle, L2 cubicle, pending decisions, active branches
- `README.md` — how agents update state via handoff packets
- Optional: simple local HTML or ToolJet stub (evaluate later)

**Done means:** Umair can open one surface and see what each laptop is doing + what decision is needed.

---

## Subtask 5 — 7pm Brief Cron

**Title:**  
[L1] Schedule 7pm America/Toronto brief cron

**Description:**

Reverse-prompt in VCOS-Brain-Grok using locked template. Confirm in Desktop cron list.

**Done means:** Cron fires 7/7; brief includes L2 git summary + Dealership 3 + AMAX 3 + 90-min chunk.

---

## Subtask 6 — Dream Cycle Lite (Before Sleep)

**Title:**  
[L1] Dream Cycle lite cron (variable, before sleep)

**Description:**

Three fields only: brief score, one prompt fix, one prevention rule. Draft soul.md/skills updates — human approves promotion.

**Done means:** 5 consecutive nights logged in `session-briefs/dream-cycles/`.

---

## Subtask 7 — L2 First Mission: VCOS HQ Sync

**Title:**  
[L2] First mission — VCOS HQ handoff sync (intern-ready)

**Description:**

Spec: Nightly (or on-demand) pull HQ repo, update handoff packets under `session-briefs/handoffs/`, push feature branch, draft ClickUp comment with summary.

Test contract: branch push succeeds; handoff packet complete; no main merge.

**Done means:** Umair reviews PR without authoring code.

---

## Subtask 8 — GitHub Coordination SOP

**Title:**  
[HQ] Document L1 ↔ L2 Git coordination rules

**Description:**

Write short SOP in `mission-control/git-coordination-sop.md`:

- L2 pushes feature branches only
- L1 pulls + reviews + merges
- Handoff packet required every mission
- Conflict resolution = human

**Done means:** Both agents seeded with SOP pointer.

---

## Subtask 9 — Friday Arsenal Test

**Title:**  
[HQ] CodeBurn 30-min test + update arsenal-index

**Due:** Friday Week 1  
**Done means:** Token visibility working; `arsenal-index.md` status updated.

---

## Subtask 10 — Sunday Scorecard

**Title:**  
[HQ] Week 1 scorecard + OH recap

**Description:**

Record: brief __/7, avg __/5, Mission Control live Y/N, L2 mission complete Y/N, Telegram Y/N.

Update `plan.md` or new `weekly-office-hours-plan-YYYY-MM-DD.md`.

**Due:** Sunday end of Week 1

---

## Suggested List Comment (after paste)

```text
Dual-Laptop Hermes activation tasks pasted from interactive OH 2026-06-19.
Week 1 = Mission Control + dual Hermes coordination (WhatsApp L1, Telegram L2).
Master plan: session-briefs/dual-laptop-hermes/plan.md (Approved).
Start: Subtask 1 tonight (manual 7pm brief).
```