# Replit File Manifest

Purpose: exact file structure Replit Agent or L2 should create for the Phase 0 dashboard app.

## Recommended App Tree

```text
mission-control-dashboard/
  README.md
  package.json
  index.html
  vite.config.ts
  tsconfig.json
  src/
    App.tsx
    main.tsx
    styles.css
    data/
      mission-control-state.sample.json
    lib/
      state.ts
      modes.ts
      freshness.ts
      sourceLinks.ts
    components/
      AppShell.tsx
      ModeSwitcher.tsx
      FreshnessBanner.tsx
      NowPanel.tsx
      DecisionQueue.tsx
      CubicleGrid.tsx
      FlywheelMetrics.tsx
      ClientLaneList.tsx
      MissionQueue.tsx
      KanbanBoard.tsx
      JourneyMap.tsx
      QAGateScorecard.tsx
      TelemetryCostPanel.tsx
      SkillCandidatePanel.tsx
      ApprovalGatePanel.tsx
      SourceLinks.tsx
      LaunchReadiness.tsx
      EmptyState.tsx
  public/
    data/
      state.json
      kanban.json
      qa-gates.json
      journey-map.json
      codeburn.json
      skill-candidates.json
```

## `package.json` Requirements

```json
{
  "scripts": {
    "dev": "vite --host 0.0.0.0",
    "build": "tsc && vite build",
    "preview": "vite preview --host 0.0.0.0"
  },
  "dependencies": {
    "@vitejs/plugin-react": "latest",
    "vite": "latest",
    "typescript": "latest",
    "react": "latest",
    "react-dom": "latest",
    "lucide-react": "latest"
  },
  "devDependencies": {}
}
```

## State Loading

Phase 0 should load `/data/state.json` first. If it fails, fall back to bundled `mission-control-state.sample.json`. Copy the initial sample from this packet's `mission-control-state.sample.json`.

Optional flywheel files for Phase 1 should be loaded independently. Missing optional files must not break the dashboard:

- `/data/kanban.json`
- `/data/qa-gates.json`
- `/data/journey-map.json`
- `/data/codeburn.json`
- `/data/skill-candidates.json`

Behavior:

- Success: render dashboard.
- Fetch fails: render fallback data and warning.
- JSON invalid: render error state.
- `updated_at` older than 24 hours: render stale warning.
- Optional snapshot missing: render missing-snapshot empty state.
- Optional snapshot invalid: render snapshot-specific warning, not a full app crash.

## README Requirements

The generated Replit app README must include:

- What the app does.
- Phase 0 read-only boundary.
- How to run locally.
- How to replace `public/data/state.json`.
- How to publish on Replit.
- What not to add without approval.
