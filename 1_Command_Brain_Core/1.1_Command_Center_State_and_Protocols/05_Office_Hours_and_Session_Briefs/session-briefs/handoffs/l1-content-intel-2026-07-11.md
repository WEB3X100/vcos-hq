# Loop A Spec — AgentOSync Content Intel Day-2 Pack

**Mission ID:** `content-intel-day2-2026-07-12`  
**Assigned by:** Grok (L1 / Cursor) + Umair  
**Assigned to:** L2 `neuralsync-intern-builder`  
**Date:** 2026-07-11  
**Status:** `queued` — awaiting L2 pickup  
**Phase gate:** Draft-only. No publish, no external send, no CRM mutation.

---

## Mission summary

Build **Day-2** of the AgentOSync Content Intel launch series. Day-1 covered Hermes production configs (operator reliability). Day-2 covers **dual-agent operating loops** — how a human + L1 strategist (Grok) + L2 builder (Hermes) run long goals without context rot.

This mission proves the Grok↔L2 handoff contract end-to-end.

---

## Branch

```text
l2/content-intel-day2-2026-07-12
```

Create from latest `main`. Never merge to `main` without explicit `APPROVED` from Umair.

---

## Allowed files (write)

| Path | Purpose |
| --- | --- |
| `01_content_drafts/**` | Draft posts (create folder if missing) |
| `cofounder-handoffs/04_briefs/l2-content-intel-day2-2026-07-12.md` | L2 handoff packet |
| `cofounder-handoffs/04_briefs/` | Brief updates only if correcting metadata |

## Read-only (do not modify)

| Path | Purpose |
| --- | --- |
| `04_Reusable_Systems_and_Skills/content-intel-routine/CLAUDE.md` | Routine rules |
| `04_Reusable_Systems_and_Skills/content-intel-routine/voice-calibration/tone-rules.md` | Voice guardrails |
| `04_Reusable_Systems_and_Skills/content-intel-routine/voice-calibration/rejected-patterns.md` | Anti-slop |
| `04_Reusable_Systems_and_Skills/content-intel-routine/inbox/starter_packet/2026-06-22-post-1.md` | Day-1 thesis reference |
| `01_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/04_Mission_Control_Dashboard/mission-control/dual-hermes-collaboration-protocol.md` | Loop architecture source |
| `cofounder-handoffs/04_briefs/l1-content-intel-2026-07-11.md` | This spec |

## Forbidden

- Publish to LinkedIn, X, Instagram, or any public channel
- Send Telegram/email/SMS to clients or prospects
- Merge to `main`, deploy, spend money, mutate ClickUp/CRM/QBO
- Invent client results or live deployment claims
- Broad repo refactors outside allowed paths

---

## Series context

| Day | Thesis | Status |
| --- | --- | --- |
| Day-1 | Hermes production configs = toy demo vs daily operator | Starter packet exists (`2026-06-22-post-1.md`) |
| **Day-2** | **Two agents in a loop beat one agent with infinite context** | **This mission** |
| Day-3 (future) | Employee 01 Front Desk wedge — missed-call → booked test drive | Not in scope |

---

## Five post hooks (L2 must develop 3–5 into full drafts)

Use these as starting angles. Pick the strongest 3–5; each needs LinkedIn + X + IG variants.

### Hook 1 — The loop beats the monolith
> One AI with perfect memory is a myth. Two specialized agents sharing files in git — that's how you actually ship long goals.

### Hook 2 — Strategist + builder split
> L1 writes the spec while you sleep. L2 builds on a feature branch while you work. You approve the merge. That's an AI-native company operating system, not a chatbot.

### Hook 3 — Context rot is a cost center
> Every time you re-explain your business to an AI, you pay twice: tokens and quality. Persistent agents with bounded missions don't forget — they hand off.

### Hook 4 — Draft-only is a feature
> The best agent teams don't auto-post. They produce approval-gated artifacts on disk. Speed without guardrails is just faster mistakes.

### Hook 5 — Proof before platform
> We're not selling "AI transformation." We're running dual-Hermes loops on real VCOS delivery lanes (dealership, finance ops, content) and showing the artifacts.

---

## Draft deliverables

Create `01_content_drafts/content-intel-day2-2026-07-12.md` containing:

### Per draft (minimum 3, target 5)

For each selected hook:

1. **Working title**
2. **Platform variants:**
   - LinkedIn post (150–250 words, operator tone)
   - X single (≤280 chars)
   - X thread outline (3–5 tweets, bullets OK)
   - Instagram caption (≤150 words + carousel angle if applicable)
3. **Proof level tag:** `opinion` | `internal-wip` | `demo` — no `client-result` without approval
4. **CTA:** soft — follow, DM, or "building in public" only; no hard sell
5. **Skeptic check** (3 bullets): claim safety, voice fit, approval needed?

### Source summary (required)

Short section at top of draft file:

- What signal/theme Day-2 addresses
- Why it follows Day-1 without repeating
- What changed in AI-native ops discourse (web research allowed, 2–3 sources max)
- What is noise — skip it

---

## Voice rules (mandatory)

From `tone-rules.md` temporary guardrails until Umair calibrates:

- Direct, operational, proof-first
- No vague hype ("game changer", "revolutionary", "10x everything")
- Label demos and WIP as such
- Tie back to operator/SMB impact when true
- Reference dual-Hermes / Grok↔L2 loop as **internal WIP** — not a shipped product claim

---

## Acceptance criteria

| # | Criterion | Verify |
| --- | --- | --- |
| 1 | Branch `l2/content-intel-day2-2026-07-12` exists on remote | `git branch -r` |
| 2 | `01_content_drafts/content-intel-day2-2026-07-12.md` exists | file on disk |
| 3 | 3–5 complete draft sets (LinkedIn + X + IG each) | count in file |
| 4 | Source summary present | section in file |
| 5 | Skeptic check on every draft | section per draft |
| 6 | No forbidden actions taken | self-attest in handoff |
| 7 | Handoff packet complete | `l2-content-intel-day2-2026-07-12.md` |
| 8 | `state.json` cubicle_l2 updated | fields below |
| 9 | Branch pushed to GitHub | remote exists |

---

## Definition of done

```text
DONE MEANS:
- Artifact: 01_content_drafts/content-intel-day2-2026-07-12.md (3–5 draft sets)
- Handoff: cofounder-handoffs/04_briefs/l2-content-intel-day2-2026-07-12.md
- Branch: l2/content-intel-day2-2026-07-12 pushed to origin
- READINESS: DRAFT_REVIEW — Umair approval required before any publish
```

---

## L2 handoff packet template

L2 must write `cofounder-handoffs/04_briefs/l2-content-intel-day2-2026-07-12.md` with:

```markdown
# L2 Handoff — content-intel-day2-2026-07-12

## Build summary
- Branch:
- Commit:
- Files touched:

## Drafts delivered
- Count:
- Recommended draft for approval (if any):
- Why:

## Blockers
- (none | list)

## Decisions needed from Umair
- (list)

## READINESS
DRAFT_REVIEW — 3–5 Day-2 drafts ready for voice/claim review. No publish authority.
```

---

## state.json updates (L2)

Update `01_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/04_Mission_Control_Dashboard/mission-control/state.json`:

```json
"cubicle_l2": {
  "status": "active" | "idle" | "blocked",
  "active_mission": "content-intel-day2-2026-07-12",
  "active_branch": "l2/content-intel-day2-2026-07-12",
  "last_session": "<timestamp + one-line summary>",
  "last_push": "<commit hash or null>",
  "pending_decisions_for_umair": ["<decisions>"]
}
```

---

## Telegram summary format (on completion)

```text
SHIP — content-intel-day2-2026-07-12
Branch: l2/content-intel-day2-2026-07-12
Drafts: 01_content_drafts/content-intel-day2-2026-07-12.md
Handoff: cofounder-handoffs/04_briefs/l2-content-intel-day2-2026-07-12.md
READINESS: DRAFT_REVIEW
Decisions: <one line>
Blockers: <none | one line>
```

---

## Loop C gate (Umair)

Before next cycle (Day-3):

1. Review drafts in `01_content_drafts/content-intel-day2-2026-07-12.md`
2. Reply `APPROVED` | `REVISE: <notes>` | `REJECT: <reason>` in Telegram or this thread
3. If approved: optionally merge branch; Grok writes Loop A for Day-3
4. Log approved/rejected drafts into `voice-calibration/` per content-intel routine

---

## Failure modes

| Condition | L2 action |
| --- | --- |
| Queue empty / spec unclear | Write BLOCKER handoff; Telegram `BLOCKER`; do not invent work |
| Git auth fails | BLOCKER with exact error; stop |
| Voice files missing | Use temporary guardrails; note in handoff |
| Research sources dry | Use hooks + dual-hermes protocol as primary source; note gap |

---

**End of Loop A spec. L2: confirm pickup with `MISSION content-intel-day2-2026-07-12` on Telegram.**