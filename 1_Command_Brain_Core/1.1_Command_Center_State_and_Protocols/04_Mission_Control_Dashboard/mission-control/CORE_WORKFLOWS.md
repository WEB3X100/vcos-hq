# VCOS Core Workflows (Solidified)

**Status:** Operator authority — use this before inventing new loops  
**Date:** 2026-07-11  
**Push gate:** Do **not** treat this as published to `origin` until Umair says **PUSH**  
**Related:** `COFOUNDER-CASTLE-OS-PRD.md` · `local-dashboard/` · dual-laptop plan · `active-context.md`

---

## 0. One rule above all

**One tonight chunk. One primary machine. One ship path. Human gates for external reality.**

If work does not produce a file path, a ClickUp next action, or an explicit approval item, it is not a core workflow — it is chat.

---

## 1. System map (who does what)

| Surface | Owns | Does not own |
| --- | --- | --- |
| **You (Sentinel)** | Priorities, approvals, publish, spend, client talk, push/merge | Doing every draft yourself |
| **L1 Mac + Castle** | Cockpit, OS state, Grok Build / Claude / Codex, HQ git | Always-on when Mac is closed |
| **L2 Windows + Hermes + Telegram** | Always-on co-founder drafts, research, handoffs on disk | Auto-publish, QBO write, fake “sent” |
| **ClickUp** | Execution truth (tasks, owners, due) | Long file storage |
| **GitHub `vcos-hq`** | Cross-laptop coordination bus | Secrets (`.hermes/`) |
| **Obsidian / HQ Markdown** | Durable decisions & protocols | Live task board |
| **Castle outbox** | L2 mission text queued locally | Delivery to Telegram/Hermes |

### Runtimes (pick one primary per mission)

| Runtime | Use for | Stop if |
| --- | --- | --- |
| **Hermes L2 (Telegram)** | Drafts, research, packs, checklists while L1 off | Needs IDE mega-refactor |
| **Grok Build (L1)** | Castle/code, bounded multi-file | Needs adversarial review only |
| **Claude Code (L1)** | Large refactors | Ownership conflicts with another editor |
| **Codex (L1)** | Review / challenge | Daily drafting |

---

## 2. Daily operating loop (default)

### 2.1 Open (5–10 min)

1. **L1:** Start Castle → `python3 server.py` → http://127.0.0.1:8765/  
2. Land **Chat Hall** (default).  
3. **Phone/Telegram:** `PING` L2 → expect `pong | host | time | model | handoffs y/n`  
4. **Command room:** confirm or set tonight:

```text
/tonight <lane> | <one task> | <done means with path>
```

5. **ClickUp:** AgentOSync view first — extract blockers/approvals only (no broad search).

### 2.2 Ship block (45–90 min) — pick **one** lane

| Priority | Lane | Castle room | Default ship path pattern |
| --- | --- | --- | --- |
| P1 | AMAX / QB truth | AMAX Tower | L2 `cofounder-handoffs/02_amax_drafts/…` or AMAX workspace specs |
| P2a | Content Intel / AgentOSync | Content Studio | `01_content_drafts/…` or content-intel-routine |
| P2b | Safar-E-Madina (Phase 1 only) | Safar Gate | `01_content_drafts/safar-e-madina/…` |
| P3 | FDE / career | FDE | evidence packs only, public-safe |
| — | Ops / sync | L2 Wing | git pull, handoff verify |

**Dispatch pattern (no bridge):**

1. Castle → lane room → **Copy mission packet** (label: *Copied — for manual handoff to L2. Not sent.*)  
2. Paste into **L2 chat pane** → Queue locally → **Copy outbox** → paste **Telegram**.  
3. L2 returns Handoff Packet + file path.  
4. Castle: `/ship add <lane> | <title> | <path>` then readiness `DRAFT → REVIEW → READY` only when human is ready to review.

### 2.3 Close (10 min)

1. Update ship readiness / approvals queue.  
2. Optional: `/note <one learning>`.  
3. ClickUp: one status line if a task moved.  
4. If L2 produced files under `cofounder-handoffs/`, leave untracked until commit policy says otherwise (never force-reset over them).

---

## 3. Core workflows (solidified)

### WF-01 — Dual-laptop heartbeat

| Step | Who | Action |
| --- | --- | --- |
| 1 | Umair | `PING` on Telegram |
| 2 | L2 | Reply pong format |
| 3 | Umair | If fail: check gateway/power; do **not** invent status in Castle |
| 4 | Umair | Optional: `/l2 status <observed>` + `/l2 model <observed>` (human-observed only) |

**Done means:** Honest L2 status known.  
**Forbidden:** Auto-marking L2 healthy without PING.

---

### WF-02 — Git sync L2 to origin (no hard reset)

| Step | Action |
| --- | --- |
| 1 | `git status --porcelain` — report untracked |
| 2 | **Keep** `.hermes/`, local `cofounder-handoffs/`, other untracked |
| 3 | `git fetch origin --prune` (retry if timeout; never invent files) |
| 4 | `git checkout main` && `git pull --ff-only origin main` |
| 5 | If ff-only fails → **STOP**, report; do not reset |
| 6 | Verify expected handoff file exists |

**Done means:** HEAD near `origin/main` + required file present **or** network-fail report.  
**Forbidden:** `git reset --hard`, `git push`, delete `.hermes/`.

**Content-intel file (when on main):**  
`cofounder-handoffs/04_briefs/l1-content-intel-2026-07-11.md`  
Mirror: `…/session-briefs/handoffs/l1-content-intel-2026-07-11.md`

---

### WF-03 — Mission dispatch (L1 → L2)

**Mission packet minimum fields:**

```text
MISSION: <outcome>
LANE: AMAX | Content | Safar | FDE | Ops | Build
DONE MEANS: <path or objective>
PRIMARY RUNTIME: hermes_l2 | grok_build | claude | codex
CONTEXT PATHS: ≤5
ALLOWED: …
FORBIDDEN: publish, QBO write, CRM write, spend, reset --hard, push
STOP: <condition>
HARD CAP: <time or turns>
APPROVAL REQUIRED: none | human sign-off before external use
```

**Done means:** L2 Handoff Packet with path + READINESS line.  
**Handoff mechanism:** Castle outbox → human Telegram only (until Phase 3 bridge approved).

---

### WF-04 — Ship definition (all lanes)

A ship is **only**:

1. File path on disk (or explicit “N/A — decision only”)  
2. Readiness: `DRAFT` → `REVIEW` → `READY` (no skip)  
3. Approval field: `none` | `human`  
4. READY blocked if approval is `none`  
5. READY still means **human sign-off before any external use**

Castle: `/ship add` · `/ship update` · `/ship remove`

---

### WF-05 — Approval gate

| External action | Phrase pattern | Agent may |
| --- | --- | --- |
| LinkedIn publish | `APPROVED LINKEDIN + #` | Draft only |
| Client send | `APPROVED: channel + target` | Draft only |
| QBO mutate | Explicit accountant/Umair | Never |
| Ads spend | `UNLOCK PHASE 2 ADS` + budget | Never until unlocked |
| Git push to origin | Umair says **PUSH** | Prepare branch; no push alone |

Castle: queue items + **Copy phrase** = clipboard only.  
`/approval clear` = local display cleanup **only**.

---

### WF-06 — AMAX (P1 client delivery)

| Element | Spec |
| --- | --- |
| Goal | July-close-forward operating truth; CEO dashboard drafts |
| Inputs | COA assets, offline sheets, specs under AMAX workspace |
| L2 work | Reclass checklists, exception queues, draft narratives |
| Forbidden | QBO write, invent balances as fact, client email as Maaz |
| Ship path | `cofounder-handoffs/02_amax_drafts/` or AMAX `specs/` |
| Gate | AMAX/human before any books-of-record claim |

---

### WF-07 — Content Intel / AgentOSync (P2a)

| Element | Spec |
| --- | --- |
| Goal | Launch series drafts + Loom blueprint; public-safe proof |
| Inputs | `agentosync-os-launch-series` seed, voice calibration |
| L2 work | LinkedIn packs, hooks, claims tables with labels |
| Forbidden | Auto-publish, fake metrics, Amax private numbers |
| Ship path | `01_content_drafts/` or content-intel-routine |
| Gate | `APPROVED LINKEDIN + draft number` |

**Keep separate from Safar-E-Madina brand** unless dual-brand explicitly requested.

---

### WF-08 — Safar-E-Madina Phase 1 (P2b market)

| Element | Spec |
| --- | --- |
| Live | https://safar-e-madina.replit.app/ |
| Repo | https://github.com/WEB3X100/Safar-E-Medina |
| Positioning | Planning desk; Amax fulfills travel |
| Phase 1 | Content + funnel + qualify script drafts |
| Blocker | WhatsApp number not configured — no paid ads |
| Phase 2 | Meta/Google only after `UNLOCK PHASE 2 ADS` |
| Ship path | `cofounder-handoffs/01_content_drafts/safar-e-madina/` |

---

### WF-09 — Castle OS operator (L1)

| When | Action |
| --- | --- |
| Start day | Castle up, PING L2, `/tonight` |
| Dispatch | Mission packet → L2 outbox → Telegram |
| After L2 returns | `/ship add` + optional `/lane set` |
| End day | Approvals review, optional `/note` |
| Code change | Grok Build / Claude against PRD; `test-phase1.sh` if UI touched |

**Slash quick list:** `/help` `/tonight` `/lane set` `/ship add|update|remove` `/approval add|clear` `/l2 status|model` `/jarvis set` `/vault set path|home` `/park add` `/priority`

---

### WF-10 — Push / publish code (gated)

| Step | Owner |
| --- | --- |
| 1. Working tree intentional; no secrets (`.hermes/`, keys) | L1 |
| 2. Castle commits present; tests green if dashboard changed | L1 |
| 3. Prefer branch `castle/p2-2026-07-11` or similar if history diverged | L1 |
| 4. Umair says **PUSH** | Human |
| 5. Push branch or main per instruction; open PR if needed | L1 agent |
| 6. L2 `pull --ff-only` after push lands | L2 |

**Until PUSH:** Castle + core workflows exist on L1 worktree only.

---

## 4. What is *not* a core workflow (parked / later)

- Dealership Sameer/Uzair commercial follow-up  
- Barbershop / restaurants reactivation  
- L2 Telegram auto-bridge (Castle Phase 3)  
- MCP agentmail / agent-cards / spend  
- ClickUp restructure (Airtable snapshot gate)  
- Live trading / broker write  
- Parallel 7-agent swarms without file ownership  

---

## 5. Handoff Packet template (mandatory agent output)

```markdown
## Handoff Packet
- Mission:
- Machine / runtime:
- What I did:
- Artifacts (paths):
- Decisions needed from Umair:
- Approval required (y/n + what):
- Next action:
- READINESS: n/11 | Approval: … | Next: …
```

---

## 6. Weekly solidify check (Sunday, 15 min)

1. Did each active day have **one** `/tonight` and **≥1** ship path?  
2. Any false “sent/connected” language in Castle or L2? → fix as truthfulness bug  
3. L2 on `origin/main` within 1 day of L1 pushes?  
4. Safar WhatsApp still blocked? → no ads  
5. Promote any 3× repeated mission to Skill Foundry candidate  

---

## 7. Push readiness checklist (before you say PUSH)

- [ ] This `CORE_WORKFLOWS.md` reviewed by Umair  
- [ ] Castle `test-phase1.sh` green on L1  
- [ ] No secrets in commit set (especially `.hermes/`, API keys, outbox with tokens)  
- [ ] Branch strategy chosen (branch+PR vs main) given L1/origin divergence  
- [ ] L2 instructed: pull after push; keep untracked `.hermes/`  
- [ ] Explicit Umair message: **PUSH** + target branch  

---

## 8. Pointer index

| Need | Open |
| --- | --- |
| Castle PRD | `COFOUNDER-CASTLE-OS-PRD.md` |
| Castle run | `local-dashboard/README.md` |
| Dual-laptop plan | `…/dual-laptop-hermes/plan.md` |
| L2 setup prompts | `…/dual-laptop-hermes/cofounder-laptop-setup-prompts.md` |
| Safar brief | `…/dual-laptop-hermes/safar-e-madina-cofounder-brief.md` |
| Live priorities | `1.2_Headquarters_Memory/active-context.md` |
| Fast path | `AGENTS.md` → ubiquitous language → state → active-context → key-workspaces |

---

`SOLIDIFY STATUS: core workflows locked for operator use | Push: waiting on Umair PUSH + checklist §7 | Next: daily run WF-01→WF-03 on one lane only`
