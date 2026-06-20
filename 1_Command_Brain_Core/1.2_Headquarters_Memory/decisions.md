# Decisions

## 2026-05-10

- VCOS HQ is the command brain.
- `gstack-Travel` is a specialized travel-agency limb.
- Dealerships are the first paid customer type.
- `Employee 01: Front Desk` is the first packaged client-facing workflow.
- The first dealership workflow is Sunday Ghost Town missed-call recovery and test-drive booking.
- Slack or Telegram is the preferred first mobile approval surface.
- Client-specific installs should use private forks from a master paid template repo.
- Domain packs must use README files as small interfaces.
- Implementation folders are hidden from default context.
- Skill adoption follows the leverage stack, not blanket installs.
- ClaudeMem is not default until evaluated against existing memory.
- Context Mode is preferred first for long-session hygiene if available.
- New repeated mistakes update `AGENTS.md` or the relevant domain README.
- Agent Teams require file ownership boundaries before work begins.
- Domain implementations require adversarial review before Gate 3 Human Approval.
- Context Mode is required for noisy tool outputs when available; otherwise manually compress raw output.
- Daily heartbeat target is 8:00 AM America/Toronto with a human-review Daily Briefing.
- VCOS should adopt the agentic OS pattern as registries plus observability, not as a new duplicate memory hierarchy.
- Dashboard buttons may draft, summarize, analyze, test, or prepare, but approval-gated actions must remain gated before execution.
- VCOS AIOS maturity uses the Four C sequence: context, connections, capabilities, cadence.
- Obsidian should open `/Users/umairkhalid/_VCOS_Headquarters` as the vault instead of creating a separate agency brain.
- GitHub should become the private history, issue, PR, and remote-routine source for VCOS HQ; secrets stay out of the repo.
- `4_Reusable_Systems_and_Skills/4.1_VCOS_Employee_OS_Template` is the reusable deployable employee OS template; VCOS HQ is not the template itself.
- Industry employee repos should be created from a polished generic `4_Reusable_Systems_and_Skills/4.1_VCOS_Employee_OS_Template` foundation, then customized by vertical.

## 2026-05-14

- Open Claw Automation Agency is the production lab for department-specific Mini Intern templates for SMBs.
- Mini Interns stay separate by default across Marketing, Sales, Ops, Reviewer/QA, Agent Infrastructure, Marketplace Skills, and Approval/Decisions.
- Separate agents are preferred over a single mega-agent to preserve least privilege, reduce context bloat, reduce hallucination risk, and create independent review angles.
- Amax is the internal proof lab for Open Claw/AgentOSync workflows; AgentOSync is the market-facing acquisition and proof engine.
- LinkedIn vertical video is the first public funnel channel, with interactive MVP triggers planned after approval.
- Trigger.dev, Modal, Higgsfield, n8n, Firecrawl/SERP, and similar stack components are planned components that must be validated before implementation.
- Kallaway/Nate Herk-inspired methods are internal strategy references only and should not be publicly attributed unless explicitly approved.
- Existing ClickUp task descriptions must be preserved verbatim before structure is added; if safe append is unavailable, add structure as comments or custom-field metadata instead of overwriting bodies.
- Higgsfield media generation skill v3 should operate as an agentic creative system: brief first, model-specific prompt second, Reviewer/QA UAT before spending credits, human approval before external use, and a self-improving loop for rejected renders.
- Media generation skills must use progressive context loading: static image jobs should not load video storyboard references; video jobs may load storyboard patterns; QA jobs should load only QA rubrics.

## 2026-05-15

- NeuralSync Agency ClickUp will be restructured into the six-folder model: `01 · COMMAND`, `02 · BUILD`, `03 · CLIENTS`, `04 · LEADS`, `05 · CONTENT`, `06 · OPS`, plus `00 · ARCHIVE`.
- Airtable is the preservation and rollback layer for the ClickUp restructure, using base name `NeuralSync ClickUp Preservation Snapshot`.
- Live ClickUp restructure is blocked until the Airtable snapshot is imported, reviewed, and approved.
- ClickUp migration must preserve descriptions, comments, tags, subtasks, nested subtasks, checklists, due dates, start dates, assignees, status, priority, time estimates, attachments, links, custom fields, and original task names.
- Migration mode is hybrid/manual-safe: agents can prepare audit, mapping, templates, and verification; high-risk moves happen manually in ClickUp UI after snapshot verification.
- Personal/day-job tasks currently in Q3 Command Center should move to Umair's private ClickUp space after snapshot preservation.
- Canonical ClickUp tags are additive only and must not delete existing tags during migration.
- Every future control room list should have a pinned README/context task so agents can understand list purpose without cold-start guessing.

## 2026-05-19

- VCOS HQ should coach Umair into stronger AI operation over time, not merely complete isolated tasks.
- Claude/Codex guidance should stay lean in `CLAUDE.md` and route deeper power-user behavior to dedicated playbooks.
- VCOS adopts the business-service-broker pattern: business workflows should be requested, provisioned, tracked, and maintained like reusable services.
- Amax Forms + WhatsApp Insights and the barber shop AVAPI demo are first practical examples of the workflow broker pattern.
- Durable prompting patterns should live in `prompting-principles.md`; raw transcripts and long tactic lists should not be loaded into every session.
- Claude Code should be treated as a configurable agent runtime, not merely a chatbot in a terminal.
- Context hygiene is a named VCOS discipline: clear between unrelated tasks, compact around 60 percent context, disconnect unused MCP servers where possible, limit command output, batch related asks, and save decisions instead of conversations.
- Managed-agent platforms should be evaluated as execution layers; proactive scheduling, retries, observability, approvals, and multi-channel routing must be owned explicitly by Trigger.dev, n8n, OpenClaw/Hermes, cron, webhooks, or another orchestrator.

## 2026-05-20

- VCOS will treat every Mini Intern and client workflow as a recursive self-improving loop: sensor, policy, tools, quality gate, output, feedback, learning update, and re-test.
- Project workspace repos stay lean and pointer-first. They declare required HQ skills and Mini Interns in `SKILLS_MANIFEST.md` instead of copying the whole HQ into every client repo.
- Skills are vendored into project/client repos only when the project must run outside VCOS HQ, needs a pinned/client-specific skill version, or deployment cannot access HQ.
- Every material project workspace commit should leave enough state, changed-file context, and next action detail for another CLI/agent to continue from GitHub without full chat history.

## 2026-05-24

- AgentOSync lean revenue execution uses an 8-hour weekly operator budget for Umair: 1 hour per weekday and 3 hours on the weekend.
- Barbershops are the first paid proof wedge for the live callable demo loop because the demo is simple, visual, and easier to close quickly.
- Dealerships remain the second wedge and the longer-term Employee 01 commercial direction, but should wait until barber proof produces inbound or a pilot.
- The primary conversion loop is `Reel -> callable live demo -> DM/booked call -> 15-minute live demo -> paid pilot`.
- GitHub and Hugging Face trust assets remain private/draft until the first paid pilot is live and proof claims are reviewed.
- AgentOSync should not chase GitHub stars, broad virality, or extra workstreams before proving one SMB will pay for the live demo workflow.

## 2026-06-09

- Meetily is added to the VCOS Arsenal as an active-evaluation privacy-first meeting intelligence candidate.
- Use Meetily pointer-first from `6_Arsenal/repos/meetily`; do not vendor it into project workspaces or treat it as a default OS dependency until it proves repeated value.
- Meetily's current supported architecture is the Tauri desktop app under `frontend/` and `frontend/src-tauri`; `backend/` is a legacy archive and should not be used for new VCOS setup.
- Human approval is required before using Meetily for client-sensitive calls, client-facing meeting workflows, or any external meeting automation.

## 2026-06-10

- The older VCOS v4 Chief of Staff mega-prompt should be decomposed, not copied forward: principles become memory, roles become Mini Interns, relationships become Graphify maps, recall becomes GBrain, navigation stays in Obsidian, and execution happens through Codex/Claude/GStack/GSD with approval gates.
- Hermes must begin as a read-only night-shift reviewer and briefing agent. It may not write, send, mutate CRM, publish, spend, delete, deploy, or finalize client-facing strategy until read-only and draft-only phases pass review.
- Real secrets must not be stored in Obsidian, GBrain, Graphify, ClickUp, chat, or git-tracked files. If a credential is pasted into chat, treat it as compromised, rotate it, and store only the fresh value in local `.env`, OS keychain, provider secrets, or deployment platform secrets.

## 2026-06-11

- The new cloned Arsenal repos are activated as pointer-first AI-native company capabilities, not as a raw memory import. Caveman handles concise handoffs, CodeBurn handles token/cost telemetry, Impeccable handles frontend quality gates, Design Extract handles design-language extraction, Career Ops provides the scrape-score-generate-track service pipeline pattern, and Browser Harness handles repeatable browser execution memory.
- VCOS should build "A Company With AI From The Ground Up" through closed loops: sensor, policy, tool, quality gate, output, metric, and learning update.
- GBrain and Graphify should ingest curated activation capsules and seed graphs first. Whole cloned vendor repos stay in `6_Arsenal/repos/` and are read only when a specific workflow needs them.
- QMD is adopted as a pointer-first retrieval router between Obsidian and agents. It may index approved markdown/docs/transcripts collections for local keyword/vector/reranked search, but it does not replace Obsidian, Graphify, GBrain, or HQ Markdown as source of truth.
- AgentOSync GTM is the public proof/revenue engine, Amax/Travel OS is the internal revenue-ops lab, Dealership OS is the Employee 01 commercial wedge, Content Intel is the first Claude Code routine candidate, and Trading Coach remains coach-only with no execution bot, signal service, broker API, or automated trading.
- The Arsenal is a capability map, not an operating system by itself. Revenue-first execution takes priority: Dealership OS delivery proof, Amax internal proof, content-intel draft production, and employee repo/skill packaging after 3+ proven runs.
- Claude Code is the primary builder for VCOS routines. Build `content-intel-routine` first, validate it, then `sprint-closer`, then `skeptic-review`; defer `morning-cockpit` until one focused lane needs a daily brief.
- Before expanding VCOS infrastructure, run the revenue readiness audit. If the last shipped artifact, daily bottleneck, paid-pilot sentence, Amax feedback status, or variance risk is unknown, treat those as blockers rather than adding more tools or docs.
- Barbershop is no longer the primary closing lane. Treat it as a working demo/proof asset until the pricing wall is diagnosed as pricing, packaging, buyer fit, or segment fit.
- Content-intel quality depends on Umair's voice calibration, not automation. The routine must run manually 5 times with approved/rejected feedback before n8n, scheduled scraping, Telegram approvals, or auto-posting are added.
- **2026-06-12:** AgentOSync Distribution Engine (first proof: AMAX Umrah inquiry desk) is the connective tissue for the elite AI-native agency model. Commission-only on closed revenue for clients that already have supply/fulfillment (travel groups, vehicles, etc.). Avoids building the hard parts. Starts with one pilot (AMAX), uses fictional dry runs + review packets + first-principles battle test before real activity. Mandatory integration of recursive self-improvement loop (Sensor-Policy-Tools-QA-Output-Feedback-Learning-Re-test) and Hermes Phase 0 read-only night briefs (ledger + approved signal capsules as sensors, standardized briefs feeding Sentinel and learning updates) for week-by-week compounding. All draft-only until explicit client + Umair approval on attribution, SLA, commission terms, brand, handoff owner, and agreement. Primary ClickUp: AgentOSync view 90175689274. See 3.7_AMAX specs (battle-tested-plan, review-packet, dry-run, ledger) and reusable agentosync-distribution-engine.md. Promote pattern after 3+ tracked qualified pilots.

## 2026-06-13
- Hermes Agent (Nous Research, open-source persistent self-improving agent) + SuperGrok subscription (Grok 4.3 + TTS + Imagine via simple OAuth, available on every tier, no API keys) + Hermes Desktop app is adopted as the primary persistent / multi-channel / cron-capable agent runtime surface for VCOS HQ work and AI-native OS cadence.
- Desktop is strongly preferred over Telegram/CLI/OpenClaw-style experiences for its native sessions (auto context separation, folders, pinning), profile UI (multiple independent agents with distinct skills + soul.md personality + memories + history), artifacts (centralized searchable images/files/links as productized second brain), skills/tools manager (prune 150+ defaults, capture auto-generated skills), visible/editable crons, easy model switching, and sub-agent visualization.
- Profiles are the VCOS implementation of role/model specialization (Mini Intern style but model-first for cost/performance per video expert guidance): one primary SuperGrok-powered "VCOS-Brain" for high-reasoning, planning, Umair-voice content, strategy, Imagine visuals, and complex orchestration; dedicated lower-cost or local-model profiles (e.g. scanner/research, librarian for artifacts/hygiene, builder/coder) for volume or free unlimited work. Avoid over-proliferation of 50 role profiles; use model strengths + one strong generalist where possible.
- Memory seeding and ongoing teaching protocol: brain-dump ubiquitous language, state summaries, active-context, decisions, prompting-principles, and core routines into the primary profile once; treat early weeks as onboarding a new teammate with specific feedback (great/miss) so it self-improves on VCOS discipline (progressive loading, approval gates, Four C, Three M, recursive loop, least privilege, ClickUp routing via AgentOSync view 90175689274).
- Adapted high-leverage use cases: (1) opportunity/challenge scanner cron (Reddit/X + signals) that matches real SMB/dealership/travel problems to VCOS assets (Employee 01 Front Desk, Mini Intern kits, domain packs) and suggests first moves/prototypes — run frequently on cheap/local profile, feed Dealership OS, AgentOSync GTM, Content Intel (draft-only); (2) cron-powered VCOS routines (night brief/sensor, morning brief/heartbeat, content-intel signals, sprint-closer style, skeptic-review) using reverse-prompting technique (full brain dump of VCOS self + "what is the best prompt/cron for this"); (3) Grok Imagine/TTS inside one agent for visuals + voice teammate feel without tool switching; (4) artifacts + librarian profile for asset memory that can be promoted pointer-first to HQ or GBrain/Graphify.
- Strict phase gates (per existing Hermes Phase 0 decision + managed-agent-runtime-evaluation.md): Phase 0 = read-only sensor/brief/draft (current). Phase 1 = internal drafts + handoff packets + ClickUp suggestions (human review required before any external). Later phases require explicit human approval for messaging gateway, limited tool use, or any mutating/external action. Always follow permission rule (always-allow safe reads; ask-first for shell/APIs; human-only for destructive/CRM/send/spend/publish).
- Cost hygiene is mandatory: use slim dedicated sessions per lane (Dealership, Amax, AgentOSync, Content, HQ), right profile for task, prune unused skills in Desktop UI, watch context window, prefer local/cheap for high-frequency scanner work. Context bloat inflates cost/quality risk even under subscription.
- Primary ClickUp for any AgentOSync-related Hermes output remains https://app.clickup.com/9017760195/v/s/90175689274 and its two main async folders. All Hermes-generated artifacts, briefs, and proposals are draft-only until human approval recorded.
- Before any hardware (e.g. DGX Spark for local unlimited inference) spend: prove ROI via value created in current loops (10x framing from video); revenue-readiness-audit must be clear. macOS install uses official one-line + Desktop app (easiest for average operator); VPS for true 24/7 when needed.
- The hermes-supergrok-vcos-playbook.md is the canonical interface/SOP for setup, profiles, prompts, and integration. Record durable lessons from first runs into decisions.md and the playbook. Route repeated value into Skill Foundry per governance.

## 2026-06-14

- AgentOSync client-facing presentation assets must read as trusted-partner operating-system walkthroughs, not sales-team coaching decks. Avoid slide language such as `Positioning`, `Sales framing`, `wow moment`, `pitch`, `close`, `conversion`, or over-hyped AI claims.
- AgentOSync dealership presentations must explain plainly how the OS organizes, enhances, and optimizes existing WhatsApp workflows for operations manager, sales manager, and CEO/owner visibility so a small team can operate with larger-team discipline.
- Blurry screenshots, unreadable phone captures, overflowing text boxes, cramped boxes, and internal CTA/coaching slides are quality failures. Future PPT/PDF work must render-check contact sheets and full-size slides before delivery.
- AgentOSync presentation quality is now a reusable design-system skill candidate: future decks should use the branded tokens/component grammar, story-hook diagnosis, client-readiness review, and banned-language scan before PPTX/PDF delivery.

## 2026-06-19

- **Browser session incident (Never Repeat A Bug):** An agent ran `gstack/bin/chrome-cdp` while trying to "use the user's logged-in browser" for Higgsfield. The script has no `--help` handler; it force-quit Chrome (`osascript` + `pkill`), symlinked the real profile into `~/.gstack/cdp-profile/chrome`, and launched a second Chrome with CDP. User was logged out across browsers. Root cause: misread "use my browser" as process hijack instead of account reuse.
- **Mandatory prevention:** Never run `chrome-cdp`, browser quit/kill commands, or profile symlink/CDP attach against the user's live default browser without explicit human approval. "Use my browser" = use the same account via CLI (`higgsfield auth login` + generate) or human-completed MCP OAuth — not quit/relaunch Chrome.
- **Higgsfield generation default path:** CLI auth + `higgsfield generate create` for carousel/assets; Grok MCP OAuth as secondary; browser UI as human-only fallback. Incident doc: `3_Project_Workspaces/3.1_AgentOSync_Revenue_Pipeline/03_gtm_campaigns/higgsfield/browser-session-incident-2026-06-19.md`.
- **Dual-Laptop Hermes (Interactive OH approved):** Week 1 = Mission Control dashboard (`mission-control/`) + dual Hermes coordination via GitHub. Laptop 1 = Chief of Staff + WhatsApp + 7pm brief. Laptop 2 = NeuralSync Intern + Telegram + VCOS HQ sync first mission. Must-ship = brief loop 7/7 avg ≥3.5. ClickUp list `901713786845`. Plan: `session-briefs/dual-laptop-hermes/plan.md` (Approved). Session: `session-briefs/interactive-office-hours-dual-laptop-hermes-2026-06-19.md`.
