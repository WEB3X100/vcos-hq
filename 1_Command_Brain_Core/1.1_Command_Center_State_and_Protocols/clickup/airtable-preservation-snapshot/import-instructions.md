# Airtable Import Instructions

Base name:

`NeuralSync ClickUp Preservation Snapshot`

## Create Tables

Create these tables in Airtable, then import the matching CSV files from this folder:

1. `Folders` -> `folders.csv`
2. `Lists` -> `lists.csv`
3. `Tasks` -> `tasks.csv`
4. `Subtasks` -> `subtasks.csv`
5. `Checklists` -> `checklists.csv`
6. `Tags` -> `tags.csv`
7. `Comments Index` -> `comments_index.csv`
8. `Attachments and Links` -> `attachments_and_links.csv`
9. `Migration Map` -> `migration_map.csv`
10. `Verification Log` -> `verification_log.csv`

## Field Type Defaults

Use text fields by default for the first import. This prevents Airtable from stripping ClickUp IDs, custom status names, URLs, or date strings.

After import, optional field upgrades:

- URL fields: `task_url`, `subtask_url`, `asset_url`
- Single select: `migration_risk`, `verification_status`, `action`, `risk`, `result`
- Checkbox: `archive_candidate`, `requires_manual_move`, `approved_by_umair`, `canonical`, `additive_only`
- Date/time: `last_updated`, `verified_at`, `created_at`

## Snapshot Completion Checklist

Before live ClickUp restructure:

- [ ] Every live folder appears in `Folders`.
- [ ] Every live list appears in `Lists`.
- [ ] Every active task appears in `Tasks`.
- [ ] Every task with subtasks has subtask IDs recorded.
- [ ] Every task with checklists has checklist state recorded.
- [ ] Every task tag appears in `Tags`.
- [ ] Every task with meaningful comments has comment references in `Comments Index`.
- [ ] Every task with attachments or links has references in `Attachments and Links`.
- [ ] Every move/rename/archive candidate has a row in `Migration Map`.
- [ ] `Verification Log` is updated from `blocked` to `snapshot_reviewed`.
- [ ] Umair approves the first migration batch.

## Do Not Skip

Do not begin with folder renames. Renaming first makes it harder to prove that context was preserved.

Do not use the ClickUp connector for high-risk moves across lists with different custom fields unless Airtable contains the before state.

