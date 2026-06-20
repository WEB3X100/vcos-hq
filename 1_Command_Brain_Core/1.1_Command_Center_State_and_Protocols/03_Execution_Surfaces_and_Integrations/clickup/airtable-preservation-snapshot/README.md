# NeuralSync ClickUp Preservation Snapshot

Purpose: preserve ClickUp context before any NeuralSync Agency restructure.

This folder is the local Airtable import package for the base:

`NeuralSync ClickUp Preservation Snapshot`

## Status

Snapshot status: schema prepared, Airtable import pending.

Live ClickUp restructure status: blocked until Airtable import and review are complete.

## Hard Gate

Do not rename, move, merge, archive, or delete any ClickUp folder, list, or task until:

1. The Airtable base exists.
2. All tables listed below are imported.
3. Active tasks are indexed in the `Tasks` table.
4. Subtasks, checklists, comments, attachments, tags, and custom fields are captured or explicitly marked unavailable.
5. `Verification Log` marks the snapshot as reviewed.
6. Umair approves the migration batch.

## Tables

- `Folders`
- `Lists`
- `Tasks`
- `Subtasks`
- `Checklists`
- `Tags`
- `Comments Index`
- `Attachments and Links`
- `Migration Map`
- `Verification Log`

## Import Order

1. `folders.csv`
2. `lists.csv`
3. `tasks.csv`
4. `subtasks.csv`
5. `checklists.csv`
6. `tags.csv`
7. `comments_index.csv`
8. `attachments_and_links.csv`
9. `migration_map.csv`
10. `verification_log.csv`

## Notes

- The ClickUp connector available in this session can read hierarchy and tasks, but there is no Airtable connector available here.
- This package must be imported into Airtable manually or through a future Airtable-enabled agent.
- CSV files intentionally use stable column names and text fields so Airtable import does not coerce important IDs or dates unexpectedly.

