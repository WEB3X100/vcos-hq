# VCOS HQ GitHub Backup Audit - 2026-06-19

## Requested Outcome

Prepare VCOS HQ for a private GitHub backup at `WEB3X100/vcos-hq`, with an audit cleanup and human review before push, so the command brain can be migrated to another laptop.

## Ownership

- Command room/domain: VCOS HQ infrastructure.
- Smallest interface used: AGENTS fast path plus GitHub plugin routing.
- Approval status: draft/review mode until Umair approves repository initialization, commit, remote creation/access, and push.
- Output location: this audit note plus `.gitignore`.

## Findings

- Local VCOS HQ was not a git repository at audit time.
- GitHub connector returned `404` for `WEB3X100/vcos-hq`; likely the repo is not created yet or the connector cannot see it.
- Local git was initialized on branch `main`; the reviewed backup boundary has been staged, but not yet committed or pushed.
- Root `.env` exists and must never be committed.
- HQ folder size is about 11 GB, mostly from project workspaces and Arsenal/vendor repos.
- Largest areas: `3_Project_Workspaces/` about 9.4 GB and `6_Arsenal/` about 1.6 GB.
- Nested git repositories were found inside project workspaces, vendor/tool repos, Arsenal repos, and the employee OS template.
- `3_Project_Workspaces/` already points at `git@github.com:WEB3X100/VCOS-Project-Workspaces.git` and has uncommitted local changes.
- `4_Reusable_Systems_and_Skills/4.1_VCOS_Employee_OS_Template/` already points at `git@github.com:WEB3X100/VCOS-Employee.git` and has uncommitted local changes/deletions.
- Dependency/runtime folders were found, including `node_modules`, `.venv`, `.next`, `__pycache__`, generated graph outputs, and local caches.
- There are 55 `.DS_Store` files.
- Secret pattern scan found no obvious live API key in curated HQ files, but did find the root `.env` and false positives/placeholders in vendored/test code.
- With the current ignore rules, the candidate first HQ commit is 199 files and about 3.4 MB.
- No candidate first-commit files over 10 MB were found.

## Cleanup Applied

- Strengthened root `.gitignore` to exclude secrets, local agent settings, dependency/runtime folders, generated graph outputs, and pointer-first cloned/vendor repos.
- Excluded nested project-workspace and employee-template repositories from the HQ backup boundary so they are not committed as broken embedded repositories.
- No project files, client files, legacy references, or raw work product were deleted.
- The reviewed backup boundary has been staged for the first commit.

## Recommended Human Review

1. Confirm whether `WEB3X100/vcos-hq` should be created as a private repo if GitHub still returns 404.
2. Confirm whether `.DS_Store` files can be removed locally before first commit.
3. Confirm the backup boundary: HQ command brain plus curated project docs, excluding cloned repos/dependencies/vendor checkouts.
4. Confirm whether `VCOS-Project-Workspaces` and `VCOS-Employee` should each get their own commit/push backup pass after HQ.
5. After approval, stage with the updated ignore rules, review `git status`, commit, add the private remote, and push.

## Do Not Include In First Commit

- `.env` or any local credentials.
- `node_modules`, virtualenvs, build outputs, caches, generated graphs, or logs.
- Cloned vendor/tool repos under `6_Arsenal/repos/` or `3_Project_Workspaces/Project repos/`.
- Duplicated external checkouts such as VibeVoice, gbrain copy, MarkItDown, and client implementation repos that already have their own repo path.
