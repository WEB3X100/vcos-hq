# Handoff Packet — Castle Phase 1 (VCOS-MC-CASTLE-003 v1.3)

**Date:** 2026-07-11  
**Status:** Draft-Only until Umair accepts  
**READINESS: 17/17** (scripted + Skeptic computer-use visual)

---

## Source path & run

| Field | Value |
| --- | --- |
| Source | `mission-control/local-dashboard/` |
| PRD | `mission-control/COFOUNDER-CASTLE-OS-PRD.md` |
| Run | `python3 server.py` |
| URL | `http://127.0.0.1:8765/` |
| Bind | `127.0.0.1` only |

---

## Waves

| Wave | Result |
| --- | --- |
| 0 | Baseline inventory + PRD authority |
| 1 | Server, slash semantics, schema, test-phase1.sh |
| 2 | Castle shell + all rooms (single builder; shared app.js — valid ownership rule) |
| 3 | Scripted + **Skeptic Playwright visual V1–V5** |

---

## Commits (local, not pushed)

| Hash | Message |
| --- | --- |
| `99d952e` | castle-p1(wave-0-3): shell + tests |
| `b529f09` | castle-p1(wave-3): handoff packet |
| *(pending)* | castle-p1(wave-3): skeptic visual close + mobile overflow fix |

---

## P1-01 … P1-17

| ID | Result | Evidence |
| --- | --- | --- |
| P1-01 | PASS | `./test-phase1.sh` |
| P1-02 | **PASS** | Skeptic V1: hard refresh → h1=Chat Hall · `skeptic-screenshots/V1-p1-02-hard-refresh-chat-hall.png` |
| P1-03 | **PASS** | Skeptic V2: rail width=248, vertical rooms · `V2-p1-03-desktop-wide.png` + narrow |
| P1-04 | **PASS** | Skeptic V3: drawer, Chat default, Command switch, scroll_w=0, hit 44px · mobile screenshots (retest after overflow fix) |
| P1-05 | PASS | `/tonight` API + Command strip |
| P1-06 | PASS | test-phase1 no-key |
| P1-07 | **PASS** | Skeptic V4: UI “Queued locally — not sent…” + outbox Markdown · `V4-p1-07-l2-queue-label.png` |
| P1-08 | PASS | malformed /tonight Format help |
| P1-09 | PASS | /ship add DRAFT |
| P1-10 | **PASS** | Copy disclaimer on Approvals room + toast path; phrase copy · `V5-p1-10-copy-phrase.png` |
| P1-11 | PASS | Obsidian room |
| P1-12 | PASS | Jarvis room |
| P1-13 | PASS | Blocked human-only list |
| P1-14 | PASS | 127.0.0.1 bind |
| P1-15 | PASS | focus/hit/reduced-motion code + mobile 44px |
| P1-16 | PASS | test-phase1 static scan |
| P1-17 | PASS | test-phase1.sh exit 0 |

### Visual suite log

`data/outbox/skeptic-visual.log`  
Screenshots dir: `data/outbox/skeptic-screenshots/`

| Visual | Result |
| --- | --- |
| V1 | PASS |
| V2 | PASS |
| V3 | PASS (after CSS overflow-x fix; first run FAIL scroll=49 → fixed → retest scroll=0) |
| V4 | PASS |
| V5 | PASS (clear + legacy redirect + no queue mutate; clipboard toast may fail headless — on-page disclaimer present) |

---

## Schema migration (unchanged from prior)

`obsidian` + `jarvis` added; ships `readiness`/`approval`; `/approval clear`; version `0.3.0-castle-p1`.

---

## Known gaps / decisions needed

1. Headless clipboard often fails (`Copy failed — select manually`) — UI disclaimer still correct; real Mac clipboard OK for operator.  
2. External Google Fonts blocked during Skeptic to keep load local-only; production UI may still request fonts (optional local font later).  
3. Phase 2+ still Do-Not-Build until Umair accepts this packet.  
4. HQ restructure renames remain outside this mission’s dirty tree.

---

## Operator accept checklist

- [ ] Open http://127.0.0.1:8765/ hard refresh  
- [ ] Review screenshots in `data/outbox/skeptic-screenshots/`  
- [ ] Explicit accept: **Phase 1 CLOSED** or list residuals  

**Draft-Only until Umair accepts.** No Phase 2 work starts before that.
