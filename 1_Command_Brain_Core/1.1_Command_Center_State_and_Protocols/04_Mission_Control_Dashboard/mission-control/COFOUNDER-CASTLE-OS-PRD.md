# PRD: VCOS Co-Founder Castle OS (Mission Control) — Swarm-Safe Build Authority

**Document ID:** `VCOS-MC-CASTLE-003`
**Version:** 1.3
**Date:** 2026-07-11
**Status:** Draft-Only — pending Sentinel (Umair) approval before Builder handoff
**Owner:** Umair (Sentinel / human CEO)
**Local baseline:** `http://127.0.0.1:8765/`
**Supersedes:** `VCOS-MC-CASTLE-002` v1.2 (all sections carried forward; changes marked ★)
**Battle-test companion:** `COFOUNDER-CASTLE-OS-BATTLE-TEST-2026-07-11.md`
**Execution runtime target:** Grok Build CLI (plan mode → wave execution), single machine, single repo

---

## 0. What changed in v1.3 ★

| Change | Reason |
| --- | --- |
| Added §15 Agent Execution Contract (waves, file ownership, commit rules, machine-checkable safety gates) | v1.2 was human-builder-safe but swarm-unsafe: parallel agents had no ownership map and no automated forbidden-pattern scan. |
| Resolved Open Decision #3: `/approval done` renamed to `/approval clear` | "done" carries approval semantics an agent will eventually misread. `clear` states the true effect: local display cleanup only. |
| P1-06, P1-14, and the state-schema check are now scripted deliverables (`test-phase1.sh`) | Converts prose safety rules into automated pass/fail gates the Skeptic lane must run. |
| Added §16 Grok Build mission constraints (scope lock, stop conditions, reframing rule) | The execution prompt and the PRD must state identical boundaries so neither can be cited against the other. |
| Acceptance suite extended: P1-16 (safety scan) and P1-17 (scripted test suite) | Done now means 17/17, all machine- or evidence-verified. |

---

## 1. Executive decision

Build **one local, truthful operator cockpit** for L1. It must make L1/L2 identity, tonight's work, draft dispatches, artifact paths, and approval gates immediately clear.

The product is **not** a remote-control dashboard, CRM, ClickUp replacement, deployment tool, or autonomous agent. L2/Hermes remains an explicitly manual, outbox-first handoff until a separately approved bridge phase (Phase 3).

### Build scope

| Included now | Explicitly excluded now |
| --- | --- |
| Fixed Castle Map, Chat Hall default, Command strip, room shell, local state/chat/outbox, truthful L2 status, README, `test-phase1.sh` ★ | Telegram API, Hermes/MCP connection, webhooks, public bind, ClickUp/GitHub tokens, QBO/CRM writes, publishing, deploy controls, cross-device/Tailscale bridges |

### The one-paragraph mission (for any agent that reads nothing else) ★

Implement Phase 1 only. Done means: all acceptance tests P1-01 through P1-17 pass with recorded evidence, the safety scan is clean, and a Handoff Packet is produced. Server binds `127.0.0.1` only, runs with zero API keys, makes zero external network calls, and no UI copy implies external delivery. Any subtask that appears to require Phase 2+ capability is a stop signal, not a workaround opportunity.

---

## 2. Critique of v1.0 and corrections (carried from v1.2)

| Finding | Why it matters | Decision |
| --- | --- | --- |
| Baseline asserted but source directory/version not a precondition. | A builder can rebuild the wrong app or overwrite working behavior. | **Wave 0 requirement:** baseline inventory — source path, run command, screenshots, API routes, `state.json` shape, known failures. No refactor before it exists. |
| Phase 1 acceptance mixed shell work with Phase 2 depth. | Inflates scope; makes "done" subjective. | Phase 1 rooms are informational/read-only except Chat, Command, and local slash operations. CRUD depth is Phase 2. |
| "Send" / approval / L2 wording could imply external execution. | Unsafe operator expectation. | Every action carries an explicit effect label: `saved locally`, `queued locally`, `copied`, or `requires human action`. |
| `state.json` owned too much without per-field authority. | Risks a stale second HQ and unsafe mutation. | Castle state is a local cockpit mirror only. ClickUp remains execution truth. |
| Room priority and mobile behavior under-specified. | A builder can recreate the flat-tab failure. | Desktop: one fixed rail. Mobile: one labelled drawer. Chat Hall is the hard default. Blueprints visually demoted. |
| Acceptance tests lacked negative tests. | Happy path hides a fake Telegram/MCP connection. | Explicit truthfulness, localhost, no-key, no-outbound, and ★ automated forbidden-pattern tests. |

---

## 3. Product contract

### Job to be done

When Umair opens the local Castle, he can answer within seconds:

1. What is tonight's one chunk and its done-means?
2. Which machine/runtime is being addressed?
3. Is an L2 message only queued, or actually delivered?
4. What artifact path exists and what approval is still needed?

### Success metrics

| ID | Metric | Target |
| --- | --- | --- |
| S1 | Chat Hall discovery | Visible on hard refresh; no navigation click required |
| S2 | Machine clarity | Every chat action names L1/L2 and its actual effect |
| S3 | Truthful dispatch | L2 free text labeled `queued locally — not sent` |
| S4 | Ship definition | Every displayed ship has lane, path, readiness, approval |
| S5 | Safety | Zero UI paths publish, send externally, mutate QBO/CRM, spend, or bind publicly |
| S6 | Buildability | A fresh builder (human or agent) can pass every Phase 1 test from this document alone |
| S7 ★ | Swarm integrity | Zero cross-ownership file edits; zero forbidden patterns in final scan |

---

## 4. Source-of-truth and safety contract

| System | Owns | Castle treatment |
| --- | --- | --- |
| ClickUp | Tasks, owners, due dates, execution truth | Link/status mirror only |
| VCOS HQ Markdown / Obsidian | Durable decisions, protocols, briefs | Pointer links and fast-path list |
| GitHub | Code and cross-machine coordination | Outside Phase 1 UI |
| L2 handoff folder | Artifacts from Hermes/L2 | Displayed path only; no live read assumed |
| Castle local files | Local UI state, local chats, outbox drafts | Editable only within the local dashboard |

### Non-negotiable action labels

| User interaction | Allowed Phase 1 effect | Required UI confirmation |
| --- | --- | --- |
| L1 free text | Append local L1 chat; optional local acknowledgement | `Saved locally` |
| L2 free text | Append local L2 chat and Markdown outbox | `Queued locally — not sent to Hermes or Telegram` |
| OS slash command | Mutate local cockpit state only | `Updated local Castle state` |
| Copy approval phrase | Clipboard only | `Copied — human approval still required` |
| Any unknown integration | None | `Not connected` or `Set me` |

**Forbidden-word rule ★ (machine-enforced in P1-16):** No action label, button, toast, or status string may contain `sent`, `synced`, `approved`, `published`, `connected`, `delivered`, or `live` in an affirmative sense unless a verified implementation proves it. Honest-negative usage (`not sent`, `not connected`) is required and exempt.

---

## 5. Phase 1 information architecture

### Desktop shell

```text
┌───────────────────────────┬────────────────────────────────────────────┐
│ CASTLE MAP (fixed 232–256)│ Command strip: tonight lane · L2 status    │
│ single vertical room list │────────────────────────────────────────────│
│                           │ ACTIVE ROOM                                │
│ Chat Hall selected by     │ Full canvas; no equal-weight tab grid      │
│ default                   │                                            │
└───────────────────────────┴────────────────────────────────────────────┘
```

### Mobile shell

- Chat Hall remains the default route.
- One labelled room drawer; never a multi-row chip grid.
- Command strip visible or reachable as a compact summary.
- Preserve current room and scroll position on orientation change.

### Rooms

| ID | Room | Phase 1 behavior | Wave-2 ownership unit ★ |
| --- | --- | --- | --- |
| `chat` | Chat Hall | Full dual L1/L2 panes; local history and outbox-only queue | Agent A |
| `command` | Command | Tonight chunk, priorities, parked list; local slash-command help | Agent B |
| `l2_wing` | L2 Wing | Read-only model/profile/gateway/handoff facts; honest empty states | Agent C |
| `amax`, `content`, `safar`, `fde` | Lane rooms | Read-only next action, gate, and "copy mission" text only | Agent D |
| `ship` | Ship Dock | Read-only local ship table; Phase 2 owns richer CRUD | Agent E |
| `approvals` | Approval Gate | Show phrase and copy it; no approval executes work | Agent E |
| `obsidian` | Obsidian Vault | Vault path, Home note, fast-path pointers | Agent F |
| `jarvis` | Jarvis Bay | Read-only agents, gateway note, cron labels, `source` + `last checked` fields | Agent F |
| `cadence` | Cadence | Read-only draft-only loop policy | Agent G |
| `blueprints` | Blueprints | Sources and critique notes; visually secondary, never default | Agent G |

---

## 6. Chat Hall requirements

### Layout

- Two labelled panes occupy at least 50% of usable desktop viewport height.
- L1 uses accent-blue identity; L2 uses green. Both use text labels in addition to colour.
- Each pane shows: machine name, runtime/channel, current effect of its send button, message stream, compose field, keyboard instruction.
- `Ctrl/Cmd+Enter` submits the focused compose field. Standard Enter creates a new line.

### Slash command API (local-only) ★ updated

```text
/help
/tonight <lane> | <task> | <done means>
/ship add <lane> | <title> | <path>
/approval add <item> | <say phrase>
/approval clear <id>          ← renamed from /approval done
/l2 status <text>
/l2 model <text>
/park add <item>
/safar blocker <text>
/note <text>
/priority
```

Validation rules:

- Pipe-delimited commands reject missing segments and show the exact expected form.
- `/approval clear` removes an item from the **local display queue only**. Its confirmation text must state: `Cleared from local display — this does not perform the approval or any external action.`
- If a user types the legacy `/approval done`, respond with help pointing to `/approval clear`; make no state change. ★
- Unknown commands return local help and create no state change.
- Free text must work with no model/API key present.

---

## 7. Data contract

Local JSON only. Validate before write; preserve unknown fields to permit Phase 2 evolution.

```json
{
  "version": "semver-local",
  "updated_at": "ISO-8601",
  "data_freshness": "session-seeded|chat-updated",
  "north_star": "string",
  "active_priority_order": ["string"],
  "parked": ["string"],
  "tonight_chunk": {"lane": "string", "task": "string", "done_means": "string", "primary_tool": "string", "do_not_open": ["string"]},
  "l1": {"name": "string", "status": "string", "channel": "string"},
  "l2": {"name": "string", "status": "string", "profile": "string", "model": "string", "gateway": "string", "dashboard_localhost": false, "mcp_configured": false, "handoffs_root": "string"},
  "ships": [{"lane": "string", "title": "string", "path": "string", "readiness": "DRAFT|REVIEW|READY", "approval": "none|human"}],
  "approvals_queue": [{"id": "string", "item": "string", "say_phrase": "string"}],
  "lanes": {},
  "obsidian": {"vault_path": "string", "home_note": "string", "fast_path": ["string"]},
  "jarvis": {"agents": ["string"], "gateway_note": "string", "cron_jobs": ["string"], "source": "string", "last_checked": "ISO-8601"}
}
```

**Per-field authority ★:** fields under `l2`, `jarvis`, and `lanes` are display-mirror fields — editable only via slash commands that describe human-observed facts (`/l2 status`, `/l2 model`). No agent or background process may infer or auto-populate them. Unknown is rendered as unknown.

---

## 8. Local API and security

| Method | Route | Phase 1 purpose |
| --- | --- | --- |
| GET | `/api/health` | Local server health and optional-LLM flag |
| GET | `/api/state` | Read local cockpit state |
| GET | `/api/chat/l1` / `/api/chat/l2` | Read local chat history |
| POST | `/api/chat/send` | Append local chat; queue L2 free text in local Markdown outbox |
| GET | `/api/outbox/l2` | Read queued Markdown only |

Security requirements (all machine-verified in P1-14/P1-16 ★):

- Bind only to `127.0.0.1`. Never `0.0.0.0` or a LAN interface.
- No CORS exceptions, public URLs, webhooks, remote fetches, credentials, or token files.
- Any API key is optional; no-key local behavior is required and tested.
- No client data, raw Hermes memory, or secrets in state, chat, or outbox.
- No new runtime dependency beyond the declared allowlist in §15.4 without a flagged Handoff Packet entry.

---

## 9. UX and accessibility requirements

- Dark operational cockpit, high density, radius ≤ 8px, semantic status colour plus text label, monospace for paths/IDs/commands.
- Visible focus states, semantic headings, labelled icon buttons, keyboard room navigation, WCAG AA text contrast.
- Minimum 44px hit targets on mobile. No icon-only navigation.
- Responsive breakpoints for phone, tablet, desktop; no horizontal scrolling on phone.
- Respect reduced-motion preferences. Transitions limited to transform/opacity, under 300ms.
- Honest empty states: `L2 not auto-connected`, `MCP: none`, `Set me`, `Not available in Phase 1`.

---

## 10. Phase 1 acceptance tests ★ (now 17)

| ID | Test | Pass condition | Verification method |
| --- | --- | --- | --- |
| P1-01 | Local start | Documented start command serves `http://127.0.0.1:8765/` | Script + manual |
| P1-02 | Default route | Hard refresh opens Chat Hall | Browser + screenshot |
| P1-03 | Desktop navigation | Castle Map stays one fixed left column; never a chip grid | Browser + screenshot |
| P1-04 | Mobile navigation | Labelled drawer works; Chat remains default | Browser (mobile viewport) + screenshot |
| P1-05 | Command strip | Tonight lane/task/done-means visible and updates after `/tonight` | Browser interaction |
| P1-06 | L1 no-key chat | Free text saved locally with zero API keys in environment | **Scripted** |
| P1-07 | L2 outbox | L2 free text appears in local outbox; UI says it was not sent | Browser interaction + outbox file check |
| P1-08 | Slash validation | Malformed `/tonight` and `/ship add` return format help, no mutation | Browser interaction |
| P1-09 | Ship record | Valid `/ship add` displays lane, title, path, readiness, approval | Browser interaction |
| P1-10 | Approval phrase | Copy action copies exact phrase; states approval not executed | Browser interaction |
| P1-11 | Obsidian room | Vault path, Home note, fast-path list or honest empty state | Browser + screenshot |
| P1-12 | Jarvis room | L2 profile/model/gateway with explicit MCP status, source, last-checked | Browser + screenshot |
| P1-13 | Safety copy | Publish, CRM, QBO, spend, deploy shown blocked/human-only | Browser + screenshot |
| P1-14 | Localhost bind | Server binds `127.0.0.1`, not `0.0.0.0` | **Scripted** |
| P1-15 | Accessibility | Visible keyboard focus; labelled controls; reduced-motion holds | Browser interaction |
| P1-16 ★ | Safety scan | Codebase scan clean: no tokens/keys/secrets, no `0.0.0.0`, no non-localhost fetch targets, no affirmative forbidden words in UI strings, legacy `/approval done` absent as an executable command | **Scripted** |
| P1-17 ★ | Test suite ships | `test-phase1.sh` exists, runs P1-01/06/14/16 plus schema validation, and exits 0 | **Scripted** |

**Negative tests are mandatory evidence**, not optional: P1-07, P1-08, P1-10 must include screenshots of the failure/refusal states.

---

## 11. Delivery requirements

Before requesting review, the Builder provides:

1. Source path and local run command.
2. Screenshot/recording of Chat Hall desktop and mobile states.
3. P1-01 through P1-17 test record, including any failures or unimplemented items.
4. `test-phase1.sh` output log. ★
5. Diff summary and state schema migration note.
6. Per-wave commit log showing ownership compliance. ★
7. Handoff packet:

```markdown
## Handoff Packet
- Mission:
- Phase: 1
- Machine/runtime:
- Waves executed and agents per wave:
- What changed:
- Artifacts (absolute/local paths):
- Tests and results (n/17):
- Safety scan result:
- Known gaps:
- Decisions needed:
- Approval required:
- READINESS: n/17 | Next:
```

---

## 12. Roadmap after Phase 1

| Phase | Trigger to start | Scope |
| --- | --- | --- |
| Phase 2 | Umair uses Phase 1 daily and confirms shell hierarchy works | Lane depth, Ship Dock/approval polish, mission export, optional local L1 model, read-only runtime/artifact/skill registry |
| Phase 3 | Explicit written approval + threat review | Telegram bridge allowlist, draft-only L2 sync, read-only integrations, any private-network/device bridge; no auto-publish |
| Phase 4 | 14 days dogfooding + 10 logged ships + zero safety incidents | Governed Kanban, background-job panels with caps, candidate promotion, multi-agent factory visibility |

### Agent OS incorporation gates (from battle test; unchanged)

- **Runtime registry:** only verified profile/model/channel/health facts with source and last-checked. Unknown shown as unknown.
- **Cron registry:** owner, purpose, inputs, output path, next run, stop condition, hard cap, approval requirement, status. No hidden/uncapped background work.
- **Morning interview:** draft mission packet only; never auto-creates a ClickUp task, cron, external send, or execution run.
- **Learning ledger:** candidate skill update links to reviewed run, lesson, Skeptic disposition, human promotion decision.
- **Curated memory only:** pointers and handoffs; no raw sessions, full agent memory, secrets, or untrusted content in the cockpit.
- **Cross-device capabilities** (Tailscale, shared mounts, remote shell, device control) are privileged Phase 3, separately approved.

---

## 13. Open human decisions

1. Confirm the canonical source directory currently serving `127.0.0.1:8765/` before any Phase 1 edit. **(Blocks Wave 0 — must be answered before the swarm starts.)**
2. Confirm whether local state persists in the HQ repo or an ignored local runtime directory.
3. ~~`/approval done` semantics~~ — **Resolved in v1.3:** renamed `/approval clear`. ★
4. Confirm the exact L2 handoff path from the Windows machine before presenting it as a clickable file destination.

---

## 14. Do-not-build list

- No live Telegram send button; no bot tokens.
- No claim that Hermes/MCP is connected from Castle.
- No public deployment route, public bind, CORS bypass, or credential storage.
- Castle never becomes execution truth instead of ClickUp.
- No 50 agent personas, no speculative analytics.
- No Phase 2–4 work while Phase 1 tests are incomplete.
- ★ No agent may edit a file outside its declared ownership.
- ★ No push to any remote, no deploy, no dependency outside the allowlist, no spend.

---

## 15. Agent Execution Contract ★ (new — governs any multi-agent build of this PRD)

### 15.1 Wave structure and file ownership

| Wave | Mode | Owner(s) | Scope | Exit gate |
| --- | --- | --- | --- | --- |
| **Wave 0** | Serial, read-only | Sentinel | Baseline inventory (§2 finding 1): confirm source dir, run command, current routes, current `state.json` shape, screenshots of current behavior. Answer to Open Decision #1 must exist. | Inventory doc committed. Human confirms source dir if ambiguous — **stop and ask** rather than guess. |
| **Wave 1** | Serial, one Builder | Builder-1 | Server scaffold, `state.json` schema + validator (§7), API routes (§8), slash-command parser (§6), base shell layout (§5). | Local commit; `test-phase1.sh` partial (P1-01, P1-06, P1-14) passes. |
| **Wave 2** | Parallel, one agent per ownership unit | Agents A–G per §5 room table | Room implementations, Chat Hall panes, Command strip, mobile drawer, CSS/accessibility. Each agent owns exactly its assigned files. | Each agent delivers a handoff packet (files touched, behavior, self-test). |
| **Wave 3** | Serial | Integrator + Skeptic | Merge Wave 2, resolve conflicts, run full P1-01–17 with browser evidence, produce Handoff Packet. | 17/17 or documented failures; no other agent commits once Wave 3 starts. |

**Conflict rule:** if a Wave 2 agent discovers a needed change in a file it doesn't own (e.g., a shared CSS token or API shape), it logs the request in its handoff packet and continues with a local workaround or stub. It never edits outside its ownership. The Integrator reconciles.

**Parallelism cap:** Wave 2 runs at most 7 concurrent agents (one per ownership unit). "As many agents as it takes" means *up to the ownership map*, never beyond it.

### 15.2 Commit rules

- Local commits only. Never push to any remote. Never deploy.
- One commit per wave exit minimum; conventional messages prefixed `castle-p1(wave-N):`.
- No commit may contain: credentials, tokens, `.env` values, absolute user paths in code (config only), or `node_modules`/build artifacts.

### 15.3 Machine-checkable safety gates (the P1-16 scan)

The Skeptic lane runs, at minimum:

```bash
# secrets and keys
grep -rniE "(api[_-]?key|token|secret|bearer |sk-[a-zA-Z0-9])" src/ && FAIL
# public bind
grep -rn "0\.0\.0\.0" src/ && FAIL
# outbound calls to non-localhost
grep -rniE "fetch\(['\"]https?://(?!(127\.0\.0\.1|localhost))" src/ && FAIL
# affirmative forbidden UI words (manual review of hits required;
# honest negatives like "not sent" / "not connected" pass)
grep -rniE "\b(sent|synced|approved|published|connected|delivered)\b" src/ | grep -viE "not (sent|synced|approved|published|connected|delivered)"
# legacy command must not execute
grep -rn "approval done" src/  # allowed only in the help-redirect string
```

Any FAIL blocks the Handoff Packet from claiming readiness.

### 15.4 Dependency allowlist

Node stdlib + one minimal server package (e.g., Express or the existing baseline's server), plus whatever the confirmed baseline already uses. Anything else must be flagged as a **Decision needed** in the Handoff Packet before merge — not installed silently.

### 15.5 Stop conditions (any lane, immediately)

1. A subtask appears to require Phase 2+ capability (Telegram, MCP, tokens, cross-device, public bind). Log as `blocked: requires human phase approval`. **Reframing a gated action to make it seem allowed is itself the stop signal.**
2. Destructive ambiguity (e.g., two candidate source directories for the baseline).
3. Conflicting requirements between this PRD and observed baseline behavior — log both, do not pick silently.
4. Three consecutive failed attempts on the same acceptance test.
5. Any request for a credential (should never occur in Phase 1).

### 15.6 Verification boundary

Browser/computer-use verification is **required** against `http://127.0.0.1:8765` and **forbidden** against anything else. No lane may open, click, or type into any external site, messaging surface, or third-party service as part of "end-to-end" verification. The end-to-end path for Phase 1 terminates at the local outbox file — verifying "delivery" beyond it is out of scope by design.

---

## 16. Mission constraints summary for the executing runtime ★

The execution prompt handed to Grok Build must state, verbatim or equivalent: Phase 1 scope lock; the wave/ownership map of §15.1; the stop conditions of §15.5; the verification boundary of §15.6; local-commit-only rules; and that the deliverable is the §11 Handoff Packet with 17/17 evidence. If the prompt and this PRD ever disagree, **this PRD wins** and the disagreement is logged as a Decision needed.

All output of the build run is **Draft-Only until Umair reviews the Handoff Packet.**# Grok Build Mission Prompt — Castle OS Phase 1 (Supervised Swarm Run)

**Pair with:** `VCOS-MC-CASTLE-003_PRD_v1.3.md` (must be in the repo before starting)
**Runtime:** Grok Build CLI, start in plan mode:

```bash
~/.local/bin/grok \
  --permission-mode plan \
  --experimental-memory \
  --compaction-mode segments \
  --compaction-detail balanced
```

Paste the mission below once plan mode is active. Approve the plan before allowing edits.

---

```text
You are the Sentinel-Orchestrator for one bounded build mission inside VCOS HQ.

MISSION
Implement Phase 1 ONLY of VCOS-MC-CASTLE-003 v1.3 (Co-Founder Castle OS).
Read the full PRD file first: VCOS-MC-CASTLE-003_PRD_v1.3.md.
Done means exactly one thing: acceptance tests P1-01 through P1-17 pass with
recorded evidence (scripted logs + browser screenshots including the negative
tests), the P1-16 safety scan is clean, and the Section 11 Handoff Packet is
produced. Nothing else counts as done. If this prompt and the PRD ever
disagree, the PRD wins and you log the disagreement as "Decision needed."

SCOPE LOCK — read twice before planning
- Phase 1 only. Phases 2/3/4 are human-gated. If any subtask appears to need
  Phase 2+ capability (Telegram, Hermes/MCP connection, webhooks, ClickUp or
  GitHub tokens, cross-device or Tailscale access, public bind, deploys),
  STOP that lane and log it as "blocked: requires human phase approval."
  Do not reframe it as necessary for done — reframing a gated action to make
  it seem allowed is itself the stop signal.
- Do-Not-Build list (PRD §14) is absolute.
- Server binds 127.0.0.1:8765 only. Zero API keys required to run. Zero
  external network calls. No UI copy implies external delivery: the exact
  action labels in PRD §4 are mandatory strings.
- The slash command is /approval clear. The legacy /approval done must NOT
  execute; it returns a help redirect only.

EXECUTION — waves with strict file ownership (PRD §15.1)
Wave 0 (serial, read-only, you as Sentinel):
  Baseline inventory before ANY edit — confirm the exact source directory
  currently serving 127.0.0.1:8765, its run command, existing routes,
  existing state.json shape, screenshots of current behavior. If two
  candidate directories exist, STOP and ask the human. Commit the inventory
  doc. This answers PRD Open Decision #1 and gates everything downstream.

Wave 1 (serial, ONE Builder agent):
  Server scaffold, state.json schema + validator (PRD §7), API routes
  (PRD §8), slash-command parser with validation rules (PRD §6), base shell
  layout (PRD §5). Also create test-phase1.sh covering P1-01, P1-06, P1-14
  and schema validation. Exit gate: local commit + partial script passes.
  No other agent writes anything until Wave 1 is committed.

Wave 2 (parallel — spawn up to 7 subagents, one per ownership unit from the
PRD §5 room table, isolated context, each owns ONLY its assigned files):
  Agent A: Chat Hall dual panes and compose behavior (PRD §6 layout)
  Agent B: Command room + Command strip
  Agent C: L2 Wing (honest empty states, source/last-checked fields)
  Agent D: Lane rooms (amax, content, safar, fde — read-only)
  Agent E: Ship Dock + Approval Gate (copy behavior + required disclaimer)
  Agent F: Obsidian Vault + Jarvis Bay rooms
  Agent G: Cadence + Blueprints (Blueprints visually demoted) + mobile
           drawer + accessibility/reduced-motion pass (PRD §9)
  Conflict rule: if an agent needs a change in a file it does not own, it
  logs the request in its handoff packet and stubs locally. It NEVER edits
  outside its ownership. Each agent ends with a handoff packet: files
  touched, behavior delivered, self-test notes.

Wave 3 (serial — one Integrator, then one Skeptic):
  Integrator: merge Wave 2, reconcile logged conflicts, single ownership of
  all files from here. No other agent commits once Wave 3 starts.
  Skeptic: run the FULL verification below.

VERIFICATION (Skeptic lane — mandatory, in this order)
1. Scripted: run test-phase1.sh — localhost-only bind, no-key startup,
   /api/health, state.json schema validation. Capture the log.
2. Static safety scan (P1-16): grep the codebase for api keys/tokens/
   secrets, "0.0.0.0", fetch/network calls to non-localhost targets, and
   affirmative forbidden UI words (sent, synced, approved, published,
   connected, delivered) — honest negatives like "not sent" pass. Verify
   the legacy "/approval done" exists only as a help-redirect string.
   Any hit = FAIL = readiness blocked.
3. Live browser verification against http://127.0.0.1:8765 ONLY — real
   clicks and keyboard for P1-01 through P1-15, including the NEGATIVE
   tests: malformed /tonight and /ship add must show format help with no
   mutation; L2 free text must show "queued locally — not sent to Hermes
   or Telegram" and land in the outbox file; approval copy must state
   human approval is still required; /approval clear must state it does
   not perform the approval. Screenshot every pass and every refusal
   state. Desktop viewport AND mobile viewport for P1-02/03/04.
   Browser use never touches any external site, service, login, or send
   path. The end-to-end path for Phase 1 terminates at the local outbox
   file by design — do not verify "delivery" beyond it.

OPERATOR LOOP
Schedule the waves, track per-agent status, synthesize handoff packets
(packets, not raw logs), resolve conflicts as Sentinel, and commit locally
at each wave exit with messages prefixed castle-p1(wave-N):. Local commits
only — never push to any remote, never deploy, never install a dependency
outside the PRD §15.4 allowlist without flagging it as "Decision needed."

STOP CONDITIONS (any lane, immediately)
- Any Phase 2+ capability requirement (log, do not work around)
- Destructive ambiguity (e.g., unclear baseline directory)
- Conflict between PRD and observed baseline behavior (log both)
- Three consecutive failures on the same acceptance test
- Any request for a credential (must never occur in Phase 1)

CLOSE
Produce the PRD §11 Handoff Packet: source path, run command, waves and
agents used, screenshots (desktop + mobile Chat Hall), full P1-01–17
results including failures, test-phase1.sh log, safety scan result, diff
summary, schema note, per-wave commit log, known gaps, decisions needed,
READINESS: n/17.

Everything produced is Draft-Only until Umair reviews the Handoff Packet.
No external send, publish, CRM mutation, spend, or deploy exists in this
mission under any framing.
```

---

## Pre-flight checklist for Umair (before pasting the mission)

1. PRD v1.3 file is committed into the Castle repo root.
2. Open Decision #1 answered or answerable: you know (or can confirm on ask) which directory currently serves :8765.
3. Open Decision #2 answered: state persists in HQ repo vs. ignored local dir — tell the agent in one line if you already know.
4. This is a **supervised** run on the L1 machine only — not the Hermes/L2 laptop, not 24/7. Watch Wave 0 and Wave 1 exits live; Wave 2 can run while you do other work.
5. Approval to start = your explicit go after reviewing the plan-mode output.
