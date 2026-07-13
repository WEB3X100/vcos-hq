# Gstack Practices Adapted for VCOS

Source reviewed: `garrytan/gstack` upstream `v1.60.1.0`, commit `7c9df1c568a9ea745508f679a329332b2c338063`, retrieved 2026-07-13 through the pointer-first Arsenal clone at `6_Arsenal/repos/gstack`.

## What VCOS adopts

| Gstack practice | VCOS adaptation | Failure prevented |
| --- | --- | --- |
| `/office-hours` before implementation | `gbrain-office-hours` or gstack Office Hours produces a decision packet | Building infrastructure before proving the product wedge |
| `/spec` interrogates why, scope, code, failures, and tests | PRD template plus deterministic validation | Vague PRDs that require repeated follow-up |
| Spec quality gate by an unfamiliar reviewer | Codex/Skeptic executability review before filing | Agent-specific assumptions hidden in the spec |
| Fresh worktree on execution | One issue, branch, worktree, and file owner map | Dirty-tree contamination and cross-agent conflicts |
| Plan completion audit | Every acceptance criterion maps to evidence | Shipping a touched file while requirements remain missing |
| Scope drift review | Compare PRD/issue intent against the actual diff | Polishing unrelated architecture instead of the product |
| Confidence-calibrated findings with quoted code | Findings require file/line evidence | Speculative reviews and repeated false corrections |
| Fresh verification before push | Re-run tests/build after final changes | Stale test claims |
| Bisectable commits | One coherent slice with its test per commit | Unreviewable mega-commits and difficult rollback |
| `/ship` continues through PR creation | Draft PR and evidence packet are mandatory | Mistaking a successful push for delivery |
| Guard/freeze boundaries | Allowed-file map plus approval gates | Unbounded edits or unsafe external action |

## What VCOS does not copy

- Do not vendor the full gstack repository or generated prompts into HQ.
- Do not require every gstack specialist for documentation-only work.
- Do not use gstack browser scripts that attach to or restart Umair's live browser.
- Do not treat a gstack command as approval to merge, deploy, publish, spend, or mutate client systems.
- Do not create a parallel source of truth. ClickUp remains business truth; GitHub remains engineering truth; VCOS HQ retains durable policy and decisions.

## Default workflow selection

```text
Vague product request
  -> Office Hours
  -> PRD/spec
  -> CEO scope review
  -> engineering review
  -> approved GitHub issue
  -> isolated build
  -> plan-completion audit
  -> adversarial review
  -> fresh tests
  -> draft PR
  -> human merge decision
```

For a small, already-specified change, begin at the sprint contract. For auth, payments, databases, production, client data, or irreversible changes, add security and ultra/adversarial review before the human gate.

## Hermes activation path

Before promotion, use the candidate repo-locally: open Hermes in the VCOS checkout and instruct it to read `AGENTS.md`, then this candidate's `SKILL.md`. This keeps the three supervised proof missions visible in Git history.

After Umair approves installation, current gstack supports Hermes directly:

```bash
cd 6_Arsenal/repos/gstack
git fetch origin --prune
./setup --host hermes
hermes skills list
```

This installs gstack skills under `~/.hermes/skills/gstack-*/`. Do not activate `/pair-agent`, browser handoff, `chrome-cdp`, or any workflow that attaches to or restarts Umair's live browser. Installing the VCOS conductor globally should wait until it passes three supervised missions; until then, the tracked repo copy is authoritative.
