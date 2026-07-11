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

function isMobile() {
  return window.matchMedia("(max-width: 640px)").matches;
}

function roomListHtml(idPrefix) {
  let html = "";
  let last = "";
  for (const r of ROOMS) {
    if (r.section !== last) {
      last = r.section;
      html += `<div class="map-title" style="padding-top:12px">${esc(last)}</div>`;
    }
    let num = "";
    if (r.id === "approvals" && state)
      num =
        state.approvals_queue?.filter((a) => a.status !== "done" && a.status !== "cleared")
          .length ?? "";
    if (r.id === "ship" && state) num = state.ships?.length ?? "";
    html += `<button type="button" class="room-btn ${activeRoom === r.id ? "active" : ""} ${
      r.secondary ? "secondary" : ""
    }" data-room="${r.id}" id="${idPrefix}-${r.id}">
      ${esc(r.label)}${num !== "" ? `<span class="num">${num}</span>` : ""}
    </button>`;
  }
  return html;
}

function closeRoomsDrawer() {
  drawerOpen = false;
  const ov = $("#rooms-overlay");
  if (ov) ov.hidden = true;
  const btn = $("#rooms-open-btn");
  if (btn) btn.setAttribute("aria-expanded", "false");
}

function openRoomsDrawer() {
  drawerOpen = true;
  const ov = $("#rooms-overlay");
  if (ov) ov.hidden = false;
  const btn = $("#rooms-open-btn");
  if (btn) btn.setAttribute("aria-expanded", "true");
  const list = $("#rooms-drawer-list");
  if (list) {
    list.innerHTML = `<div class="map-title">Castle Map</div>` + roomListHtml("drawer");
    list.querySelectorAll("[data-room]").forEach((b) => {
      b.addEventListener("click", () => {
        activeRoom = b.dataset.room;
        closeRoomsDrawer();
        render();
      });
    });
  }
}

/* ——— Shell ——— */
function renderMap() {
  const map = $("#castle-map");
  const label = ROOMS.find((r) => r.id === activeRoom)?.label || activeRoom;
  // Desktop rail (hidden via CSS on ≤640)
  map.innerHTML = `<div class="map-title">Castle Map</div>` + roomListHtml("rail");
  map.querySelectorAll("[data-room]").forEach((btn) => {
    btn.addEventListener("click", () => {
      activeRoom = btn.dataset.room;
      render();
    });
  });

  // Mobile bar
  const bar = $("#mobile-rooms-bar");
  const openBtn = $("#rooms-open-btn");
  if (bar && openBtn) {
    bar.hidden = !isMobile();
    openBtn.textContent = `Rooms · ${label}`;
    openBtn.onclick = () => {
      if (drawerOpen) closeRoomsDrawer();
      else openRoomsDrawer();
    };
  }
  $("#rooms-close-btn") && ($("#rooms-close-btn").onclick = closeRoomsDrawer);
  $("#rooms-backdrop") && ($("#rooms-backdrop").onclick = closeRoomsDrawer);
  if (!isMobile()) closeRoomsDrawer();
  else if (drawerOpen) openRoomsDrawer();
  else closeRoomsDrawer();
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
  const tonightCmd = `/tonight ${t.lane || "lane"} | ${t.task || "task"} | ${t.done_means || "done means"}`;
  return panel(
    "Command",
    "Tonight's one chunk. ClickUp remains execution truth.",
    `<div class="grid grid-2">
      <div class="card">
        <h2>Tonight chunk <button type="button" class="btn" data-prefill="${esc(
          tonightCmd
        )}">Edit</button></h2>
        <p><strong>${esc(t.lane || "—")}</strong></p>
        <p>${esc(t.task || "")}</p>
        <p class="mono">done_means: ${esc(t.done_means || "")}</p>
        <p class="mono">tool: ${esc(t.primary_tool || "")}</p>
        <h2 style="margin-top:12px">Do not open</h2>
        <ul class="list gate-list">${(t.do_not_open || []).map((x) => `<li>${esc(x)}</li>`).join("")}</ul>
      </div>
      <div class="stack">
        <div class="card"><h2>Priorities <button type="button" class="btn" data-prefill="/priority">Edit</button></h2><ul class="list">${pri}</ul></div>
        <div class="card"><h2>Parked <button type="button" class="btn" data-prefill="/park add item">Edit</button></h2><ul class="list">${park}</ul></div>
        <div class="card"><h2>Slash help</h2>
          <div class="prompt-box">/tonight a | b | c
/lane set amax | next_action | value
/ship add lane | title | path
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
  const stale = isStale(j.last_checked, 24);
  const cardClass = stale ? "card stale-border" : "card";
  return panel(
    "L2 Wing",
    "Human-observed co-founder facts only. MCP: none unless stated.",
    `<div class="${cardClass}">
      ${
        stale
          ? `<p class="stale-warn">Stale — re-confirm with human before treating as current.</p>`
          : ""
      }
      <table>
        <tr><th>Field</th><th>Value</th></tr>
        <tr><td>Name</td><td>${esc(l.name)}</td></tr>
        <tr><td>Status</td><td><span class="badge warn">${esc(l.status || "unknown")}</span></td></tr>
        <tr><td>Profile</td><td class="mono">${esc(l.profile || "unknown")}</td></tr>
        <tr><td>Model</td><td class="mono">${esc(l.model || "unknown")}</td></tr>
        <tr><td>Gateway</td><td>${esc(l.gateway || "unknown")}</td></tr>
        <tr><td>Localhost dashboard on L2</td><td>${
          l.dashboard_localhost ? "yes" : '<span class="badge bad">no</span>'
        }</td></tr>
        <tr><td>MCP</td><td>${l.mcp_configured ? "configured" : "none"}</td></tr>
        <tr><td>Handoffs root</td><td class="mono">${esc(l.handoffs_root || "Set me")}</td></tr>
        <tr><td>Last checked</td><td class="mono">${esc(j.last_checked || "unknown")} (${relativeTime(
          j.last_checked
        )})</td></tr>
      </table>
      <p class="effect-tag" style="margin-top:12px">L2 not auto-dispatched from this UI · outbox-first handoff</p>
    </div>`
  );
}

function renderLane(key) {
  const laneKey = key === "content" ? "content_intel" : key;
  const lane = state.lanes?.[laneKey] || state.lanes?.[key];
  if (!lane)
    return panel(key, "Lane unset", `<div class="card mono">unset — use /lane set ${key} | field | value</div>`);
  const nextList = (lane.next_actions || []).map((x) => `<li>${esc(x)}</li>`).join("");
  const gates = (lane.gates || []).map((x) => `<li>${esc(x)}</li>`).join("");
  const blockers = (lane.blockers || []).map((x) => `<li>${esc(x)}</li>`).join("");
  const packet = assembleMissionPacket(laneKey, lane);
  const lastUp = lane.last_update ? `last updated ${relativeTime(lane.last_update)}` : "last updated unset";
  return panel(
    lane.name || key,
    `Priority ${lane.priority ?? "—"} · ${lane.status || ""}`,
    `<div class="grid grid-2">
      <div class="stack">
        <div class="card"><h2>Goal</h2><p>${esc(lane.goal || "")}</p>
          <p class="mono">folder: ${esc(lane.handoff_folder || "unset")}</p>
          <p class="mono">${esc(lastUp)}</p>
          <table style="margin-top:10px">
            <tr><th>Field</th><th>Value</th></tr>
            <tr><td>next_action</td><td>${fieldOrUnset(lane.next_action)}</td></tr>
            <tr><td>gate</td><td>${fieldOrUnset(lane.gate)}</td></tr>
            <tr><td>owner</td><td>${fieldOrUnset(lane.owner)}</td></tr>
            <tr><td>copy_mission_text</td><td>${fieldOrUnset(lane.copy_mission_text)}</td></tr>
          </table>
          <div class="btn-row">
            <button class="btn primary" type="button" data-mission-packet="${esc(packet)}">Copy mission packet</button>
            <button class="btn" type="button" data-prefill="/lane set ${esc(laneKey)} | next_action | ">Edit lane</button>
          </div>
          <p class="effect-tag">Copied — for manual handoff to L2. Not sent.</p>
        </div>
        <div class="card"><h2>Next actions (legacy list)</h2><ul class="list ok-list">${
          nextList || "<li class=unset>unset</li>"
        }</ul></div>
      </div>
      <div class="stack">
        <div class="card"><h2>Blockers</h2><ul class="list">${blockers || "<li class=unset>unset</li>"}</ul></div>
        <div class="card"><h2>Gates</h2><ul class="list gate-list">${
          gates || "<li>Draft-only default</li>"
        }</ul></div>
      </div>
    </div>`
  );
}

function renderShip() {
  const rows = (state.ships || [])
    .map((s) => {
      const r = shipReadiness(s);
      const ap = shipApproval(s);
      const block = s.ready_block
        ? `<div class="ready-block">${esc(s.ready_block)}</div>`
        : "";
      const readyNote =
        r === "READY"
          ? `<div class="ready-note">READY — human sign-off still required before any external use.</div>`
          : "";
      return `<tr>
      <td class="mono">${esc(s.id || "")}</td>
      <td>${esc(s.lane)}</td>
      <td>${esc(s.title)}</td>
      <td class="mono">${esc(s.path)}</td>
      <td><span class="badge">${esc(r)}</span>${block}${readyNote}</td>
      <td>${esc(ap)}</td>
    </tr>`;
    })
    .join("");
  return panel(
    "Ship Dock",
    "Local ship records. READY is display-only.",
    `<div class="card">
      <table>
        <tr><th>ID</th><th>Lane</th><th>Title</th><th>Path</th><th>Readiness</th><th>Approval</th></tr>
        ${rows || "<tr><td colspan=6 class=mono>No ships — /ship add lane | title | path</td></tr>"}
      </table>
      <div class="prompt-box" style="margin-top:10px">/ship update ship-001 | readiness | REVIEW
/ship update ship-001 | readiness | READY
/ship remove ship-001</div>
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
      <td class="mono">${esc(a.last_copied || "")}</td>
      <td><button class="btn" type="button" data-copy-phrase="${esc(sayPhrase(a))}" data-ap-id="${esc(
        a.id
      )}">Copy phrase</button></td>
    </tr>`
    )
    .join("");
  return panel(
    "Approval Gate",
    "Copy phrase for human use. This UI never executes external sign-off.",
    `<div class="card">
      <table>
        <tr><th>ID</th><th>Item</th><th>Say phrase</th><th>Last copied</th><th></th></tr>
        ${rows || "<tr><td colspan=5>Empty queue</td></tr>"}
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
    "Second brain pointers. Never guess vault path.",
    `<div class="card">
      <table>
        <tr><th>Field</th><th>Value</th></tr>
        <tr><td>Vault path</td><td class="mono">${
          o.vault_path ? esc(o.vault_path) : '<span class="unset">Set me</span>'
        }</td></tr>
        <tr><td>Home note</td><td class="mono">${
          o.home_note ? esc(o.home_note) : '<span class="unset">Set me</span>'
        }</td></tr>
      </table>
      <div class="btn-row">
        <button class="btn" type="button" data-prefill="/vault set path ">Edit path</button>
        <button class="btn" type="button" data-prefill="/vault set home ">Edit home</button>
      </div>
      <h2 style="margin-top:12px">Fast path</h2>
      <ul class="list">${fp || "<li class=unset>Set me</li>"}</ul>
    </div>`
  );
}

function renderJarvis() {
  const j = state.jarvis || {};
  const l = state.l2 || {};
  const agents = j.agents || [];
  let agentRows = "";
  if (!agents.length) {
    agentRows = `<tr><td colspan="6" class="unset">unknown</td></tr>`;
  } else {
    for (const a of agents) {
      if (typeof a === "string") {
        agentRows += `<tr><td>${esc(a)}</td><td class="unset">unknown</td><td class="unset">unknown</td><td class="unset">unknown</td><td class="unset">unknown</td><td class="unset">unknown</td></tr>`;
      } else {
        const u = (v) =>
          !v || v === "unknown"
            ? `<span class="unset">unknown</span>`
            : esc(v);
        agentRows += `<tr>
          <td>${esc(a.id || "unknown")}</td>
          <td>${u(a.model)}</td>
          <td>${u(a.channel)}</td>
          <td>${u(a.health)}</td>
          <td>${u(a.source)}</td>
          <td class="mono">${u(a.last_checked)}</td>
        </tr>`;
      }
    }
  }
  const crons = j.cron_jobs || [];
  let cronRows = "";
  if (!crons.length) {
    cronRows = `<tr><td colspan="8" class="unset">unknown</td></tr>`;
  } else {
    for (const c of crons) {
      if (typeof c === "string") {
        cronRows += `<tr><td colspan="8">${esc(c)}</td></tr>`;
      } else {
        cronRows += `<tr>
          <td>${fieldOrUnset(c.owner)}</td>
          <td>${fieldOrUnset(c.purpose)}</td>
          <td class="mono">${fieldOrUnset(c.output_path)}</td>
          <td>${fieldOrUnset(c.next_run)}</td>
          <td>${fieldOrUnset(c.stop_condition)}</td>
          <td>${fieldOrUnset(c.hard_cap)}</td>
          <td>${fieldOrUnset(c.approval_required)}</td>
          <td>${fieldOrUnset(c.status)}</td>
        </tr>`;
      }
    }
  }
  return panel(
    "Jarvis Bay",
    "Display-only registry. Never polls MCP or network health.",
    `<div class="card">
      <table>
        <tr><th>Field</th><th>Value</th></tr>
        <tr><td>Gateway note</td><td>${esc(j.gateway_note || l.gateway || "unknown")}</td></tr>
        <tr><td>MCP</td><td>${l.mcp_configured ? "configured" : "none"}</td></tr>
        <tr><td>Source</td><td class="mono">${esc(j.source || "unknown")}</td></tr>
        <tr><td>Last checked</td><td class="mono">${esc(j.last_checked || "unknown")}</td></tr>
      </table>
      <h2 style="margin-top:12px">Agents</h2>
      <table>
        <tr><th>id</th><th>model</th><th>channel</th><th>health</th><th>source</th><th>last_checked</th></tr>
        ${agentRows}
      </table>
      <div class="btn-row">
        <button class="btn" type="button" data-prefill="/jarvis set agent-id | model | ">Edit agent</button>
      </div>
      <h2 style="margin-top:12px">Cron jobs (read-only)</h2>
      <table>
        <tr><th>owner</th><th>purpose</th><th>output_path</th><th>next_run</th><th>stop</th><th>hard_cap</th><th>approval_required</th><th>status</th></tr>
        ${cronRows}
      </table>
      <p class="effect-tag">Display only — no MCP call, network probe, or scheduling action</p>
    </div>`
  );
}

function renderCadence() {
  return panel(
    "Cadence",
    "Draft-only loops. Observation log is local only.",
    `<div class="grid grid-2">
      <div class="card"><h2>Policy</h2>
        <ul class="list ok-list">
          <li>One mission per session when possible</li>
          <li>Stop condition + hard cap required</li>
          <li>Outputs land as local files / outbox</li>
          <li>Human sign-off before external use</li>
        </ul>
      </div>
      <div class="card"><h2>Recent activity</h2>
        <div id="cadence-activity" class="prompt-box" style="max-height:200px">Loading…</div>
        <p class="effect-tag">Observation only — log cannot trigger actions</p>
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
        <h2>Critique notes</h2>
        <textarea id="critique-box" class="prompt-box" style="min-height:120px;width:100%">${esc(
          saved
        )}</textarea>
        <div class="btn-row">
          <button class="btn primary" type="button" id="btn-save-critique">Save notes</button>
          <button class="btn" type="button" id="btn-copy-critique">Copy notes</button>
        </div>
        <p class="effect-tag">Save writes localStorage + data/critique-notes.md (local only)</p>
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
  const prev = content;
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
    if (data.preserve_input || (data.effect || "").includes("FAILED")) {
      input.value = prev;
      toast(data.effect || "Queue write FAILED — message not saved");
    } else {
      toast(data.effect || "Saved locally");
    }
    if (data.state) state = data.state;
    await loadChats();
    render();
  } catch (e) {
    toast(String(e.message || e));
    if (input) input.value = prev;
  } finally {
    const inp = $(`#chat-input-${channel}`);
    if (inp) {
      inp.disabled = false;
      inp.focus();
    }
  }
}

function fieldOrUnset(v) {
  if (v === undefined || v === null || String(v).trim() === "") {
    return `<span class="unset">unset</span>`;
  }
  return esc(v);
}

function relativeTime(iso) {
  if (!iso) return "";
  const t = Date.parse(iso);
  if (!t) return esc(iso);
  const sec = Math.floor((Date.now() - t) / 1000);
  if (sec < 60) return `${sec}s ago`;
  if (sec < 3600) return `${Math.floor(sec / 60)}m ago`;
  if (sec < 86400) return `${Math.floor(sec / 3600)}h ago`;
  return `${Math.floor(sec / 86400)}d ago`;
}

function isStale(iso, hours = 24) {
  if (!iso) return true;
  const t = Date.parse(iso);
  if (!t) return true;
  return Date.now() - t > hours * 3600 * 1000;
}

function assembleMissionPacket(laneKey, lane) {
  const t = state.tonight_chunk || {};
  const ships = (state.ships || []).filter(
    (s) =>
      String(s.lane || "").toLowerCase().includes(String(laneKey).replace("_intel", "")) ||
      String(s.lane || "").toLowerCase() === String(lane.name || "").toLowerCase()
  );
  const shipLines = ships
    .map((s) => `- ${s.id}: ${s.title} | ${s.path} | ${shipReadiness(s)} | approval=${shipApproval(s)}`)
    .join("\n");
  return (
    `# Mission packet (local draft)\n` +
    `Lane: ${lane.name || laneKey}\n` +
    `Goal: ${lane.goal || ""}\n` +
    `next_action: ${lane.next_action || "unset"}\n` +
    `gate: ${lane.gate || "unset"}\n` +
    `owner: ${lane.owner || "unset"}\n` +
    `copy_mission_text: ${lane.copy_mission_text || "unset"}\n` +
    `last_update: ${lane.last_update || "unset"}\n\n` +
    `## Tonight\n` +
    `lane: ${t.lane || ""}\ntask: ${t.task || ""}\ndone_means: ${t.done_means || ""}\n\n` +
    `## Ships\n${shipLines || "(none)"}\n`
  );
}

function wireMain() {
  document.querySelectorAll("[data-copy]").forEach((b) =>
    b.addEventListener("click", () => copyText(b.getAttribute("data-copy")))
  );
  document.querySelectorAll("[data-mission-packet]").forEach((b) =>
    b.addEventListener("click", async () => {
      await copyText(b.getAttribute("data-mission-packet"));
      toast("Copied — for manual handoff to L2. Not sent.");
    })
  );
  document.querySelectorAll("[data-prefill]").forEach((b) =>
    b.addEventListener("click", () => {
      activeRoom = "chat";
      const cmd = b.getAttribute("data-prefill") || "";
      render();
      const input = $("#chat-input-l1");
      if (input) {
        input.value = cmd;
        input.focus();
      }
    })
  );
  document.querySelectorAll("[data-copy-phrase]").forEach((b) =>
    b.addEventListener("click", async () => {
      await copyText(b.getAttribute("data-copy-phrase"));
      toast("Copied — human sign-off still required");
      const id = b.getAttribute("data-ap-id");
      if (id && apiMode) {
        try {
          const res = await fetch("/api/approval/copied", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ id }),
          });
          const data = await res.json();
          if (data.state) {
            state = data.state;
            if (activeRoom === "approvals") render();
          }
        } catch (_) {}
      }
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
  if ($("#cadence-activity") && apiMode) {
    fetch("/api/cadence/activity")
      .then((r) => r.json())
      .then((o) => {
        $("#cadence-activity").textContent = (o.lines || []).join("\n") || "(empty)";
      })
      .catch(() => {
        $("#cadence-activity").textContent = "(unavailable)";
      });
  }
  $("#btn-save-critique")?.addEventListener("click", async () => {
    const text = $("#critique-box")?.value || "";
    localStorage.setItem("vcos_mc_critique", text);
    if (apiMode) {
      try {
        await fetch("/api/critique/save", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ text }),
        });
        toast("Saved locally (localStorage + data/critique-notes.md)");
      } catch {
        toast("Saved locally (browser only)");
      }
    } else toast("Saved locally (browser)");
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
