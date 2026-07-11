# Marketing Mini Intern — Project State

**Updated:** 2026-07-11 America/Toronto
**Observed L1 branch:** `main` with extensive uncommitted HQ restructuring
**Remote Castle branch observed by L1:** `origin/castle/core-workflows-2026-07-11` at `40253c5` during the Castle interrogation
**Observed L2 state:** `main`, clean tracked tree, untracked `.hermes/` and `cofounder-handoffs/`; Castle/MMI interfaces absent
**Published coordination branch:** `codex/hermes-marketing-mini-intern` at `a96b3fd` (first packet commit)
**Status:** Design packet pushed for L2 preflight; not merged and not implemented

## North star

Ship one trustworthy co-founder loop: Umair activates a bounded marketing mission through Telegram; Hermes produces five relevant LinkedIn kits for one selected brand; Castle presents evidence and feedback; Umair combines and approves the exact final version; repository state teaches the next agent what shipped and what comes next.

## Current validated workflow

**NONE.** The workflow is specified but has not passed a real overnight Telegram → Hermes → repository handoff → Castle review UAT.

## Shipped

- Dual-Hermes Mission Control Week 1 scaffold exists on the older shared `main` history.
- Castle branch `40253c5` was reviewed on L1; verdict was NO-GO for merge pending stabilization.

## Designed and published for review, not implemented

- Marketing Mini Intern product requirements.
- Capability schemas and state machine.
- Bounded implementation phase and first overnight UAT.
- Grok supervised build prompt.
- GitHub co-founder memory, PRD-grilling, and shipping contract.

These interfaces are now available on `codex/hermes-marketing-mini-intern`. They remain design artifacts—not a working Marketing Mini Intern—until L2 fetches the branch and implementation/UAT passes.

## Working now

Have L2 fetch `codex/hermes-marketing-mini-intern`, verify the commit, read this packet, and re-run preflight against the exact paths.

## Blocked

- L1 contains a large staged/unstaged HQ restructure and many untracked artifacts.
- L2 has not yet fetched and verified the newly published Castle/MMI coordination branch.
- Castle remains NO-GO for direct merge until test truthfulness, outbound behavior, atomic writes, runtime-data separation, and integration strategy are fixed.
- The canonical first brand for the supervised seven-day run is not yet recorded.

## Approval queue

- Human selects the first brand before real marketing UAT.
- Human reviews the clean documentation PR before merge.
- Every M2 post requires exact-version human approval and manual publishing.
- Future scheduling/autopost requires a separate PRD, security review, kill switch, and explicit written authorization after evidence review.

## Next

Run `L2-RESUME-PROMPT.md` through the approved Hermes Telegram surface and review the returned preflight before any implementation.
