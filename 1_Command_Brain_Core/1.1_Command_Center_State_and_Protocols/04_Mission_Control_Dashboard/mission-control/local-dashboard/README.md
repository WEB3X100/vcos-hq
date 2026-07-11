# VCOS Co-Founder Castle OS — Local Dashboard (Phase 1)

**PRD authority:** `../COFOUNDER-CASTLE-OS-PRD.md` (VCOS-MC-CASTLE-003 v1.3)  
**Run:** `python3 server.py` → **http://127.0.0.1:8765/**  
**Bind:** `127.0.0.1` only · **Deps:** Python stdlib only  

## What this is

Local operator cockpit: Castle Map (left), Command strip, Chat Hall default (L1 | L2), lane rooms, Ship Dock, Approval Gate, Obsidian + Jarvis rooms.

## What this is not

Remote Hermes control, Telegram auto-send, ClickUp replacement, CRM/QBO, ads, public bind.

## L1 vs L2 send effects

| Pane | Effect label |
| --- | --- |
| L1 free text | Saved locally |
| L2 free text | Queued locally — not sent to Hermes or Telegram |
| Slash commands | Updated local Castle state only |
| Copy approval phrase | Copied — human sign-off still required |

## Tests

```bash
chmod +x test-phase1.sh
./test-phase1.sh
```

## Optional model replies (L1)

```bash
export XAI_API_KEY=...   # optional
python3 server.py
```

No-key mode is required to pass Phase 1.
