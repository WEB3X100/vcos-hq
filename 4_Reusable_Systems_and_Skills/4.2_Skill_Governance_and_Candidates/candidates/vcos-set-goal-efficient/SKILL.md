---
name: vcos-set-goal-efficient
description: Run a bounded, evidence-backed VCOS goal loop while minimizing context duplication and expensive model usage. Use when Umair wants to test a token-efficient alternative to vcos-set-goal, explicitly asks for Sol/Terra/Luna routing, quality-per-token optimization, a micro-swarm, Mini Intern profiles, side-by-side workflow benchmarking, or a durable multi-agent outcome with machine checks and an independent review. Preserve the original skill for control runs.
---

# VCOS Set Goal Efficient

## Outcome

Test whether a durable goal can retain the acceptance, approval, ownership, and evidence standards of `vcos-set-goal` while reducing avoidable tokens through adaptive model routing, compact context packets, deterministic evidence work, delta-only re-review, and a maximum three-worker micro-swarm.

This is an experimental side-by-side skill. Never edit or replace `vcos-set-goal` from this workflow.
No token or cost saving is proven until the three-task benchmark passes with measured evidence.

## Invocation

Treat user text after `$vcos-set-goal-efficient` as the goal.

Supported flags:

- `--quality flagship|balanced|economy` (default `balanced`)
- `--token-budget N` approximate saved packet input + output character-token proxy; provider telemetry is required for total tokens/cost
- `--max-sol-calls N` (default: flagship `2`, balanced `1`, economy `0`)
- `--qa-depth basic|semantic|adversarial` (default inferred from risk)
- `--swarm-size 1|2|3` workers beyond Sentinel (default `2`)
- `--max-cycles N` (default `3`)
- `--cycle-minutes N` (default `30`)
- `--draft-only`
- `--auto` only for internal, reversible, machine-checkable work

If the goal is missing, ask for one outcome and what observable state means done.

## Mandatory Parity Contract

Read `references/parity-contract.md`. Preserve these guarantees from the production skill:

1. Three to seven observable done truths.
2. At least one binary non-LLM machine check before implementation.
3. Exclusive writable paths per lane.
4. Draft-only approval gates when external action is uncertain.
5. Independent Skeptic review every cycle, plus semantic depth when judgment risk is meaningful.
6. A reviewable evidence packet and explicit final verdict.
7. Bounded cycles and hard stops.

In addition, an independent Skeptic evaluates every cycle, including mechanical goals. For low-risk work that evaluation may be compact and checklist-led, but it may not be skipped or performed by the Builder.

Efficiency may reduce context and agent count. It may not weaken those guarantees.

## Phase 0 — Route Before Spawning

Create a compact `ARTIFACT-CONTRACT.yaml` beside the goal state with:

```yaml
goal_id: VCOS-GOAL-YYYYMMDD-###
quality: balanced
risk_score: 0
reversible: true
done_truths: []
machine_checks: []
approval_gates: []
context_packet: "{goal_dir}/context/CONTEXT-PACKET.md"
routing_mode: profile-only
max_sol_calls: 1
token_budget_proxy: null
max_dispatches_per_cycle: 4
swarm_size: 2
qa_depth: semantic
dispatches_used: 0
sol_calls_used: 0
token_proxy_used: 0
```

Choose the goal home in this order: `.planning/goals/`, the VCOS mission-control goals directory, `05_Coordination/goals/`, then `.goals/`. Replace the example context path with `{goal_dir}/context/CONTEXT-PACKET.md`. Initialize `ACTIVE-GOAL.md`, append-only `GOAL-CYCLE-LOG.md`, `ARTIFACT-CONTRACT.yaml`, and `artifacts/` there before cycle 1. `ACTIVE-GOAL.md` owns cycle/status, truth results, evidence links, approval gates, budgets, and the writable-path manifest. Sentinel is the sole writer for goal state and binder indexes.

Score risk using `references/model-routing.md`, then run:

```bash
python3 scripts/route_lane.py --role architect --quality balanced --consequence 1 --ambiguity 2 --novelty 1 --quality-leverage 2 --verification-difficulty 2 --max-sol-calls 1 --sol-calls-used 0 --reversible
```

Record the result. Do not claim a model was used unless the execution surface actually exposes model selection.

### Routing modes

- `native-model`: dispatcher accepts an explicit model identifier.
- `cross-runtime`: a model-specific API/thread/profile runs a saved dispatch packet.
- `profile-only`: current subagent runtime has no model selector; use the role, context, and token controls but label model choice as recommended, not executed.

If `spawn_agent` lacks a model parameter, use `profile-only`. Do not encode “Terra-style” or “Sol-style” as proof of an actual model.

## Phase 1 — Build One Context Packet

Use Luna-profile mechanical extraction or inline deterministic inspection to produce one compact context packet. Do not fork the full conversation by default.

The packet contains only:

- goal and done truths
- exact approval boundaries
- up to five read-first paths
- relevant excerpts or diff pointers
- file ownership
- required commands
- unresolved decisions

Default subagent dispatch is `fork_turns="none"`. Pass the context packet path plus the smallest task-local excerpt. Use `fork_turns="3"` only when recent conversational nuance is essential. Never use `fork_turns="all"` without recording why the duplicated context is worth the cost.

## Phase 2 — Choose the Smallest Micro-Swarm

Read `references/mini-intern-profiles.md`.

Do not spawn extra production lanes for a task that one Builder can complete. A separate read-only Skeptic is mandatory every cycle. Add other workers only when:

- two deliverables have non-overlapping writable paths; or
- independent semantic review is required.

Sentinel remains in the root. Use at most three concurrent workers and the configured maximum dispatches per cycle. Sequential waves count against that dispatch budget too.

### Quality modes

| Mode | Quality kernel | Production | QA | Final judge |
| --- | --- | --- | --- | --- |
| `flagship` | Sol recommended for architecture or core artifact | Terra | deterministic + Luna, then Terra semantic | Sol only for critical/disputed findings |
| `balanced` | Terra | Terra | deterministic + Luna | Terra; Sol only on escalation |
| `economy` | Terra brief only when needed | Luna for mechanical, Terra for judgment | deterministic + Luna | Terra only if a gate fires |

Use Sol for a narrow quality-defining packet, not the entire repository history. A flagship run normally permits one Sol architecture/core call and one conditional judge call.

## Phase 3 — Execute in Dependency Waves

Use this default sequence:

1. **Context wave:** Curator prepares the packet; Research Scout runs only if current facts matter.
2. **Quality-kernel wave:** Architect or Core Builder fixes the mechanism, narrative, design contract, or difficult artifact section.
3. **Production wave:** Production Builder implements the approved kernel.
4. **Cheap QA wave:** run commands first; Luna-profile QA and evidence operate on results and diffs.
5. **Semantic gate:** Terra-profile Skeptic reviews meaning, UX, correctness, safety, or causal behavior.
6. **Conditional Sol gate:** only for flagship/high-risk work, disputed findings, or architecture that still materially affects the outcome.
7. **Reuse wave:** Luna-profile Documenter extracts the SOP or Mini Intern capability after acceptance.

Sequential dependencies must not be forced into parallel agents.

For strategy, business, offer, product, or public-facing goals, the Skeptic must run a council review with Contrarian, Expansionist, Logician, Researcher, Buyer/User, and Judge lenses. One independent reviewer may apply all lenses in a compact packet; the final Judge verdict and truth-by-truth evidence remain mandatory.

## Phase 4 — Compact Dispatch Contract

Every worker receives:

```yaml
goal_id: ...
cycle: 1
role: production-builder
routing_mode: profile-only
recommended_model: gpt-5.6-terra
reasoning_effort: medium
input_budget: 30000
output_budget: 5000
context_packet: "{goal_dir}/context/CONTEXT-PACKET.md"
read_first: []
writable_paths: []
review_only_paths: []
success_checks: []
approval_gates: []
escalate_if: []
```

Handoffs are findings-first and capped at about 800 words:

```yaml
goal_id: ...
cycle: 1
lane: production-builder
status: pass|fail|blocked
artifacts:
  - path: ...
    action: created|updated|reviewed
verification:
  - check: ...
    result: pass|fail|not_run
    evidence: ...
truths_addressed:
  - truth: ...
    result: pass|fail|blocked
    evidence: ...
blockers: []
findings: []
escalation_needed: false
next_action: ...
```

Agents reference artifact paths; they do not paste full files, logs, or prior handoffs.

At collection, Sentinel rejects or quarantines any touched path outside that lane's writable manifest, records missing checks as `UNKNOWN`, and attributes every artifact/check to goal ID, cycle, and lane.

## Phase 5 — QA Pyramid

Always review in this order:

1. **Deterministic:** build, test, lint, schema, link, file, route, or screenshot-format checks.
2. **Luna-profile mechanical QA:** checklist coverage, formatting, manifest reconciliation, duplicates, missing evidence.
3. **Terra semantic QA:** meaning, UX comprehension, accessibility, logic, claim safety, workflow causality.
4. **Sol conditional judge:** critical risk, flagship quality, security/finance/legal/public claims, or unresolved reviewer disagreement.

Lower-cost QA is a filter, not permission to use a weak final judge for ambiguous high-risk work.

Every cycle ends with a separate Skeptic verdict covering each done truth, every required machine check, binder readiness, and blocking findings. The Builder cannot self-certify completion.

On remediation, send only:

- failed truth or finding
- relevant diff
- affected screenshot/check
- requested acceptance state

Do not repeat the whole review.

## Phase 6 — Evidence Without an Evidence Swarm

Prefer scripts and Sentinel for repetitive evidence bookkeeping. Spawn an Evidence Clerk only when evidence itself requires interpretation.

Maintain a lean binder:

- `00_REVIEW_INDEX.md`
- `evidence-ledger.md`
- `machine-checks.md`
- `adversarial-review.md`
- `artifact-manifest.md`
- `run-metrics.json`

Store noisy output in `raw-checks/`; link it rather than pasting it into agent prompts.

`run-metrics.json` records:

```json
{
  "skill": "vcos-set-goal-efficient",
  "routing_mode": "profile-only",
  "quality_mode": "balanced",
  "cycles": 1,
  "dispatches": 2,
  "full_context_forks": 0,
  "done_truths_passed": 0,
  "done_truths_total": 0,
  "prompt_chars": 0,
  "output_chars": 0,
  "token_proxy": 0,
  "actual_model_ids": [],
  "routing_evidence": [],
  "sol_calls_used": 0,
  "machine_checks_passed": 0,
  "machine_checks_total": 0,
  "critical_findings": 0,
  "major_findings": 0,
  "independent_skeptic_complete": false,
  "binder_ready": false,
  "ownership_reconciled": false,
  "approval_gates_satisfied": false,
  "council_gate_satisfied": false,
  "human_review_minutes": 0,
  "final_verdict": "pending"
}
```

Set `council_gate_satisfied` to true only when the required council review passed or the goal was explicitly classified as not applicable to the council rule.

Count prompt characters from the exact saved dispatch packets and output characters from exact saved handoff/evaluation packets; store the counted paths in `routing_evidence`. This measures packet volume only: it excludes system/developer context, skill instructions, files read through tools, cached input, and root-orchestrator tokens. Token proxy is `ceil((prompt_chars + output_chars) / 4)` and is not an API billing measurement or total-token estimate. Reject a nonzero character count paired with a zero or inconsistent token proxy. Provider usage or CodeBurn telemetry is required for actual total-token/cost comparison.

### Budget ledger

Before each dispatch, Sentinel reserves one dispatch, its input/output envelope, and any enforced Sol call in `ARTIFACT-CONTRACT.yaml`. After collection, replace reservations with measured character/provider usage. A null token budget means the human did not set one; benchmark runs must use an explicit nonzero budget. Do not dispatch if the action would exceed `max_dispatches_per_cycle`, `max_sol_calls`, `swarm_size`, or the aggregate token proxy. If safety routing requires Sol but the cap is zero, stop for approval or change quality mode; never silently override the cap. `qa_depth=basic` uses the mandatory Skeptic checklist; `semantic` adds UX/logic/claim lenses; `adversarial` adds failure-mode, buyer/user, contrarian, and judge lenses. Mandatory council gates override a shallower setting. `cycle_minutes` is checked at collect boundaries; on expiry collect a partial handoff and decide.

## Phase 7 — Compare Against the Control

Use `references/benchmark-protocol.md`. Run the production and experimental skills on equivalent isolated tasks. Never let one run read the other run's output.

Compare:

- completion truth pass rate
- critical/major findings
- machine-check pass rate
- cycles and dispatches
- full-context forks
- prompt/output character proxy
- estimated model cost only when actual model IDs are known
- human review time

Run:

```bash
python3 scripts/compare_runs.py control.json efficient.json pair-review.json
```

This command validates one pair only and cannot recommend promotion. Use the aggregate evaluator described in the benchmark protocol for the three-task gate. Do not promote this skill until at least three representative paired runs show no material quality regression and a meaningful context/token reduction.

## Atomic Completion Gate

Complete only when all done truths pass with evidence, all required machine checks pass, the independent Skeptic says `complete`, the binder is review-ready, the ownership reconciliation passes, required council/adversarial review is recorded, and every approval gate is satisfied. Then save `GOAL-SUMMARY.md`. Otherwise record `continue`, `blocked`, or `max_cycles` in `ACTIVE-GOAL.md` and append the cycle result to `GOAL-CYCLE-LOG.md`.

## Hard Stops

Stop for human direction when:

- a required model-specific dispatch would spend money without approval
- the runtime cannot actually enforce a model required by the goal
- external send, publish, deploy, spend, customer mutation, or destructive action lacks approval
- quality gates fail at max cycles
- token budget is exhausted before required semantic review
- file ownership overlaps

Never save tokens by skipping approval gates, machine checks, or the independent semantic verdict.
