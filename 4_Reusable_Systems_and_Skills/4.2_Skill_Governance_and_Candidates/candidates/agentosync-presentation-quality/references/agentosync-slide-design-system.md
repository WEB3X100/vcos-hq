# AgentOSync Slide Design System

Use this reference when coding, redesigning, or reviewing AgentOSync decks.

## Design Intent

AgentOSync decks should feel like an operating review from a partner who has already understood the business. The design must avoid hype and show the client their own workflow more clearly than they have seen it before.

## Brand Tokens

Use these defaults unless a specific client template overrides them:

| Token | Value | Use |
| --- | --- | --- |
| `navy` | `#020722` | slide background |
| `panel` | `#07142c` | proof-object panels |
| `panel2` | `#0a1c36` | callouts and secondary rails |
| `line` | `#173555` | subtle borders/dividers |
| `cyan` | `#36d7ff` | primary accent, active route |
| `blue` | `#1d72ff` | secondary accent |
| `green` | `#22e3a1` | approved/safe/ready |
| `gold` | `#f7cf68` | review/waiting |
| `red` | `#ff6b6b` | risk/blocked/never automatic |
| `white` | `#ffffff` | main text |
| `paper` | `#eef7ff` | secondary readable text |
| `muted` | `#a9bbca` | supporting labels only |

## Typography

- Use a clean sans system such as Aptos/Aptos Display when building PowerPoint.
- Claim title: 34-42px.
- Section claim: 34-40px with generous whitespace.
- Panel title: 16-19px.
- Panel body: 13-16px.
- Table labels: 12-14px, high contrast.
- Do not use tiny gray text for important content.

## Layout Grammar

Use a `1280x720` canvas. Keep the top cyan rule as the consistent deck spine.

Preferred slide families:

- Diagnosis table: role, context needed, what breaks.
- Role section divider: one sharp claim plus one support sentence.
- Workflow map: current tool -> structured fields -> record -> draft -> approval.
- Priority queue: item, intent, urgency, next action.
- Approval matrix: can draft, needs review, never automatic.
- Owner brief: daily operating brief plus exception commands.
- Operating model: three-role system and handoff rhythm.
- Client next steps: 4-5 boxes that form a validation path.

## Proof Object Rules

Every slide needs one main proof object. It may be a table, queue, flow, matrix, swimlane, role map, checklist, chart, or operating brief.

Do not use boxes as decoration. A box must represent a stage, role, status, rule, queue item, or decision point.

For screenshots:

- Use only if crisp at final slide size.
- If phone text is hard to read, recreate it as a clean flow, table, or message-state diagram.
- Do not use blurry screenshots as proof. It weakens trust.

## Component Grammar

Panel:

- Fill `panel`, line `line`, 1px border.
- Top accent strip 5px.
- 16px horizontal padding minimum.
- 16px vertical breathing room minimum for 2+ lines.

Flow node:

- Equal width and height across equal stages.
- Semantic connectors only; do not use arrows as decoration.
- Direction must be left-to-right unless showing escalation upward.

Queue:

- Header row in cyan.
- Status chips use green/gold/red.
- Keep action copy short enough to scan.

CTA step:

- Numbered title.
- One short body sentence.
- Client-facing verb: pick, confirm, define, walk, decide.

## Visual QA

Before export, render all slides and check:

- no text spill, clipping, overlap, or cramped boxes
- consistent top rule, page marker, kicker placement
- no low-resolution logo or rough crop
- no three consecutive slides with the same layout rhythm
- visual proof is readable at contact-sheet size
- the PDF works without speaker notes
