# UI Design System And Screens

Purpose: Impeccable + Open Design style requirements for a polished Replit dashboard.

## Design Principle

Mission Control should feel like a quiet command cockpit: dense, legible, fast to scan, and built for repeated daily use. Avoid marketing hero sections, decorative cards, gradient blobs, oversized headings, or generic SaaS filler.

## Visual Tone

| Attribute | Requirement |
| --- | --- |
| Density | High information density with clear grouping |
| Palette | Neutral base with restrained status colors; avoid one-hue purple/blue dominance |
| Typography | Compact headings, readable body, no viewport-scaled font sizes |
| Corners | 6-8px radius max for cards and panels |
| Motion | Minimal; only for loading or freshness pulse |
| Icons | Use lucide icons if available; otherwise text labels are acceptable for Phase 0 |
| Layout | Full-width app shell, not floating marketing sections |

## Suggested Tokens

```css
:root {
  --bg: #f7f8fa;
  --panel: #ffffff;
  --panel-muted: #f0f3f6;
  --text: #17202a;
  --muted: #5f6b7a;
  --line: #d9dee5;
  --accent: #256f8f;
  --success: #2f7d4f;
  --warning: #a86418;
  --danger: #b33a3a;
  --focus: #6b5b95;
  --radius: 8px;
}
```

## App Shell

Desktop layout:

- Left rail: modes, source diagnostics, launch readiness.
- Top bar: updated time, data freshness, current lane, search/filter input.
- Main area: mode-specific widgets.
- Right rail: pending decisions and source links.

Mobile layout:

1. Current lane and done-means
2. Pending decisions
3. Cubicle status
4. Mode switcher
5. Selected mode widgets
6. Source diagnostics

## Required Components

| Component | Purpose | Design notes |
| --- | --- | --- |
| `ModeSwitcher` | Switches Brief, Intern Mission, Client Lane, Office Hours, Approval, Build | Segmented control, stable height |
| `FreshnessBanner` | Shows fresh/stale/missing data | Top band, not modal |
| `NowPanel` | One active lane and done-means | Highest priority; avoid huge headline |
| `DecisionQueue` | Pending Umair decisions | Always visible on desktop |
| `CubicleGrid` | L1/L2 status | Two compact panels |
| `FlywheelMetrics` | Streaks, scores, delegation level | Small metric cells |
| `ClientLaneList` | Dealership, AMAX, Content Intel, AgentOSync | Status rows, not oversized cards |
| `MissionQueue` | Active mission, branch, handoff | Use monospace for branch/file names |
| `KanbanBoard` | Triage, Ready, In Progress, Review, Done, Blocked | Compact columns; cards show owner, QA score, branch, gate |
| `JourneyMap` | Labyrinth-style run observability | Timeline with prompt/tool/API/model/test summaries, never raw secrets |
| `QAGateScorecard` | GStack + Browser Harness review result | Score, pass/return status, critical findings |
| `TelemetryCostPanel` | CodeBurn cost and loop visibility | Highlight runaway loops and high-cost tasks |
| `SkillCandidatePanel` | Skill promotion pipeline | Show disabled `Promote to Skill` control until Phase 3 |
| `ApprovalGatePanel` | Shows what cannot be executed | Clear read-only labels |
| `SourceLinks` | Links back to owning files | Source label on every operational claim |
| `LaunchReadiness` | Replit launch checklist | Checklist with pass/warn/block states |

## Screen Specs

### 1. Brief Mode

Purpose: decide the next 90-minute focus.

Visible order:

1. `NowPanel`
2. `DecisionQueue`
3. `ClientLaneList`
4. `FlywheelMetrics`
5. `SourceLinks`

### 2. Intern Mission Mode

Purpose: make L2 execution unambiguous.

Visible order:

1. Active mission
2. Active branch
3. Handoff file path
4. Test contract
5. PR/merge gate
6. Blockers for Umair

### 3. Client Lane Mode

Purpose: route attention to revenue/proof lanes.

Visible order:

1. Dealership OS
2. AMAX
3. Content Intel
4. AgentOSync GTM
5. Parking lot

Each lane should show: priority, current sentence, next action, approval gate, source.

### 4. Office Hours Mode

Purpose: pressure-test plans before they become intern-ready.

Visible order:

1. Thesis
2. Strongest evidence
3. Riskiest assumption
4. Kill criteria
5. Next test

### 5. Approval Review Mode

Purpose: separate human approvals from passive status.

Visible order:

1. Pending decisions from `state.json`
2. Approval-gated action classes
3. Draft-only lanes
4. External surfaces blocked until approval

### 6. Build Mode

Purpose: know whether the dashboard can launch on Replit.

Visible order:

1. Replit file manifest
2. Data source status
3. Browser QA checklist
4. Accessibility checks
5. Deployment gate

### 7. Observability Mode

Purpose: diagnose why an agent succeeded or failed without reopening noisy session logs.

Visible order:

1. Run outcome and mission id
2. Timeline of prompt, tool call, API response, model switch, test, error, and handoff summaries
3. Failed or warning step highlighted
4. Source file / PR / handoff links
5. Redaction status

### 8. QA Gates Mode

Purpose: ensure automated review defends Umair's attention before work reaches human approval.

Visible order:

1. Overall QA score and threshold
2. GStack CEO/Eng/Design findings
3. Browser Harness result and screenshot/evidence link
4. Security/approval gate finding
5. Return-to-intern reasons when score is below 8/10

### 9. Cost Mode

Purpose: spot expensive loops and model/task mismatches early.

Visible order:

1. Current budget period
2. Highest-cost tasks
3. Loop and retry warnings
4. Model/task pairs needing cheaper routing
5. Source snapshot and update time

### 10. Skill Foundry Mode

Purpose: turn repeated wins into reusable skills without bypassing review.

Visible order:

1. Skill candidates
2. Evidence runs
3. Owner department
4. Approval status
5. Disabled `Promote to Skill` action until Phase 3 draft hooks are approved

### 11. Kanban Mode

Purpose: show the software factory board without making Replit the task runner.

Visible order:

1. Triage
2. Ready
3. In Progress
4. Review
5. Done
6. Blocked

## Empty/Error States

| State | UI copy |
| --- | --- |
| No pending decisions | `No human decisions are currently listed in state.json.` |
| Missing state | `Mission Control state file is missing. Use bundled sample only.` |
| Stale state | `State may be stale. Verify before acting.` |
| No active mission | `No L2 mission is queued. L2 should idle.` |
| Source unavailable | `Source file not available in this build. Open HQ repo.` |
| Missing flywheel snapshot | `No approved snapshot found for this flywheel view yet.` |
| QA below threshold | `Automated QA returned this to the intern before human review.` |
| Skill candidate draft | `Skill candidate is draft-only until Umair approves promotion.` |

## Anti-Patterns

- Do not put cards inside cards.
- Do not create a landing page before the dashboard.
- Do not hide pending approvals below the fold on desktop.
- Do not make action buttons look executable in Phase 0.
- Do not show raw client/customer data.
- Do not show raw prompts, API payloads, tokens, or secrets in observability views.
- Do not make `Promote to Skill`, `Assign Agent`, `Run QA`, or `Move Card` controls executable in Phase 0/1.
- Do not use oversized hero headings inside dashboard panels.
- Do not use visual decoration that competes with decisions and blockers.
