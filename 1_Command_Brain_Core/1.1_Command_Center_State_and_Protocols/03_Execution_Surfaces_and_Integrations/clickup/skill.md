---
name: clickup-os
version: 1.0.0
owner: Umair · NeuralSync Agency · VCOS HQ
description: >
  Load this skill whenever any VCOS Employee agent needs to read, write, update,
  triage, or audit ClickUp. Covers the full NeuralSync Agency space (ID 90173622282),
  workspace navigation rules, task naming conventions, health pulse protocol, and
  approval gates. Also used when running weekly or monthly workspace health audits.
  Triggers: any mention of ClickUp, task creation, folder routing, list assignment,
  workspace audit, health pulse, or "where does this task go."
workspace_id: "9017760195"
space_id: "90173622282"
space_name: "NeuralSync Agency"
last_audited: "2026-05-14"
agent_roles_in_scope: [Sentinel, Builder, Skeptic, Kingmaker]
approval_gate: >
  Never create, move, close, or delete tasks without Umair approval unless the
  task is explicitly marked agent-executable in its description.
---

# ClickUp Operating Skill — NeuralSync Agency

## Purpose

This skill gives any VCOS Employee agent a complete, authoritative operating manual
for the NeuralSync Agency ClickUp space. It answers three questions every agent must
be able to answer before touching ClickUp:

1. **Where does this task belong?**
2. **How must it be named and formatted?**
3. **Is this safe to do without human approval?**

It also defines the Health Pulse Protocol — the recurring audit routine that keeps
the workspace clean, gives Umair feedback on workspace drift, and prevents entropy
as the team scales.

---

## Section 1 — Workspace Architecture

### 1.1 Canonical Folder Structure

The NeuralSync Agency space uses six active folders numbered for chronological
priority. Numbers are the navigation anchor. The keyword in caps is the function.
Agents use this table to route every task before acting.

```
NeuralSync Agency (Space ID: 90173622282)
│
├── 01 · COMMAND    — Strategy, Roadmap, Decisions
├── 02 · BUILD      — Systems, Automations, AI Employees
├── 03 · CLIENTS    — Active Delivery and Accounts
├── 04 · LEADS      — Pipeline and Outreach
├── 05 · CONTENT    — Social, Media, and Proof Assets
├── 06 · OPS        — Team, Finance, and Internal Admin
│
└── 00 · ARCHIVE    — Inactive folders and dead lists (hidden from sidebar)
```

> **Rule:** No folder exists outside this set without Umair approval. If a task
> does not fit any folder above, the agent must flag it to the Sentinel before
> creating a new folder.

---

### 1.2 Folder and List Definitions

Each folder answers a different question. Agents route by matching the task's
*intent* to the question, not by guessing from the task name alone.

---

#### 01 · COMMAND — Strategy, Roadmap, Decisions

**Routing question:** "Does this task define the plan, record a decision, or set a
priority for the week?"

| List | ID | Purpose |
|------|----|---------|
| `00 · Weekly Priorities` | (create if missing) | Active weekly outcomes for Umair and leads. One task per outcome. Status drives the week. |
| `01 · Roadmap and Milestones` | (create if missing) | Q3/Q4 goals, MRR targets, ARR milestones. Read-only for most agents. |
| `02 · Decisions and Approvals` | (create if missing) | Logged decisions, approval records, gate ratifications. Append-only. |

**Agent rules for COMMAND:**
- Sentinel reads `00 · Weekly Priorities` daily at 8:00 AM Toronto time.
- Builder and Kingmaker never create tasks here without Sentinel routing.
- Skeptic audits `02 · Decisions and Approvals` weekly to confirm every approval
  gate was formally logged before work shipped.
- Personal tasks (day-job, personal errands, family) must never enter this folder.
  If spotted, the Sentinel flags and removes them immediately.

---

#### 02 · BUILD — Systems, Automations, AI Employees

**Routing question:** "Am I building something — an automation, a workflow, an AI
employee, a template, or a tool?"

| List | ID | Purpose |
|------|----|---------|
| `00 · Build Control Room` | `901711785684` | All active build tasks. Replaces "Production Control Room." Primary list for Builder agent. |
| `01 · AI Employees and Skills` | (create if missing) | Employee repo work (Employee 01 Front Desk, Employee 02 Marketing, etc.), skill candidates, skill governance tasks. |
| `02 · Automations and Workflows` | (create if missing) | All n8n, Make, Vapi, and voice AI builds. Dealership, clinic, and restaurant tasks live here — tagged by vertical, not in separate lists. |
| `03 · Templates and Reference` | `901710071435` | Master templates, SOPs, how-to guides, configuration references. Read-heavy, write-rarely. |

**Agent rules for BUILD:**
- A voice AI task tagged `[dealership]` and a voice AI task tagged `[clinic]` both
  go in `02 · Automations and Workflows`. They are never split into separate lists.
- Every task in `00 · Build Control Room` must have: assignee, status, and a
  description that states the success criterion. Tasks without all three are P2
  hygiene violations (see Health Pulse section).
- The Builder agent creates tasks here. The Skeptic agent reviews them before the
  status moves to `in review` or beyond.

---

#### 03 · CLIENTS — Active Delivery and Accounts

**Routing question:** "Is this task for a specific named client or active delivery
outcome?"

| List | ID | Purpose |
|------|----|---------|
| `00 · Delivery Control Room` | `901713630958` | Master active delivery list. All client-facing work that is actively in flight. |
| `01 · Amax Travel` | (create if missing) | Amax-specific tasks: Odoo CRM, Systrix data map, content, finance reporting, review workflows. |
| `02 · AgentOSync GTM` | (create if missing) | AgentOSync go-to-market: dealership wedge, Ammar platform, lead funnel plumbing, proof assets. |
| `03 · Other Active Clients` | (create if missing) | One task per active client (Sameer, Usman, any new client). When a client grows to 5+ tasks, they get their own named list. |

**Agent rules for CLIENTS:**
- Amax Travel is the internal proof lab. Any workflow tested internally for Amax
  before external release belongs here, not in BUILD.
- The Delivery Control Room is Umair's primary daily read. Keep it clean.
  Completed tasks must be closed within 24 hours of completion. Stale "in progress"
  tasks older than 5 days without an update are P1 flags.
- No task enters CLIENTS without a named assignee and a due date.
- Client-facing sends, CRM mutations, and external communications require Umair
  approval before status moves to `complete`. This is a hard approval gate.

---

#### 04 · LEADS — Pipeline and Outreach

**Routing question:** "Is this a new lead, deal, or outreach task — something about
acquiring a new client rather than delivering for an existing one?"

| List | ID | Purpose |
|------|----|---------|
| `00 · Active Leads` | (create if missing) | One task per prospect. Status: `new → contacted → qualified → proposal sent → closed`. |
| `01 · Deals In Progress` | (create if missing) | Proposals sent and in active conversation. Includes Usman proposal, Sameer scoping. |
| `02 · Outreach and Proposals` | (create if missing) | LinkedIn outreach tasks, Upwork bids, email drip tasks, proposal drafts. |

**Agent rules for LEADS:**
- The old "1. CRM" folder (Leads, Deals, Accounts, Contacts) is archived. Never
  reference or resurrect it.
- Every lead task uses the prefix convention: `[Source] Company — Contact Name`.
  Example: `[LinkedIn] Sameer Auto Group — Sameer Khan`.
- The Sales agent owns this folder. The Sentinel monitors for leads stalled in
  `contacted` for more than 7 days without a follow-up task.
- No outbound message or proposal sends without Umair approval. Draft-only rule
  applies to all tasks in `02 · Outreach and Proposals`.

---

#### 05 · CONTENT — Social, Media, and Proof Assets

**Routing question:** "Is this task about creating or publishing a post, video,
proof asset, or content calendar item?"

| List | ID | Purpose |
|------|----|---------|
| `00 · Content Control Room` | (create if missing) | All in-flight content tasks across brands. Kingmaker's primary list. |
| `01 · AgentOSync Social` | (create if missing) | LinkedIn, X, Instagram posts — proof posts, use case content, hero video assets. |
| `02 · Amax Social` | `901710992822` | Amax Travel content calendar. Social posts, travel content, review responses. |

**Agent rules for CONTENT:**
- The Kingmaker agent drafts content tasks here. Nothing is published without
  Umair approval. Status `draft → approved → published` — never skip `approved`.
- Generated media from Higgsfield (Nano Banana Pro or Seedance 2.0) stays in
  `draft` status until Umair explicitly marks it `approved`.
- Social calendars are not client delivery. Amax social content belongs in
  `05 · CONTENT → 02 · Amax Social`, not in `03 · CLIENTS`.
- Content tasks must include: platform, format, target publish date, and a one-line
  brief in the description.

---

#### 06 · OPS — Team, Finance, and Internal Admin

**Routing question:** "Is this about running the team, paying bills, managing tools,
or internal company admin?"

| List | ID | Purpose |
|------|----|---------|
| `00 · Team and Standups` | `901710072464` | Team tasks, standup notes, meeting agendas, company operations. |
| `01 · Finance and Tools` | (create if missing) | Invoice tracking, tool spend reviews, cash flow, monthly finance tasks. |

**Agent rules for OPS:**
- Personal tasks (move prep, weekend plans, day-job decks) must never appear in
  this folder or anywhere in the NeuralSync Agency space. If the Sentinel
  encounters personal tasks, it flags them for removal immediately.
- Finance tasks require Umair approval before any spend decision is logged as
  final. Read-only for all agents except Sentinel when flagging.

---

#### 00 · ARCHIVE — Inactive Folders and Dead Lists

All archived folders and lists are moved here and hidden from the sidebar. Agents
must never pull tasks from Archive without explicit instruction. Archived content
includes:

- ✨ Template Guide (empty, never used)
- Scope of Work (empty)
- 2. Client Onboarding (3 lists, near-zero tasks)
- 5. Billing & Invoicing
- 6. Client Feedback & Testimonials
- 8. SOPs & Documentation (4 lists)
- 1. CRM — Leads, Deals, Accounts, Contacts (replaced by 04 · LEADS)
- Voice AI - Restaurant (merged into 02 · Automations and Workflows)
- Voice AI - Clinics (merged into 02 · Automations and Workflows)
- 04 Voice AI -- Dealership (merged into 02 · Automations and Workflows)
- ALEX REED (inactive client)
- Cellmart LinkedIn Auto Posting Engine (inactive)
- A.S | Real Estate Zillow House Video Automation (inactive)

---

## Section 2 — Naming Conventions

Every agent must follow these naming rules exactly. Inconsistent naming is the
primary cause of team members being unable to find their work. The Skeptic audits
naming compliance during every Health Pulse.

### 2.1 Folder Naming

```
NN · KEYWORD — Short description
```

- `NN` = two-digit number, zero-padded (01, 02, 03...)
- `KEYWORD` = single-word function in ALL CAPS
- `—` = em dash separator
- Short description = what lives here, in sentence case, under 5 words

**Examples:**
```
✅ 01 · COMMAND — Strategy, Roadmap, Decisions
✅ 02 · BUILD — Systems, Automations, AI Employees
✅ 03 · CLIENTS — Active Delivery and Accounts

❌ Production Systems
❌ 3. Client stuff
❌ New Folder (2)
```

### 2.2 List Naming

```
NN · Function Name
```

- `NN` = two-digit number (00 is always the Control Room or primary list)
- `Function Name` = title case, concise, describes what lives in this list

**Examples:**
```
✅ 00 · Delivery Control Room
✅ 01 · Amax Travel
✅ 02 · AgentOSync GTM

❌ Amax - Content Calendar
❌ AgentoSync Modern Social Media Calendar
❌ A.S | Clinic Receptionist Marketing
```

### 2.3 Task Naming

```
[Client/Project] Action verb — Specific outcome
```

- Bracket prefix = which client or project this belongs to
- Action verb = what is being done (Build, Draft, Review, Fix, Map, Create...)
- Specific outcome = the measurable result, not a vague label

**Examples:**
```
✅ [Amax] Build AR/AP control table v1 in Airtable
✅ [Employee-01] Draft missed call recovery workflow for internal test
✅ [AgentOSync] Fix lead funnel — WhatsApp follow-up sequence
✅ [Sameer] Review dealership appraisal MVP scope

❌ Finance
❌ Cash flow forecast
❌ Do the thing
❌ Voice AI
❌ Template Questionaire
```

### 2.4 Status Vocabulary

Every task must use one of these statuses exactly. No custom statuses without
Umair approval. Agents never invent new status names.

| Status | Meaning |
|--------|---------|
| `briefing` | Task is defined but not yet scoped or assigned |
| `scoping` | Assignee is defining the approach and subtasks |
| `not started` | Scoped and assigned, work has not begun |
| `in progress` | Actively being worked on |
| `in review` | Submitted for Skeptic or human review |
| `approved` | Reviewed and cleared to proceed or publish |
| `completed` | Done. Close within 24 hours. |
| `blocked` | Cannot proceed — reason must be in comments |
| `parked` | Intentionally paused for later — reason required |

---

## Section 3 — Agent Routing Decision Tree

When a task comes to mind, any team member or agent follows this tree before
creating or moving a task. Agents must run this logic before every ClickUp write.

```
New task or idea arrives
│
├── Does it define the plan, record a decision, or set weekly priorities?
│   └── YES → 01 · COMMAND
│
├── Am I building something (automation, workflow, AI employee, tool, template)?
│   └── YES → 02 · BUILD
│       ├── AI employee or skill work → 01 · AI Employees and Skills
│       ├── Automation, n8n, Vapi, voice AI → 02 · Automations and Workflows
│       └── Template or reference document → 03 · Templates and Reference
│
├── Is this for a specific named client or active delivery?
│   └── YES → 03 · CLIENTS
│       ├── Amax Travel → 01 · Amax Travel
│       ├── AgentOSync GTM → 02 · AgentOSync GTM
│       └── Other client → 03 · Other Active Clients
│
├── Is this a new lead, deal, proposal, or outreach task?
│   └── YES → 04 · LEADS
│       ├── New prospect → 00 · Active Leads
│       ├── Active deal or proposal → 01 · Deals In Progress
│       └── Outreach or drip → 02 · Outreach and Proposals
│
├── Is this a social post, video, content calendar item, or proof asset?
│   └── YES → 05 · CONTENT
│       ├── AgentOSync brand → 01 · AgentOSync Social
│       └── Amax brand → 02 · Amax Social
│
├── Is this internal — team, billing, tools, company admin?
│   └── YES → 06 · OPS
│       ├── Team or standup → 00 · Team and Standups
│       └── Finance or tools → 01 · Finance and Tools
│
└── Still unsure?
    └── Flag to Sentinel. Do not create the task until routed.
```

---

## Section 4 — Approval Gates

These gates are non-negotiable. No agent bypasses them. Every gate requires a
logged approval in `01 · COMMAND → 02 · Decisions and Approvals` or explicit
confirmation in the active thread from Umair before proceeding.

| Action | Gate Required | Agent That Enforces |
|--------|--------------|---------------------|
| Sending any client-facing message | Yes — Umair approval | Sentinel |
| Publishing any content (social, GitHub, website) | Yes — Umair approval | Sentinel + Kingmaker |
| CRM mutation (adding, updating, or deleting a contact or deal) | Yes — Umair approval | Sentinel |
| Closing or archiving a folder or list | Yes — Umair approval | Sentinel |
| Creating a new folder outside the 6-folder structure | Yes — Umair approval | Sentinel |
| Budget or tool spend decision | Yes — Umair approval | Sentinel |
| Moving a task to `approved` status | Yes — Umair review | Skeptic |
| Any external API call that writes data (Vapi, Twilio, HubSpot) | Yes — Umair approval | Sentinel |
| Internal task creation, updates, and comments | No gate — agent-executable | Any agent |
| Reading any task, list, or folder | No gate | Any agent |
| Running a Health Pulse (read-only audit) | No gate | Sentinel / Skeptic |

**Draft-only rule:** All external outputs from any agent default to `draft` status
until Umair explicitly approves. The phrase "Draft-only until Umair approves" must
appear in any task description where the output could trigger an external action.

---

## Section 5 — Health Pulse Protocol

The Health Pulse is a structured workspace audit run by the Sentinel (and optionally
assisted by the Skeptic) on a defined cadence. It produces a concise diagnostic
report for Umair that surfaces drift, dead weight, and structural issues before
they compound.

### 5.1 Pulse Cadence

| Pulse Type | Frequency | Trigger | Owner |
|------------|-----------|---------|-------|
| Daily Standup Pulse | Every working day, 8:00 AM Toronto | Automatic (cadence hook) | Sentinel |
| Weekly Structure Pulse | Every Monday | Automatic | Sentinel + Skeptic |
| Monthly Deep Audit | First Monday of each month | Automatic | Sentinel + Skeptic |
| On-Demand Pulse | Any time Umair requests | Manual trigger | Any agent |

---

### 5.2 Daily Standup Pulse (5-minute read)

**What the Sentinel checks:**

1. Open tasks in `00 · Delivery Control Room` with status `in progress` for more
   than 5 days without a comment update → flag as **P1 drift**.
2. Any task in any list missing assignee, status, or description → flag as
   **P2 hygiene violation**.
3. Tasks tagged `[blocked]` for more than 24 hours without a comment explaining
   the blocker → flag as **P0 blocker** and notify Umair immediately.
4. Any tasks in `01 · COMMAND → 00 · Weekly Priorities` that moved to `completed`
   yesterday → surface as wins in the briefing.

**Output format — Daily Standup Pulse:**

```
DAILY STANDUP PULSE — [DATE] — 8:00 AM Toronto

🔴 P0 BLOCKERS (need Umair decision today)
- [Task name] | List: [list] | Blocked since: [date] | Blocker: [summary]

🟠 P1 DRIFT (stalled in progress, no update)
- [Task name] | Assignee: [name] | Last update: [X days ago]

🟡 P2 HYGIENE (missing fields)
- [Task name] | Missing: [assignee / status / description]

🟢 COMPLETED YESTERDAY
- [Task name] | Outcome: [one line]

📋 TODAY'S ACTIVE PRIORITIES (from Weekly Priorities list)
1. [Task name] — [assignee]
2. [Task name] — [assignee]
3. [Task name] — [assignee]

⏳ APPROVALS WAITING ON UMAIR
- [Task name] | Waiting since: [date] | Action needed: [one line]
```

---

### 5.3 Weekly Structure Pulse (15-minute audit)

**What the Sentinel and Skeptic check every Monday:**

**Folder health:**
- [ ] Are all 6 active folders present and correctly named?
- [ ] Has any new folder appeared outside the canonical 6? If yes → flag.
- [ ] Are there any lists with zero tasks that have existed for more than 2 weeks?
      → Archive candidate. Flag for Umair decision.

**List health:**
- [ ] Are all lists following the `NN · Function Name` naming convention?
- [ ] Does every list have at least one task with correct naming format?
- [ ] Are there any duplicate lists serving the same purpose? → Merge candidate.

**Task health:**
- [ ] Tasks in `in progress` for more than 7 days without subtask progress → P1.
- [ ] Tasks in `briefing` for more than 14 days without movement → P2 (stale
      idea, needs decision: scope it or park it).
- [ ] Tasks with no due date in CLIENTS or LEADS → P2 hygiene violation.
- [ ] Tasks that belong in a different folder (wrong routing) → flag and propose move.

**Content discipline:**
- [ ] Are personal tasks or day-job tasks present anywhere in the space? → Remove.
- [ ] Is the `00 · ARCHIVE` folder growing? → Surface archived items older than
      90 days for permanent deletion decision.

**Output format — Weekly Structure Pulse:**

```
WEEKLY STRUCTURE PULSE — Week of [DATE]

WORKSPACE SCORE: [X/10]
(Score drops 1 point for each P0, 0.5 for each P1, 0.2 for each P2)

FOLDER AUDIT
✅ All 6 canonical folders present
⚠️  [Issue found, if any]

LIST AUDIT
- Total lists: [N]
- Lists with zero tasks: [N] → Archive candidates: [list names]
- Naming violations: [N] → [list names]

TASK AUDIT
- P0 blockers: [N]
- P1 drift (stale in-progress): [N]
- P2 hygiene (missing fields): [N]
- Stale briefing tasks (14+ days): [N]

ROUTING VIOLATIONS (tasks in wrong folder)
- [Task name] | Currently in: [folder] | Should be in: [folder]

MERGE CANDIDATES (duplicate list intent)
- [List A] and [List B] serve the same purpose → recommend merge

ARCHIVE CANDIDATES (empty or dead lists)
- [List name] — [N] tasks — last activity: [date]

WINS THIS WEEK
- [Task name] completed → [one-line outcome]
- [Task name] completed → [one-line outcome]

RECOMMENDED ACTIONS FOR UMAIR (approval needed)
1. Archive [list name] — confirmed empty
2. Merge [list A] into [list B]
3. Rename [folder] to match naming convention
```

---

### 5.4 Monthly Deep Audit (30-minute audit)

The Monthly Deep Audit runs the full Weekly Structure Pulse plus the following
additional checks:

**Workspace growth assessment:**
- How many new lists were created this month? Are they justified?
- How many tasks were completed this month vs. created? (throughput ratio)
- Which assignees have the most overdue tasks? (workload imbalance signal)
- Which folders are generating the most new tasks? (activity heatmap)
- How many tasks are sitting in `parked` with no revival date? (decision debt)

**Structure evolution check:**
- Has the team grown? Does the folder structure still serve current team size?
- Are there new verticals, clients, or product lines that need their own list?
- Are any lists consistently over 20 tasks? → May need to split into sublists.
- Are any folders consistently empty? → Candidate for permanent removal.

**Skill feedback loop:**
- Which ClickUp naming or routing rules are being broken most frequently?
  → Update this SKILL.md with a clarification or example.
- Has any new folder or list been created that improves on the canonical structure?
  → Propose a structure upgrade for Umair approval.

**Output format — Monthly Deep Audit:**

```
MONTHLY DEEP AUDIT — [MONTH YEAR]

WORKSPACE HEALTH SCORE: [X/10]
Last month: [X/10] | Trend: [↑ improving / → stable / ↓ degrading]

GROWTH METRICS
- Tasks created this month: [N]
- Tasks completed this month: [N]
- Throughput ratio: [N completed / N created] (target: ≥ 0.8)
- New lists added: [N] | Justified: [Y/N with notes]

ACTIVITY HEATMAP
- Most active folder: [folder name] ([N] tasks updated)
- Least active folder: [folder name] ([N] tasks updated)
- Top assignee by completion: [name] ([N] tasks)
- Top assignee by overdue: [name] ([N] overdue)

DECISION DEBT
- Tasks parked > 30 days: [N] → [list names]
- Tasks in briefing > 30 days: [N] → recommend: scope or delete

STRUCTURE UPGRADE PROPOSALS (requires Umair approval)
1. [Proposed change] — Reason: [one line]
2. [Proposed change] — Reason: [one line]

SKILL UPDATE RECOMMENDATIONS
- Rule that is being broken most: [rule] → Proposed clarification: [text]
- New pattern observed that improves workflow: [description]

NEXT MONTH FOCUS
- [One structural improvement to implement]
- [One naming convention to reinforce with team]
```

---

### 5.5 Workspace Health Score Definition

The Health Score (0–10) is calculated during every Weekly and Monthly pulse.
It gives Umair a single number that reflects workspace discipline.

```
Base score: 10

Deductions:
- Each P0 blocker (task blocked > 24h, no comment):     -1.0 per occurrence
- Each P1 drift (in progress > 7 days, no update):      -0.5 per occurrence
- Each P2 hygiene violation (missing field):             -0.2 per occurrence
- Each routing violation (task in wrong folder):         -0.3 per occurrence
- Each naming violation (folder, list, or task):         -0.2 per occurrence
- Each empty list present > 14 days (not archived):      -0.3 per occurrence
- Personal task found in agency space:                   -0.5 per occurrence
- Approval gate bypassed (output published without gate):-2.0 per occurrence

Score bands:
9.0 – 10.0 → 🟢 Healthy. Workspace is clean and navigable.
7.0 – 8.9  → 🟡 Drift detected. Run cleanup before it compounds.
5.0 – 6.9  → 🟠 Degraded. Team is losing time navigating. Cleanup session needed.
Below 5.0  → 🔴 Critical. Workspace is causing execution friction. Escalate to Umair.
```

---

## Section 6 — Escalation and Triage Priority Levels

When the Sentinel detects a problem, it classifies it before surfacing it to Umair.
Classification determines urgency and whether Umair needs to act today.

| Level | Name | Condition | Agent Action | Umair Needed? |
|-------|------|-----------|-------------|---------------|
| P0 | Client on fire | Client deliverable overdue 2+ days, no update, no subtask | Sentinel pings Umair immediately. Adds comment to task. Blocks weekly report. | YES — same day |
| P1 | Milestone at risk | Task due this week, `in progress`, no update in 48h | Sentinel posts to team channel. 24h window to resolve. | Only if unresolved in 24h |
| P2 | Hygiene violation | Missing assignee, status, or description on any task | Sentinel posts task comment tagging assignee. No escalation. | NO — auto-handled |
| P3 | Drift warning | Task overdue < 24h, recent activity visible | Sentinel asks assignee to close or update due date. Single message. | NO — auto-handled |

---

## Section 7 — Forbidden Actions

These actions are never taken by any agent under any circumstances without explicit
written approval from Umair in the current thread or in `02 · Decisions and Approvals`.

```
❌ Delete any task, list, or folder
❌ Archive any folder or list without Umair approval
❌ Send any external message (email, SMS, WhatsApp, LinkedIn DM)
❌ Publish any content to any social platform
❌ Mutate any CRM record (create, update, or delete contact/deal)
❌ Create a new folder outside the 6-folder canonical structure
❌ Change any task's assignee to someone not on the team
❌ Mark any task as `completed` if it has a client-facing output pending approval
❌ Move tasks out of ARCHIVE back into active folders without approval
❌ Exceed the 6-folder structure without approval
```

---

## Section 8 — Quick Reference Card

Copy this card into any agent context where fast lookup is needed.

```
NEURALSYNC AGENCY CLICKUP — QUICK REFERENCE

WORKSPACE: 9017760195 | SPACE: 90173622282

ROUTING (match task intent to folder):
  01 · COMMAND    → plan, roadmap, decision
  02 · BUILD      → automation, workflow, AI employee, tool
  03 · CLIENTS    → specific client delivery
  04 · LEADS      → new lead, deal, proposal, outreach
  05 · CONTENT    → post, video, proof asset, calendar
  06 · OPS        → team, billing, admin

NAMING:
  Folder:  NN · KEYWORD — Short description
  List:    NN · Function Name
  Task:    [Client/Project] Action — Specific outcome

STATUSES (in order):
  briefing → scoping → not started → in progress →
  in review → approved → completed
  (also: blocked, parked)

HEALTH PULSE CADENCE:
  Daily    8AM Toronto → standup pulse (5 min)
  Weekly   Monday     → structure pulse (15 min)
  Monthly  1st Monday → deep audit (30 min)

APPROVAL GATES (never skip):
  - External sends → Umair
  - Content publish → Umair
  - CRM write → Umair
  - Folder/list archive → Umair
  - Budget decisions → Umair

FORBIDDEN WITHOUT APPROVAL:
  Delete, archive, send, publish, mutate CRM, create folder #7+
```

---

## Section 9 — Version Log and Skill Update Protocol

When a Health Pulse identifies a naming pattern or routing rule that needs
clarification, the Skeptic proposes an update to this file. Updates require
Umair approval before they are committed. The version number increments on every
approved structural change.

| Version | Date | Change | Approved by |
|---------|------|--------|------------|
| 1.0.0 | 2026-05-14 | Initial structure built from live ClickUp audit of NeuralSync Agency space | Umair |

**To propose an update:** The Skeptic adds a row to this table in draft form and
flags it in `01 · COMMAND → 02 · Decisions and Approvals` with status `in review`.
Umair reviews and approves or rejects. No agent self-approves a skill update.

---

*VCOS Employee ClickUp Operating Skill — v1.0.0*
*NeuralSync Agency · Built by AgentOSync Command Partner*
*Human approval required before any external action.*
