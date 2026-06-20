# Adversarial Launch Review

Purpose: skeptical review gate before building or publishing the Replit dashboard.

## Current Verdict

**Buildable, but only as Phase 0 read-only.** Do not add auth, live GitHub sync, ClickUp sync, write actions, or agent buttons in the first build.

## Main Findings

| Severity | Finding | Fix |
| --- | --- | --- |
| High | Dashboard could imply action authority if buttons are enabled | Phase 0 buttons must be disabled or rendered as status labels |
| High | Static `state.json` may become stale and mislead Umair | Show freshness banner and stale warning |
| High | Replit published filesystem should not be treated as source of truth | Use bundled/read-only JSON; future storage requires approval |
| Medium | Too many widgets could bury the next action | Default Brief mode must put active lane and decisions first |
| Medium | File paths moved during command-center reorg | Use numbered-room paths in source links |
| Medium | AI-generated UI may become generic SaaS card wall | Enforce cockpit layout and no nested cards |
| Low | Replit default URL may be unattractive | Use default URL for proof; custom domain after one week |

## Required Changes Before Replit Build

- Include `public/data/state.json` sample.
- Include `src/data/mission-control-state.sample.json` fallback.
- Implement `FreshnessBanner`.
- Implement `ApprovalGatePanel`.
- Implement source labels.
- Implement mode-to-widget deterministic ordering.
- Include launch README.

## Required Changes Before Public Sharing

- Confirm no raw client data.
- Confirm no secrets in repo.
- Run browser QA.
- Human approval for default Replit URL sharing.
- Separate approval before custom domain.

## Do Not Add Yet

- User login
- GitHub OAuth
- ClickUp API
- Drive API
- state editing
- cron/scheduler
- autonomous agent task execution
- webhooks

