# Arsenal Index

Master table of every gem, repo, tool, framework, API, prompt pack, and reference in the arsenal.

**To add an entry:** say `"Add gem: [URL or name] — [description]"` and Claude will fill and append the row.
**To query:** say `"Arsenal query: I need to [do X]"` and Claude will filter this table by `problem-tags`.

---

| Name | Type | URL / Path | Problem it solves | problem-tags | Status | Notes |
|------|------|-----------|-------------------|--------------|--------|-------|
| Caveman | tool | https://github.com/JuliusBrussee/caveman / **Local**: `6_Arsenal/repos/caveman` | Reduces agent output verbosity and agent-to-agent chatter so multi-agent work costs fewer tokens and produces cleaner handoffs | `llm-ops` `ai-agents` | cloned-evaluation | Pointer-first only. Treat as output-compression discipline for Codex/Claude/Gemini-style agents; do not install globally until a repeated workflow proves value. |
| Graphify | framework | https://github.com/safishamsi/graphify / **Local**: `6_Arsenal/repos/graphify` | Turns codebases, docs, transcripts, PDFs, images, videos, and SQL schemas into queryable knowledge graphs with `graph.json`, `GRAPH_REPORT.md`, wiki, and Obsidian exports | `ai-agents` `search` `research` `llm-ops` `documents` | active-evaluation | Cloned and CLI-installed on 2026-06-10 with `graphifyy==0.8.36`. Use through `graphify-obsidian-rag-architecture.md`; quarantine Obsidian imports under `1.3_Knowledge_Graphs/imports/` before promotion. |
| QMD | tool | https://github.com/tobi/qmd / **Local**: `6_Arsenal/repos/qmd` | Local context router for markdown notes, docs, transcripts, and knowledge bases using BM25, vector search, and local LLM reranking | `ai-agents` `search` `llm-ops` `documents` `meetings` | cloned-evaluation | Use between Obsidian and agents as fast local retrieval over approved collections. Do not treat as a vault replacement or source of truth; install/MCP activation is gated until a scoped proof run. |
| Browser Harness | framework | https://github.com/browser-use/browser-harness / **Local**: `6_Arsenal/repos/browser-harness` | Self-improving browser automation harness that lets agents build durable site-specific browser skills from successful runs | `automation` `web-scraping` `ai-agents` `frontend` | cloned-evaluation | Use for repeatable web ops, demo QA, site workflows, and scraper/operator tasks. Requires explicit approval before connecting to authenticated/client-sensitive browser sessions. |
| claude-video | tool | https://github.com/bradautomates/claude-video | Lets Claude Code ingest any video: yt-dlp downloads, FFmpeg chops into frames, Whisper transcribes, feeds screenshots + transcript to Claude | `media` `ai-agents` `content` | untested | Auto-scales frame rate up to 100 frames; useful for video review, content extraction |
| Open Design | framework | https://github.com/nexu-io/open-design | Open-source local alternative to Claude Design; auto-detects 16 coding agent CLIs and drives them with 19 skills and 71+ brand-grade design systems | `frontend` `ai-agents` `content` | untested | Works with Claude Code, Codex, Cursor, Gemini CLI, and more — not locked to Claude |
| CodeBurn | tool | https://github.com/getagentseal/codeburn / **Local**: `6_Arsenal/repos/codeburn` | Local token/cost telemetry for AI coding sessions across Codex, Claude, Cursor, Gemini, and other tools | `llm-ops` `analytics` `ai-agents` | cloned-evaluation | Use as the token-maxing dashboard for VCOS. Reads local logs; no proxy or API key by default. Good for weekly spend, waste, one-shot rate, model, and project analysis. |
| Impeccable | framework | https://github.com/pbakaus/impeccable / **Local**: `6_Arsenal/repos/impeccable` | Front-end design command suite and detector rules for turning AI-generated UI into polished product-quality interfaces | `frontend` `ai-agents` `brand` | cloned-evaluation | Use as the design QA layer for the software factory. Pointer-first; install project skill only after a UI build needs it. |
| Design Extract | tool | https://github.com/Manavarya09/design-extract / **Local**: `6_Arsenal/repos/design-extract` | Extracts design systems, tokens, themes, screenshots, accessibility notes, brand voice, and AI prompts from websites | `frontend` `ai-agents` `brand` `research` | cloned-evaluation | Use for brand/design ingestion and competitor/site reference extraction. Approval required for authenticated/client-sensitive pages or publishing derived client-facing assets. |
| Career Ops | framework | https://github.com/santifer/career-ops / **Local**: `6_Arsenal/repos/career-ops` | Reference architecture for scrape-score-generate-track human-in-loop opportunity pipelines | `automation` `research` `documents` `sales` | cloned-evaluation | Original domain is job search. In VCOS, generalize the pattern into lead/opportunity ops, pilot qualification, and service-company delivery pipelines. |
| n8n-mcp | tool | https://github.com/czlonkowski/n8n-mcp | MCP server for building n8n automations via Claude Code; uses TypeScript validation to check nodes and workflows before committing as JSON | `automation` `ai-agents` `backend` | untested | Covers 1,650+ n8n nodes; not fully open source — check license before commercial use |
| Token Dashboard | tool | https://github.com/nateherkai/token-dashboard | Analytics dashboard for Claude API usage and token spend across projects and models; GitHub repo with setup guide and video | `llm-ops` `analytics` | active | From Nate Herkai; paired with video tutorial; local or hosted deployment options; useful for cost tracking across VCOS projects |
| Claude Code Masters Course Pack | course-collection | **Local**: `/6_Arsenal/claude-code-resources/` | Curated bundle: Three Ms/Four Cs frameworks (AIS-OS), skill evaluation guide (6 best plugins), Claude Design Masterclass (B.R.A.N.D. + 2-hour course), website 3D pipeline (hero-video + Superpowers) | `ai-agents` `frontend` `llm-ops` `infrastructure` | active | From Nate Herkai. Covers operator mindset (Three Ms), AIOS architecture (Four Cs), brand systems (B.R.A.N.D.), plugin installation, website workflows. **Integration:** Merged into skill-leverage-stack.md, skill-registry.md (claude-design-brand-system + website-hero-video-pipeline), state.md (Three Ms + Four Cs). No duplicate folders.
| GBrain | framework | https://github.com/garrytan/gbrain / **Local**: `6_Arsenal/repos/gbrain` | Adds a persistent AI-agent brain layer with hybrid search, synthesis, graph traversal, skillpacks, and operational memory patterns | `ai-agents` `search` `llm-ops` `automation` `prompts` | active-evaluation | Cloned and CLI-linked locally on 2026-06-01. Use pointer-first through `gbrain-activation.md`; human approval required before importing client/private data, configuring API keys, or starting recurring jobs. |
| GStack | framework | https://github.com/garrytan/gstack / **Local**: `6_Arsenal/repos/gstack` | Garry Tan's Claude Code software-factory stack with office-hours, CEO/eng/design reviews, QA, ship, browse, spec, and other agent workflow skills | `ai-agents` `llm-ops` `automation` `frontend` `backend` `prompts` | active-evaluation | Cloned locally on 2026-06-02. Use pointer-first across project workspaces; do not vendor into projects unless a standalone repo requires a pinned copy. |
| Meetily | app | https://github.com/Zackriya-Solutions/meetily / **Local**: `6_Arsenal/repos/meetily` | Privacy-first local AI meeting assistant for recording, transcribing, summarizing, and exporting meeting intelligence without default cloud processing | `ai-agents` `automation` `documents` `llm-ops` `meetings` `scheduling` | active-evaluation | Cloned locally on 2026-06-09. Current supported path is Tauri desktop app in `frontend/` and `frontend/src-tauri`; `backend/` is legacy archive. Human approval required before using it on client-sensitive calls or external meeting workflows. |
| ToolJet | app-framework | https://github.com/ToolJet/ToolJet / **Local**: `3_Project_Workspaces/Project repos/tooljet` | Open-source low-code builder for internal tools, admin panels, workflow dashboards, and operator consoles across APIs, databases, SaaS tools, and custom JS/Python transforms | `automation` `frontend` `backend` `analytics` `crm` `sales` `scheduling` `infra` | active-evaluation | Local working copy is under project repos in this workspace. Best evaluated as an internal HQ/operator console layer, not as the VCOS memory source or agent runtime. AGPL-licensed; local clone produced a macOS case-insensitive SVG filename collision warning. |
| Twenty | app | https://github.com/twentyhq/twenty / **Local**: `6_Arsenal/repos/twenty` | Open-source CRM for testing lead/account/contact workflows, sales pipeline views, operator handoffs, and CRM-adjacent AgentOSync demos without mutating a client CRM | `crm` `sales` `automation` `frontend` `backend` `infra` | cloned-evaluation | Cloned locally on 2026-06-15. Pointer-first evaluation candidate for AgentOSync CRM/operator workflows; external sends, CRM mutations, imports, and client-facing use remain approval-gated. |
| AIS-OS | framework | https://github.com/nateherkai/AIS-OS / **Local**: `6_Arsenal/repos/ais-os` | Lean AI operating system starter kit for Claude Code using onboarding, Four C audits, Three Ms level-up sessions, connection registry, decisions, and weekly shipped artifacts | `ai-agents` `automation` `llm-ops` `prompts` `infra` | active-evaluation | Cloned locally on 2026-06-10. Activated pointer-first through `ais-os-activation.md`; use as an operating pattern for VCOS, not a replacement vault or parallel source of truth. |

---

## Tag Reference

Use consistent tags so queries work reliably. Add new tags here as needed.

| Tag | Use for |
|-----|---------|
| `ai-agents` | Building, orchestrating, or deploying AI agents |
| `llm-ops` | LLM infrastructure, prompt management, evals, cost control |
| `automation` | Workflow automation, event triggers, scheduled jobs |
| `web-scraping` | Data extraction from websites |
| `crm` | CRM integrations, lead management, contact data |
| `sales` | Sales workflows, outreach, follow-up sequences |
| `content` | Content creation, copywriting, social media |
| `media` | Image, video, audio generation or editing |
| `frontend` | UI components, landing pages, dashboards |
| `backend` | APIs, databases, server-side logic |
| `analytics` | Reporting, metrics, dashboards, data pipelines |
| `email` | Email sending, parsing, or automation |
| `sms-voice` | SMS, WhatsApp, phone call automation |
| `scheduling` | Booking, calendar, appointment workflows |
| `meetings` | Meeting capture, transcription, notes, summaries, and follow-up extraction |
| `documents` | PDF, spreadsheet, document generation or parsing |
| `search` | Search, semantic retrieval, RAG |
| `prompts` | Prompt libraries, system prompt templates |
| `research` | Research tools, data sources, market intel |
| `infra` | Deployment, hosting, CI/CD, monitoring |
| `finance` | Financial data, modeling, reporting |
| `dealerships` | Auto dealership specific |
| `travel` | Travel industry specific |
| `clinics` | Healthcare / clinic specific |
