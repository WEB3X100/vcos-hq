# Replit Agent Build Prompt

Paste this into Replit Agent after creating a new React + TypeScript app.

```text
Build a Phase 0 read-only VCOS Mission Control dashboard.

Use React + TypeScript + Vite. Do not add a backend. Do not require secrets. The app must run on Replit with:

npm run dev

Use this file structure:

- package.json with dev/build/preview scripts
- index.html
- vite.config.ts
- src/App.tsx
- src/main.tsx
- src/styles.css
- src/data/mission-control-state.sample.json
- src/lib/state.ts
- src/lib/modes.ts
- src/lib/freshness.ts
- src/lib/sourceLinks.ts
- src/components/AppShell.tsx
- src/components/ModeSwitcher.tsx
- src/components/FreshnessBanner.tsx
- src/components/NowPanel.tsx
- src/components/DecisionQueue.tsx
- src/components/CubicleGrid.tsx
- src/components/FlywheelMetrics.tsx
- src/components/ClientLaneList.tsx
- src/components/MissionQueue.tsx
- src/components/KanbanBoard.tsx
- src/components/JourneyMap.tsx
- src/components/QAGateScorecard.tsx
- src/components/TelemetryCostPanel.tsx
- src/components/SkillCandidatePanel.tsx
- src/components/ApprovalGatePanel.tsx
- src/components/SourceLinks.tsx
- src/components/LaunchReadiness.tsx
- src/components/EmptyState.tsx
- public/data/state.json
- public/data/kanban.json
- public/data/qa-gates.json
- public/data/journey-map.json
- public/data/codeburn.json
- public/data/skill-candidates.json

Product requirements:

1. The app is a dense operational cockpit, not a landing page.
2. Load /data/state.json first. If fetch fails, fall back to bundled sample data copied from this launch packet's mission-control-state.sample.json and show a warning.
3. Show updated_at and stale-state warning if older than 24 hours.
4. Support modes: brief, intern_mission, client_lane, office_hours, approval_review, build, observability, qa_gates, cost, skill_foundry, kanban.
5. Reorder widgets by mode using deterministic mapping.
6. Every operational widget must show a source label.
7. Pending decisions must be highly visible.
8. Approval-gated actions must be read-only. Do not render enabled action buttons for sends, CRM mutations, publishing, spending, deletion, or deployment.
9. Mobile layout must show active lane and pending decisions before metrics.
10. No raw client data. Only summaries from state.json.
11. Add flywheel widgets for Labyrinth-style observability, automated QA gates, CodeBurn telemetry, skill candidates, and Kanban. These read optional JSON snapshots only. If files are absent, show explicit empty states.
12. Do not make Replit execute Hermes, GitHub mutations, ClickUp updates, skill promotion, QA reruns, or Kanban moves. Any related affordance must be disabled/read-only in Phase 0/1.
13. Automated QA items below 8/10 must be labeled returned to intern, not approval-ready.
14. Observability views must show summaries and redaction status only, never raw secrets, customer data, or full API payloads.

Data shape:

Use this TypeScript contract:

type MissionControlState = {
  updated_at: string;
  week: number;
  flywheel: {
    delegation_level: string;
    brief_score_last?: number;
    brief_score_7pm_cron?: number;
    brief_delivery_streak?: number;
    dealership_demo_score?: number;
  };
  cubicle_l1: CubicleState;
  cubicle_l2: CubicleState;
  github: {
    coordination_repo: string;
    local_path_recommended?: string;
    open_prs: string[];
    open_branches: string[];
  };
  client_lanes: Record<string, {
    priority: string;
    bullets: string[];
  }>;
  tonight_chunk: {
    lane: string;
    task: string;
    done_means: string;
    status: string;
    l1_complete?: string;
  };
  parking_lot: string[];
  flywheel_snapshots?: Record<string, {
    path: string;
    status: "missing" | "sample" | "fresh" | "stale" | "blocked";
    updated_at?: string;
    source?: string;
  }>;
};

type CubicleState = {
  name: string;
  device: string;
  channel: string;
  profile: string;
  status: string;
  last_session?: string | null;
  active_mission?: string | null;
  active_branch?: string | null;
  last_push?: string | null;
  pending_decisions_for_umair: string[];
};

Design requirements:

- restrained neutral palette with status colors
- compact typography
- stable panel dimensions
- no nested cards
- no decorative gradient blobs
- no hero section
- 6-8px radius max
- source labels on cards
- clear empty states

Acceptance tests:

- npm run build succeeds
- desktop viewport shows lane, pending decisions, cubicles, and client lanes
- mobile viewport shows active lane and decisions before metrics
- changing modes changes widget order
- missing data warning appears if /data/state.json is unavailable
- stale data warning appears if updated_at is old
- no enabled write/action buttons exist in Phase 0
- flywheel modes render either snapshot data or missing-snapshot empty states
- Promote to Skill / Assign Agent / Run QA / Move Card controls are disabled or absent
- below-threshold QA is not shown as ready for human approval

After building, provide:

- files created
- how to run
- what data file to replace
- any risks or missing requirements
```
