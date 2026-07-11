#!/usr/bin/env python3
"""
VCOS Co-Founder Castle OS — local server (Phase 1)
Python stdlib only (+ baseline imports). Binds 127.0.0.1 only.

Usage:
  python3 server.py
  open http://127.0.0.1:8765/
"""

from __future__ import annotations

import json
import os
import re
import traceback
import urllib.error
import urllib.request
from datetime import datetime, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
CHATS = DATA / "chats"
OUTBOX = DATA / "outbox"
STATE_PATH = DATA / "state.json"
PORT = int(os.environ.get("VCOS_MC_PORT", "8765"))
HOST = "127.0.0.1"

for d in (CHATS, OUTBOX):
    d.mkdir(parents=True, exist_ok=True)

for name, seed in (
    ("l1.json", {"channel": "l1", "label": "Main Mac / Sentinel", "messages": []}),
    ("l2.json", {"channel": "l2", "label": "L2 Co-Founder (outbox)", "messages": []}),
):
    p = CHATS / name
    if not p.exists():
        p.write_text(json.dumps(seed, indent=2) + "\n", encoding="utf-8")


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def chat_path(channel: str) -> Path:
    if channel not in ("l1", "l2"):
        raise ValueError("channel must be l1 or l2")
    return CHATS / f"{channel}.json"


def append_message(channel: str, role: str, content: str, meta: dict | None = None) -> dict:
    path = chat_path(channel)
    data = read_json(path)
    msg = {
        "id": f"{channel}-{int(datetime.now().timestamp() * 1000)}",
        "role": role,
        "content": content,
        "ts": now_iso(),
        "meta": meta or {},
    }
    data.setdefault("messages", []).append(msg)
    data["messages"] = data["messages"][-200:]
    write_json(path, data)
    return msg


def migrate_state(state: dict) -> dict:
    """Preserve unknown fields; fill PRD §7 required shape."""
    state.setdefault("version", "0.3.0-castle-p1")
    if not str(state.get("version", "")).startswith("0.3"):
        state["version"] = "0.3.0-castle-p1"
    state.setdefault("data_freshness", "session-seeded")
    state.setdefault("north_star", "")
    state.setdefault("active_priority_order", [])
    state.setdefault("parked", [])
    state.setdefault("tonight_chunk", {})
    tc = state["tonight_chunk"]
    for k in ("lane", "task", "done_means", "primary_tool"):
        tc.setdefault(k, "")
    tc.setdefault("do_not_open", [])
    state.setdefault("l1", {"name": "Main Mac", "status": "unknown", "channel": "local"})
    state.setdefault("l2", {})
    l2 = state["l2"]
    for k, v in (
        ("name", "L2 Co-Founder"),
        ("status", "unknown"),
        ("profile", ""),
        ("model", ""),
        ("gateway", ""),
        ("dashboard_localhost", False),
        ("mcp_configured", False),
        ("handoffs_root", ""),
    ):
        l2.setdefault(k, v)
    state.setdefault("lanes", {})
    for lk, lane in list(state["lanes"].items()):
        if not isinstance(lane, dict):
            continue
        lane.setdefault("next_action", "")
        lane.setdefault("gate", "")
        lane.setdefault("owner", "")
        lane.setdefault("last_update", "")
        lane.setdefault("copy_mission_text", "")
    state.setdefault("obsidian", {
        "vault_path": "",
        "home_note": "Home.md",
        "fast_path": [
            "AGENTS.md",
            "1_Command_Brain_Core/1.2_Headquarters_Memory/ubiquitous_language.md",
            "1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/00_Live_State_and_GSD/state.md",
            "1_Command_Brain_Core/1.2_Headquarters_Memory/active-context.md",
            "1_Command_Brain_Core/1.2_Headquarters_Memory/key-workspaces.md",
        ],
    })
    if not state.get("jarvis"):
        state["jarvis"] = {
            "agents": [l2.get("profile") or "neuralsync-intern-builder"],
            "gateway_note": l2.get("gateway") or "unknown — set via /l2 status",
            "cron_jobs": [],
            "source": "local state mirror (human-observed)",
            "last_checked": now_iso(),
        }
    else:
        state["jarvis"].setdefault("source", "local state mirror (human-observed)")
        state["jarvis"].setdefault("last_checked", now_iso())
        state["jarvis"].setdefault("agents", [])
        state["jarvis"].setdefault("cron_jobs", [])
        state["jarvis"].setdefault("gateway_note", "")

    ships = state.setdefault("ships", [])
    for s in ships:
        if "readiness" not in s and "status" in s:
            st = str(s.get("status", "")).lower()
            if st in ("done", "ready"):
                s["readiness"] = "READY" if st == "ready" else "DRAFT"
            elif "review" in st:
                s["readiness"] = "REVIEW"
            else:
                s["readiness"] = "DRAFT"
        s.setdefault("readiness", "DRAFT")
        ap = str(s.get("approval", "none"))
        if ap not in ("none", "human"):
            s["approval"] = "human" if ap and ap != "none" else "none"
        s.setdefault("lane", "")
        s.setdefault("title", "")
        s.setdefault("path", "")

    for a in state.setdefault("approvals_queue", []):
        if "say_phrase" not in a and "say" in a:
            a["say_phrase"] = a["say"]
        a.setdefault("say_phrase", "")
        a.setdefault("id", "")
        a.setdefault("item", "")
        a.setdefault("last_copied", "")

    # jarvis.agents may be list of strings or list of dicts
    j = state.get("jarvis") or {}
    agents = j.get("agents") or []
    if agents and isinstance(agents[0], str):
        j["agents"] = [
            {
                "id": a,
                "model": "unknown",
                "channel": "unknown",
                "health": "unknown",
                "source": "unknown",
                "last_checked": "",
            }
            for a in agents
        ]
        state["jarvis"] = j
    elif not agents:
        j["agents"] = []
        state["jarvis"] = j
    j.setdefault("cron_jobs", [])

    return state


def load_state() -> dict:
    state = read_json(STATE_PATH)
    return migrate_state(state)


def save_state(state: dict) -> None:
    state = migrate_state(state)
    state["updated_at"] = now_iso()
    state["data_freshness"] = "chat-updated"
    write_json(STATE_PATH, state)


def append_l2_outbox(text: str) -> Path:
    """Raises OSError on write failure so caller can preserve compose input."""
    path = OUTBOX / "l2-telegram-queue.md"
    block = f"\n---\n## Queued locally {now_iso()}\n\n```text\n{text.strip()}\n```\n"
    if path.exists():
        path.write_text(path.read_text(encoding="utf-8") + block, encoding="utf-8")
    else:
        path.write_text(
            "# L2 outbox (local only)\n\n"
            "Blocks are queued on this Mac. Human pastes into Telegram.\n"
            "Not auto-dispatched to Hermes.\n"
            + block,
            encoding="utf-8",
        )
    return path


HELP = """Slash commands (update local Castle state only):

/help
/tonight <lane> | <task> | <done means>
/l2 status <text>
/l2 model <text>
/ship add <lane> | <title> | <path>
/ship update <id> | <field> | <value>
/ship remove <id>
/approval add <item> | <say phrase>
/approval clear <id>
/lane set <lane> | <field> | <value>
/jarvis set <agent> | <field> | <value>
/vault set path <value>
/vault set home <value>
/park add <item>
/priority
/note <text>
/safar blocker <text>

Effect: Updated local Castle state only.
L1 free text: Saved locally.
L2 free text: Queued locally — not sent to Hermes or Telegram.
Legacy /approval done is not supported — use /approval clear.
"""

LANE_KEYS = ("amax", "content", "content_intel", "safar", "fde", "trading", "gtm")
LANE_FIELDS = ("next_action", "gate", "owner", "copy_mission_text")
JARVIS_AGENT_FIELDS = ("model", "channel", "health", "source", "last_checked")
SHIP_FIELDS = ("lane", "title", "path", "readiness", "approval")
READINESS_ORDER = {"DRAFT": 0, "REVIEW": 1, "READY": 2}


def append_activity(line: str) -> None:
    path = OUTBOX / "cadence-activity.log"
    with path.open("a", encoding="utf-8") as f:
        f.write(f"{now_iso()} | {line}\n")


def normalize_lane_key(name: str) -> str:
    n = name.strip().lower().replace(" ", "_")
    if n == "content":
        return "content_intel"
    return n


def apply_os_command(text: str) -> tuple[str, bool]:
    raw = text.strip()
    if not raw.startswith("/"):
        return ("", False)

    state = load_state()
    lower = raw.lower()

    if lower in ("/help", "/?"):
        return (HELP, False)

    # Legacy redirect — no mutation
    if lower.startswith("/approval done"):
        return (
            "Unknown form. /approval done is retired because it sounds like a human sign-off.\n"
            "Use: /approval clear <id>\n"
            "That only clears the local display queue — it does not perform the human sign-off or any external action.",
            False,
        )

    if lower.startswith("/tonight"):
        body = raw[len("/tonight") :].strip()
        if not body:
            return ("Format: /tonight <lane> | <task> | <done means>", False)
        parts = [p.strip() for p in body.split("|")]
        if len(parts) < 3 or not all(parts[:3]):
            return ("Format: /tonight <lane> | <task> | <done means>  (all three segments required)", False)
        state.setdefault("tonight_chunk", {})
        state["tonight_chunk"]["lane"] = parts[0]
        state["tonight_chunk"]["task"] = parts[1]
        state["tonight_chunk"]["done_means"] = parts[2]
        save_state(state)
        return (
            "Updated local Castle state (tonight_chunk):\n"
            f"- lane: {parts[0]}\n- task: {parts[1]}\n- done_means: {parts[2]}",
            True,
        )

    if lower.startswith("/l2 status "):
        state.setdefault("l2", {})["status"] = raw[len("/l2 status ") :].strip()
        state.setdefault("jarvis", {})["gateway_note"] = state["l2"]["status"]
        state["jarvis"]["last_checked"] = now_iso()
        save_state(state)
        return (f"Updated local Castle state: l2.status = {state['l2']['status']}", True)

    if lower.startswith("/l2 model "):
        state.setdefault("l2", {})["model"] = raw[len("/l2 model ") :].strip()
        save_state(state)
        return (f"Updated local Castle state: l2.model = {state['l2']['model']}", True)

    if lower.startswith("/ship add"):
        body = raw[len("/ship add") :].strip()
        parts = [p.strip() for p in body.split("|")]
        if len(parts) < 3 or not all(parts[:3]):
            return ("Format: /ship add <lane> | <title> | <path>  (all three segments required)", False)
        ships = state.setdefault("ships", [])
        sid = f"ship-{len(ships) + 1:03d}"
        ships.append(
            {
                "id": sid,
                "date": datetime.now().date().isoformat(),
                "lane": parts[0],
                "title": parts[1],
                "path": parts[2],
                "readiness": "DRAFT",
                "approval": "human",
            }
        )
        save_state(state)
        return (
            f"Updated local Castle state: ship {sid} recorded (readiness DRAFT). "
            "Human sign-off still required before any external use.",
            True,
        )

    if lower.startswith("/ship update"):
        body = raw[len("/ship update") :].strip()
        parts = [p.strip() for p in body.split("|")]
        if len(parts) < 3 or not all(parts[:3]):
            return ("Format: /ship update <id> | <field> | <value>", False)
        sid, field, value = parts[0], parts[1].lower(), parts[2]
        if field not in SHIP_FIELDS:
            return (f"Unknown field. Allowed: {', '.join(SHIP_FIELDS)}", False)
        ship = next((s for s in state.get("ships", []) if s.get("id") == sid), None)
        if not ship:
            return (f"No ship id {sid}", False)
        if field == "readiness":
            value = value.upper()
            if value not in READINESS_ORDER:
                return ("readiness must be DRAFT | REVIEW | READY", False)
            cur = ship.get("readiness", "DRAFT")
            # no skip forward; rollback REVIEW→DRAFT ok; READY← only from REVIEW
            if value == "READY" and cur != "REVIEW":
                return ("readiness transitions DRAFT → REVIEW → READY only (no skipping)", False)
            if value == "REVIEW" and cur not in ("DRAFT", "REVIEW", "READY"):
                return ("Invalid current readiness", False)
            if value == "DRAFT" and cur not in ("DRAFT", "REVIEW", "READY"):
                return ("Invalid rollback", False)
            if value == "READY" and ship.get("approval") == "none":
                ship["ready_block"] = "READY blocked — approval field is 'none'"
                save_state(state)
                return (
                    "READY blocked — approval field is 'none'. Local display only; nothing external.",
                    True,
                )
            ship.pop("ready_block", None)
            ship["readiness"] = value
            if value == "READY":
                append_activity(f"ship {sid} READY | lane={ship.get('lane')}")
            save_state(state)
            return (
                f"Updated local Castle state: ship {sid} readiness={value}"
                + (
                    ". READY — human sign-off still required before any external use."
                    if value == "READY"
                    else ""
                ),
                True,
            )
        if field == "approval" and value not in ("none", "human"):
            return ("approval must be none | human", False)
        ship[field] = value
        save_state(state)
        return (f"Updated local Castle state: ship {sid}.{field}", True)

    if lower.startswith("/ship remove"):
        body = raw[len("/ship remove") :].strip()
        if not body:
            return ("Format: /ship remove <id>", False)
        sid = body.split()[0]
        before = len(state.get("ships", []))
        state["ships"] = [s for s in state.get("ships", []) if s.get("id") != sid]
        if len(state["ships"]) == before:
            return (f"No ship id {sid}", False)
        save_state(state)
        return (f"Updated local Castle state: removed ship {sid}", True)

    if lower.startswith("/lane set"):
        body = raw[len("/lane set") :].strip()
        parts = [p.strip() for p in body.split("|")]
        if len(parts) < 3 or not all(parts[:3]):
            return ("Format: /lane set <lane> | <field> | <value>", False)
        lk = normalize_lane_key(parts[0])
        field = parts[1].lower()
        value = parts[2]
        if field not in LANE_FIELDS:
            return (f"Unknown field. Allowed: {', '.join(LANE_FIELDS)}", False)
        lane = state.setdefault("lanes", {}).setdefault(lk, {"name": parts[0]})
        lane[field] = value
        lane["last_update"] = now_iso()
        append_activity(f"lane {lk} last_update | field={field}")
        save_state(state)
        return (f"Updated local Castle state: lanes.{lk}.{field}", True)

    if lower.startswith("/jarvis set"):
        body = raw[len("/jarvis set") :].strip()
        parts = [p.strip() for p in body.split("|")]
        if len(parts) < 3 or not all(parts[:3]):
            return ("Format: /jarvis set <agent> | <field> | <value>", False)
        agent_id, field, value = parts[0], parts[1].lower(), parts[2]
        if field not in JARVIS_AGENT_FIELDS:
            return (f"Unknown field. Allowed: {', '.join(JARVIS_AGENT_FIELDS)}", False)
        agents = state.setdefault("jarvis", {}).setdefault("agents", [])
        # ensure dict list
        if agents and isinstance(agents[0], str):
            agents = [
                {"id": a, "model": "unknown", "channel": "unknown", "health": "unknown", "source": "unknown", "last_checked": ""}
                for a in agents
            ]
            state["jarvis"]["agents"] = agents
        rec = next((a for a in agents if isinstance(a, dict) and a.get("id") == agent_id), None)
        if not rec:
            rec = {
                "id": agent_id,
                "model": "unknown",
                "channel": "unknown",
                "health": "unknown",
                "source": "unknown",
                "last_checked": "",
            }
            agents.append(rec)
        rec[field] = value
        if field != "last_checked":
            rec["last_checked"] = now_iso()
        state["jarvis"]["last_checked"] = now_iso()
        save_state(state)
        return (f"Updated local Castle state: jarvis.agents[{agent_id}].{field}", True)

    if lower.startswith("/vault set path "):
        val = raw[len("/vault set path ") :].strip()
        if not val:
            return ("Format: /vault set path <value>", False)
        state.setdefault("obsidian", {})["vault_path"] = val
        save_state(state)
        return ("Updated local Castle state: obsidian.vault_path", True)

    if lower.startswith("/vault set home "):
        val = raw[len("/vault set home ") :].strip()
        if not val:
            return ("Format: /vault set home <value>", False)
        state.setdefault("obsidian", {})["home_note"] = val
        save_state(state)
        return ("Updated local Castle state: obsidian.home_note", True)

    if lower.startswith("/approval add"):
        body = raw[len("/approval add") :].strip()
        parts = [p.strip() for p in body.split("|")]
        if len(parts) < 2 or not parts[0] or not parts[1]:
            return ("Format: /approval add <item> | <say phrase>", False)
        q = state.setdefault("approvals_queue", [])
        aid = f"ap-{len(q) + 1:03d}"
        q.append({"id": aid, "item": parts[0], "say_phrase": parts[1], "type": "manual", "status": "waiting"})
        save_state(state)
        return (f"Updated local Castle state: queue item {aid} (local display only)", True)

    if lower.startswith("/approval clear "):
        aid = raw[len("/approval clear ") :].strip()
        q = state.get("approvals_queue", [])
        new_q = [a for a in q if a.get("id") != aid]
        if len(new_q) == len(q):
            return (f"No local queue item id {aid}", False)
        state["approvals_queue"] = new_q
        save_state(state)
        return (
            f"Cleared {aid} from local display — this does not perform the human sign-off or any external action.",
            True,
        )

    if lower.startswith("/park add "):
        item = raw[len("/park add ") :].strip()
        if not item:
            return ("Format: /park add <item>", False)
        state.setdefault("parked", []).append(item)
        save_state(state)
        return (f"Updated local Castle state: parked += {item}", True)

    if lower.startswith("/priority"):
        lines = "\n".join(
            f"{i+1}. {p}" for i, p in enumerate(state.get("active_priority_order", []))
        )
        return (f"Priorities (local mirror):\n{lines or '(empty)'}", False)

    if lower.startswith("/note "):
        note = raw[len("/note ") :].strip()
        notes_path = OUTBOX / "os-notes.md"
        with notes_path.open("a", encoding="utf-8") as f:
            f.write(f"\n- [{now_iso()}] {note}\n")
        return ("Saved locally to outbox/os-notes.md", True)

    if lower.startswith("/safar blocker "):
        b = raw[len("/safar blocker ") :].strip()
        if not b:
            return ("Format: /safar blocker <text>", False)
        lane = state.setdefault("lanes", {}).setdefault("safar", {})
        lane.setdefault("blockers", []).append(b)
        save_state(state)
        return ("Updated local Castle state: safar.blockers", True)

    return (f"Unknown command. Try /help\nYou said: {raw[:200]}", False)


def optional_l1_llm(user_text: str, history: list[dict]) -> str | None:
    key = os.environ.get("XAI_API_KEY") or os.environ.get("GROK_API_KEY")
    if not key:
        return None
    model = os.environ.get("XAI_MODEL", "grok-3")
    messages = [
        {
            "role": "system",
            "content": (
                "You are VCOS Main Mac Sentinel inside Castle OS. "
                "Draft-only for external actions. Prefer slash commands for state changes. Be concise."
            ),
        }
    ]
    for m in history[-12:]:
        role = m.get("role")
        if role in ("user", "assistant"):
            messages.append({"role": role, "content": m.get("content", "")[:4000]})
    messages.append({"role": "user", "content": user_text[:6000]})
    body = json.dumps({"model": model, "messages": messages, "temperature": 0.4}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.x.ai/v1/chat/completions",
        data=body,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"(model error: {e})"


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, fmt: str, *args: Any) -> None:
        print(f"[castle] {self.address_string()} {fmt % args}")

    def _send(self, code: int, body: Any, content_type: str = "application/json") -> None:
        raw = (
            body
            if isinstance(body, (bytes, bytearray))
            else (
                body.encode("utf-8")
                if content_type != "application/json"
                else json.dumps(body, ensure_ascii=False).encode("utf-8")
            )
        )
        self.send_response(code)
        self.send_header("Content-Type", f"{content_type}; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(raw)

    def _read_json(self) -> dict:
        n = int(self.headers.get("Content-Length") or 0)
        if n == 0:
            return {}
        return json.loads(self.rfile.read(n).decode("utf-8"))

    def do_GET(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        if path == "/api/health":
            return self._send(
                200,
                {
                    "ok": True,
                    "time": now_iso(),
                    "host": HOST,
                    "llm": bool(os.environ.get("XAI_API_KEY") or os.environ.get("GROK_API_KEY")),
                },
            )
        if path == "/api/state":
            return self._send(200, load_state())
        if path.startswith("/api/chat/"):
            channel = path.rstrip("/").split("/")[-1]
            try:
                return self._send(200, read_json(chat_path(channel)))
            except Exception as e:
                return self._send(400, {"error": str(e)})
        if path == "/api/outbox/l2":
            p = OUTBOX / "l2-telegram-queue.md"
            text = p.read_text(encoding="utf-8") if p.exists() else "# empty\n"
            return self._send(200, {"path": str(p), "markdown": text})
        if path == "/api/cadence/activity":
            p = OUTBOX / "cadence-activity.log"
            text = p.read_text(encoding="utf-8") if p.exists() else ""
            lines = [ln for ln in text.strip().splitlines() if ln][-30:]
            return self._send(200, {"lines": lines})
        return super().do_GET()

    def do_POST(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        try:
            if path == "/api/chat/send":
                return self._chat_send()
            if path == "/api/os":
                payload = self._read_json()
                reply, changed = apply_os_command(payload.get("command", ""))
                return self._send(
                    200, {"reply": reply, "changed": changed, "state": load_state()}
                )
            if path == "/api/approval/copied":
                payload = self._read_json()
                aid = (payload.get("id") or "").strip()
                st = load_state()
                for a in st.get("approvals_queue", []):
                    if a.get("id") == aid:
                        a["last_copied"] = now_iso()
                        save_state(st)
                        return self._send(200, {"ok": True, "state": load_state()})
                return self._send(404, {"error": "not found"})
            if path == "/api/critique/save":
                payload = self._read_json()
                text = payload.get("text") or ""
                path_out = DATA / "critique-notes.md"
                path_out.write_text(text, encoding="utf-8")
                return self._send(200, {"ok": True, "path": str(path_out), "effect": "Saved locally"})
            return self._send(404, {"error": "not found"})
        except Exception as e:
            traceback.print_exc()
            return self._send(500, {"error": str(e)})

    def _chat_send(self) -> None:
        payload = self._read_json()
        channel = (payload.get("channel") or "").strip()
        content = (payload.get("content") or "").strip()
        if channel not in ("l1", "l2"):
            return self._send(400, {"error": "channel must be l1 or l2"})
        if not content:
            return self._send(400, {"error": "empty content"})

        user_msg = append_message(channel, "user", content)
        replies: list[dict] = []
        state_changed = False
        effect = ""

        if content.startswith("/"):
            reply, state_changed = apply_os_command(content)
            effect = "Updated local Castle state" if state_changed else "No state change"
            if reply:
                replies.append(
                    append_message(
                        channel,
                        "system",
                        f"[{effect}]\n{reply}",
                        {"kind": "os", "state_changed": state_changed},
                    )
                )
        elif channel == "l2":
            try:
                out_path = append_l2_outbox(content)
            except OSError as e:
                return self._send(
                    200,
                    {
                        "user": user_msg,
                        "replies": [
                            append_message(
                                channel,
                                "system",
                                f"Queue write FAILED — message not saved\n({e})",
                                {"kind": "l2_queue_fail"},
                            )
                        ],
                        "effect": "Queue write FAILED — message not saved",
                        "state_changed": False,
                        "state": None,
                        "preserve_input": True,
                    },
                )
            effect = "Queued locally — not sent to Hermes or Telegram"
            replies.append(
                append_message(
                    channel,
                    "system",
                    (
                        f"{effect}.\n"
                        f"Outbox file: {out_path.name}\n"
                        "Human pastes into Telegram when ready. "
                        "Use Copy outbox in Chat Hall."
                    ),
                    {"kind": "l2_queue"},
                )
            )
        else:
            hist = read_json(chat_path("l1")).get("messages", [])
            llm = optional_l1_llm(content, hist)
            if llm:
                replies.append(append_message(channel, "assistant", llm, {"kind": "llm"}))
                effect = "Saved locally (+ model reply)"
            else:
                effect = "Saved locally"
                replies.append(
                    append_message(
                        channel,
                        "system",
                        (
                            f"{effect}.\n"
                            "• Slash commands update local Castle state only (/help)\n"
                            "• Model replies need XAI_API_KEY in server env (optional)\n"
                            "• L2: use the L2 pane (queues local outbox — not auto-dispatched)"
                        ),
                        {"kind": "local_ack"},
                    )
                )

        return self._send(
            200,
            {
                "user": user_msg,
                "replies": replies,
                "effect": effect,
                "state_changed": state_changed,
                "state": load_state() if state_changed else None,
            },
        )


def main() -> None:
    # Ensure migrated state on disk
    if STATE_PATH.exists():
        save_state(load_state())
    os.chdir(ROOT)
    httpd = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"VCOS Castle → http://{HOST}:{PORT}/")
    print(f"  data: {DATA}")
    print(
        "  LLM: "
        + (
            "optional key present"
            if (os.environ.get("XAI_API_KEY") or os.environ.get("GROK_API_KEY"))
            else "off (no-key local mode)"
        )
    )
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nbye")


if __name__ == "__main__":
    main()
