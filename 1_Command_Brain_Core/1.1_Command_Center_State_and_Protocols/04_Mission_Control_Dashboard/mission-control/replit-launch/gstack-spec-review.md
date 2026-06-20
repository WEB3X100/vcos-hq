# GStack-Style Spec Review

Purpose: pressure-test the dashboard PRD before build using office-hours, spec, review, and ship discipline.

## Office Hours Critique

### Strongest Reason To Build

Mission Control solves a real operating pain: Umair and agents need one place to see current work, approvals, L1/L2 status, and source-of-truth links without reopening the whole HQ.

### Riskiest Assumption

That the dashboard will stay useful if it is only read-only and mostly file-backed. The MVP must prove it saves time before adding API writes, auth, scheduled sync, or agent action buttons.

### Scope Trap

Turning the dashboard into an all-in-one VCOS operating system too early. The first useful version should answer: what is alive, what needs approval, what should L1/L2 do next, and where is the source file?

### Kill Criteria

- If Umair still has to open more than three files to decide the next action.
- If the dashboard shows stale state without warning.
- If widgets create ambiguity about whether a task is draft-only or executable.
- If the Replit app requires secrets in Phase 0.

## Spec Review

| Area | Current risk | Fix in launch packet |
| --- | --- | --- |
| Data freshness | Static JSON can become stale | Show `updated_at`, stale warning, and source diagnostics |
| Approval gates | UI could imply buttons execute actions | Phase 0 uses read-only labels and disabled action affordances |
| File routing | Moved command-center paths could confuse agents | Use numbered-room paths and source labels |
| Personalization | Widget switching could become vague | Use explicit mode-to-widget mapping |
| Replit deployment | App may assume filesystem writes | Bundle sample JSON first; later approved API/storage |
| Mobile usability | Dense dashboard can collapse poorly | Define compact priority order |
| Client privacy | Dashboard could expose raw client data | Render summaries only; never raw CRM/QB/client exports |

## Build Recommendation

Use a simple React + Vite + TypeScript app on Replit for Phase 0.

Recommended stack:

- `React`
- `TypeScript`
- `Vite`
- CSS modules or plain CSS with design tokens
- Static JSON import or public `/data/state.json`
- No backend in Phase 0

Why: fastest path to a polished dashboard, easiest Replit boot, no secrets, low blast radius.

## Launch Checklist

- [ ] PRD accepted
- [ ] State schema implemented
- [ ] Sample data committed
- [ ] Responsive dashboard verified
- [ ] Stale-state warning implemented
- [ ] Approval-gated actions are read-only
- [ ] Source links render
- [ ] Replit run command works
- [ ] Browser QA pass complete
- [ ] Human approval before any public/custom-domain sharing

