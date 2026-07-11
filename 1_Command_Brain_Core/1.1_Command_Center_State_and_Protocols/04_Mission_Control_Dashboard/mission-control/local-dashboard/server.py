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
/approval add <item> | <say phrase>
/approval clear <id>
/park add <item>
/priority
/note <text>
/safar blocker <text>

Effect: Updated local Castle state only.
L1 free text: Saved locally.
L2 free text: Queued locally — not sent to Hermes or Telegram.
Legacy /approval done is not supported — use /approval clear.
"""


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
            out_path = append_l2_outbox(content)
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
