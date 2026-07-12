# Weekly Office Hours Plan: 2026-06-15 to 2026-06-21

Status: Draft. Built from `sunday-office-hours-2026-06-14.md` before Umair confirms final goals for the week.

Purpose: pressure-test the week, clarify outcomes, define trackable subtasks, and expose manual work that should become Claude Code/Codex routines, skills, or scheduled tasks.

## Office Hours Pressure Test

### 1. Demand Reality

The week has two live proof lanes and one blocked GTM lane:

- Dealership OS has a real demo, but needs a sales-facing packet that proves "we will not miss leads after posting cars."
- AMAX has a concrete finance/control-tower proof, but cannot move into live QB/DB mapping until CFO/Maaz policy approvals are recorded.
- Content-intel cannot start quality automation until Umair provides voice calibration.

The danger is building more infrastructure while the real blockers are approval, packaging, and human-provided inputs.

### 2. Status Quo That Must Change

- Dealership demo is real but not yet compressed into a 4-minute owner story.
- AMAX finance work is strong but still waiting on policy sign-off.
- Personal/health constraints surfaced but are not yet on an execution checklist.
- Weekly review context now exists locally and in ClickUp, but it needs one successful Claude/team review cycle before promotion.

### 3. Desperate Specificity

The most specific humans this week:

- Sameer/Uzair need to understand and replay one sales-owner workflow.
- Maaz/CFO need to approve or revise the AMAX accounting/control tower direction.
- Umair needs to provide voice examples and decide whether these three lanes are truly this week's top 3.

### 4. Narrowest Wedge

Do not broaden into full platforms.

- Dealership: one day, three leads, one owner morning brief.
- AMAX: one approval packet, four to five policy decisions, one narrow finance view after approval.
- Content: one voice calibration packet, then one manual content-intel run.

### 5. Observation Required

By next Sunday, each active lane needs an observable outcome:

- Dealership: owner can explain the 4-minute flow without the agent present.
- AMAX: explicit yes/revise decision captured for COA/deferred revenue/TICO/account cleanup.
- Content: voice files exist, or the blocker is officially reclassified as "Umair input not available."

### 6. Future Fit

These lanes fit the 12-month VCOS direction if they produce reusable operating chunks:

- Dealership sales demo packet -> reusable dealership proof workflow.
- AMAX CFO approval packet -> reusable finance-control approval workflow.
- Voice calibration -> reusable founder-voice content system.
- Weekly office hours -> reusable skill-harvest and task-slowdown detection loop.

## Draft Weekly Outcomes

### Outcome 1: Dealership Sales Demo Packet

Goal: create a sanitized one-day sales lead manager packet that Sameer/Uzair can rehearse and explain in 4 minutes.

Definition of done:

- 3 fake Marketplace leads tied to 2 inventory records.
- Each lead has intent/temperature classification.
- Each lead has an approval-gated reply draft.
- One owner morning brief covers hot leads, stale inventory, competitor signal, and one content idea.
- 4-minute owner talk track exists.
- No external messages, CRM mutation, or marketplace publishing.

Slowdown sensors:

- If no sample leads exist by midweek, generate fake leads from the existing schema.
- If the flow takes longer than 4 minutes to explain, reduce the demo to one hot lead + one stale follow-up + one morning brief.
- If owner cannot restate the value, rewrite the story around "we do not miss leads after posting cars."

Draft subtasks:

| Subtask | Description | Done Means | Manual Work To Watch | Automation Candidate |
| --- | --- | --- | --- | --- |
| Build sample lead set | Create 3 sanitized Marketplace-style messages and map them to 2 inventory records. | Lead table exists with source, vehicle, intent, urgency, next action. | Inventing examples repeatedly. | Fake lead generator for dealership demos. |
| Classify lead intent | Tag each lead as hot/warm/cold and identify reply strategy. | Each lead has a temperature tag and reason. | Re-explaining intent taxonomy. | Lead-intent classifier prompt/skill. |
| Draft approval replies | Write reply drafts that require human approval before send. | Each lead has a safe draft and approval note. | Rewriting similar replies. | Approval-gated reply draft routine. |
| Create owner morning brief | Summarize what needs owner approval this morning. | One brief under 1 page. | Rebuilding brief format manually. | Dealership morning brief template. |
| Rehearse 4-minute flow | Script owner walkthrough in plain language. | Owner can explain value as "we do not miss leads." | Long unfocused explanation. | Sales-demo talk-track generator. |

Approval gates:

- No real customer data.
- No external sends.
- No CRM/marketplace mutation.
- No pricing/financing/warranty language without approval.

## Outcome 2: AMAX CFO Approval Unblock

Goal: turn the AMAX COA/finance-control work into a clear approval packet for Maaz/CFO so live QuickBooks/DB/ToolJet mapping does not proceed on assumptions.

Definition of done:

- Approval packet summarizes upgraded COA direction.
- Four to five policy questions are explicit.
- CFO/Maaz response is captured as yes/revise/blocked for each item.
- Next handoff to Sara/TrySoft/Sohaib is only drafted until approval.

Slowdown sensors:

- If approval meeting is not scheduled, the blocker is scheduling/decision access, not build complexity.
- If CFO cannot answer policy questions, convert each into accountant-facing wording.
- If the packet is too broad, reduce to one narrow finance view: cash, AR aging, AP aging, P&L by class.

Draft subtasks:

| Subtask | Description | Done Means | Manual Work To Watch | Automation Candidate |
| --- | --- | --- | --- | --- |
| Compress approval packet | Summarize COA upgrade, deferred revenue, TICO, account cleanup decisions. | One approval-ready packet exists. | Rewriting CFO summaries. | CFO approval packet generator. |
| Extract policy decision table | Create yes/revise/block table for 4-5 decisions. | Each decision has owner, risk, recommended answer. | Hunting decisions across docs. | Policy-decision extractor. |
| Prepare Maaz/CFO agenda | Draft agenda for review call/message. | Agenda explains decisions and consequence of no answer. | Recreating meeting agenda. | Approval meeting agenda template. |
| Record approval result | Capture answer per decision after review. | Handoff notes and ClickUp draft updated after human approval. | Manual status reconciliation. | Approval result logger. |
| Draft mapping handoff | Prepare QB -> DB -> Hermes -> ToolJet next-step handoff, gated on approval. | Handoff draft exists but is not executed. | Re-explaining data map. | Finance mapping handoff template. |

Approval gates:

- No live QuickBooks changes.
- No client-facing finance claims.
- No DB/ToolJet mapping based on unapproved accounting policy.
- No account rename/split/delete until Maaz/CFO approval.

## Outcome 3: Voice Calibration + First Content-Intel Manual Run

Goal: unblock content-intel by collecting Umair voice calibration and running one manual source sweep + draft set.

Definition of done:

- 10 approved posts/drafts are collected.
- 5 rejected or never-say examples are collected.
- 3-5 tone rules are written.
- One manual content-intel run produces signal summary + 3 draft posts.
- Rejections/edits are logged before any automation.

Slowdown sensors:

- If voice samples are not provided, do not build n8n or auto-posting.
- If drafts do not sound like Umair, improve voice rules before adding sources.
- If manual run takes too long, identify which step is slow: source finding, signal filtering, drafting, or editing.

Draft subtasks:

| Subtask | Description | Done Means | Manual Work To Watch | Automation Candidate |
| --- | --- | --- | --- | --- |
| Collect approved examples | Umair supplies 10 examples that sound right. | `approved-posts.md` or equivalent content exists. | Repeatedly asking for voice context. | Voice calibration intake form. |
| Collect rejected examples | Umair supplies 5 examples/patterns to avoid. | Rejected/never-say list exists. | Fixing the same tone mistakes. | Voice negative-constraint extractor. |
| Write tone rules | Convert examples into 3-5 operating rules. | Short tone rules exist. | Long subjective editing loops. | Tone-rule synthesizer. |
| Run manual source sweep | Review trusted AI/SMB/dealership/travel signals. | Signal summary exists. | Re-searching same sources. | Source sweep routine. |
| Draft 3 posts | Draft three approval-gated posts in Umair voice. | Drafts exist and are marked Draft-Only. | Rewriting from scratch. | Content-intel draft routine after 5 manual runs. |

Approval gates:

- No public posting.
- No auto-posting integration.
- No client names, screenshots, or proof claims without approval.
- No n8n automation before 5 manual runs and feedback logging.

## Outcome 4: Personal Operating Constraints

Goal: remove personal/health friction that affects execution capacity.

Definition of done:

- Namaz consistency tracker exists in personal checklist or Q3 Command Center.
- Dental booking task exists.
- Physio booking task exists.
- Walk-in clinic hair/scalp task exists.
- Pakistan meds sequencing and knee allergy cream task exists.

Slowdown sensors:

- If personal tasks stay in chat, they will not execute.
- If they require calls during business hours, schedule time blocks rather than leaving them as generic todos.

Draft subtasks:

| Subtask | Description | Done Means | Manual Work To Watch | Automation Candidate |
| --- | --- | --- | --- | --- |
| Namaz tracker | Add simple weekly tracker outside noisy project files. | Tracker exists and is easy to update. | Re-discussing consistency without a visible tracker. | Weekly personal operating review prompt. |
| Book dental | Create dated task and make call/booking. | Appointment booked or blocker recorded. | Repeating same health todo weekly. | Appointment follow-up reminder. |
| Book physio | Create dated task and make call/booking. | Appointment booked or blocker recorded. | Same as above. | Appointment follow-up reminder. |
| Walk-in clinic | Plan visit for hair/scalp and meds sequence. | Visit completed or date chosen. | Medical items drifting. | Health checklist routine. |
| Knee cream | Add specific item to errand/meds checklist. | Item acquired/applied or blocker recorded. | Small errands living in memory only. | Personal checklist sweep. |

Approval gates:

- Personal task tracking can be internal.
- Do not expose private health details to team/client surfaces.

## Outcome 5: Weekly Review + Skill Harvest System

Goal: validate the Claude/Codex weekly review loop and make slowdowns visible.

Definition of done:

- ClickUp task `86e1w6343` is used as Claude/team-visible context.
- One Claude/team review draft is produced from that task.
- Corrections are logged.
- Skill candidate `claude-visible-weekly-review` has one validation note.
- Weekly work review automation remains Draft-Only.

Slowdown sensors:

- If Claude reviews stale lanes again, the ClickUp task context is insufficient.
- If team cannot tell what to do next, task descriptions need sharper "done means" fields.
- If automation recommendations are vague, require input/output packet and failure modes.

Draft subtasks:

| Subtask | Description | Done Means | Manual Work To Watch | Automation Candidate |
| --- | --- | --- | --- | --- |
| Review ClickUp packet | Claude/team reviews task `86e1w6343`. | Draft feedback returned. | Copy-pasting local context. | Claude-visible context packet skill. |
| Log corrections | Capture where Claude misunderstood or lacked context. | Correction note exists. | Same context mistake repeating. | Context-mistake logger. |
| Update skill candidate | Add validation result to `claude-visible-weekly-review`. | Validation log updated. | Skill candidates not getting feedback. | Weekly skill validation routine. |
| Harvest slowdowns | Identify manual steps from this week. | Candidate table updated. | Manual work disappearing into chat. | Slowdown detector in weekly review. |

Approval gates:

- No team notification unless Umair approves.
- No public/client use.
- No ClickUp mutation beyond approved task updates.

## Draft ClickUp Task Payloads

Do not post until Umair approves.

### [3.6] Dealership OS - build one-day sales lead manager demo packet

Description:

Build a sanitized one-day dealership sales packet using 3 fake Marketplace leads and 2 inventory records. Include intent/temperature classification, approval-gated reply drafts, one owner morning brief, and a 4-minute owner talk track. Done means Sameer/Uzair can explain the value as: "we do not miss leads after posting cars." Draft-only; no external sends, CRM mutation, marketplace publishing, pricing, financing, or warranty language.

Subtasks:

- Create 3 sample Marketplace-style leads tied to 2 inventory records.
- Tag each lead hot/warm/cold with reason.
- Draft approval-gated replies.
- Produce one owner morning brief.
- Rehearse and tighten 4-minute owner flow.

### [3.7] AMAX - secure CFO approval on COA/deferred revenue/TICO

Description:

Prepare and present the AMAX finance approval packet for Maaz/CFO. Capture explicit yes/revise/block answers on upgraded COA direction, deferred revenue for Hajj/Umrah deposits, TICO/trust handling, and which accounts Sara can rename/split. Done means each policy item has a recorded answer and the QB -> DB -> Hermes -> ToolJet mapping handoff is ready but not executed.

Subtasks:

- Compress approval packet.
- Extract four to five policy decisions.
- Draft Maaz/CFO review agenda.
- Record approval results after human/client review.
- Draft gated mapping handoff.

### [4.2] Skill Candidate - validate Claude-visible weekly review context

Description:

Use ClickUp task `86e1w6343` as the Claude/team-visible source packet for weekly review and skill harvest because Claude may not have local file access. Done means Claude/team can produce a useful weekly status + skill-harvest draft from ClickUp context alone, and the local skill candidate validation log is updated.

Subtasks:

- Ask Claude/team to review task `86e1w6343`.
- Log what context was sufficient or missing.
- Update `claude-visible-weekly-review` validation log.
- Identify next context packet improvement.

### [Q3] Personal operating constraints - health + namaz execution checklist

Description:

Create a private personal execution checklist for namaz consistency and health follow-through. Done means dental, physio, walk-in clinic, meds sequence, and knee cream each have a dated next action or recorded blocker. Keep private; do not expose health details to team/client surfaces.

Subtasks:

- Add namaz consistency tracker.
- Book dental.
- Book physio.
- Plan walk-in clinic for hair/scalp and medication sequence.
- Add knee allergy cream to errand/meds checklist.

## Slowdown Detection Board

Use this during the week.

| Slowdown | If Observed | Likely Cause | Response | Automation/Skill Candidate |
| --- | --- | --- | --- | --- |
| Dealership packet not started | No sample leads by midweek | Artifact creation too fuzzy | Generate fake leads and reduce scope | Dealership demo packet generator |
| AMAX approval not scheduled | No Maaz/CFO review path | Missing person/approval | Draft one message/agenda for Umair approval | Approval meeting packet routine |
| Content-intel still blocked | No voice files | Human input missing | Stop automation; ask for voice pack only | Voice calibration intake |
| Personal tasks drift | Still only in chat | No execution surface | Move to Q3/private checklist | Personal operating checklist |
| Claude gives stale review | Mentions parked lanes as active | Context packet insufficient | Update ClickUp task/context priority | Claude-visible context packet |
| Same manual summary repeated | Similar task descriptions written 2+ times | No template | Capture task payload format | ClickUp task payload generator |

## Automation / Skill Harvest Candidates

| Candidate | Owning Home | Current Stage | Trigger | Input Packet | Output Packet | Approval Gate | Next Validation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Dealership one-day demo packet generator | `3.6`, then `2.1`/`4.2` if repeated | Pattern | "build dealership sales demo packet" | Inventory, fake/real leads, approval limits | Demo packet + owner brief + talk track | No external send/CRM mutation | Build manually once this week |
| AMAX CFO approval packet generator | `3.7`, possible Finance/Ops skill | Pattern | "prepare AMAX CFO approval packet" | COA workbook, cfo brief, open decisions | Decision table + agenda + handoff | CFO/Maaz approval before live changes | Use for this approval round |
| Voice calibration intake | `content-intel-routine`, then Marketing/Infrastructure | Pattern | "calibrate Umair voice" | Approved/rejected examples, tone notes | Tone rules + negative constraints | Approval before publishing | Collect pack this week |
| Claude-visible context packet | `4.2` | Skill Candidate | "Claude doesn't have local context" | Fast path + latest brief + task purpose | ClickUp task/comment context packet | Approval before team notify/client use | Validate task `86e1w6343` |
| Weekly slowdown detector | `1.1`/`4.2` | Experiment | "where is work slowing down?" | Current weekly tasks and statuses | Slowdown board + automation candidates | Approval before task mutation | Use in next Sunday review |

## Open Questions For Umair

1. Are these still the right top three work goals for this week: Dealership demo packet, AMAX CFO approval, voice calibration/content-intel?
2. Which one outcome must happen even if the week gets messy?
3. Do you want the personal health/namaz items tracked in ClickUp Q3, a private checklist, or only in Sunday brief constraints?
4. Should I create the ClickUp task set from the draft payloads after you approve wording?
5. Who is the actual reviewer for the Claude-visible weekly review task: Claude agent, Usman/team, or just Umair first?

## Recommendation

Keep the week to three work lanes plus one personal operating lane:

1. Dealership owner-demo packet.
2. AMAX CFO approval unblock.
3. Voice calibration for content-intel.
4. Private Q3 health/namaz execution checklist.

Everything else goes into parking lot unless it directly unblocks one of those lanes.

