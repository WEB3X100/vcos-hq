# Key Workspaces

Purpose: compact lookup for recurring workspaces and command rooms.

## ClickUp

Workspace: `9017760195`
Primary AgentOSync space/view: `90175689274` — AgentoSync
Legacy NeuralSync Agency space: `90173622282` — NeuralSync Agency

Current live structure status: the AgentOSync space/view is the first reference whenever ClickUp is discussed. NeuralSync Agency may still contain legacy tasks and mirrored control-room items, but AgentOSync task reading, updating, weekly scans, and team async review should start from the AgentOSync space/view unless the human explicitly says otherwise. Restructure is gated until Airtable preservation snapshot is imported and approved.

Primary AgentOSync ClickUp view:

`https://app.clickup.com/9017760195/v/s/90175689274`

Use this view first when the human asks to read, update, summarize, or orchestrate AgentOSync / NeuralSync Agency tasks. It is ClickUp-only; do not assume Drive is the execution source unless the task explicitly mentions Drive files.

Main AgentOSync async activity folders:

- Folder `90178817003`: `https://app.clickup.com/9017760195/v/f/90178817003/90175689274`
- Folder `90178817004`: `https://app.clickup.com/9017760195/v/f/90178817004/90175689274`

| Area | Preferred list | ID |
| --- | --- | --- |
| Production systems | 00 - Production Control Room | `901711785684` |
| Client delivery | 00 - Delivery Control Room | `901713630958` |
| Umair / Q3 command | 00 - Q3 Command Center | `901713630962` |

## AgentOSync Daily Operating Route

When making daily progress on AgentOSync:

1. Open/read the primary AgentOSync ClickUp view above.
2. Use ClickUp workspace `9017760195`, space/view `90175689274` first.
3. Check the two main async folders `90178817003` and `90178817004` before legacy NeuralSync lists.
4. Route active client/demo work through the AgentOSync Client Delivery folder/list surfaces first, then legacy `00 - Delivery Control Room` (`901713630958`) only when mirrored tasks require it.
5. Route reusable systems, Vapi/n8n builds, Mini Interns, and OpenClaw production work through the AgentOSync build/production surfaces first, then legacy `00 - Production Control Room` (`901711785684`) only when mirrored tasks require it.
6. Use `00 - Q3 Command Center` (`901713630962`) only for Umair priorities, weekly control, and personal operating constraints.
7. Extract only task names, statuses, due dates, owners, blockers, approvals, links, and next actions unless deeper task detail is needed.

## ClickUp Restructure Target

| Target folder | Primary control list | Status |
| --- | --- | --- |
| `01 · COMMAND — Strategy, Roadmap, Decisions` | `00 · Weekly Priorities` | Pending creation after snapshot |
| `02 · BUILD — Systems, Automations, AI Employees` | `00 · Build Control Room` | Pending rename after snapshot |
| `03 · CLIENTS — Active Delivery and Accounts` | `00 · Delivery Control Room` | Pending rename after snapshot |
| `04 · LEADS — Pipeline and Outreach` | `00 · Active Leads` | Pending creation after snapshot |
| `05 · CONTENT — Social, Media, and Proof` | `00 · Content Control Room` | Pending creation after snapshot |
| `06 · OPS — Team, Finance, and Admin` | `00 · Team and Standups` | Pending rename after snapshot |
| `00 · ARCHIVE — Inactive Folders and Dead Lists` | n/a | Pending creation after snapshot |

## Airtable Preservation Snapshot

Base name: `NeuralSync ClickUp Preservation Snapshot`

Local import package:

`/Users/umairkhalid/_VCOS_Headquarters/1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/clickup/airtable-preservation-snapshot`

Rule: do not rename, move, merge, archive, or delete ClickUp folders/lists/tasks until this Airtable snapshot is imported, reviewed, and approved.

## Repo / Domain Links

| Domain | Home |
| --- | --- |
| VCOS HQ | `/Users/umairkhalid/_VCOS_Headquarters` |
| VCOS Project Workspaces | `/Users/umairkhalid/_VCOS_Headquarters/3_Project_Workspaces` |
| VCOS Project Workspaces GitHub | `https://github.com/WEB3X100/VCOS-Project-Workspaces` |
| VCOS Employee template | `/Users/umairkhalid/_VCOS_Headquarters/4_Reusable_Systems_and_Skills/4.1_VCOS_Employee_OS_Template` |
| VCOS Employee GitHub | `https://github.com/WEB3X100/VCOS-Employee` |
| GStack shared repo | `/Users/umairkhalid/_VCOS_Headquarters/6_Arsenal/repos/gstack` |
| GStack GitHub | `https://github.com/garrytan/gstack` |
| GBrain shared repo | `/Users/umairkhalid/_VCOS_Headquarters/6_Arsenal/repos/gbrain` |
| Meetily shared repo | `/Users/umairkhalid/_VCOS_Headquarters/6_Arsenal/repos/meetily` |
| Meetily GitHub | `https://github.com/Zackriya-Solutions/meetily` |
| gstack-Travel | `https://github.com/WEB3X100/gstack-Travel` |
| Ethnic Apparel Gem client workspace | `/Users/umairkhalid/_VCOS_Headquarters/3_Project_Workspaces/3.3_Ethnic_Apparel_Gem_Client_Workspace` |
| PakTextile Marketplace repo | `/Users/umairkhalid/_VCOS_Headquarters/3_Project_Workspaces/3.3_Ethnic_Apparel_Gem_Client_Workspace/3.3.2_Marketplace_MVP_Build/PakTextile-Marketplace` |
| PakTextile Marketplace GitHub | `https://github.com/WEB3X100/PakTextile-Marketplace` |
| Premium FDE / AI-Native ERP Consultant project | `/Users/umairkhalid/_VCOS_Headquarters/3_Project_Workspaces/3.8_Premium_FDE_Applied_AI_Target` (brand + AI-Native Consultant OS build + FDE evidence lane; see root README.md and 00_Game_Plan_and_Brand_Strategy/) |

## Office Hours Router

Read before any laptop-wide search for session briefs, weekly plans, or activation critiques:

`1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/session-briefs/README.md`

| Topic | Canonical path |
| --- | --- |
| Dual-laptop Hermes plan (Approved) | `.../session-briefs/dual-laptop-hermes/plan.md` |
| Interactive OH finalized (2026-06-19) | `.../session-briefs/interactive-office-hours-dual-laptop-hermes-2026-06-19.md` |
| Mission Control dashboard | `.../mission-control/state.json` |
| Hermes ClickUp tasks | https://app.clickup.com/9017760195/v/li/901713786845 |
| Latest Sunday office hours recap | `.../session-briefs/sunday-office-hours-*.md` (newest date) |
| Latest weekly plan draft | `.../session-briefs/weekly-office-hours-plan-*.md` (newest date) |

HQ absolute base: `/Users/umairkhalid/_VCOS_Headquarters`

## Rule

Use this file before ClickUp or repo search. Search only when the needed ID or repo is missing.
