# Data Contract And Retrieval Safety

Purpose: make the dashboard retrieval-safe, source-labeled, and personalized by task without hallucinating.

## Source Hierarchy

| Rank | Source | Dashboard behavior |
| --- | --- | --- |
| 1 | `../state.json` | Structured render |
| 2 | `../dashboard.md` | Link and optionally display summary excerpts written by humans/agents |
| 3 | `../../../05_Office_Hours_and_Session_Briefs/session-briefs/README.md` | Router link only |
| 4 | `../../../00_Live_State_and_GSD/state.md` | Link only in Phase 0 |
| 5 | ClickUp URLs in `key-workspaces.md` | External links only |
| 6 | Optional Phase 1 snapshot JSON files | Render only if present and source-labeled |

Phase 0 must not crawl the repository. It uses known files only.

## `state.json` Contract

Expected fields:

```ts
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
  flywheel_snapshots?: {
    kanban?: SnapshotStatus;
    qa_gates?: SnapshotStatus;
    journey_map?: SnapshotStatus;
    codeburn?: SnapshotStatus;
    skill_candidates?: SnapshotStatus;
  };
};

type SnapshotStatus = {
  path: string;
  status: "missing" | "sample" | "fresh" | "stale" | "blocked";
  updated_at?: string;
  source?: string;
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
```

## Derived Fields Allowed

The dashboard may derive:

- `isStale`: true if `updated_at` is older than 24 hours.
- `decisionCount`: total pending decisions from L1 and L2.
- `laneCount`: number of entries in `client_lanes`.
- `hasActiveL2Mission`: true if `cubicle_l2.active_mission` exists.
- `launchStatus`: computed from local QA checklist, not from business state.

The dashboard must not invent:

- owner names not present in source
- dates not present in source
- client status not present in source
- approval outcomes
- task completion
- revenue claims

## Personalization Engine

Personalization is deterministic in Phase 0.

```ts
type DashboardMode =
  | "brief"
  | "intern_mission"
  | "client_lane"
  | "office_hours"
  | "approval_review"
  | "build"
  | "observability"
  | "qa_gates"
  | "cost"
  | "skill_foundry"
  | "kanban";

type WidgetId =
  | "now"
  | "decisions"
  | "cubicles"
  | "flywheel"
  | "client_lanes"
  | "mission_queue"
  | "office_hours"
  | "approval_gates"
  | "journey_map"
  | "qa_scorecard"
  | "telemetry_cost"
  | "skill_candidates"
  | "kanban_board"
  | "source_links"
  | "launch_readiness";
```

Widget order:

| Mode | Widget order |
| --- | --- |
| `brief` | `now`, `decisions`, `client_lanes`, `cubicles`, `flywheel`, `source_links` |
| `intern_mission` | `mission_queue`, `cubicles`, `decisions`, `source_links`, `launch_readiness` |
| `client_lane` | `client_lanes`, `decisions`, `now`, `source_links` |
| `office_hours` | `office_hours`, `decisions`, `source_links`, `launch_readiness` |
| `approval_review` | `decisions`, `approval_gates`, `client_lanes`, `source_links` |
| `build` | `launch_readiness`, `source_links`, `mission_queue`, `decisions` |
| `observability` | `journey_map`, `qa_scorecard`, `decisions`, `source_links` |
| `qa_gates` | `qa_scorecard`, `launch_readiness`, `mission_queue`, `source_links` |
| `cost` | `telemetry_cost`, `mission_queue`, `decisions`, `source_links` |
| `skill_foundry` | `skill_candidates`, `approval_gates`, `source_links` |
| `kanban` | `kanban_board`, `qa_scorecard`, `decisions`, `source_links` |

## Phase 1 Flywheel Snapshot Contracts

These files are optional until Umair approves the GitHub snapshot sync. Replit reads them only from `/public/data/` or approved GitHub raw URLs. If absent, render empty states.

### `kanban.json`

```ts
type KanbanSnapshot = {
  updated_at: string;
  source: string;
  columns: Array<{
    id: "triage" | "ready" | "in_progress" | "review" | "done" | "blocked";
    title: string;
    cards: Array<{
      id: string;
      title: string;
      owner_agent?: string;
      source?: string;
      acceptance_criteria?: string[];
      qa_score?: number;
      branch?: string;
      approval_gate?: string;
      status: string;
    }>;
  }>;
};
```

### `qa-gates.json`

```ts
type QAGatesSnapshot = {
  updated_at: string;
  source: string;
  threshold: number;
  reviews: Array<{
    mission_id: string;
    branch?: string;
    overall_score: number;
    status: "passed" | "returned_to_intern" | "blocked" | "pending";
    reviewers: Array<{
      lane: "gstack_ceo" | "gstack_eng" | "gstack_design" | "browser_harness" | "security_approval";
      score?: number;
      finding_summary: string;
      evidence_link?: string;
    }>;
    return_reasons?: string[];
  }>;
};
```

### `journey-map.json`

```ts
type JourneyMapSnapshot = {
  updated_at: string;
  source: string;
  runs: Array<{
    mission_id: string;
    run_id: string;
    agent: string;
    outcome: "succeeded" | "failed" | "blocked" | "cancelled";
    started_at?: string;
    ended_at?: string;
    steps: Array<{
      timestamp?: string;
      type: "prompt" | "tool_call" | "api_response" | "model_switch" | "test" | "error" | "handoff";
      status: "ok" | "warning" | "failed";
      summary: string;
      source_file?: string;
      redaction_level: "none" | "summary_only" | "sensitive_removed";
    }>;
  }>;
};
```

### `codeburn.json`

```ts
type CodeBurnSnapshot = {
  updated_at: string;
  source: string;
  budget_period: string;
  tasks: Array<{
    task_id: string;
    agent?: string;
    model?: string;
    tokens_in?: number;
    tokens_out?: number;
    estimated_cost_usd?: number;
    duration_minutes?: number;
    retry_count?: number;
    loop_count?: number;
    status: "normal" | "watch" | "intervene" | "blocked";
  }>;
};
```

### `skill-candidates.json`

```ts
type SkillCandidatesSnapshot = {
  updated_at: string;
  source: string;
  candidates: Array<{
    id: string;
    title: string;
    trigger_phrase?: string;
    evidence_runs: string[];
    status: "detected" | "drafted" | "reviewed" | "approved" | "promoted" | "retired";
    owner_department: string;
    approval_required: true;
    proposed_path?: string;
  }>;
};
```

## Source Labels

Every widget must show a source label.

Examples:

- `Source: state.json > tonight_chunk`
- `Source: state.json > cubicle_l2`
- `Source: key-workspaces.md > AgentOSync Daily Operating Route`
- `Source: approval-gates.md`

## Retrieval Guardrails

- If source data is missing, show a missing-state warning.
- If source data is stale, show a stale-state warning.
- If two sources conflict, show both links and mark `source conflict`.
- If a field is absent, render `Not listed` instead of guessing.
- If an action is gated, render `Approval required` and do not show an enabled action button.
- If the dashboard cannot access ClickUp/Drive/GitHub live data, label those cards as links, not synced state.
- If a snapshot includes raw prompts, API payloads, secrets, customer records, or client-private fields, do not render the raw value. Render `Sensitive details redacted`.
- If automated QA score is below 8/10 or has a critical finding, keep the item out of human approval-ready status and label it `Return to intern`.
- If a skill candidate is not human-approved, keep any "Promote to Skill" affordance disabled and label it `Draft only`.

## AIS-OS Four C Mapping

| Four C | Dashboard implementation |
| --- | --- |
| Context | Render current state, active context, source links |
| Connections | Show ClickUp/GitHub/Hermes/Drive anchors as links |
| Capabilities | Show what L1/L2 can do in current phase |
| Cadence | Show 7pm brief, heartbeat, mission queue, and stale-state warnings |

## GBrain/QMD Future Path

Phase 0: known files only.

Phase 1 candidate: QMD indexes approved Markdown collection:

- `00_Live_State_and_GSD/state.md`
- `1.2_Headquarters_Memory/active-context.md`
- `1.2_Headquarters_Memory/key-workspaces.md`
- `04_Mission_Control_Dashboard/mission-control/`
- `05_Office_Hours_and_Session_Briefs/session-briefs/README.md`

Phase 2 candidate: GBrain synthesis over approved summaries only. No client/private data import without explicit approval.
