# Browser Harness Launch QA

Purpose: test contract for a Replit-hosted Mission Control dashboard.

## QA Philosophy

The dashboard passes only if it helps Umair decide what to do next without creating false confidence. Visual polish matters, but source accuracy and approval-gate clarity matter more.

## Test Environments

| Environment | URL |
| --- | --- |
| Replit preview | Replit webview URL |
| Replit published app | Default Replit published URL |
| Local fallback | `http://localhost:5173` |

## Viewports

| Device | Size |
| --- | --- |
| Desktop | 1440 x 1000 |
| Laptop | 1280 x 800 |
| Tablet | 900 x 1100 |
| Mobile | 390 x 844 |

## Smoke Tests

- [ ] App loads without console errors.
- [ ] Dashboard renders with bundled/sample `state.json`.
- [ ] `updated_at` is visible.
- [ ] Fresh/stale/missing-state banner renders correctly.
- [ ] Mode switcher changes widget order.
- [ ] Optional flywheel modes render empty states when snapshot files are absent.
- [ ] Pending decisions render from L1/L2 state.
- [ ] Cubicle status renders L1 and L2.
- [ ] Client lanes render from `client_lanes`.
- [ ] Source labels appear on every operational widget.
- [ ] External links open in a new tab or are clearly marked.

## Approval-Gate Tests

- [ ] No enabled buttons for external sends.
- [ ] No enabled buttons for CRM/customer mutation.
- [ ] No enabled buttons for publishing.
- [ ] No enabled buttons for spending or deployment.
- [ ] Approval Review mode clearly separates decisions from passive status.
- [ ] Draft-only status is visible for gated lanes.
- [ ] `Promote to Skill`, `Assign Agent`, `Run QA`, and `Move Card` are not enabled controls in Phase 0/1.
- [ ] QA scores below 8/10 are shown as returned to intern, not human approval-ready.

## Visual QA

- [ ] No text overlaps at mobile or desktop widths.
- [ ] Long branch names wrap or truncate cleanly.
- [ ] Cards/panels do not resize unexpectedly on hover.
- [ ] No nested card visual clutter.
- [ ] Top priority content is visible above the fold on desktop.
- [ ] On mobile, active lane and decisions appear before secondary metrics.
- [ ] Color is not dominated by a single hue family.
- [ ] Status colors are distinguishable without relying only on color.

## Data Integrity QA

- [ ] Missing optional fields render `Not listed`, not invented text.
- [ ] Missing `state.json` renders a clear error state.
- [ ] Stale `updated_at` renders a warning.
- [ ] Unknown mode falls back to `brief`.
- [ ] Empty pending decisions renders the approved empty-state copy.
- [ ] Empty mission queue tells L2 to idle, not invent work.
- [ ] Missing `kanban.json`, `qa-gates.json`, `journey-map.json`, `codeburn.json`, or `skill-candidates.json` shows missing snapshot copy.
- [ ] Sensitive observability fields render redacted summaries, not raw payloads.

## Replit Launch QA

- [ ] `package.json` has `dev`, `build`, and `preview` scripts.
- [ ] Replit run command starts the Vite app.
- [ ] App binds to `0.0.0.0` / Replit-compatible host through Vite config or script.
- [ ] No required secrets for Phase 0.
- [ ] Build succeeds without network-only runtime dependencies.
- [ ] Published app does not require the editor filesystem to mutate state.
- [ ] README explains how to replace `state.json`.

## Accessibility QA

- [ ] Keyboard can reach mode switcher and links.
- [ ] Focus states are visible.
- [ ] Contrast is readable for text and status tags.
- [ ] Each panel has a meaningful heading.
- [ ] Icons have labels or accessible names.

## Browser Harness Scenario Script

```text
1. Open dashboard URL.
2. Wait for main heading "Mission Control".
3. Capture desktop screenshot.
4. Verify freshness banner includes updated timestamp.
5. Click "Intern Mission" mode.
6. Verify active mission, branch, and handoff fields are visible.
7. Click "Approval Review" mode.
8. Verify pending decisions appear and no write action buttons are enabled.
9. Click "Observability" mode and verify missing/sanitized snapshot behavior.
10. Click "QA Gates" mode and verify below-threshold copy if sample data includes a failed review.
11. Click "Kanban" mode and verify board columns do not expose executable move controls.
12. Set viewport to 390x844.
13. Verify active lane and decisions appear before metrics.
14. Capture mobile screenshot.
15. Check console errors.
16. Report pass/fail with screenshots and blockers.
```

## Launch Decision

| Result | Action |
| --- | --- |
| All smoke + approval + Replit tests pass | Publish to default Replit URL |
| Visual issues only | Fix before custom domain |
| Data/source/approval issue | Block launch |
| Missing state or stale-state warning broken | Block launch |
