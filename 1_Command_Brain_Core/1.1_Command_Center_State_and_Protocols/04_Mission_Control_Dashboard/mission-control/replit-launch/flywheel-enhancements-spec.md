# Mission Control Flywheel Enhancements Spec

**Date:** 2026-06-20  
**Status:** Draft for Replit Phase 0/1 build  
**Scope:** Labyrinth observability, skill promotion, automated QA gates, CodeBurn telemetry, and multi-agent Kanban  
**Boundary:** Replit is a read-only renderer until explicit later phase approval.

## Verdict

Build the flywheel as **snapshot-driven visibility first**. Do not let Replit become the action layer.

The compounding value comes from seeing the loop clearly:

```text
mission idea -> Kanban card -> intern run -> journey map -> automated QA
  -> human approval -> merge/ship -> skill candidate -> better next mission
```

In Phase 0/1, every arrow is represented by source-labeled JSON snapshots and links. The laptops, Hermes, GitHub, GStack, Browser Harness, and CodeBurn remain the systems that produce evidence.

## Phase Rules

| Phase | Flywheel capability | Allowed implementation |
| --- | --- | --- |
| 0 | UI scaffolds flywheel views | Bundled sample + missing-snapshot empty states |
| 1 | Private GitHub snapshot sync | Laptops push JSON; Replit reads snapshots |
| 2 | Authenticated dashboard | Private access + source diagnostics |
| 3 | Draft-only hooks | Create draft skill-promotion request or draft QA request only |
| 4 | Write/action hooks | Per-action human approval required |

## 1. Labyrinth Observability

Purpose: reveal why an agent run succeeded or failed without reopening noisy raw logs.

Dashboard view: `Observability`

Inputs:

- `journey-map.json`
- PR link, handoff link, test evidence link when available

Required fields:

- mission id
- run id
- agent/profile
- outcome
- timeline of summarized steps
- failure/warning step
- model switches
- redaction level

Rules:

- Show summaries, not raw prompts, secrets, API keys, customer records, or full API payloads.
- Every step needs a source or `Not listed`.
- A failed mission should answer: which step, which prompt/tool, which missing test.

## 2. Skill-Creation Pipeline

Purpose: convert repeated wins into reusable VCOS skills.

Dashboard view: `Skill Foundry`

Inputs:

- `skill-candidates.json`
- successful PR handoffs
- approved 7pm brief packets
- QA evidence

Pipeline:

```text
detected -> drafted -> reviewed -> approved -> promoted -> retired
```

`Promote to Skill` behavior:

- Phase 0/1: disabled/read-only label only.
- Phase 3: may create a **draft** promotion request, not a durable skill.
- Phase 4: any durable skill write still requires human approval and skill governance review.

Promotion trigger:

- 3+ successful uses, or
- one high-leverage win with clear repeatability, owner department, input packet, output packet, tools, approval gate, and failure mode.

## 3. Automated GStack QA Gates

Purpose: protect Umair from reviewing ungraded work.

Dashboard view: `QA Gates`

Inputs:

- `qa-gates.json`
- GStack CEO/Eng/Design review packet
- Browser Harness / Playwright smoke and visual evidence
- security/approval gate check

Default threshold:

- overall score >= 8/10
- no critical approval-gate violation
- no broken build/test evidence

If below threshold:

- status becomes `returned_to_intern`
- item does not appear as human approval-ready
- dashboard shows return reasons

## 4. Telemetry And Token Maxing

Purpose: catch costly loops, retries, stalled tasks, and model/task mismatch.

Dashboard view: `Cost`

Inputs:

- `codeburn.json`

Watch conditions:

- loop count > 3
- repeated retries on same task
- no progress after a configured time window
- cost spike by mission, model, or agent
- high-cost model used for low-complexity work

Dashboard behavior:

- Show highest-cost tasks first.
- Show `watch` and `intervene` statuses distinctly.
- Recommend review labels only; do not auto-switch models from Replit.

## 5. Multi-Agent Kanban Orchestration

Purpose: replace a linear mission queue with a visible software-factory board.

Dashboard view: `Kanban`

Columns:

- Triage
- Ready
- In Progress
- Review
- Done
- Blocked

Card fields:

- id
- title
- owner agent
- source
- acceptance criteria
- QA score
- branch
- approval gate
- status

Rules:

- Phase 0/1 cards are read-only.
- Replit must not move cards, assign agents, create ClickUp tasks, or trigger work.
- The orchestrator may break work into subtasks only from approved local/Hermes workflows, then push a snapshot later.

## Secure Replit Architecture

Phase 1 target:

```text
Laptop 1 / Laptop 2 / Hermes / GStack / CodeBurn
  -> write sanitized JSON snapshots locally
  -> push snapshots to private VCOS HQ GitHub repo on approved cadence
  -> Replit pulls snapshots
  -> Replit renders source-labeled widgets
```

Air-gap requirement:

- The dashboard reads from GitHub or bundled files.
- The dashboard never holds production secrets.
- The dashboard never opens local laptop ports.
- The dashboard never has credentials that can mutate VCOS, ClickUp, GitHub, Drive, CRM, or client systems in Phase 0/1.

## Build Priority

1. Keep current Phase 0 cockpit shippable.
2. Add flywheel modes with missing-snapshot empty states.
3. Add sample snapshot loaders after core UI is green.
4. Add Browser Harness checks for read-only controls.
5. Only after one useful week, approve private GitHub snapshot sync.

## Kill Criteria

Pause the flywheel expansion if:

- Replit needs secrets before Phase 2.
- Any button looks executable while still read-only.
- Observability exposes raw prompts, customer data, or API payloads.
- Kanban becomes a second source of truth instead of a snapshot.
- QA scores become decorative and do not block human review.
