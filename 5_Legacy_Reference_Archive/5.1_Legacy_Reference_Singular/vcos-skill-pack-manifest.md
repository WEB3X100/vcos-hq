# VCOS Skill Pack Manifest

Purpose: define the first VCOS HQ command-brain skills/SOPs and the first travel-domain limb skills/SOPs.

## Installed Local Skill

| Skill | Path | Purpose |
| --- | --- | --- |
| `vcos-command-router` | `/Users/umairkhalid/_VCOS_Headquarters/.agents/skills/vcos-command-router/SKILL.md` | Routes work between VCOS HQ, ClickUp command rooms, Drive, and domain packs such as `gstack-Travel`. |

## VCOS HQ Command-Brain Skills/SOPs

| Candidate | Status | Purpose |
| --- | --- | --- |
| `vcos-command-router` | installed | Decide whether work belongs to HQ, a command room, Drive, or a domain pack. |
| `clickup-command-review` | SOP-backed | Review Production, Delivery, and Q3 command rooms. |
| `drive-clickup-sync` | SOP-backed | Keep Drive as file home and ClickUp as execution home. |
| `production-control-room` | SOP-backed | Keep production tasks consolidated into reusable systems. |
| `client-delivery-triage` | SOP-backed | Keep delivery focused on active outcomes, blockers, demos, proposals, and close paths. |
| `q3-command-center` | SOP-backed | Protect Umair's brain from personal/day-job/investment overload. |

## gstack-Travel Domain-Pack Skills/SOPs

| Candidate | Purpose |
| --- | --- |
| `travel-crm-intake` | Capture lead source, traveler/client profile, trip intent, budget, urgency, and owner. |
| `travel-lead-followup` | Standard follow-up flow across email, WhatsApp, and CRM status. |
| `travel-proposal-deck` | Build travel offer/proposal decks from client context and itinerary options. |
| `amax-odoo-crm` | Odoo CRM tracking, lead wastage repair, follow-up sequencing, and CFO reporting. |
| `travel-content-calendar` | Social/calendar content production for travel client distribution. |
| `travel-client-weekly-brief` | Weekly client status summary from ClickUp, Drive, and CRM context. |

## Setup Path

1. Keep upstream gstack generic.
2. Keep VCOS HQ references and skills in `/Users/umairkhalid/_VCOS_Headquarters`.
3. Keep travel-specific implementation in `https://github.com/WEB3X100/gstack-Travel`.
4. Link every travel-domain task back to VCOS HQ command rooms.
5. Promote a SOP into a skill only when it is reused at least three times.

## Repo Link

- `gstack-Travel`: `https://github.com/WEB3X100/gstack-Travel`

