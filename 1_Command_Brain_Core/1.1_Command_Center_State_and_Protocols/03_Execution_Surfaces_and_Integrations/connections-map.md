# VCOS Connections Map

Purpose: track what VCOS can reach, why it matters, and what permissions are safe.

Default stance: read-first, least privilege, approval-aware writes.

| Bucket | System | Status | Access pattern | Safe first capability | Write gate |
| --- | --- | --- | --- | --- | --- |
| Tasks | ClickUp | known workspace IDs | Connector/API/CLI when available | Read command-room tasks and blockers | Approval before status/comment changes visible to clients |
| Files | Google Drive | preferred file truth | Connector/Drive tools | Find and summarize linked docs/decks/sheets | Approval before sharing, deleting, or final client edits |
| Code / OS history | GitHub | recommended for VCOS HQ | Git repo + private remote | Issues, diffs, PR review, routine source | Approval before public repo changes or destructive git actions |
| Calendar | Google Calendar | candidate | Connector | Daily planning and availability summary | Approval before creating/changing external events |
| Comms | Slack / Telegram | candidate approval surface | Connector/API once selected | Approval queue and notifications | Approval before external/client sends |
| Email | Gmail / Workspace | candidate | Connector/API/CLI | Triage and draft replies | Approval before sending |
| CRM | Odoo / dealership CRM | gated candidate | API/browser only after workflow trust | Read mock/internal lead data | Approval before customer/CRM mutation |
| Meetings | Fireflies or transcripts | candidate | Export/import or connector | Extract decisions and action items | Approval before sharing externally |
| Revenue | Stripe/QuickBooks/Odoo | future candidate | API/read-only first | Revenue snapshots and anomaly review | Approval before financial changes |
| Knowledge | VCOS Markdown + Drive | active | Local files + Drive | Fast-path memory and curated wiki | Approval before archival/deletion |
| Knowledge graph | Graphify | active-evaluation | Local CLI + project `graphify-out/graph.json` | Query project/domain relationships before broad reads | Approval before exposing MCP/HTTP server or sharing private graph outputs |

## Connection Rules

- Prefer APIs or CLIs with narrow endpoint references over broad always-on MCP context when token cost matters.
- Keep API reference notes local and concise when a workflow repeatedly uses the same endpoints.
- Put stable IDs directly in skill files when it prevents repeated discovery calls.
- Use separate service accounts or least-privilege tokens for agent access where possible.
- Never paste API keys into chat. Use `.env` locally or configured secret stores/cloud environment variables.
- Remote routines cannot see local `.env` files. They need explicit cloud environment variables.

## Initial Priority

1. GitHub private repo for VCOS HQ history and issues.
2. ClickUp read path for command-room blocker and task summaries.
3. Google Drive read path for file truth.
4. Slack or Telegram approval surface.
5. Calendar daily planning.
6. CRM only after the Employee 01 mock workflow passes approval gates.
