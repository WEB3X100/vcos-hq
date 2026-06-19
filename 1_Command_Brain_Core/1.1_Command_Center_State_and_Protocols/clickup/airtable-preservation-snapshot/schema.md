# Airtable Schema — NeuralSync ClickUp Preservation Snapshot

## `Folders`

Primary field: `folder_id`

Fields:

- `folder_id`
- `folder_name`
- `space_id`
- `space_name`
- `current_status`
- `target_folder_name`
- `migration_action`
- `archive_candidate`
- `notes`

## `Lists`

Primary field: `list_id`

Fields:

- `list_id`
- `list_name`
- `folder_id`
- `folder_name`
- `space_id`
- `space_name`
- `target_folder_name`
- `target_list_name`
- `migration_action`
- `archive_candidate`
- `notes`

## `Tasks`

Primary field: `task_id`

Fields:

- `task_id`
- `task_url`
- `current_folder_id`
- `current_folder_name`
- `current_list_id`
- `current_list_name`
- `parent_task_id`
- `parent_task_name`
- `task_name`
- `original_task_name`
- `full_description`
- `status`
- `priority`
- `assignees`
- `due_date`
- `start_date`
- `tags`
- `custom_fields_summary`
- `subtask_count`
- `subtask_ids`
- `checklist_count`
- `checklist_summary`
- `comments_index_status`
- `attachments_links_summary`
- `last_updated`
- `proposed_destination_folder`
- `proposed_destination_list`
- `migration_risk`
- `verification_status`
- `notes`

## `Subtasks`

Primary field: `subtask_id`

Fields:

- `subtask_id`
- `parent_task_id`
- `subtask_url`
- `current_folder_name`
- `current_list_name`
- `subtask_name`
- `status`
- `assignees`
- `due_date`
- `tags`
- `description_present`
- `last_updated`
- `proposed_destination_folder`
- `proposed_destination_list`
- `verification_status`

## `Checklists`

Primary field: `checklist_record_id`

Fields:

- `checklist_record_id`
- `task_id`
- `task_url`
- `checklist_name`
- `item_name`
- `item_status`
- `assignee`
- `due_date`
- `preservation_status`
- `notes`

## `Tags`

Primary field: `tag_record_id`

Fields:

- `tag_record_id`
- `task_id`
- `task_url`
- `tag_name`
- `tag_type`
- `canonical`
- `additive_only`
- `notes`

## `Comments Index`

Primary field: `comment_record_id`

Fields:

- `comment_record_id`
- `task_id`
- `task_url`
- `comment_id`
- `author`
- `created_at`
- `summary`
- `full_comment_available`
- `migration_relevance`
- `notes`

## `Attachments and Links`

Primary field: `asset_record_id`

Fields:

- `asset_record_id`
- `task_id`
- `task_url`
- `asset_type`
- `asset_name`
- `asset_url`
- `source_field`
- `preservation_status`
- `notes`

## `Migration Map`

Primary field: `migration_record_id`

Fields:

- `migration_record_id`
- `object_type`
- `object_id`
- `object_name`
- `current_folder_name`
- `current_list_name`
- `target_folder_name`
- `target_list_name`
- `action`
- `risk`
- `requires_manual_move`
- `reason`
- `approved_by_umair`
- `status`

## `Verification Log`

Primary field: `verification_record_id`

Fields:

- `verification_record_id`
- `batch_name`
- `object_type`
- `object_id`
- `object_name`
- `pre_move_snapshot_present`
- `description_verified`
- `tags_verified`
- `assignees_verified`
- `dates_verified`
- `subtasks_verified`
- `checklists_verified`
- `comments_verified`
- `attachments_links_verified`
- `custom_fields_verified`
- `verified_by`
- `verified_at`
- `result`
- `notes`

