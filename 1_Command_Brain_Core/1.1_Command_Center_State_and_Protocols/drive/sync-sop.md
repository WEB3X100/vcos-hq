# Drive + ClickUp Sync SOP

Drive is the file source of truth. ClickUp is the execution source of truth.

## Rule

Every file-backed ClickUp task should include:

- Drive source link
- File or folder name
- Desired output
- Owner
- Due date
- Definition of done
- Where final outputs should be saved

## Codex / Claude Workflow

When given a Drive link:

1. Confirm access or metadata if a connector is available.
2. Add the link to the relevant ClickUp task.
3. Summarize the file only if needed.
4. Add final outputs back to the same ClickUp task.

