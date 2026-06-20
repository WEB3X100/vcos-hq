# VCOS Employee Template Strategy

Purpose: define the relationship between VCOS HQ and the reusable `4_Reusable_Systems_and_Skills/4.1_VCOS_Employee_OS_Template` GitHub repo.

Repo:

- `https://github.com/WEB3X100/VCOS-Employee`

## Strategic Role

`4_Reusable_Systems_and_Skills/4.1_VCOS_Employee_OS_Template` is the portable operating-system template for agent employees.

VCOS HQ is the command brain. `4_Reusable_Systems_and_Skills/4.1_VCOS_Employee_OS_Template` is the deployable employee OS layer that can be customized for a company, vertical, department, or role.

The goal is to polish one generic foundation, then create specific repos for industry employees such as:

- Dealership front desk employee.
- Travel concierge employee.
- Clinic intake employee.
- Real estate lead-response employee.
- Restaurant missed-call / reservation employee.

## Boundary

| Layer | Owns | Should not own |
| --- | --- | --- |
| VCOS HQ | Strategy, memory, routing, approvals, skill governance, cross-client protocols | Client-specific employee execution |
| `4_Reusable_Systems_and_Skills/4.1_VCOS_Employee_OS_Template` | Generic employee OS template, role lanes, placeholders, 1_Command_Brain_Core/1.2_Headquarters_Memory/schema conventions, reusable skills | HQ-wide decisions or active client execution truth |
| Industry employee repos | Vertical-specific employee package, integrations, SOPs, client outputs | Global HQ governance |
| Client instances | Client-specific context, credentials, active delivery state | Reusable template rules unless promoted back upstream |

## Current Repo Assessment

The existing repo uses a "Neural Castle" architecture:

- `00_Constitution_Hall/`: strategy and PRD.
- `10_Central_Intelligence/`: global template brain.
- `20_Operations_Library/`: SOPs.
- `30_Asset_Vault/`: vertical and franchise templates.
- `40_Production_Floor/`: active products and client instances.
- `50_Kaizen_Center/`: post-mortems.
- `90_System_Admin/`: session state and diagrams.

Useful patterns to preserve:

- Global -> vertical -> local inheritance.
- Reusable franchise/client template.
- Employee lanes: Builder, Kingmaker, Skeptic/Reviewer, Sentinel/Ops.
- Compounding learning loop from local lessons back into vertical/global templates.
- Scouter/autonomy levels.
- Human escalation rules.

Issues to fix before using it as the master template:

- The repo currently mixes HQ, template, internal product, and client-instance concerns.
- Top-level naming is more thematic than operational; future agents need smaller interfaces.
- `README.md` references AgentoSync under `Closeloop`, while repo files show `AgentoSync`.
- `AGENTS.md` is missing, so Codex/agent sessions do not have a standard fast path.
- Some employee numbering conflicts exist, such as Sentinel appearing as Employee 03 in a path named Employee 04.
- Client/product implementation material should not live inside the generic template once the foundation is polished.

## Recommended Target Structure

The master `4_Reusable_Systems_and_Skills/4.1_VCOS_Employee_OS_Template` template should become lean and cloneable:

```text
VCOS-Employee/
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── TEMPLATE_MANIFEST.md
├── 1_Command_Brain_Core/1.2_Headquarters_Memory/
│   ├── active-context.md
│   ├── decisions.md
│   ├── ubiquitous-language.md
│   └── key-workspaces.md
├── operating-system/
│   ├── employee-charter.md
│   ├── four-c-audit.md
│   ├── connections-map.md
│   ├── approval-gates.md
│   ├── autonomy-levels.md
│   └── cadence-hooks.md
├── roles/
│   ├── builder/README.md
│   ├── kingmaker/README.md
│   ├── skeptic/README.md
│   └── sentinel/README.md
├── 4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/
│   ├── manifest.md
│   └── candidates/README.md
├── verticals/
│   └── _template/README.md
├── client-instance/
│   ├── README.md
│   ├── local-brain.md
│   └── outputs/README.md
├── references/
│   └── README.md
└── archive/
    └── README.md
```

## Template Instantiation Flow

Use this flow when creating a new employee:

1. Clone or generate from `4_Reusable_Systems_and_Skills/4.1_VCOS_Employee_OS_Template`.
2. Fill `TEMPLATE_MANIFEST.md`.
3. Select the vertical profile.
4. Fill `client-instance/local-brain.md`.
5. Set the employee role or role mix.
6. Define allowed connections and approval gates.
7. Run the Four C audit.
8. Run one mock workflow.
9. Record lessons.
10. Promote reusable lessons upstream only after they apply beyond the one client.

## Placeholder Contract

The template should expose a small set of required placeholders:

- `{{EMPLOYEE_NAME}}`
- `{{EMPLOYEE_ROLE}}`
- `{{VERTICAL}}`
- `{{DEPARTMENT}}`
- `{{CLIENT_OR_COMPANY}}`
- `{{PRIMARY_OUTCOME}}`
- `{{SOURCE_OF_TRUTH_TASKS}}`
- `{{SOURCE_OF_TRUTH_FILES}}`
- `{{APPROVAL_SURFACE}}`
- `{{CONNECTIONS_ALLOWED}}`
- `{{WRITE_ACTIONS_ALLOWED}}`
- `{{ESCALATION_RULES}}`
- `{{OUTPUT_DESTINATIONS}}`

Keep placeholders explicit and few. A template with too many placeholders becomes harder to instantiate than writing the context fresh.

## Skill Strategy

Generic skills belong in `4_Reusable_Systems_and_Skills/4.1_VCOS_Employee_OS_Template` only if they apply across industries:

- Onboard employee.
- Audit Four C maturity.
- Level-up workflow.
- Draft-only approval packet.
- Run mock workflow.
- Capture lesson learned.
- Update local brain.

Vertical skills belong in industry repos:

- Dealership missed-call recovery.
- Travel itinerary intake.
- Clinic appointment intake.
- Real estate lead qualifier.

Client-specific skills belong in the client instance until repeated across clients.

## Memory Strategy

Use the same principle as VCOS HQ:

- Active memory stays compact.
- Raw material stays out of active memory.
- Local brain stores client/company facts.
- Vertical profile stores industry patterns.
- Decisions and repeated mistakes are promoted upward only when reusable.

## GitHub Strategy

Use GitHub as the distribution and review layer:

- `4_Reusable_Systems_and_Skills/4.1_VCOS_Employee_OS_Template`: private master template until productized.
- `VCOS-Employee-Dealerships`: dealership-specific employee package.
- `VCOS-Employee-Travel`: travel-specific employee package.
- `VCOS-Employee-Clinics`: clinic-specific employee package.
- Client repos or private forks: client-specific implementations.

Do not commit secrets. Remote routines should use environment variables or connector secrets.

## Next Actions

1. Create a GitHub issue in `4_Reusable_Systems_and_Skills/4.1_VCOS_Employee_OS_Template`: "Refactor repo into generic employee OS template."
2. Add `AGENTS.md` and `CLAUDE.md` to `4_Reusable_Systems_and_Skills/4.1_VCOS_Employee_OS_Template`.
3. Create `TEMPLATE_MANIFEST.md`.
4. Move legacy Neural Castle files into `archive/` or map them into the new structure.
5. Convert the franchise `claude.md` into `client-instance/local-brain.md`.
6. Normalize role folders and employee numbering.
7. Build the first vertical package from dealerships after the Employee 01 mock flow passes.

