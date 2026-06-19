# NeuralSync ClickUp Restructure Status

Last updated: 2026-05-15

## Live ClickUp Status

Read-only verification confirmed the old ClickUp structure is still live.

No live ClickUp folders, lists, tasks, tags, subtasks, checklists, due dates, assignees, comments, attachments, custom fields, or descriptions have been intentionally changed by this restructure pass.

## What Has Been Implemented

- Copied ClickUp operating skill into VCOS HQ:
  - `clickup/skill.md`
- Replaced old ClickUp protocol with six-folder, preservation-first protocol:
  - `clickup/protocol.md`
- Added canonical tag taxonomy:
  - `clickup/tag-taxonomy.md`
- Added pinned context task templates:
  - `clickup/pinned-context-task-templates.md`
- Added Airtable preservation import package:
  - `clickup/airtable-preservation-snapshot/`
- Updated HQ memory:
  - `1.2_Headquarters_Memory/key-workspaces.md`
  - `1.2_Headquarters_Memory/decisions.md`
  - `1.1_Command_Center_State_and_Protocols/state.md`

## What Is Still Gated

Do not execute these until Airtable snapshot import and review are complete:

- Create ClickUp destination folders/lists.
- Rename `3. Production Systems`.
- Rename `4. Client Delivery`.
- Rename `7. Internal Operations`.
- Move personal/day-job tasks to private space.
- Move or merge Voice AI tasks.
- Add canonical tags to live tasks.
- Create pinned context tasks in ClickUp.
- Archive dead folders/lists.

## Airtable Import Package

Folder:

`/Users/umairkhalid/_VCOS_Headquarters/1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/clickup/airtable-preservation-snapshot`

Files:

- `README.md`
- `schema.md`
- `folders.csv`
- `lists.csv`
- `tasks.csv`
- `subtasks.csv`
- `checklists.csv`
- `tags.csv`
- `comments_index.csv`
- `attachments_and_links.csv`
- `migration_map.csv`
- `verification_log.csv`

## Known Limitation

No Airtable connector is available in this Codex session. The package is Airtable-ready, but the actual Airtable base must be created/imported manually or by a future Airtable-enabled agent before live ClickUp migration.

