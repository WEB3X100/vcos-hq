# Mission Control Replit Launch Packet

Purpose: launch-ready packet for building the VCOS Mission Control dashboard on Replit without reopening the whole HQ.

## Read Order

1. `mission-control-dashboard-prd.md`
2. `gstack-spec-review.md`
3. `flywheel-enhancements-spec.md`
4. `gbrain-office-hours-questions-2026-06-20.md`
5. `ui-design-system-and-screens.md`
6. `data-contract-and-retrieval-safety.md`
7. `browser-harness-launch-qa.md`
8. `replit-file-manifest.md`
9. `replit-agent-build-prompt.md`
10. `mission-control-state.sample.json`

## Launch Boundary

Phase 0 is read-only. The dashboard may display state, decisions, blockers, handoffs, and launch readiness. It must not send messages, mutate CRM/customer records, publish content, spend money, delete files, or deploy production changes.

Phase 0/1 flywheel rule: local laptops and approved agents may generate snapshots such as `state.json`, `kanban.json`, `qa-gates.json`, `journey-map.json`, `codeburn.json`, and `skill-candidates.json`. Replit only renders those snapshots. Replit must not become the actor that runs Hermes, mutates GitHub, promotes skills, posts ClickUp comments, or triggers agent work.

## Source Files

| Source | Purpose |
| --- | --- |
| `../state.json` | Live Mission Control state |
| Future snapshot files | `kanban.json`, `qa-gates.json`, `journey-map.json`, `codeburn.json`, and `skill-candidates.json` once Phase 1 data sync is approved |
| `mission-control-state.sample.json` | Replit app seed data |
| `../dashboard.md` | Current human-readable dashboard |
| `../README.md` | Mission Control operating interface |
| `../../README.md` | Numbered-room interface for Mission Control |
| `../../../00_Live_State_and_GSD/state.md` | HQ live state |
| `../../../../../1.2_Headquarters_Memory/active-context.md` | Current focus and risk |
| `../../../../../1.2_Headquarters_Memory/key-workspaces.md` | ClickUp, repo, and router anchors |

## Definition Of Ready

- PRD has one north-star use case and a clear Phase 0 boundary.
- Data contract defines what fields are rendered from `state.json`.
- UI spec defines modes, widgets, responsive layout, and empty/error states.
- QA plan defines smoke, visual, responsive, data, and approval-gate checks.
- Replit prompt names the exact stack and file manifest.
