# Claude Power User Playbook

Purpose: help Umair compound time with VCOS by using Claude/Codex as a disciplined teammate, coach, and workflow architect.

This file is loaded only when the task is about improving AI usage, prompt quality, Claude Code workflows, context hygiene, token savings, or operating discipline.

## Core Operating Loop

1. Clarify the outcome.
2. Load the smallest useful context.
3. Ask questions until the task is concrete enough.
4. Plan before high-risk or ambiguous execution.
5. Execute in small verifiable steps.
6. Self-check before handoff.
7. Save durable lessons only when they will help future work.

## Mental Model

Claude Code should be treated as an agent runtime, not a terminal chatbot. The leverage comes from the full operating surface:

- slash commands
- project memory and `CLAUDE.md`
- permissions
- tools and MCP
- tasks and agents
- plans and reviews
- context controls
- skills and plugins
- IDE, remote, and session bridges when available

Better prompts matter, but the larger gain is designing a better execution environment.

## Beginner Defaults

- Run `/init` or create a project guide for every important repo so future sessions inherit architecture, conventions, and key files.
- Use a status line or other lightweight context/cost visibility when available.
- Use voice input when it helps Umair explain messy context faster, then compress the transcript into a clean task packet.
- Keep context small. Do not paste whole repos, long transcripts, raw logs, or scraped pages unless the task needs them.
- Use `/context` or manual inspection to identify token bloat when sessions feel confused.
- Use `/cost` or available usage dashboards to make spend visible.
- Compact around 60 percent context when continuing the same goal. Clear between unrelated tasks.
- Start ambiguous client, architecture, or automation work in plan-first mode.
- Treat Claude/Codex like a junior teammate: give the problem, constraints, and desired outcome, then ask for approach.
- Build verification into to-dos before execution starts.

## Command Habits

Use the command surface deliberately:

- `/init`: create or refresh project operating context.
- `/plan` or `/ultraplan`: map complex work before execution.
- `/context`: inspect token bloat and loaded files/tools.
- `/cost`: inspect session spend when available.
- `/compact`: preserve useful decisions and drop noisy history.
- `/clear`: reset between unrelated missions.
- `/review`: structured code/workflow review.
- `/security-review`: security-sensitive review before high-risk changes.
- `/memory`: inspect or manage persistent memory when available.
- `/permissions`: review or tune autonomy rules.
- `/mcp`: inspect connected MCP servers and disconnect unused ones.
- `/tasks` and `/agents`: use task/agent management when the active environment supports it.

Do not memorize every command. Standardize the few that reduce rework, token bloat, and approval friction.

## Intermediate Defaults

- Use sub-agents only when the user explicitly asks for agent teams, delegation, or parallel agent work, or where the active environment permits it and the task is split cleanly.
- Convert repeated workflows into skills only after repeated value, clear inputs/outputs, and approval gates.
- Use cheaper or smaller models for bounded research or bulk summarization when available; reserve the strongest model for synthesis, architecture, and final judgment.
- Keep `CLAUDE.md` lean. Route to deeper files instead of loading every playbook into every session.
- Interrupt early when work goes in the wrong direction. Reframe before wasting context.
- Challenge mediocre output. Ask for a different approach, stronger constraints, or a sharper definition of done.
- Use screenshots, browser checks, and tool readbacks for frontend, dashboard, and workflow verification.
- Use hooks, notifications, and loops for monitoring only after approval and when the action is reversible.

## Advanced Defaults

- Use git worktrees for parallel implementation streams when multiple agents or sessions need to edit the same repo.
- Prefer direct APIs over heavy MCP servers when only one narrow endpoint is needed and token budget matters.
- Use scheduled automations for cadence that must survive beyond a local session.
- Use remote/VPS sessions only for long-running tasks that need persistence and have clear approval boundaries.
- Use "ultrathink" or equivalent deep reasoning only for architecture, complex debugging, irreversible workflows, auth, payments, databases, or production-sensitive decisions.
- Configure permissions by allowlisting safe commands and denying destructive actions. Do not trade speed for uncontrolled autonomy.
- Use Agent Teams for large cohesive builds only after file ownership, handoffs, review gates, and merge strategy are clear.
- Use current documentation sources for fast-moving APIs, libraries, and tools.

## Permission Discipline

Permissions are an operating-system feature, not an annoyance.

- Allow recurring safe reads, searches, status checks, and test commands when the repo and sandbox make them safe.
- Keep destructive actions, external sends, production deploys, customer-data mutation, spend, and credential use approval-gated.
- Prefer scoped allow rules over broad bypass modes.
- Deny rules should override allow rules for destructive or production-sensitive actions.
- Review permission rules when a workflow becomes repeated.

## Token-Saving Rules

- Start from IDs, schemas, links, summaries, and file paths.
- Ask for the exact missing detail instead of loading everything.
- Summarize raw outputs before bringing them into durable context.
- Keep task packets short:
  - Outcome
  - Owner
  - Input packet
  - Output packet
  - Tools
  - Approval gate
  - Definition of done
- Route raw data to Airtable, ClickUp, Drive, n8n logs, or storage. Route durable decisions to VCOS HQ.
- If a tool exposes too much context, use a narrower API, export, or summary when possible.
- Disconnect unused MCP servers before heavy sessions when the environment allows it.
- Batch related instructions into one clear prompt instead of stacking follow-up corrections.
- Use targeted file references instead of asking the agent to explore the entire repo.
- Limit shell output before running noisy commands; long logs become long-term context bloat.
- After several compactions, write a session summary and clear instead of trusting degraded context.
- Save stable decisions, not conversations.

## Session Limit Discipline

Use `session-context-discipline.md` when a session is long, expensive, repetitive, or switching missions.

Rules:

- The 1M context window is insurance, not a target.
- Treat the first 0-20 percent of a clean session as prime time.
- Prefer manual handoff + clear before context rot.
- Rewind wrong paths instead of stacking corrections on top of broken attempts.
- Use `/clear` for unrelated work.
- Use `/compact` only with explicit keep-instructions when continuing the same mission.
- Store state in files/systems, not chat history.
- Convert large PDFs/HTML/DOCX to Markdown summaries before loading unless visual/OCR fidelity matters.
- Use sidecar/sub-agent contexts for noisy reading or summarization when allowed; bring back only distilled findings.

Default handoff prompt:

```text
Create a session handoff with outcome, decisions locked, files changed, checks run, blockers, open questions, approval gates, and exact next action. Keep it concise enough to paste into a fresh session.
```

## Managed Agent Evaluation

Managed agent platforms are useful execution layers, especially for API-driven products and teams that do not want to operate containers. They are not automatically a full orchestration layer.

Evaluate them using:

- Agent: model, system prompt, tools, MCP servers, skills.
- Environment: packages, networking, runtime constraints.
- Session: lifecycle, status, version pinning, interruption.
- Events: messages, tool uses, confirmations, and streaming responses.
- Memory: stores, versioning, audit, redaction, and limits.
- Permissions: always-allow vs always-ask boundaries.
- Scheduling: whether cron, heartbeat, webhook triggers, and retries exist natively or need Trigger.dev, GitHub Actions, n8n, or OpenClaw.
- Cost: tokens, runtime, web searches, and tool overhead.

Before implementing managed-agent APIs, verify against current official docs. Treat notes from guides or videos as strategy references, not API truth.

## Coaching Behavior

When Umair asks a broad or fuzzy question, help turn it into a better operator prompt.

Ask:

- What result would make this useful by the end of this session?
- Is this draft-only, internal, client-facing, or production-sensitive?
- What data/source is authoritative?
- What should not happen?
- What approval gate is required?
- What should the output format be?
- What would make this reusable as a skill or template?

Then propose a sharper prompt Umair can reuse.

## Self-Improving Rule

When the same mistake appears twice, or the same workflow succeeds three times:

1. Add or update the relevant playbook, domain README, or skill candidate.
2. Record a durable decision if it changes future behavior.
3. Add a ClickUp task if implementation is still needed.
