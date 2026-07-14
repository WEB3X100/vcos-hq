# Side-by-Side Benchmark Protocol

## Purpose

Compare `vcos-set-goal` with `vcos-set-goal-efficient` without diluting the production skill or leaking one run's answer into the other.

## Task set

Run at least three isolated tasks:

1. Small repo-backed documentation or UI change with binary checks.
2. Medium artifact requiring one Builder and semantic review.
3. Flagship artifact where architecture or narrative quality matters.

Use separate branches/worktrees or disposable directories. Give both runs the same source inputs, done truths, gates, and time limit.
Use a fixed evaluator rubric/version and record actual model IDs when enforceable. If variance matters, repeat a paired task rather than treating one stochastic output as decisive.

## Required metrics

- final verdict
- critical and major findings
- passed/total machine checks
- cycles
- dispatches
- full-context forks
- prompt and output characters
- token proxy (`ceil(chars / 4)`)
- actual provider tokens/cost when available
- human review minutes
- artifact preference from a blind reviewer
- saved dispatch/handoff paths used for character counts

## Quality gate

Efficient wins only when:

- no critical or major quality regression
- every mandatory truth and machine check passes
- human reviewer does not prefer the control for a material reason
- context/token proxy is lower by at least 25% on two of three tasks
- every paired run records isolation and a blind preference of `tie` or `efficient`; a material `control` preference fails that pair

Do not promote based on one easy task.

## Isolation

- Validators receive raw artifacts and acceptance criteria, not the intended answer.
- The reviewer does not know which skill produced which artifact when practical.
- Model routing is recorded as actual only when enforced by the runtime.
- Character/token estimates stay separate from provider usage measurements.
- Store blind preference and isolation in a pair-level review record shared by neither run; do not duplicate them in run metrics.

`scripts/compare_runs.py` validates one pair and never recommends promotion. Store three pair-result JSON files in a benchmark manifest and run `scripts/evaluate_benchmark.py MANIFEST.json`; only that aggregate command can return `promotion_eligible: true`.
