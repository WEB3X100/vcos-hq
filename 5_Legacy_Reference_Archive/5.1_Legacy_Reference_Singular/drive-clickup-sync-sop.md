# Drive + ClickUp Sync SOP

Purpose: keep collaborative files in Drive and execution control in ClickUp.

## Source Of Truth

- Drive is the home for working files: sheets, docs, decks, folders, drafts, exports, assets.
- ClickUp is the home for execution: owner, status, due date, next action, decisions, and blockers.
- Every ClickUp task that depends on a file should include the Drive link in the task description.

## Required ClickUp Fields For File-Backed Work

Each file-backed task should include:

- Drive source link
- File or folder name
- Desired output
- Owner
- Due date
- Definition of done
- Where final outputs should be saved

## Folder Pattern

Use the Drive folder structure as the file home and ClickUp command rooms as the work home.

Suggested mapping:

| Drive folder | ClickUp home |
| --- | --- |
| `Claude code W N8N` | Production Control Room / n8n + MCP tasks |
| `Openclaw Architecture` | Production Control Room / OpenClaw tasks |
| `Marketing Automation` | Production Control Room / marketing automation tasks |
| `Vapi Voice Agent` | Production Control Room / voice AI tasks |
| `Cowork` | Q3 Command Center or Production, depending on work type |
| `VCOS HQ` | Q3 Command Center / operating system references |
| `100x Engineer` | Production or Team Management, depending on work type |

## Codex Workflow

When a user gives a Drive link:

1. Confirm access with Google Drive metadata.
2. Add the Drive link to the relevant ClickUp task.
3. If no task exists, create one in the right command room using `key-workspaces.md`.
4. Do not copy file contents into ClickUp unless it is a short summary or definition of done.
5. Add final output links back to the same ClickUp task.

## Nate Herk Sheet

- File: `Nate Herk - Video Database.xlsx`
- Drive ID: `13M5N8pJnUu-R7bh8zqM-hUBCZsYaydZ5`
- ClickUp task: `86e1acgyb`

