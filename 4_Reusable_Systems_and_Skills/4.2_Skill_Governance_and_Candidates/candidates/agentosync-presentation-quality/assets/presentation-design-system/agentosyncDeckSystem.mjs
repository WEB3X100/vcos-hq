export const AgentOSyncDeckSystem = {
  slide: {
    width: 1280,
    height: 720,
  },
  colors: {
    navy: "#020722",
    panel: "#07142c",
    panel2: "#0a1c36",
    cyan: "#36d7ff",
    blue: "#1d72ff",
    green: "#22e3a1",
    gold: "#f7cf68",
    red: "#ff6b6b",
    white: "#ffffff",
    paper: "#eef7ff",
    muted: "#a9bbca",
    line: "#173555",
  },
  type: {
    display: "Aptos Display",
    body: "Aptos",
    claim: 36,
    sectionClaim: 38,
    bodyLarge: 23,
    panelTitle: 17,
    panelBody: 14,
    table: 13,
    footer: 10,
  },
  spacing: {
    pageX: 58,
    topRule: 8,
    kickerY: 34,
    titleY: 76,
    panelPadX: 16,
    panelPadY: 18,
    minBoxBreathing: 16,
  },
  bannedClientPhrases: [
    "positioning",
    "sales framing",
    "wow moment",
    "recommended close",
    "close on",
    "pitch",
    "conversion",
    "no-brainer",
  ],
};

export function addAgentOSyncBackground(ctx, slide, { title, kicker, page }) {
  const C = AgentOSyncDeckSystem.colors;
  const T = AgentOSyncDeckSystem.type;
  const S = AgentOSyncDeckSystem.spacing;
  ctx.addShape(slide, { x: 0, y: 0, w: ctx.W, h: ctx.H, fill: C.navy, line: ctx.line() });
  ctx.addShape(slide, { x: 0, y: 0, w: ctx.W, h: S.topRule, fill: C.cyan, line: ctx.line() });
  ctx.addText(slide, { name: "kicker-label", text: kicker, x: S.pageX, y: S.kickerY, w: 520, h: 24, size: 12, bold: true, color: C.cyan, valign: "middle" });
  ctx.addText(slide, { text: title, x: S.pageX, y: S.titleY, w: 930, h: 96, size: T.claim, bold: true, color: C.white, typeface: T.display });
  ctx.addText(slide, { text: page, x: 1168, y: 676, w: 54, h: 18, size: T.footer, color: C.muted, align: "right" });
}

export function addAgentOSyncPanel(ctx, slide, { title, body, x, y, w, h, accent, bodySize }) {
  const C = AgentOSyncDeckSystem.colors;
  const T = AgentOSyncDeckSystem.type;
  const S = AgentOSyncDeckSystem.spacing;
  ctx.addShape(slide, { x, y, w, h, fill: C.panel, line: ctx.line(C.line, 1) });
  ctx.addShape(slide, { x, y, w, h: 5, fill: accent || C.cyan, line: ctx.line() });
  ctx.addText(slide, { text: title, x: x + S.panelPadX, y: y + S.panelPadY, w: w - S.panelPadX * 2, h: 28, size: T.panelTitle, bold: true, color: C.white });
  ctx.addText(slide, { text: body, x: x + S.panelPadX, y: y + 54, w: w - S.panelPadX * 2, h: h - 70, size: bodySize || T.panelBody, color: C.muted });
}

export function addStatusChip(ctx, slide, { text, x, y, w, status }) {
  const C = AgentOSyncDeckSystem.colors;
  const fill = status === "safe" ? C.green : status === "review" ? C.gold : status === "risk" ? C.red : C.cyan;
  ctx.addShape(slide, { x, y, w, h: 30, fill, line: ctx.line() });
  ctx.addText(slide, { text, x: x + 8, y: y + 4, w: w - 16, h: 20, size: 12, bold: true, color: C.navy, align: "center", valign: "middle" });
}

export function addSemanticConnector(ctx, slide, { x1, y, x2, color }) {
  const C = AgentOSyncDeckSystem.colors;
  const c = color || C.green;
  ctx.addShape(slide, { x: x1, y, w: x2 - x1, h: 3, fill: c, line: ctx.line() });
  ctx.addShape(slide, { x: x2 - 9, y: y - 5, w: 12, h: 12, fill: c, line: ctx.line() });
}

export function buildClientCtaSteps() {
  return [
    ["1. Pick one workflow", "Choose the smallest workflow worth validating."],
    ["2. Confirm sample data", "Use sanitized vehicles, leads, roles, and approval rules."],
    ["3. Define review points", "Agree what can be drafted, reviewed, or never automated."],
    ["4. Walk the demo", "Run the workflow live and inspect the operating view."],
    ["5. Decide live lane", "Choose the smallest safe lane for real validation."],
  ];
}
