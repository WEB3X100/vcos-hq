# Ubiquitous Language

Use these terms consistently across VCOS, ClickUp, Drive, Claude, Codex, and domain packs.

| Term | Meaning |
| --- | --- |
| VCOS HQ | The command brain: routing, memory, protocols, decisions, cross-client orchestration. |
| Command Brain | The central system that decides where work belongs and what context to load. |
| Second Brain | The VCOS memory and retrieval layer: context, connections, notes, transcripts, decisions, project memory, and GBrain-backed lookup. It remembers but does not act on its own. |
| AI OS | The VCOS action layer: skills, automations, routines, Mini Interns, and operator surfaces that do work from the Second Brain with approval gates. |
| Domain Pack | A specialized limb for a client, industry, or workflow family. |
| Limb | A domain pack or client repo that executes specialized work but does not own headquarters memory. |
| Deep Module | A domain pack with a small README interface and hidden implementation details. |
| Interface | The short README or protocol an agent reads first. |
| Implementation | Messy details, raw data, swipe files, historical notes, and execution artifacts hidden from default context. |
| Command Room | A ClickUp list used for focused execution control. |
| Production Control Room | ClickUp home for reusable systems, MCP, n8n, skills, templates, and production infrastructure. |
| Delivery Control Room | ClickUp home for active client outcomes, demos, proposals, blockers, and close paths. |
| Q3 Command Center | ClickUp home for Umair bandwidth, day-job work, investments, tools, and personal operations. |
| Active Context | The compact current-state file an agent reads before working. |
| Decision | A durable choice that should guide future agents. |
| Blocker | A specific unresolved issue preventing progress. |
| SOP | A repeatable process. It becomes a skill only after repeated value. |
| Skill | A packaged agent behavior with explicit trigger, inputs, workflow, and output standards. |
| Skill Candidate | A SOP being tested before promotion into a permanent skill. |
| Context Rot | Degradation from too much raw context, stale chat history, or noisy tool output. |
| Progressive Context Loading | Load the smallest useful file first, then deeper files only when needed. |
| Never Repeat A Bug | When a mistake is found, update AGENTS.md or the domain README with a negative constraint. |
| Mini Intern | A specialized AI employee template with separate memory, skills, tools, credentials, approval gates, and handoff packets. |
| Least Privilege | Give each Mini Intern only the tools, secrets, memory, schedules, and external access required for its role. |
| Handoff Packet | A short structured summary passed between agents instead of noisy full chat histories. |
| Visual Format Inversion | Identify the expected visual pattern in a niche, then deliberately use a contrasting format to break feed fatigue. |
| Idea Explosivity | A 1-100 shock score for how strongly an idea contrasts the viewer's current belief with a new useful reality. |
| Shock Score | Short name for Idea Explosivity. Scores below 70 usually need a sharper contrast before production. |
| Visual Pacifier | Subtle continuous motion that holds attention during educational content without distracting from the main point. |
| Four Hook Commandments | Reviewer/QA rubric for media hooks: Alignment, Speed to Value, Clarity, and Curiosity. |
| Visual-Audio Alignment | The visual, text, and spoken/written hook must reinforce the same idea without creating comprehension drag. |
| 3-5 Word Rule | On-screen hook text should usually be three to five words so it is instantly readable in feed. |
| Self-Improving Loop | When output fails review, log the failure and update the relevant skill, reference, or negative constraint so it is less likely to repeat. |
| Recursive Self-Improvement Loop | The VCOS operating loop where sensors, policies, tools, QA gates, outputs, feedback, learning updates, and re-tests make Mini Interns and workflows improve over time. |
| Sensor Layer | The observable inputs a Mini Intern or workflow can learn from, such as ClickUp tasks, Git commits, forms, CRM-safe logs, generated outputs, client feedback, and dashboard metrics. |
| Policy Layer | The rules that define what an agent may do, what requires approval, what must be logged, and what must never happen. |
| Monitoring Intern | A Sentinel-style reviewer that watches failed tasks, repeated corrections, rejected outputs, and winning patterns, then routes improvements into skills, policies, trackers, or project manifests. |
