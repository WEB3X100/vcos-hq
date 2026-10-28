# Skill and Agent Test Register

Last updated: 2026-10-28.

| Item | Test | Evidence | Result | Remaining gate |
| --- | --- | --- | --- | --- |
| Proposal generation | Validate skill structure and run source/claim/pricing preflight against Chrome Auto + Proposal Pricing inputs | Candidate skill and Drive manifest in this repository | Partial | Approved brand kit; actual client-ready PDF render; human visual review |
| Slide generation | Validate skill structure and define two real test briefs (Chrome Auto and NeuralSync portfolio) | Candidate skill, test cases, and Drive manifest | Partial | Approved deck master; two PPTX/PDF renders that open without errors; human visual review |
| Agent roster | Define roles, memory scope, least-privilege boundaries, and Campaign Room handoff | `00_START_HERE/agent-roster.md` and OpenMaus prompt packets | Partial | Verify models, caps, access, shared memory, room visibility, and permissions in runtime |
| Brand kit | Identify candidate source assets and require one shared token/master source | Drive manifest and `neuralsync-brand-kit` candidate | Blocked | Sohaib-owned brand-kit approval and OpenMaus/VPS availability |

“Partial” means a repository or static validation passed; it does not mean a production render, runtime import, or external action succeeded.

## Required closeout evidence

- screenshot or exported configuration for every OpenMaus bot;
- a permission-boundary test per bot;
- one rejected-action test proving the external-action gate;
- opened/inspected PDF for Chrome Auto;
- opened/inspected PPTX and PDF for both deck briefs;
- human approval record for brand tokens and master template;
- ClickUp comment linking the commit/PR and this register.
