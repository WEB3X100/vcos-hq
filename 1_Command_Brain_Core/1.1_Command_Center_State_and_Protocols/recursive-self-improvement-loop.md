# Recursive Self-Improvement Loop

Purpose: make VCOS HQ, Mini Interns, and project workspaces compound from every client workflow, failed output, repeated correction, and successful pattern.

VCOS should not only coordinate Mini Interns. VCOS should observe how Mini Interns work, detect where they fail or win, update the relevant context/skill/tool/policy, and redeploy a better version.

## Core Loop

```text
Sensor -> Policy -> Tools -> Quality Gate -> Output -> Feedback -> Learning Update -> Re-test
```

| Layer | VCOS Meaning | Durable Home |
| --- | --- | --- |
| Sensor | What the system can observe: ClickUp changes, Git commits, client calls, forms, WhatsApp, CRM logs, Higgsfield outputs, rejected drafts, dashboard metrics | Project workspace, ClickUp, Drive, trackers, approved logs |
| Policy | What the system may do, must ask, must log, or must never do | `AGENTS.md`, `approval-gates.md`, domain README, employee guides |
| Tools | Deterministic capabilities: APIs, MCP/CLI tools, n8n, Trigger.dev, Modal, GitHub, Higgsfield, Hyperframes, CRM, dashboards | Skill docs, runtime notes, project manifests |
| Quality Gate | Reviewer QA, validation contracts, eval checks, claim checks, human approval | Reviewer QA pack, launch checklists, validation notes |
| Output | Draft, workflow, code, asset, handoff packet, dashboard, proposal, report | Project workspace, client repo, ClickUp, Drive |
| Feedback | Human taste, failed query, blocked generation, QA rejection, performance metric, client response | Tracker, postmortem, review note, session handoff |
| Learning Update | Skill improvement, negative constraint, new checklist, tool request, tracker field, new domain rule | Skill Foundry, decisions, state, domain README, Employee OS |
| Re-test | Controlled rerun proving the system improved | Test note, git commit, validation report, capability dashboard status |

## When To Trigger

Trigger this loop when:

- a human corrects the same behavior twice
- a generated output is rejected
- a tool/API blocks or fails
- a Mini Intern chooses the wrong owner or handoff
- a project repeats the same workflow
- a tracker shows a winning pattern
- a task stalls because context, tool access, or approval rules were unclear
- a client workflow produces reusable knowledge

## Failure Classifier

When something fails, classify the root cause before fixing:

| Failure Type | Symptom | Update |
| --- | --- | --- |
| Context gap | Agent did not know something stable | Update project brief, domain README, `active-context.md`, or Employee guide |
| Skill gap | Agent knew the goal but lacked repeatable process | Add/update skill candidate or reference |
| Tool gap | Agent needed deterministic access/action | Update runtime/tool notes or create integration task |
| Policy gap | Approval, risk, or permission boundary was unclear | Update `approval-gates.md`, `AGENTS.md`, or project manifest |
| QA gap | Bad output passed too far downstream | Update Reviewer QA checklist or validation contract |
| Handoff gap | Next agent lacked enough structured context | Update handoff packet/template |
| Data gap | Missing field, tracker, source, ID, or metric | Update tracker schema or project data model |
| Taste gap | Output was technically correct but not right for Umair/client | Add taste constraint, example, or negative pattern |

## Success Classifier

When something works well, decide if it should compound:

| Success Pattern | Action |
| --- | --- |
| Used once, maybe useful | Save to project note only |
| Used twice or clearly reusable | Add to Skill Registry as pattern/candidate |
| Used 3+ times successfully | Promote to validated skill or installed Mini Intern capability |
| Wins in a client/demo scenario | Add to capability dashboard and proof lane |
| Becomes client-safe/packageable | Move toward Marketplace Skills |

## Mini Intern Loop Template

Each Mini Intern should define:

```markdown
## Recursive Loop

- Sensors:
- Policies:
- Tools:
- Quality gates:
- Outputs:
- Feedback signals:
- Learning update files:
- Re-test method:
```

## Project Workspace Loop

Every client/project workspace should include a `SKILLS_MANIFEST.md`.

The manifest must list:

- active Mini Interns
- HQ skills used by pointer
- local project-only skills
- approval gates
- feedback signals
- where successful patterns should be promoted

Project repos should commit progress and handoffs so another CLI/agent can continue without full chat history.

## Monitoring Intern Pattern

The Sentinel or Monitoring Intern reviews work for improvement opportunities:

1. Scan recent project commits, handoffs, rejected outputs, blockers, and tracker rows.
2. Identify repeated failures and repeated wins.
3. Classify root cause.
4. Create a specific improvement patch or task.
5. Update the relevant skill/context/policy.
6. Re-test the workflow.
7. Promote or demote the capability stage.

## Guardrails

- Do not self-improve by taking external action without approval.
- Do not mutate CRM/customer data as a learning experiment.
- Do not publish generated content just because the loop says it is ready.
- Do not use private client data as public proof without approval.
- Do not copy every HQ skill into every client repo.
- Do not store raw dumps in durable memory; summarize into facts, decisions, links, IDs, and next actions.

## Output Packet

Use this when logging an improvement:

```markdown
## Recursive Improvement Log

- Date:
- Source project / intern:
- Signal:
- Failure or success:
- Root cause category:
- Update made:
- Files changed:
- Re-test method:
- Promotion/demotion decision:
- Approval needed:
```
