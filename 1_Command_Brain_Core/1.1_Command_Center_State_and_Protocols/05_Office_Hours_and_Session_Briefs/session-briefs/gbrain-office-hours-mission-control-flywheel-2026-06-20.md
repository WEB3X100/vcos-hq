# GBrain Office Hours - Mission Control Flywheel Enhancements

**Date:** 2026-06-20  
**Status:** Draft critique packet  
**Mode:** Solution Grill + Office Hours + Skill Foundry Review  
**Subject:** Mission Control Replit dashboard PRD and flywheel enhancements  
**Retrieval:** HQ fast path + Office Hours router + dual-laptop Hermes plan + Mission Control launch packet. `gbrain` CLI was unavailable in this shell, so this packet follows the GBrain Office Hours skill format with direct HQ file reads.

## Verdict

**Incorporate all five enhancements, but ship them as source-labeled read-only views first.**

The flywheel is valuable only if it reduces Umair's cognitive load. If the dashboard becomes another command surface before the guardrails are proven, it will increase risk. The right move is:

```text
local agents generate evidence -> GitHub stores sanitized snapshots -> Replit renders the cockpit
```

## Hard Truth

The dashboard can become either a compounding command center or an attractive second backlog. The difference is whether each widget answers a decision Umair actually needs to make in under 60 seconds.

Do not build "agent swarm theater." Build evidence routing:

- What moved?
- What failed?
- What was reviewed?
- What needs approval?
- What should become a reusable skill?
- What is burning time or tokens?

## Sharper Version

Mission Control should become the **read-only operating mirror** of the dual-laptop Hermes factory:

| Flywheel module | Dashboard job | Phase 0/1 boundary |
| --- | --- | --- |
| Labyrinth Observability | Show why a run succeeded/failed | Summarized `journey-map.json`, redacted |
| Skill Pipeline | Show promotion candidates | Disabled `Promote to Skill` until Phase 3 |
| GStack QA Gates | Block weak work before human review | `qa-gates.json`, score >= 8/10 |
| CodeBurn Telemetry | Expose cost/loop risk | `codeburn.json`, watch/intervene labels |
| Kanban Orchestration | Show factory flow | `kanban.json`, read-only columns/cards |

## Proof Test

Within the first useful week of Replit:

1. Umair opens the dashboard and identifies the next action in under 60 seconds.
2. One L2 mission appears as a read-only Kanban card.
3. One QA scorecard shows pass/fail evidence before human approval.
4. One fake/sample journey map explains a failed step without raw logs.
5. One skill candidate appears as draft-only.
6. No enabled write/action controls exist.

Pass condition: dashboard saves time without creating a new place where autonomous agents can act.

## Approval Gates

- External sends: blocked.
- Publishing: blocked.
- CRM/client-system mutation: blocked.
- GitHub mutation from Replit: blocked.
- ClickUp mutation from Replit: blocked.
- Skill promotion: draft-only until human approval.
- Replit public/custom domain: allowed only after QA and human approval of what data is exposed.

## June 20 Forcing Questions

### 1. Usefulness

1. What exact decision should Mission Control help Umair make in under 60 seconds?
2. Which dashboard view would Umair open first at 7pm: Brief, Kanban, Approval Review, or Observability?
3. What would make the Replit dashboard useful even if L2 is not activated yet?

### 2. Data And Source Truth

4. Which file is the source of truth for the first Kanban snapshot?
5. Which optional snapshot should ship first: `qa-gates.json`, `journey-map.json`, `codeburn.json`, `kanban.json`, or `skill-candidates.json`?
6. What data must never leave the local laptops, even in summarized form?
7. Should Replit pull from GitHub raw, GitHub Pages/static files, or manual file upload for Phase 1?

### 3. Safety

8. What visible label makes it impossible to mistake read-only cards for executable controls?
9. Which actions should stay blocked even after Phase 3 draft-only hooks?
10. What redaction rule should apply to prompts and API responses in journey maps?

### 4. QA And Review

11. Is 8/10 the correct automated QA threshold before a mission reaches Umair?
12. Which review lanes are mandatory for code: GStack CEO, Eng, Design, Browser Harness, security/approval?
13. What failure should automatically return work to L2 before human review?

### 5. Skill Flywheel

14. What is the first real workflow likely to deserve `Promote to Skill`: 7pm brief, L2 handoff, Browser Harness QA, or Office Hours critique?
15. Is 3+ successful uses still the default promotion rule, or should high-leverage one-off wins enter a draft lane?
16. Who owns approval of new skills: Umair only, Infrastructure, or the relevant department owner plus Umair?

### 6. Cost And Orchestration

17. What CodeBurn threshold should trigger `watch` versus `intervene`?
18. Should the Kanban board mirror ClickUp, GitHub issues, or a lightweight VCOS JSON board first?
19. What prevents Triage from becoming another dumping ground?
20. What is the kill criterion that tells us the flywheel dashboard is too much too soon?

## Recommended Defaults

| Decision | Recommendation |
| --- | --- |
| First flywheel snapshot | `kanban.json` + `qa-gates.json` because they directly protect mission flow |
| First observability data | sample journey map only until redaction rules are proven |
| Skill pipeline | show candidates, no live promotion |
| QA threshold | 8/10 and no critical approval violation |
| Cost threshold | start manual: `watch` for loop_count > 3, `intervene` for repeated no-progress loop |
| Phase 1 sync | private GitHub snapshots, Replit read-only pull |

## Next Actions

1. Keep Phase 0 dashboard focused on state, decisions, and source links.
2. Add flywheel modes with empty states and disabled controls.
3. Create the first `kanban.json` and `qa-gates.json` sample only after the core dashboard passes build.
4. Run Browser Harness QA against the read-only controls.
5. Revisit the 20 questions in the next interactive Office Hours session before enabling GitHub snapshot sync.

## Capture

- Incorporated into `04_Mission_Control_Dashboard/mission-control/replit-launch/`.
- Office Hours packet saved here for the June 20 interactive question session.
- Durable rule: Replit displays flywheel evidence; it does not run the flywheel.
