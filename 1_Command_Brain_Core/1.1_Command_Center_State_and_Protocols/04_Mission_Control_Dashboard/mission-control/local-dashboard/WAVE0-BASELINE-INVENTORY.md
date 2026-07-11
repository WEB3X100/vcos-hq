# Wave 0 — Baseline Inventory

**Date:** 2026-07-11  
**Authority:** VCOS-MC-CASTLE-003 v1.3  
**Source path:** `mission-control/local-dashboard/`  
**Run command:** `python3 server.py` → `http://127.0.0.1:8765/`  
**Bind:** `127.0.0.1:8765` (ThreadingHTTPServer)  
**Health (verified):** `{"ok": true, "llm": false}`

## Files

| File | Role |
| --- | --- |
| `server.py` | Static + API, slash OS, dual chat, optional XAI (urllib) |
| `index.html` | Shell |
| `app.js` | Flat-tab UI + dual chat |
| `styles.css` | Dark theme |
| `data/state.json` | Cockpit state |
| `data/chats/l1.json`, `l2.json` | Chat history |
| `data/outbox/l2-telegram-queue.md` | L2 queue |
| `README.md` | Run notes |

## API routes (existing)

| Method | Path |
| --- | --- |
| GET | `/api/health` |
| GET | `/api/state` |
| GET | `/api/chat/{l1\|l2}` |
| GET | `/api/outbox/l2` |
| POST | `/api/chat/send` |
| POST | `/api/os` |

## Imports (stdlib + baseline)

`json`, `os`, `re`, `traceback`, `urllib.error`, `urllib.request`, `datetime`, `http.server`, `pathlib`, `typing`, `urllib.parse`  
**No pip packages.** Allowlist override: Python stdlib only + existing imports.

## Known UX failures (critique → Phase 1 fix)

- Flat equal-weight tabs (wraps to chip grid on narrow/desktop top)
- Chat not spatial primary / hard default hierarchy
- No Castle Map left rail
- No `obsidian` / `jarvis` in state
- Copy can imply external effects without strong labels
- `/approval done` used (must become `/approval clear` + legacy help redirect)

## state.json vs PRD §7 schema — migration notes

| PRD field | Baseline | Action |
| --- | --- | --- |
| `version` | `0.2.0-local-chats` | Bump to `0.3.0-castle-p1` |
| `obsidian` | **missing** | Add with empty/set-me defaults |
| `jarvis` | **missing** | Add from l2 facts + source/last_checked |
| `ships[].readiness` | uses `status` | Map `status`→`readiness` DRAFT\|REVIEW\|READY; keep extra fields |
| `ships[].approval` | free text | Normalize to `none`\|`human` where possible; preserve extras |
| `approvals_queue[].say_phrase` | field is `say` | Accept both; write `say_phrase` going forward |
| `data_note`, `critique`, `prompts`, `sources`, `clickup` | present | **Preserve** (unknown fields ok) |
| `l2.dashboard_localhost`, `mcp_configured` | present | Keep |
| `l1.device`, `l1.role` | present | Preserve |

## Screenshots

Wave 0 does not attach binary screenshots in git; current behavior captured via API health/state probes. Wave 3 Skeptic captures desktop/mobile Chat Hall screenshots after shell redesign.

## Dependency note

Optional LLM uses `urllib` to `api.x.ai` only when `XAI_API_KEY` set — Phase 1 must pass with key **unset** (P1-06).
