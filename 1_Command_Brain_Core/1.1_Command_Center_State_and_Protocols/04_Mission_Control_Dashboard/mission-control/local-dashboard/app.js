/* VCOS Co-Founder Castle OS — Phase 1 UI
   PRD VCOS-MC-CASTLE-003 v1.3
*/

const ROOMS = [
  { id: "chat", label: "Chat Hall", section: "Core" },
  { id: "command", label: "Command", section: "Core" },
  { id: "l2_wing", label: "L2 Wing", section: "Core" },
  { id: "amax", label: "AMAX Tower", section: "Lanes" },
  { id: "content", label: "Content Studio", section: "Lanes" },
  { id: "safar", label: "Safar Gate", section: "Lanes" },
  { id: "fde", label: "FDE", section: "Lanes" },
  { id: "ship", label: "Ship Dock", section: "Ops" },
  { id: "approvals", label: "Approval Gate", section: "Ops" },
  { id: "obsidian", label: "Obsidian Vault", section: "Brain" },
  { id: "jarvis", label: "Jarvis Bay", section: "Brain" },
  { id: "cadence", label: "Cadence", section: "System" },
  { id: "blueprints", label: "Blueprints", section: "System", secondary: true },
];

let state = null;
let apiMode = false;
let activeRoom = "chat"; // hard default
let chatCache = { l1: null, l2: null };
let drawerOpen = false;

const $ = (s) => document.querySelector(s);

function toast(msg) {
  const el = $("#toast");
  el.textContent = msg;
  el.classList.add("show");
  setTimeout(() => el.classList.remove("show"), 1800);
}

async function copyText(text) {
  try {
    await navigator.clipboard.writeText(text);
    toast("Copied");
  } catch {
    toast("Copy failed — select manually");
  }
}

function esc(s) {
  return String(s ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function sayPhrase(a) {
  return a.say_phrase || a.say || "";
}

function shipReadiness(s) {
  return s.readiness || s.status || "DRAFT";
}

function shipApproval(s) {
  const a = s.approval;
  if (a === "none" || a === "human") return a;
  if (!a || a === "none") return "none";
  return "human";
}

/* ——— Shell ——— */
function renderMap() {
  const map = $("#castle-map");
  let html = `<button type="button" class="drawer-toggle" id="drawer-toggle" aria-expanded="${drawerOpen}">
    Rooms · ${esc(ROOMS.find((r) => r.id === activeRoom)?.label || activeRoom)}
  </button>`;
  html += `<div class="map-title">Castle Map</div>`;
  let last = "";
  for (const r of ROOMS) {
    if (r.section !== last) {
      last = r.section;
      html += `<div class="map-title" style="padding-top:12px">${esc(last)}</div>`;
    }
    let num = "";
    if (r.id === "approvals" && state)
      num = state.approvals_queue?.filter((a) => a.status !== "done" && a.status !== "cleared").length ?? "";
    if (r.id === "ship" && state) num = state.ships?.length ?? "";
    html += `<button type="button" class="room-btn ${activeRoom === r.id ? "active" : ""} ${
      r.secondary ? "secondary" : ""
    }" data-room="${r.id}">
      ${esc(r.label)}${num !== "" ? `<span class="num">${num}</span>` : ""}
    </button>`;
  }
  map.innerHTML = html;
  map.classList.toggle("collapsed", !drawerOpen && window.innerWidth <= 900);
  map.querySelectorAll("[data-room]").forEach((btn) => {
    btn.addEventListener("click", () => {
      activeRoom = btn.dataset.room;
      drawerOpen = false;
      render();
    });
  });
  $("#drawer-toggle")?.addEventListener("click", () => {
    drawerOpen = !drawerOpen;
    renderMap();
  });
}

function renderCmdStrip() {
  const t = state?.tonight_chunk || {};
  const l2 = state?.l2 || {};
  $("#cmd-strip").innerHTML = `
    <span class="label">Tonight</span>
    <span class="chunk"><strong>${esc(t.lane || "—")}</strong> · ${esc(t.task || "Set via /tonight")}</span>
    <span class="meta">done: ${esc(t.done_means || "—")} · L2: ${esc(l2.status || "unknown")} · ${esc(
      l2.model || "?"
    )}</span>
  `;
}

function renderTop() {
  $("#version-label").textContent = `v${state?.version || "?"} · ${state?.data_freshness || ""} · ${
    apiMode ? "api" : "static"
  }`;
  const dot = $("#fresh-dot");
  const text = $("#fresh-text");
  if (!apiMode) {
    dot.className = "dot bad";
    text.textContent = "API down — run python3 server.py";
  } else {
    dot.className = "dot ok";
    text.textContent = `API up · updated ${state?.updated_at || "—"} · localhost only`;
  }
}

function panel(title, sub, body) {
  return `<div class="panel-header"><h1>${esc(title)}</h1><p>${esc(sub)}</p></div>${body}`;
}

/* ——— Rooms ——— */
function msgHtml(m) {
  return `<div class="msg ${esc(m.role || "system")}">
    <div class="msg-meta">${esc(m.role)} · ${esc(m.ts || "")}</div>
    <div class="msg-body">${esc(m.content || "")}</div>
  </div>`;
}

function chatPane(ch, title, sub, effect, messages, extraClass) {
  const body = (messages || []).map(msgHtml).join("") || `<p class="mono">No messages yet.</p>`;
  return `
    <div class="chat-pane ${extraClass}" data-channel="${ch}">
      <div class="chat-head">
        <div>
          <h2>${esc(title)}</h2>
          <p>${esc(sub)}</p>
          <div class="effect-tag">Send effect: ${esc(effect)}</div>
        </div>
        <span class="badge ${ch}">${ch.toUpperCase()}</span>
      </div>
      <div class="chat-log" id="chat-log-${ch}">${body}</div>
      <div class="chat-compose">
        <textarea id="chat-input-${ch}" rows="3" placeholder="${
          ch === "l1" ? "L1 · Main Mac — try /help or free text" : "L2 · queue for human Telegram paste"
        }" aria-label="${ch} compose"></textarea>
        <div class="btn-row">
          <button class="btn primary" type="button" data-send="${ch}">${
            ch === "l2" ? "Queue locally" : "Send"
          }</button>
          <button class="btn" type="button" data-help="${ch}">/help</button>
        </div>
        <p class="mono">Ctrl/Cmd+Enter to submit · Enter = new line</p>
      </div>
    </div>`;
}

function renderChat() {
  if (!apiMode) {
    return panel(
      "Chat Hall",
      "Server required",
      `<div class="card"><div class="prompt-box">cd local-dashboard
python3 server.py
# http://127.0.0.1:8765/</div></div>`
    );
  }
  const l1m = chatCache.l1?.messages || [];
  const l2m = chatCache.l2?.messages || [];
  return panel(
    "Chat Hall",
    "Separate machines. Local effects only unless human pastes outbox into Telegram.",
    `
    <div class="chat-grid">
      ${chatPane(
        "l1",
        "Main Mac · Sentinel (L1)",
        "This laptop · local OS brain",
        "Saved locally (optional model if key set)",
        l1m,
        "l1"
      )}
      ${chatPane(
        "l2",
        "L2 Co-Founder (Windows)",
        "Hermes via human Telegram paste",
        "Queued locally — not sent to Hermes or Telegram",
        l2m,
        "l2"
      )}
    </div>
    <div class="card" style="margin-top:12px">
      <h2>L2 local outbox</h2>
      <p class="mono">data/outbox/l2-telegram-queue.md — human copies into Telegram</p>
      <div class="btn-row">
        <button class="btn primary" type="button" id="btn-copy-outbox">Copy full outbox</button>
        <button class="btn" type="button" id="btn-refresh-chats">Refresh chats</button>
      </div>
      <div class="prompt-box" id="outbox-preview" style="max-height:100px">…</div>
    </div>`
  );
}

function renderCommand() {
  const t = state.tonight_chunk || {};
  const pri = (state.active_priority_order || []).map((p, i) => `<li>P${i + 1} · ${esc(p)}</li>`).join("");
  const park = (state.parked || []).map((p) => `<li>${esc(p)}</li>`).join("");
  return panel(
    "Command",
    "Tonight's one chunk. ClickUp remains execution truth.",
    `<div class="grid grid-2">
      <div class="card">
        <h2>Tonight chunk</h2>
        <p><strong>${esc(t.lane || "—")}</strong></p>
        <p>${esc(t.task || "")}</p>
        <p class="mono">done_means: ${esc(t.done_means || "")}</p>
        <p class="mono">tool: ${esc(t.primary_tool || "")}</p>
        <h2 style="margin-top:12px">Do not open</h2>
        <ul class="list gate-list">${(t.do_not_open || []).map((x) => `<li>${esc(x)}</li>`).join("")}</ul>
        <div class="btn-row">
          <button class="btn primary" type="button" data-copy="${esc(
            `/tonight ${t.lane || "lane"} | ${t.task || "task"} | ${t.done_means || "done"}`
          )}">Copy /tonight form</button>
        </div>
      </div>
      <div class="stack">
        <div class="card"><h2>Priorities</h2><ul class="list">${pri}</ul></div>
        <div class="card"><h2>Parked</h2><ul class="list">${park}</ul></div>
        <div class="card"><h2>Slash help</h2>
          <div class="prompt-box">/tonight a | b | c
/ship add lane | title | path
/approval clear ap-001
/help</div>
          <p class="effect-tag">Slash effects: Updated local Castle state only</p>
        </div>
      </div>
    </div>`
  );
}

function renderL2Wing() {
  const l = state.l2 || {};
  const j = state.jarvis || {};
  return panel(
    "L2 Wing",
    "Read-only mirror of human-observed co-founder facts. MCP: none unless stated.",
    `<div class="card">
      <table>
        <tr><th>Field</th><th>Value</th></tr>
        <tr><td>Name</td><td>${esc(l.name)}</td></tr>
        <tr><td>Status</td><td><span class="badge warn">${esc(l.status || "unknown")}</span></td></tr>
        <tr><td>Profile</td><td class="mono">${esc(l.profile || "—")}</td></tr>
        <tr><td>Model</td><td class="mono">${esc(l.model || "—")}</td></tr>
        <tr><td>Gateway</td><td>${esc(l.gateway || "unknown")}</td></tr>
        <tr><td>Localhost dashboard on L2</td><td>${
          l.dashboard_localhost ? "yes" : '<span class="badge bad">no</span>'
        }</td></tr>
        <tr><td>MCP</td><td>${
          l.mcp_configured ? "configured" : '<span class="badge">none</span>'
        }</td></tr>
        <tr><td>Handoffs root</td><td class="mono">${esc(l.handoffs_root || "Set me")}</td></tr>
        <tr><td>Jarvis source</td><td class="mono">${esc(j.source || "—")}</td></tr>
        <tr><td>Last checked</td><td class="mono">${esc(j.last_checked || "—")}</td></tr>
      </table>
      <p class="effect-tag" style="margin-top:12px">L2 not auto-dispatched from this UI · outbox-first handoff</p>
    </div>`
  );
}

function renderLane(key) {
  const lane = state.lanes?.[key] || state.lanes?.[key === "content" ? "content_intel" : key];
  if (!lane) return panel(key, "Not available in Phase 1", `<div class="card mono">Set me in state.json lanes</div>`);
  const next = (lane.next_actions || []).map((x) => `<li>${esc(x)}</li>`).join("");
  const gates = (lane.gates || []).map((x) => `<li>${esc(x)}</li>`).join("");
  const blockers = (lane.blockers || []).map((x) => `<li>${esc(x)}</li>`).join("");
  const mission = `MISSION: ${lane.goal || lane.name}\nLANE: ${lane.name}\nDONE MEANS: (set path)\nFORBIDDEN: publish, QBO write, CRM write, spend`;
  return panel(
    lane.name || key,
    `Priority ${lane.priority ?? "—"} · ${lane.status || ""} · read-only Phase 1`,
    `<div class="grid grid-2">
      <div class="stack">
        <div class="card"><h2>Goal</h2><p>${esc(lane.goal || "")}</p>
          <p class="mono">folder: ${esc(lane.handoff_folder || "—")}</p>
          <div class="btn-row"><button class="btn primary" type="button" data-copy="${esc(
            mission
          )}">Copy mission draft</button></div>
          <p class="effect-tag">Copied — human still dispatches via Chat Hall / Telegram</p>
        </div>
        <div class="card"><h2>Next actions</h2><ul class="list ok-list">${next || "<li>—</li>"}</ul></div>
      </div>
      <div class="stack">
        <div class="card"><h2>Blockers</h2><ul class="list">${blockers || "<li>None listed</li>"}</ul></div>
        <div class="card"><h2>Gates</h2><ul class="list gate-list">${gates || "<li>Draft-only default</li>"}</ul></div>
      </div>
    </div>`
  );
}

function renderShip() {
  const rows = (state.ships || [])
    .map(
      (s) => `<tr>
      <td>${esc(s.lane)}</td>
      <td>${esc(s.title)}</td>
      <td class="mono">${esc(s.path)}</td>
      <td><span class="badge">${esc(shipReadiness(s))}</span></td>
      <td>${esc(shipApproval(s))}</td>
    </tr>`
    )
    .join("");
  return panel(
    "Ship Dock",
    "Artifacts with paths. Chat text alone is not a ship.",
    `<div class="card">
      <table>
        <tr><th>Lane</th><th>Title</th><th>Path</th><th>Readiness</th><th>Approval</th></tr>
        ${rows || "<tr><td colspan=5 class=mono>No ships yet — /ship add lane | title | path</td></tr>"}
      </table>
      <p class="effect-tag" style="margin-top:10px">Records are local Castle state only</p>
    </div>`
  );
}

function renderApprovals() {
  const rows = (state.approvals_queue || [])
    .map(
      (a) => `<tr>
      <td class="mono">${esc(a.id)}</td>
      <td>${esc(a.item)}</td>
      <td class="mono">${esc(sayPhrase(a))}</td>
      <td><button class="btn" type="button" data-copy-phrase="${esc(
        sayPhrase(a)
      )}">Copy phrase</button></td>
    </tr>`
    )
    .join("");
  return panel(
    "Approval Gate",
    "Copy phrase for human use. This UI never executes external sign-off.",
    `<div class="card">
      <table>
        <tr><th>ID</th><th>Item</th><th>Say phrase</th><th></th></tr>
        ${rows || "<tr><td colspan=4>Empty queue</td></tr>"}
      </table>
      <p class="effect-tag" style="margin-top:10px">Copied — human sign-off still required · /approval clear only clears local display</p>
    </div>
    <div class="card" style="margin-top:12px">
      <h2>Blocked / human-only</h2>
      <ul class="list gate-list">
        <li>Publish social / LinkedIn / ads</li>
        <li>CRM or QBO mutation</li>
        <li>Client outbound messages</li>
        <li>Spend / deploy / production destroy</li>
      </ul>
    </div>`
  );
}

function renderObsidian() {
  const o = state.obsidian || {};
  const fp = (o.fast_path || []).map((p) => `<li class="mono">${esc(p)}</li>`).join("");
  return panel(
    "Obsidian Vault",
    "Second brain pointers. One vault. Progressive load.",
    `<div class="card">
      <table>
        <tr><th>Field</th><th>Value</th></tr>
        <tr><td>Vault path</td><td class="mono">${esc(o.vault_path || "Set me")}</td></tr>
        <tr><td>Home note</td><td class="mono">${esc(o.home_note || "Home.md")}</td></tr>
      </table>
      <h2 style="margin-top:12px">Fast path</h2>
      <ul class="list">${fp || "<li class=mono>Set me</li>"}</ul>
    </div>`
  );
}

function renderJarvis() {
  const j = state.jarvis || {};
  const l = state.l2 || {};
  const agents = (j.agents || []).map((a) => `<li>${esc(a)}</li>`).join("");
  const crons = (j.cron_jobs || []).map((c) => `<li>${esc(c)}</li>`).join("");
  return panel(
    "Jarvis Bay",
    "Agent registry (local mirror). Not a remote-control plane.",
    `<div class="card">
      <table>
        <tr><th>Field</th><th>Value</th></tr>
        <tr><td>Gateway note</td><td>${esc(j.gateway_note || l.gateway || "unknown")}</td></tr>
        <tr><td>L2 model</td><td class="mono">${esc(l.model || "—")}</td></tr>
        <tr><td>L2 profile</td><td class="mono">${esc(l.profile || "—")}</td></tr>
        <tr><td>MCP</td><td>${l.mcp_configured ? "configured" : "none"}</td></tr>
        <tr><td>Source</td><td class="mono">${esc(j.source || "—")}</td></tr>
        <tr><td>Last checked</td><td class="mono">${esc(j.last_checked || "—")}</td></tr>
      </table>
      <h2 style="margin-top:12px">Agents</h2>
      <ul class="list">${agents || "<li class=mono>none listed</li>"}</ul>
      <h2 style="margin-top:12px">Cron labels</h2>
      <ul class="list">${crons || "<li class=mono>none listed</li>"}</ul>
      <p class="effect-tag">L2 not auto-dispatched · MCP: none unless human-observed</p>
    </div>`
  );
}

function renderCadence() {
  return panel(
    "Cadence",
    "Draft-only loops. Hard caps. No background external actions.",
    `<div class="grid grid-2">
      <div class="card"><h2>Policy</h2>
        <ul class="list ok-list">
          <li>One mission per session when possible</li>
          <li>Stop condition + hard cap required</li>
          <li>Outputs land as local files / outbox</li>
          <li>Human sign-off before external use</li>
        </ul>
      </div>
      <div class="card"><h2>Suggested loops</h2>
        <ul class="list">
          <li>Morning: PING L2 (Telegram) · set /tonight</li>
          <li>Ship block: one MISSION with path</li>
          <li>Bookend: HANDOFF packet · /note</li>
        </ul>
      </div>
    </div>`
  );
}

function renderBlueprints() {
  const sources = (state.sources || [])
    .map((s) => `<tr><td>${esc(s.name)}</td><td class="mono">${esc(s.path)}</td></tr>`)
    .join("");
  const saved = localStorage.getItem("vcos_mc_critique") || "";
  return panel(
    "Blueprints",
    "Secondary room. Critique + sources. Never the homepage.",
    `<div class="grid grid-2">
      <div class="card">
        <h2>Sources</h2>
        <table><tr><th>Name</th><th>Path</th></tr>${sources}</table>
        <p class="mono" style="margin-top:8px">PRD: mission-control/COFOUNDER-CASTLE-OS-PRD.md</p>
      </div>
      <div class="card">
        <h2>Critique notes (browser localStorage)</h2>
        <textarea id="critique-box" class="prompt-box" style="min-height:120px;width:100%">${esc(
          saved
        )}</textarea>
        <div class="btn-row">
          <button class="btn primary" type="button" id="btn-save-critique">Save notes</button>
          <button class="btn" type="button" id="btn-copy-critique">Copy notes</button>
        </div>
      </div>
    </div>`
  );
}

function renderRoom() {
  const map = {
    chat: renderChat,
    command: renderCommand,
    l2_wing: renderL2Wing,
    amax: () => renderLane("amax"),
    content: () => renderLane("content"),
    safar: () => renderLane("safar"),
    fde: () => renderLane("fde"),
    ship: renderShip,
    approvals: renderApprovals,
    obsidian: renderObsidian,
    jarvis: renderJarvis,
    cadence: renderCadence,
    blueprints: renderBlueprints,
  };
  return (map[activeRoom] || renderChat)();
}

async function loadChats() {
  if (!apiMode) return null;
  const [l1, l2, outbox] = await Promise.all([
    fetch("/api/chat/l1").then((r) => r.json()),
    fetch("/api/chat/l2").then((r) => r.json()),
    fetch("/api/outbox/l2")
      .then((r) => r.json())
      .catch(() => ({ markdown: "" })),
  ]);
  chatCache.l1 = l1;
  chatCache.l2 = l2;
  return outbox;
}

async function sendChat(channel) {
  const input = $(`#chat-input-${channel}`);
  const content = (input?.value || "").trim();
  if (!content) return;
  input.value = "";
  input.disabled = true;
  try {
    const res = await fetch("/api/chat/send", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ channel, content }),
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || "send failed");
    if (data.state) state = data.state;
    await loadChats();
    render();
    toast(data.effect || "Saved locally");
  } catch (e) {
    toast(String(e.message || e));
    if (input) input.value = content;
  } finally {
    input.disabled = false;
    input?.focus();
  }
}

function wireMain() {
  document.querySelectorAll("[data-copy]").forEach((b) =>
    b.addEventListener("click", () => copyText(b.getAttribute("data-copy")))
  );
  document.querySelectorAll("[data-copy-phrase]").forEach((b) =>
    b.addEventListener("click", () => {
      copyText(b.getAttribute("data-copy-phrase"));
      toast("Copied — human sign-off still required");
    })
  );
  document.querySelectorAll("[data-send]").forEach((b) =>
    b.addEventListener("click", () => sendChat(b.getAttribute("data-send")))
  );
  document.querySelectorAll("[data-help]").forEach((b) =>
    b.addEventListener("click", () => {
      const ch = b.getAttribute("data-help");
      const input = $(`#chat-input-${ch}`);
      if (input) {
        input.value = "/help";
        input.focus();
      }
    })
  );
  ["l1", "l2"].forEach((ch) => {
    const input = $(`#chat-input-${ch}`);
    if (!input) return;
    input.addEventListener("keydown", (e) => {
      if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) {
        e.preventDefault();
        sendChat(ch);
      }
    });
  });
  $("#btn-copy-outbox")?.addEventListener("click", async () => {
    const o = await fetch("/api/outbox/l2").then((r) => r.json());
    await copyText(o.markdown || "");
  });
  $("#btn-refresh-chats")?.addEventListener("click", async () => {
    await loadChats();
    render();
  });
  if ($("#outbox-preview")) {
    fetch("/api/outbox/l2")
      .then((r) => r.json())
      .then((o) => {
        $("#outbox-preview").textContent = o.markdown || "(empty)";
      })
      .catch(() => {});
  }
  $("#btn-save-critique")?.addEventListener("click", () => {
    localStorage.setItem("vcos_mc_critique", $("#critique-box")?.value || "");
    toast("Saved locally (browser)");
  });
  $("#btn-copy-critique")?.addEventListener("click", () =>
    copyText($("#critique-box")?.value || "")
  );
  const log1 = $("#chat-log-l1");
  const log2 = $("#chat-log-l2");
  if (log1) log1.scrollTop = log1.scrollHeight;
  if (log2) log2.scrollTop = log2.scrollHeight;
}

function render() {
  if (!state) return;
  renderTop();
  renderMap();
  renderCmdStrip();
  $("#main").innerHTML = renderRoom();
  wireMain();
}

async function loadState() {
  try {
    const health = await fetch(`/api/health?t=${Date.now()}`);
    if (health.ok) {
      apiMode = true;
      state = await fetch(`/api/state?t=${Date.now()}`).then((r) => r.json());
      await loadChats();
      render();
      return;
    }
  } catch (_) {
    apiMode = false;
  }
  const res = await fetch(`data/state.json?t=${Date.now()}`);
  if (!res.ok) throw new Error("state load failed");
  state = await res.json();
  apiMode = false;
  render();
}

$("#btn-reload")?.addEventListener("click", () =>
  loadState()
    .then(() => toast("Reloaded"))
    .catch((e) => toast(String(e)))
);
$("#btn-copy-tonight")?.addEventListener("click", () => {
  const t = state?.tonight_chunk || {};
  copyText(`LANE: ${t.lane}\nTASK: ${t.task}\nDONE MEANS: ${t.done_means}`);
});

loadState().catch((e) => {
  $("#main").innerHTML = `<div class="card"><h2>Load failed</h2><p class="mono">${esc(
    e.message
  )}</p><p>Run: python3 server.py</p></div>`;
});
