# Mini Intern Profiles

Profiles describe capability and context boundaries. Model selection is separate.

| Profile | Default tier | Owns | Receives | Returns |
| --- | --- | --- | --- | --- |
| Sentinel | Terra | routing, approvals, ownership, merge, stop decision | artifact contract + compact handoffs | next wave + final verdict |
| Context Curator | Luna | task-local context packet | named inputs, max five paths | facts, excerpts, pointers, unknowns |
| Architect | Sol for flagship; Terra otherwise | mechanism, architecture, design contract | compressed inputs + acceptance truths | quality kernel and tradeoffs |
| Core Builder | Sol only when quality leverage is high | critical artifact section | approved kernel + exact owned files | artifact + checks |
| Production Builder | Terra | implementation and integration | approved kernel + owned paths | diff + machine results |
| QA Runner | Luna | mechanical checklist | checks, diff, acceptance list | failures only |
| Evidence Clerk | script/Luna | manifests and proof links | check results + artifact paths | reconciled binder |
| Semantic Skeptic | Terra | UX, meaning, logic, accessibility, safety | truths + diff + evidence | severity-ranked findings |
| Final Judge | Sol conditional | disputed or high-risk verdict | findings packet only | pass, reshape, or block |
| Documenter | Luna | SOP and reusable pattern | accepted artifacts + lessons | concise reusable system |

## Prompt rules

- State one deliverable.
- Give exact writable paths.
- Use `fork_turns="none"` by default.
- Cap read-first paths at five.
- Refer to files instead of pasting them.
- Request findings, evidence, caveats, and next action—not chain of thought.
- Stop when the owned deliverable and checks are complete.

## Concurrency

With four total slots, use Sentinel plus at most three workers. Parallelize only non-overlapping outputs. Architect -> Builder -> Skeptic remains sequential.
