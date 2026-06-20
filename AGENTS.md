# VCOS HQ Agent Instructions

You are operating inside VCOS Headquarters, the command brain for cross-client and multi-agent work.

## Mandatory Fast Path

Before executing any task, read these files in order:

1. `1_Command_Brain_Core/1.2_Headquarters_Memory/ubiquitous_language.md`
2. `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/state.md`
3. `1_Command_Brain_Core/1.2_Headquarters_Memory/active-context.md`
4. `1_Command_Brain_Core/1.2_Headquarters_Memory/key-workspaces.md`

Then route the task through the smallest relevant interface. If the task belongs to a domain, read only that domain's `README.md` before deciding whether deeper context is needed.

## Office Hours Fast Path

When the human says `office hours`, `GBrain office hours`, `grill this plan`, `dual-laptop Hermes`, `7pm brief setup`, or `NeuralSync intern activation`:

1. Read `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/session-briefs/README.md` (router — do not search the laptop).
2. Open only the matched subject file from the router table.
3. For dual-laptop Hermes work, read in order:
   - `session-briefs/dual-laptop-hermes/plan.md`
   - `session-briefs/gbrain-office-hours-dual-laptop-hermes-2026-06-19.md` (latest OH critique)
4. Run `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/candidates/gbrain-office-hours/SKILL.md` or gstack `/office-hours` on the subject plan.
5. Save new critique packets under `session-briefs/` and update the router README latest-files table.

Do not start with repo-wide grep or filesystem search for office hours artifacts.

ClickUp routing rule: whenever ClickUp is discussed, first reference the AgentOSync space view at `https://app.clickup.com/9017760195/v/s/90175689274`. The main team async activity folders are:

- `https://app.clickup.com/9017760195/v/f/90178817003/90175689274`
- `https://app.clickup.com/9017760195/v/f/90178817004/90175689274`

## Boot Contract

Every agent session must start by answering internally:

- What is the requested outcome?
- Which command room or domain owns it?
- What is the smallest context file needed next?
- Does this action require human approval?
- Where should outputs be saved or linked?

Do not start with broad repo scans. Do not load legacy `5_Legacy_Reference_Archive/5.1_Legacy_Reference_Singular/` or `5_Legacy_Reference_Archive/5.2_Legacy_References_Plural/` folders unless the fast path points there.

When spawning an Agent Team, establish strict file ownership before work begins:

- Sentinel owns orchestration, task routing, approvals, and handoffs.
- Builder owns implementation files inside the active domain or project implementation folder.
- Skeptic/Reviewer owns QA, test plans, review notes, and adversarial findings.
- Documenter owns README, SOP, and handoff docs only when explicitly assigned.

Teammates must communicate handoffs through agent messages, ClickUp comments, or designated handoff notes. They must not edit shared files outside their assigned ownership without explicit coordination.

## Arsenal — Swiss Army Knife

The Arsenal at `6_Arsenal/` is the personal curated resource library. Every gem, repo, tool, framework, API, and prompt pack the human has hunted lives there.

When the human says "what do I have for X", "arsenal query:", "Swiss Army Knife for X", or "check my arsenal":
1. Read `6_Arsenal/arsenal-index.md`.
2. Filter by `problem-tags` matching the stated problem.
3. Return a ranked shortlist (most relevant first): name, type, URL, one sentence on why it fits.
4. If nothing matches, say so — never invent entries.

When the human says "add gem: [URL/name] — [description]":
1. Confirm: name, type, URL, problem-it-solves, at least two `problem-tags`.
2. Append a row to `6_Arsenal/arsenal-index.md`.
3. Confirm the addition.

Arsenal entries that get 3+ active uses should be flagged as skill candidates in `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/vcos-task-skill-map.md`.

## Context Discipline

- Prefer fast-path files over broad folder scans.
- Load domain `README.md` files before reading domain `implementation/` folders.
- Do not read raw references, exports, logs, or scraped data unless the task explicitly needs them.
- Keep raw tool output out of durable memory. Summarize decisions, blockers, and next actions only.
- Use sub-agents or isolated execution for large builds, audits, scraping, or broad searches when available.
- Route raw tool outputs, API responses, web scraping, large terminal logs, and browser snapshots through Context Mode when available.
- If Context Mode is unavailable, manually compress raw output before bringing it into the main session. Keep only facts, decisions, errors, IDs, links, and next actions.
- When a task produces a repeated failure, repeated correction, or reusable win, route it through `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/recursive-self-improvement-loop.md` instead of leaving the learning in chat history.
- For persistent agent surfaces (Hermes Desktop + SuperGrok profiles): seed memory once with fast-path files + ubiquitous language + state summaries + decisions (brain-dump + "you are the VCOS persistent agent following AGENTS.md discipline"). Use dedicated slim sessions per project/lane. Prune skills. Give explicit feedback early so it self-improves. See hermes-supergrok-vcos-playbook.md. Never feed raw noisy logs or client data unless approved.

## GSD State Machine

For headquarters-level work:

- `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/project.md` is the vision.
- `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/requirements.md` is the hard spec.
- `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/state.md` is the live decision and blocker file.
- `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/roadmap.md` is the progress and sequencing file.

Load only the state file required for the task.

## Deep Module Rule

Domains are deep modules:

- `2_Domain_Packs/<domain>/README.md` is the interface.
- `2_Domain_Packs/<domain>/implementation/` is hidden by default.
- Read implementation files only when the current task explicitly requires deeper context.

## Never Repeat A Bug

When a human, Codex, Claude, or review process catches a repeated mistake:

1. Add a negative constraint to this file or the relevant domain `README.md`.
2. Add the decision to `1_Command_Brain_Core/1.2_Headquarters_Memory/decisions.md`.
3. Add any active blocker to `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/state.md`.

## Browser And Session Safety

**2026-06-19 incident:** Running `gstack/bin/chrome-cdp` force-quit Chrome, symlinked the real profile, and launched a second instance — user was logged out across browsers.

**Never do without explicit human approval:**

- Run `gstack/bin/chrome-cdp` or any script that quits, force-kills, or relaunches the user's default browser.
- `pkill` / `killall` / `osascript quit` against Chrome, Safari, Arc, Brave, or Edge.
- Symlink or copy the user's real browser profile (`~/Library/Application Support/Google/Chrome`, etc.) for agent control.
- Cookie-import or CDP attach flows that close the user's active browser session.

**Note:** `chrome-cdp` has no `--help`. Any first argument is treated as a port; a mistaken invocation still runs the destructive quit/launch flow.

**When the human says "use my browser" or "I'm already logged in":**

- Interpret as **use the same authenticated account**, not **hijack the browser process**.
- Prefer provider CLI auth (`higgsfield auth login`) or MCP OAuth the human completes (`/mcps` → authenticate).
- Do not attach to, quit, or restart the human's live browser to "reuse" a session.

**Higgsfield approved paths:** `higgsfield auth login` + `higgsfield generate create`, Grok MCP OAuth on `https://mcp.higgsfield.ai/mcp`, or human generates in the UI. See `3_Project_Workspaces/3.1_AgentOSync_Revenue_Pipeline/03_gtm_campaigns/higgsfield/browser-session-incident-2026-06-19.md`.

Before a domain implementation is submitted for Gate 3 Human Approval, trigger an adversarial review:

- Prefer Codex adversarial review when available.
- Use Claude `/review` for normal implementation review.
- Use `/ultra review` or equivalent multi-agent review for massive architecture changes, production-sensitive changes, auth, payments, databases, or irreversible workflows.

If review finds an error:

1. Fix the issue.
2. Log the root cause in `1_Command_Brain_Core/1.2_Headquarters_Memory/decisions.md`.
3. Add a prevention rule to the relevant domain `README.md` or this file.
4. Re-run the review gate before human approval.

## Human Approval Gates

Agents may draft, analyze, summarize, and prepare outputs. Agents must stop for explicit human approval before:

- Sending external email, SMS, WhatsApp, Slack, Telegram, or client-facing messages.
- Publishing content, ads, landing pages, posts, videos, or public assets.
- Updating or deleting CRM/customer data.
- Spending money, increasing API/ad budget, or deploying capital.
- Making destructive repo, filesystem, database, or production changes.
- Presenting final client-facing strategy, pricing, or proposal terms.

Default mode is Draft-Only until approval is recorded in ClickUp, Slack/Telegram, or the active thread.

## Cadence Hooks

The Sentinel may use Claude Code loops, Hermes/OpenClaw cron jobs (via Desktop or CLI), or scheduled automations to establish a heartbeat.

Hermes Agent + SuperGrok (OAuth) with Hermes Desktop is the preferred persistent runtime for always-on memory, multi-session context hygiene, role-specific profiles (skills + soul.md + memories), artifacts (centralized assets), visible crons, and messaging gateways (Telegram/Slack/Signal for phone reach and approval surfaces). See `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/hermes-supergrok-vcos-playbook.md` for VCOS-specific profiles, memory seeding (ubiquitous language + state + decisions), adapted routines (scanner, briefs, content-intel), phase gates (starts Phase 0 read-only), and cost hygiene. Desktop sessions/folders + profile switching are superior to mono-thread chat apps for preventing context rot and cost bloat.

Default daily heartbeat:

- Time: 8:00 AM America/Toronto.
- Read `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/state.md`.
- Read `1_Command_Brain_Core/1.2_Headquarters_Memory/active-context.md`.
- Fetch active ClickUp blockers when connector access is available.
- Output a Daily Briefing to the configured human review surface: Slack, Telegram, ClickUp, or current thread.

Daily Briefing must include:

- Active outcomes.
- Blockers.
- Human decisions needed.
- Agent-executable next actions.
- Approval requests waiting on the human.

## VCOS vs Domain Packs

VCOS HQ is the brain. Domain packs are limbs.

- Strategy, memory, shared protocols, ClickUp/Drive routing, and reusable skill policy stay in VCOS HQ.
- Travel-specific execution belongs in `2_Domain_Packs/2.2_Travel_Domain_Pack/` and `gstack-Travel`.
- Client-specific files stay in Drive and are linked from ClickUp tasks.

## First Commercial Wedge

The first paid product wedge is `Employee 01: Front Desk` for dealerships.

Primary workflow:

- Sunday Ghost Town missed-call recovery and test-drive booking.
- Solve after-hours/weekend lead loss.
- Use dealership domain pack first.
- Human approval is required before external communications or CRM mutation until the workflow is explicitly trusted by the client.

## Skill Governance

Read `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/skill-leverage-stack.md` before installing or adopting new Claude/gstack skills.

Default order:

1. Skill Creator
2. Review / Ultra Review
3. Context Mode
4. Superpowers
5. Front-end Design
6. GSD for larger builds
7. ClaudeMem only if it complements existing memory

Do not install every skill everywhere. Adopt a skill only when it reduces time, cost, mistakes, or context load.
