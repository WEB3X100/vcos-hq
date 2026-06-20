# Mission Control Dashboard PRD

**Product:** VCOS Mission Control  
**Host target:** Replit first; default Replit URL for proof, custom domain after one useful week.  
**Phase:** Phase 0 read-only cockpit  
**Owner:** VCOS HQ / Mission Control  
**Primary users:** Umair, L1 Chief of Staff Hermes, L2 NeuralSync Intern
**Operating boundary:** Replit renders approved snapshots only; local laptops/Hermes/GitHub own all actions.

## One Sentence

Mission Control is a read-only cockpit that shows what VCOS should do next, what needs Umair approval, what L1/L2 Hermes are doing, and which source file owns the truth.

## Problem

VCOS has enough useful state that humans and agents can lose time opening the wrong files, reading stale session briefs, or acting from noisy context. The dashboard needs to make the active operating picture visible without letting agents mutate anything.

## Goals

- Show the live L1/L2 status from `state.json`.
- Show the current focus lane, done-means, blockers, and pending decisions.
- Route humans and agents to the correct source file with one click.
- Personalize visible widgets by selected work mode.
- Make approval gates impossible to miss.
- Prepare a Replit app that can evolve from static/read-only to API-backed later.
- Visualize the closed-loop flywheel: observe runs, grade QA, track cost, route Kanban work, and harvest skill candidates without enabling autonomous writes.

## Non-Goals

- No external sends.
- No CRM, ClickUp, Drive, QuickBooks, or client-system mutation.
- No publishing or public claims.
- No broad HQ search from the app.
- No private/client raw data in public UI.
- No autonomous agent action from dashboard buttons in Phase 0.
- No live prompt/tool/API log streaming from Hermes or laptops in Phase 0.
- No skill promotion, QA rerun, Kanban assignment, or GitHub mutation initiated from Replit in Phase 0/1.

## Primary Workflow

1. Umair opens the dashboard.
2. The dashboard loads `state.json` or a bundled sample during local proof.
3. The top band shows active lane, tonight chunk, and pending decisions.
4. Umair switches mode: Brief, Intern Mission, Client Lane, Office Hours, Approval Review, or Build.
5. The dashboard reorders widgets for that mode.
6. Each widget links back to the source file or operating surface.
7. If data is stale or missing, the dashboard shows a visible stale-state warning instead of hallucinating.
8. Optional flywheel widgets render only source-labeled snapshot data. Missing snapshots show empty states, not guesses.

## User Modes

| Mode | First question answered | Primary widgets |
| --- | --- | --- |
| Brief | What should I focus on next? | Active lane, blockers, approvals, next 90-minute block |
| Intern Mission | What should L2 do and what branch owns it? | Mission queue, active branch, test contract, handoff status |
| Client Lane | What is moving revenue/proof? | Dealership, AMAX, Content Intel, AgentOSync GTM |
| Office Hours | What assumption needs pressure-testing? | thesis, strongest evidence, riskiest assumption, kill criteria |
| Approval Review | What needs Umair yes/no/revise? | pending decisions, approval gates, source links |
| Build | What must exist before Replit launch? | file manifest, data contract, QA checklist, deployment status |
| Observability | Why did the agent succeed or fail? | journey map, prompts/tools summary, failures, model switches |
| QA Gates | Did automated review protect Umair's attention? | GStack review, Browser Harness status, score, return reasons |
| Cost | Is any agent burning tokens or looping? | CodeBurn telemetry, loop warnings, model/task cost |
| Skill Foundry | What repeatable win should become a skill? | promotion candidates, evidence, approval status |
| Kanban | Where is each mission in the factory? | Triage, Ready, In Progress, Review, Done, Blocked |

## Phase 0 Data Sources

| Source | Use | Handling |
| --- | --- | --- |
| `state.json` | Cubicles, flywheel, lanes, tonight chunk, parking lot | Render structured fields only |
| `dashboard.md` | Current narrative dashboard | Link, do not parse deeply |
| `session-briefs/README.md` | Office Hours router | Link only |
| `key-workspaces.md` | ClickUp anchors | Link only |
| `kanban.json` | Phase 1 mission board snapshot | Optional read-only render |
| `qa-gates.json` | Phase 1 GStack/Browser Harness review snapshot | Optional read-only render |
| `journey-map.json` | Phase 1 Labyrinth-style observability snapshot | Optional read-only render with redactions |
| `codeburn.json` | Phase 1 telemetry/cost snapshot | Optional read-only render |
| `skill-candidates.json` | Phase 1 skill-promotion candidate snapshot | Optional read-only render |

## Required Screens

- Dashboard home
- Mode-specific cockpit view
- Approval queue view
- Mission queue view
- Multi-agent Kanban view
- Journey Map / Observability view
- QA Gates view
- Telemetry & Cost view
- Skill Foundry candidate view
- Data/source diagnostics view
- Launch readiness view

## Required States

- Loading
- Fresh data
- Stale data
- Missing state file
- Empty mission queue
- No pending approvals
- Source unavailable
- Mobile compact layout

## Acceptance Criteria

- The app can be launched on Replit with one run command.
- No secrets are required for Phase 0.
- `state.json` can be replaced with a newer file without code changes.
- Every visible operational claim has a source label.
- Pending decisions are visibly separated from passive status.
- Approval-gated actions are displayed as read-only.
- "Promote to Skill" is displayed as a disabled/read-only candidate control until Phase 3 draft-only hooks are explicitly approved.
- Automated QA score is visible before human approval review when `qa-gates.json` exists; scores below 8/10 are marked `returned_to_intern`.
- Journey-map event summaries never show secrets, raw client data, or unredacted API payloads.
- Telemetry flags repeated loops, high cost, and stalled tasks from snapshots only.
- Mobile viewport shows active lane, decisions, and cubicles without overlap.
- Desktop viewport shows dense but scannable operational cards.

## Phase Gates

| Phase | Allowed | Gate |
| --- | --- | --- |
| 0 | Read-only UI over static/bundled JSON | Current sprint |
| 1 | Pull state and flywheel snapshots from private GitHub raw or approved API | Umair approves data source and redaction rules |
| 2 | Authenticated private dashboard | Auth decision and secret handling review |
| 3 | Draft-only action hooks, including skill-promotion draft requests | Approval-gate UI and audit log exist |
| 4 | Any write action | Explicit human approval per action class |
