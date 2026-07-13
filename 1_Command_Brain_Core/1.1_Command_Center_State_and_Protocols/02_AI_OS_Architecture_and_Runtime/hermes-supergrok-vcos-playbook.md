# Hermes Agent + SuperGrok VCOS HQ Playbook

**Purpose**: Turn Hermes (open-source, persistent, self-improving agent by Nous Research) + SuperGrok subscription (Grok 4.3 reasoning + TTS + Imagine via OAuth) + Hermes Desktop into the primary persistent "Machine" and "Cadence" layer for VCOS HQ. This directly advances the AI-native operating system goal by giving the command brain always-on memory, proactive sensors (scans/briefs), specialized profiles (Mini Intern equivalents), slim context sessions, artifacts second-brain, and cron-driven routines — all while respecting VCOS disciplines (progressive context, approval gates, ubiquitous language, recursive self-improvement, least privilege, revenue-first).

**Status**: Phase 0 (read-only night briefs / sensors / drafts). See gates below. All output draft-only until human approval in ClickUp / thread / Desktop.

**Primary references (read these first per fast path)**: AGENTS.md, ubiquitous_language.md, state.md, active-context.md, key-workspaces.md, decisions.md, managed-agent-runtime-evaluation.md, this playbook.

**ClickUp rule (always)**: AgentOSync work references https://app.clickup.com/9017760195/v/s/90175689274 first. Main async folders: https://app.clickup.com/9017760195/v/f/90178817003/90175689274 and https://app.clickup.com/9017760195/v/f/90178817004/90175689274.

## Why This Combo for VCOS (Four C + Three M + Revenue Loops)

- **Context**: Persistent long-term memory across sessions + deliberate seeding with VCOS ubiquitous language, state, decisions, and prompting principles. No more re-explaining the command brain every chat. Self-improves the longer it runs.
- **Connections**: Messaging gateways (Telegram/Slack/Signal/WhatsApp) for phone reach and approval surfaces. One agent, multiple channels. Artifacts centralize links/files/images generated or dropped.
- **Capabilities**: Grok 4.3 (heavy reasoning, long-form, planning, research, Umair-voice drafts) + Imagine (images/videos on demand inside the agent — no app switching for content/proof visuals) + TTS (voice notes back on messaging — "talking to a teammate"). Sub-agents for parallel work. Local-model profiles for unlimited free research/scans.
- **Cadence**: Cron jobs (visible/editable in Desktop) for heartbeats, night briefs, opportunity scanners, content-intel signals, sprint-closer style reviews. VPS or persistent local run for 24/7 even when laptop is off. "The agent that never forgets" becomes the AI OS that acts without constant prompting.
- **Revenue loops it accelerates**:
  1. Dealership OS (Sunday Ghost Town missed-call, test-drive booking, Employee 01 Front Desk).
  2. Amax internal proof (QuickBooks/CFO, distribution desk signals).
  3. Content Intel (signals → drafts in voice; visuals via Imagine).
  4. AgentOSync GTM / Mini Intern packaging (opportunity scanner finds real SMB challenges; profiles as packaged employee behaviors).
- **Machine strengthening**: Profiles + sessions = clean, cost-controlled, specialized execution (model-first per expert guidance, not 50 micro-roles). Aligns with OpenClaw/Hermes fit in managed runtime eval (multi-channel assistant + scheduled/proactive work).
- **Control & ownership**: Open-source, runs on your machine/sandbox/VPS. Memory and conversations live in your environment. "It is yours."

Desktop is the recommended daily surface (polished, Apple-like sessions/profiles/artifacts/cron UI, better than Telegram or pure CLI per detailed walkthroughs). CLI still useful for setup/VPS.

## Phase Gates (Strict — Do Not Skip)

**Phase 0 (current — read-only sensor / brief / draft)**: 
- Read approved sources, query Graphify/GBrain (pointer-first), summarize, produce night briefs or opportunity scans, draft handoff packets / ClickUp suggestions / content outlines / prototype ideas.
- Use Desktop or messaging for review.
- No external sends, no CRM mutation, no publishing, no spend, no deletion, no deployment, no final client strategy.

**Phase 1 (internal drafts + handoffs, human review required)**: Drafts that stay inside VCOS (ClickUp task text, handoff notes, internal briefs, generated assets in artifacts for review). Human must approve before any use in client comms or public.

**Later phases**: Require explicit human approval (recorded in ClickUp/Slack/thread) + updated decision in decisions.md. Messaging gateway activation, limited external tool use, cron that triggers any outbound, etc.

Always follow the permission rule from managed-agent-runtime-evaluation.md:
- Always allow: safe reads, bounded searches, local formatting, non-destructive checks.
- Ask first: shell, external APIs, client data, webhooks, generated sends.
- Human-only: destructive, production, spend, CRM, external messages, credentials.

Before any phase advance or hardware (DGX Spark etc.): run revenue-readiness-audit.md. Prove value in active loops first.

## Supervised Engineering Mission Exception

Phase 0 remains the rule for unattended Hermes crons and messaging sessions. A human may explicitly approve a bounded engineering mission without granting general Phase 1 authority. In that mission Hermes must run `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/candidates/hermes-prd-sprint-conductor/SKILL.md` and may edit only the exact paths frozen in its sprint contract.

The engineering chain is:

```text
Outcome -> Office Hours -> PRD -> acceptance criteria -> GitHub issue/sprint
        -> isolated worktree -> implementation -> completion audit
        -> adversarial review -> fresh verification -> draft PR
```

Use the pointer-first gstack clone at `6_Arsenal/repos/gstack` for current planning, review, testing, and shipping patterns. Do not vendor its full workflow into VCOS. Installing gstack into Hermes, enabling GitHub issue automation, merging, deploying, sending externally, or expanding file authority requires separate human approval.

For the first three proof missions, invoke the tracked conductor repo-locally by telling Hermes to read `AGENTS.md` and then `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/candidates/hermes-prd-sprint-conductor/SKILL.md`. After explicit approval, gstack's current Hermes host install is `./setup --host hermes` from the Arsenal clone; verify with `hermes skills list`. Do not globally install the VCOS conductor until the three supervised missions pass.

Completion is based on artifacts and machine evidence, not narration. After two consecutive status-only turns, unverifiable Git evidence, or correction churn that does not advance acceptance criteria, stop with `BLOCKED` and one precise action for Umair.

## macOS Setup (User's Machine — Draft-Only Guidance)

**Recommended path (Desktop installer for macOS 12+)**:
1. Download the Hermes Desktop installer from the official site: https://hermes-agent.nousresearch.com/desktop (or https://hermes-agent.nousresearch.com/docs/getting-started/installation).
2. Run the installer (.dmg). It sets up both CLI and the polished Desktop app.
3. Open the Desktop app (or terminal: `hermes desktop` after CLI install).
4. In terminal (or via Desktop flows): run `hermes setup` (full wizard; configures basics, can include desktop).
5. **Critical (never skip)**: `hermes doctor` — checks install, reports exactly what is missing and how to fix. Run every time something feels off.
6. Reload/restart terminal or app after install steps.

**CLI-only alternative** (for VPS or minimal):
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
# then
hermes setup
hermes doctor
```

**Connect SuperGrok (Grok 4.3 + full surface — one login)**:
1. Run `hermes model` (opens model picker; in Desktop use the equivalent UI).
2. Select **xAI Grok OAuth (SuperGrok Subscription)** (or "xAI Grok OAuth (SuperGrok / X Premium+)").
3. Browser opens → sign in at accounts.x.ai with your Grok/SuperGrok account and approve.
4. Token is reused automatically for chat (Grok 4.3), TTS, image generation (Imagine), and video.
5. No API key copying. Works on every subscription tier that includes the features.
6. Verify: start a chat in Desktop or `hermes --tui` / `hermes 2E` equivalent and confirm Grok 4.3 responses.

**Migrate note** (if coming from OpenClaw): `hermes claw migrate`.

**VPS / always-on (Phase 0 Night-Shift for VCOS)**: Same install script works on a small Linux VPS ($5–15/mo sufficient for Hermes + SuperGrok OAuth; more RAM/CPU if running local models for the Scanner profile). The VPS runs the persistent "Machine + Cadence" layer: night briefs, opportunity/challenge scanner (every 20-60 min on low-cost profile), heartbeat crons, and sensor collection while your laptop is off. Outputs stay draft-only (handoff packets, ClickUp-suggested text, internal briefs) and are reviewed by human before any use. Desktop remains primary for seeding, heavy interaction, profile management, and artifacts review. CLI/VPS is the always-on executor.

Key data location (critical to understand and back up): `~/.hermes/` (per-user). Contains memories, learned skills, session history, configs, cron jobs (`.json` + output dir), auth state, and agent persona/soul. Losing it means the agent forgets its VCOS training.

**Recommended VPS providers and sizing (start minimal)**:
- Hetzner Cloud, DigitalOcean, Linode, OVH, or similar Ubuntu 24.04 LTS droplets.
- Starter: 2 vCPU / 4 GB RAM / 40-80 GB SSD (~$5-8/mo). Fine for Grok OAuth (API calls) + gateway + crons.
- If Scanner uses local models (Qwen etc. for free unlimited scans): 8+ GB RAM or GPU instance (higher cost; evaluate only after revenue-readiness clear and Phase 0 proven).
- Location: Choose low-latency to your primary regions if messaging or API calls are frequent.

**Security & Hardening Baseline (mandatory before any Hermes install — least privilege)**:
- Non-root dedicated user (e.g. `adduser --disabled-password vcos-hermes`).
- SSH keys only (disable password login in `/etc/ssh/sshd_config`: `PasswordAuthentication no`, `PermitRootLogin no`).
- Firewall: `ufw allow OpenSSH`, `ufw enable`. Open only additional ports if self-hosting any gateways (prefer provider messaging like Telegram bots).
- fail2ban for SSH brute-force protection.
- Automatic security updates: `unattended-upgrades` or cron `apt update && apt upgrade -y`.
- Minimal OS: No unnecessary packages, services, or exposed ports.
- Hermes user: Limit filesystem access to its home + any explicitly needed output dirs. Run gateway/crons under this user.
- Secrets: All auth (including SuperGrok OAuth sessions) lives in `~/.hermes/`. Never commit to git. Use `HERMES_HOME` env if needed for custom paths. Rotate/backup securely.
- Updates: Regular `hermes doctor`, system patches, and Hermes updates via official script (test in staging first).

**Hermes Install & Persistent Gateway on VPS (step-by-step)**:
1. Provision clean Ubuntu 24.04 VPS, harden as above, create dedicated user, login as that user.
2. Install (as the hermes user):
   ```bash
   curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
   source ~/.bashrc   # or ~/.zshrc
   hermes doctor
   ```
   (Some headless installs support `--skip-browser` flag per community guides.)
3. **SuperGrok / xAI OAuth on headless** (known tricky area — open issues exist for multi-process shared auth state):
   - Preferred: Perform initial `hermes model` + browser OAuth on a local Desktop/machine (easy browser callback), then securely rsync or copy the relevant auth/config files from `~/.hermes/` to the VPS (or use the manual token paste fallback documented in Hermes GitHub issues/PRs for xai-oauth).
   - Alternative: SSH X11 forwarding or local port tunnel for the OAuth callback during first setup.
   - Once set, the OAuth session should auto-refresh in the background for Grok 4.3 / Imagine / TTS.
   - Verify with a simple chat. For multiple profiles or gateway + crons: Be aware of shared auth state caveats (see GitHub issue on profiled/multi-process OAuth); workarounds exist (test one profile first).
4. Configure messaging if desired (post-approval for gateways):
   ```bash
   hermes gateway setup
   ```
   Follow wizard for Telegram, etc. (bots are common for always-reachable agents).
5. **Make it persistent (gateway daemon handles crons + messaging delivery)**:
   - Test foreground first: `hermes gateway`
   - User-level service (good for dedicated user):
     ```bash
     hermes gateway install
     # Enable lingering so it survives logout
     loginctl enable-linger $(whoami)
     systemctl --user enable --now hermes-gateway
     systemctl --user status hermes-gateway
     journalctl --user -u hermes-gateway -f   # watch logs
     ```
   - System-wide (recommended for clean server deployments, survives reboots cleanly):
     ```bash
     sudo hermes gateway install --system
     systemctl enable --now hermes-gateway
     journalctl -u hermes-gateway -f
     ```
   - The gateway daemon ticks every ~60s, runs due crons in isolated sessions, and keeps messaging live.
6. Set up VCOS crons (use reverse prompting in a seeded profile; see earlier section). Crons are stored under `~/.hermes/cron/`. They run unattended via the gateway.
7. Verify persistence: Reboot the VPS, confirm gateway is running and a test cron fires. Run `hermes doctor` after reboot.
8. Backup strategy: Regularly rsync or snapshot the entire `~/.hermes/` directory (contains everything the agent has learned). Treat it like your Second Brain state. Version critical seeds/prompts in the VCOS repo (pointers).

**VCOS-Specific Tailoring for VPS Hermes (Phase 0 only)**:
- **Profiles on server**: Run the persistent process primarily under a "VCOS-Scanner" or main seeded profile for always-on work (opportunity scanner, night briefs). Use Desktop for Brain-Grok heavy reasoning/Imagine and initial seeding. Copy or re-apply seeds to VPS profiles.
- **Phase 0 enforcement**: All VPS crons and sessions must be explicitly prompted for "read-only sensor / draft / handoff packet only. No external actions, no CRM, no publish. Output clean structured summaries with sources and recommended next actions for human review. Reference primary AgentOSync ClickUp view https://app.clickup.com/9017760195/v/s/90175689274 and async folders first."
- **Approved sources only**: User (or future safe read-only skills) feeds summaries of state/active-context/Graphify exports. Hermes does not have broad unaudited web or client data access in Phase 0.
- **Outputs**: Direct crons to produce files in `~/.hermes/cron/output/` or specified paths. Human pulls them (scp, shared drive, or later gated integration) and reviews before ClickUp (Production Control Room or AgentOSync surfaces) or handoff.
- **Least privilege & isolation**: Dedicated user + tight prompts + skill pruning. One main persistent gateway instance; spin isolated sessions for jobs.
- **Monitoring & health**: Periodically run `hermes doctor` via a safe cron or external check. Watch logs with journalctl. Monitor disk (memory grows with use) and basic resource usage. Add simple external uptime/ping if desired.
- **Revenue loops**: Prioritize the opportunity/challenge scanner cron (low-cost profile) feeding Dealership OS, Amax, AgentOSync GTM. Night briefs for AMAX distribution or general signals (per existing state notes). All draft-only.
- **Integration**: Pointer-first to Second Brain (compress outputs before promoting to GBrain/Graphify or `1.3_Knowledge_Graphs/`). Execution truth remains ClickUp (AgentOSync view first). Use Production Control Room list for reusable Hermes/VPS infrastructure tracking once set up.
- **Testing cadence**: Prove one cron end-to-end (e.g., night brief) on VPS before adding scanner frequency or additional profiles. Log learnings in decisions.md and this playbook after first successful unattended runs.

**Known Caveats & Mitigations (from Hermes docs/issues/community)**:
- Headless setup wizard / OAuth can hang or require workarounds (non-interactive SSH, browser callbacks). Mitigate by hybrid local + copy or manual fallbacks.
- Multi-profile / gateway + cron shared auth state has open documentation/workaround needs.
- Memory/skill growth: Prune regularly; backup before major changes.
- Cost control: Same session hygiene rules apply — dedicated slim contexts for VPS jobs.
- Updates: Test on a cheap instance; the agent is self-improving so re-seed/verify after updates.
- Serverless alternatives (mentioned in Hermes materials): Daytona, Modal for hibernation (near-zero idle cost) — evaluate later as pointer if VPS baseline proves value.

**VPS Setup Checklist (Prioritized for VCOS Phase 0)**:
1. Provision + harden VPS (dedicated user, SSH keys, ufw, fail2ban, updates).
2. Install Hermes as dedicated user + `hermes doctor`.
3. Handle SuperGrok OAuth (local first + transfer or documented fallback).
4. `hermes gateway setup` (messaging if approved later).
5. Install and start persistent gateway (`hermes gateway install` + systemctl + lingering or `--system`).
6. Seed VCOS identity (copy from Desktop seed or paste summaries + "Phase 0 read-only only" rules).
7. Create/verify first safe cron (night brief or scanner) using reverse prompting. Confirm it appears in `hermes cron list` and runs.
8. Reboot test + log monitoring.
9. Backup `~/.hermes/`.
10. Run first unattended output, review as human, log to ClickUp (AgentOSync view) + update playbook/decisions. Do not advance phase without explicit approval.

Official & community refs (verify current):
- Installation & data layout: https://hermes-agent.nousresearch.com/docs/getting-started/installation (notes `~/.hermes/`)
- Gateway & cron: Search Hermes docs for "gateway" and "cron" (daemon handles scheduling/delivery; `hermes gateway install --system`).
- GitHub repo: https://github.com/nousresearch/hermes-agent (issues for OAuth headless, multi-process auth, health status).
- Community tutorials often cover DigitalOcean/Hostinger-style systemd setups with `hermes gateway install` + `systemctl --user`.

**First verification on VPS**: `hermes doctor`, confirm gateway service active post-reboot, one cron fires and produces clean Phase 0 output, `hermes cron status` / list works.

Run revenue-readiness-audit.md before committing to paid VPS or scaling frequency. All VPS Hermes work stays within Phase 0 gates until human approval recorded.

This turns the VPS into the reliable always-on sensor and cadence engine for the AI OS while keeping full control and discipline.

Official docs (always verify latest):
- Installation: https://hermes-agent.nousresearch.com/docs/getting-started/installation
- xAI Grok OAuth: https://hermes-agent.nousresearch.com/docs/guides/xai-grok-oauth
- Quickstart: https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- GitHub: https://github.com/nousresearch/hermes-agent

**First verification**: `hermes doctor`, create a test session, switch profiles, check artifacts and cron UI (Desktop); on VPS confirm gateway service + cron execution.

## Recommended VCOS Profiles (Desktop Sidebar)

Profiles = separate full Hermes agents (own skills, soul.md/personality, memories, session history). Switch with one click. Model-based for efficiency (per expert: know strengths, avoid mental overhead of 50 roles + chained context costs).

| Profile Name          | Primary Model / Source          | Core Purpose for VCOS                                      | When to Use                                      | Notes / Soul Seed Focus |
|-----------------------|---------------------------------|------------------------------------------------------------|--------------------------------------------------|-------------------------|
| VCOS-Brain-Grok      | SuperGrok OAuth (Grok 4.3)     | High-reasoning, strategy, planning, long-form in Umair voice, complex orchestration, skeptic deep reviews, Imagine visuals | Sentinel work, plans, content drafts, Dealership scoping, AMAX finance logic, Trading Coach thinking | Primary "smart" profile. Seed with full VCOS identity. Use Imagine here. |
| VCOS-Scanner         | Local (Qwen/Nemotron on hardware if available) or cheap/fast fallback | Frequent, low/no-cost scanning of Reddit/X/signals for challenges/opportunities; research; content-intel raw signals | Every 20min or daily opportunity scans, signal sweeps, background monitoring | Unlimited free intelligence ideal for the "daily AI business opportunity scan" pattern. Prune heavy skills. |
| VCOS-Librarian       | Grok or local                  | Artifacts curation, link/file/image organization, second-brain hygiene, promotion to GBrain/Graphify pointers | Drop links/assets during research; librarian drops without extra instruction; search artifacts | Leverages Desktop Artifacts view heavily. |
| VCOS-Builder         | GPT-equivalent (if strong coding limits) or Grok or local | Implementation, code gen, following execute-plan / browser harness patterns, feature builds | Coding tasks, prototype scaffolding, employee repo updates | Match to actual coding strength of the model. |
| VCOS-Skeptic         | Grok 4.3 (or dedicated)        | Adversarial review, QA, design-review style, "never repeat a bug" checks | Before handoffs, before human review gates, on content/claims/proposals | Enforce VCOS reviewer ownership. |

**Multi-tasking example**: High-level strategy in VCOS-Brain-Grok → handoff research to Scanner → coding to Builder → review in Skeptic. Or parallel sub-agents inside one profile for same-skill multi-strand work (e.g. 5 features of a micro-SaaS/Employee kit).

Start with 2-3 (Brain + Scanner + Librarian). Add as proven.

**Sub-agents vs Profiles**: Profiles = different skills/personality/model/memory (use for distinct VCOS roles or model strengths). Sub-agents = copies of the current agent for parallel execution of the *same* skillset (e.g. spin 5 sub-agents to build different features simultaneously).

## Session & Folder Organization (Desktop)

- Every new conversation in Desktop creates or goes into a clean session.
- Create folders: Dealership-Sameer-Uzair, Amax-Finance-Proof, AgentOSync-GTM-Distribution, Content-Intel, Trading-Coach, HQ-Strategy-Weekly, Opportunity-Scanner.
- Pin important sessions.
- Before switching topics: use new session (or `/new` equivalent). This keeps every message slim (only that thread's history is sent) → dramatically lower cost and better focus vs. one polluted mono-thread.
- Visible context window at bottom of Desktop: watch it, start fresh when high.
- Result: "If you manage your contexts and your sessions well, you are not paying a thousand dollars a month."

## Memory Seeding & "Keep Teaching It" Protocol (Pro Tip 3 + 8 Applied)

**First action in new primary profile (VCOS-Brain-Grok)**:

Paste (or have it read local paths if supported; otherwise full paste of summaries):

```
You are the persistent VCOS HQ command brain agent. VCOS Headquarters is the AI-native operating system command brain for cross-client and multi-agent work.

Core identity and rules (never contradict; carry this forward in every session and across messaging gateways):

[PASTE FULL: 1_Command_Brain_Core/1.2_Headquarters_Memory/ubiquitous_language.md]

[PASTE KEY SECTIONS: state.md Current State + Active Decisions + the Hermes/Phase 0 bullet + Next Actions summary]

[PASTE: active-context.md key paragraphs on current focus, fast path, architecture, risk]

[PASTE: key-workspaces.md ClickUp rule + primary view + AgentOSync daily operating route]

[PASTE RELEVANT: decisions.md latest entries especially the 2026-06-13 Hermes adoption]

You follow AGENTS.md and CLAUDE.md discipline exactly: progressive context loading, fast path first, draft-only until approval, human gates for external/CRM/publish/spend/destructive, AgentOSync ClickUp view first, etc.

Your job: act as the never-forgetting, self-improving persistent layer. Run read-only Phase 0 briefs and sensors. Produce clean handoff packets instead of full history. Use reverse prompting when designing crons or complex prompts. Give me your best VCOS-native output and remember feedback (great / miss) so you get sharper.

Start by confirming you have internalized the ubiquitous language and current priorities (Dealership OS real-client MVP first, Amax QuickBooks proof, content-intel after voice samples, AgentOSync GTM, Trading Coach protected). Then ask for the first task or confirm first cron setup.
```

**Ongoing**: Treat first weeks like onboarding a new teammate. Be specific. Give feedback on every output ("this brief nailed the ClickUp routing but missed the revenue-readiness blocker — update your memory"). It remembers and improves. This is how it "builds a deepening understanding of you" and of VCOS.

Update soul.md (profile personality file) or persistent memory with the above + any VCOS-specific tone rules once calibrated.

## Cron Setup + Reverse Prompting (Highest Leverage for Cadence)

Desktop cron UI (bottom nav): see all scheduled tasks, create manually, high confidence they will fire (big improvement over chat/CLI "I hope it scheduled").

**Reverse prompting technique (brain dump → super-intelligence designs the prompt)**:
1. New session in right profile.
2. Brain-dump everything relevant about the goal, VCOS self, interests/constraints, exact output shape wanted, success criteria, VCOS rules (ubiquitous language, gates, ClickUp view, etc.).
3. Then: "Based on everything I just told you about VCOS and me, what is the single best cron prompt / schedule / wording I should use to set this up reliably?"
4. Use the output it gives you as the actual cron definition. It will be detailed, formatted, time-aware, and avoid common failure modes (stale data, bad formatting, missing economic events, etc.).

**Example adapted VCOS crons** (start with 1-2; use Scanner profile for high-frequency):

- **Night brief / Phase 0 sensor (Hermes Phase 0 as specified)**: Every night or early AM. Scanner or Brain profile. "You are compiling the VCOS nightly sensor brief. Pull fresh 24h signals from approved sources only (no memory cutoff reliance). Cover: key ClickUp blockers from primary AgentOSync view + async folders, new challenges/opportunities on relevant SMB channels that map to Dealership OS / AgentOSync Mini Interns / Employee 01, Amax ledger or finance signals if accessible, content-intel raw signals. Format: one-line vibe summary, bold bullets, sources/links, why this matters to current priorities (Dealership first), recommended next action (draft-only). Include exact ClickUp view link. Output as clean handoff packet."
- **Opportunity / challenge scanner (biggest money use case)**: Every 20-60 min (Scanner profile, local preferred for cost). "Scan Reddit, X, forums for real founder/SMB challenges in dealerships (after-hours leads, test-drive booking), travel booking/ops, barbershops, general SMB admin/sales. For each high-signal one: link to source/thread, quote the pain, why VCOS/AgentOSync/Employee 01/Mini Interns is positioned to solve it (reference known assets without hallucinating), suggested first move, and (if appropriate) a one-paragraph prototype idea. Output dashboard-style with sources. Low noise — only actionable for our current lanes."
- **Morning / heartbeat brief**: 8AM America/Toronto on Brain profile. Similar to night but forward-looking + state/active-context refresh + human decisions needed.
- **Content-intel signal or sprint-closer style**: Daily or end-of-focused-session. Respect voice calibration files first (manual 5+ runs).

Use Desktop to create the cron with the reverse-prompt output. Confirm it appears in the cron list.

## Grok Imagine, TTS, and Artifacts in VCOS

- **Imagine (images + short video)**: In any session (preferably Brain profile): "Using Grok Imagine, create [exact visual for content proof, LinkedIn hook, demo screenshot concept, thumbnail, deck asset]. Follow B.R.A.N.D. or Four Hook Commandments if relevant. Deliver the asset here." It generates and (in Desktop) lands in Artifacts. No copy-paste or app switch.
- **TTS**: Ask for spoken response. On messaging gateway: "Reply with a voice note summary of the brief." Changes the feel from wall-of-text to teammate.
- **Artifacts view (Desktop)**: All images, files, links sent to the agent are automatically centralized and searchable. Drop inspiration links during research; Librarian profile can just receive them ("file this"). Search "dealership" or "reddit" to surface. Use as the living second-brain layer before promotion to HQ memory / GBrain / Graphify (pointer-first, curated summaries only).

This productizes asset memory and pairs perfectly with content-intel + proof-packager routines.

## Cost Hygiene (Critical Even With Subscription)

Context (especially large models) is the #1 bill inflator (3-4x). Desktop solves it better than 99% of Hermes usage:
- Dedicated slim sessions per lane/folder.
- Right profile for the job (Scanner/local for volume scans; Brain only when real intelligence needed).
- Prune skills in the skills/tools UI (150+ out of box add context/cost; turn off irrelevant; watch auto-generated skills from your VCOS actions and toggle).
- Tool sets for complex grouped work.
- Watch context window UI element; start new session proactively.
- Local hardware profile = free unlimited for scanner/hygiene work.

## Skills & Tool Management

Desktop skills UI: review installed, toggle off anything not VCOS-relevant (file ops, search, code, Grok image/TTS, cron, messaging, basic shell if bounded). Auto-generated skills (e.g. from building dealership briefs or opportunity scans) are gold — capture them, test, promote winners to VCOS Skill Foundry after 3+ validated runs per governance.

Tool sets: group related skills for complex VCOS workflows (e.g. "dealership-brief-kit").

## Integration Points with Existing VCOS Stack

- **GBrain / Graphify**: Hermes reads (via user or future skills) or user pastes summaries; Hermes output (briefs, findings) is compressed and promoted pointer-first into `1_Command_Brain_Core/1.3_Knowledge_Graphs/` or Graphify imports. Never bulk noisy import.
- **ClickUp**: All execution truth stays in ClickUp. Hermes produces draft task text, blockers, next actions, handoff notes. Human pastes/creates after review. Primary surface = AgentOSync view.
- **Obsidian / HQ files**: Fast path files are the seed. Hermes works on summaries or user-curated exports. Pointer-first.
- **Arsenal / other tools**: Hermes can orchestrate or call out to gstack (pointer), QMD, etc., once skills are enabled and approved. Keep pointer-first.
- **Skill promotion**: Repeated valuable Hermes workflows (e.g. the scanner prompt, a reverse-prompted cron template) become skill candidates after 3+ successes. Package into `4_Reusable_Systems_and_Skills/...`.
- **Employee OS Template**: Profiles + soul.md + skills + memory + cron + handoff packets are a living prototype for what a packaged "Employee 01" or Mini Intern runtime can look like. Lessons flow back to the template repo.
- **Messaging for approvals**: Once past Phase 0/1 gates and approved, connect Telegram/Slack as the mobile surface (aligns with existing "Slack or Telegram is the first mobile approval surface").

## Pro Tips Applied to VCOS (Direct from Source Material)

1. Start small: Pick one lane (e.g. Dealership OS or one AMAX brief) + one profile + one cron. Get it working before adding scanner or full routines.
2. Connect messaging gateway early (after Phase 1 approval): Reach the agent from phone, hand off tasks, receive voice notes or briefs.
3. Use memory on purpose: The initial big brain-dump + ongoing specific feedback is how it carries VCOS context everywhere.
4. Use Grok Imagine for visuals: Every content/proof/demo asset request goes through the agent.
5. Run `hermes doctor` (or Desktop equivalent health) every time something feels off.
6. Test the voice/TTS feature: Changes daily feel.
7. Pair with VPS for true persistence (night scanner + crons keep running).
8. Keep teaching it: First weeks = onboarding. Specificity + feedback = compounding sharpness on VCOS way of working.
9. Desktop organization (sessions/folders/profiles/artifacts/crons/skills UI) is the biggest productivity unlock over previous agent chat experiences. Use it.
10. Reverse prompting + brain dump = best crons and complex prompts. Never just "wing it" with super intelligence available.
11. Scanner as automated employee: Finds challenges 24/7, matches to your (VCOS) skills/assets, suggests moves + prototypes. The ethical high-leverage way to create value.
12. Model/profile choice for outcome + cost: Grok for the hard VCOS brain work; cheaper/local for volume. Output and ROI matter more than "one agent to rule them all."

## First Human Run Checklist (Draft — Requires Your Action on Machine)

1. Install Desktop app + CLI via official installer (https://hermes-agent.nousresearch.com/desktop). Run `hermes doctor`.
2. Connect SuperGrok via `hermes model` / Desktop model picker. Confirm Grok 4.3 + Imagine works in a test chat.
3. Create the 3 starter profiles (VCOS-Brain-Grok first, then Scanner, Librarian).
4. In VCOS-Brain-Grok: paste the memory seed block (core files + identity). Confirm it internalizes (ask it to restate priorities and ClickUp rule).
5. Set up first cron (night brief or opportunity scanner) using reverse prompting in the right profile. Verify it appears in Desktop cron list.
6. Create session folders for active lanes.
7. Run one manual opportunity scan or night brief. Review output in Desktop. Give explicit feedback. Save the brief as draft artifact or handoff note.
8. Drop any inspiration links into Librarian or a session; check Artifacts view.
9. Log first impressions + any issues in this thread or a ClickUp note under AgentOSync view. Update decisions.md / this playbook with learnings after first 3 runs.
10. Before any gateway, cron that touches external, or phase advance: record human approval.

**Revenue-readiness note**: Do not expand to hardware or heavy automation until current loops (Dealership MVP, Amax proof, first content drafts) have clear shipped artifacts, daily bottlenecks diagnosed, and paid-pilot language.

## References & Maintenance

- Update this playbook after repeated value or failures (route through recursive-self-improvement-loop.md).
- New durable decisions → decisions.md and state.md.
- 3+ successful VCOS-specific workflows here → skill candidates in the Foundry.
- Arsenal: if Hermes or specific prompt packs become recurring "gems", add via the arsenal process.
- Always re-read fast path + this playbook before Hermes work.

This is the interface. Load it when the task involves persistent agents, crons, memory-heavy VCOS work, or opportunity sensing for the revenue loops.

**Next after first runs**: Skeptic-style review of outputs, promotion of good prompts/crons into reusable skills or employee template patterns, and clear human decision on Phase 1 activation + messaging gateway.

Build the AI-native OS one clean, persistent, self-improving loop at a time. Start small, teach deliberately, keep context slim, respect the gates.
