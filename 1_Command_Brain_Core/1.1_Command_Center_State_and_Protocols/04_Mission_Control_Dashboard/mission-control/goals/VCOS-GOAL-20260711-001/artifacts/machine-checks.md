# Machine Checks

| Check | Result | Evidence |
| --- | --- | --- |
| Goal packet files exist | PASS | all required binder, dispatch, and contract files exist |
| Diagnostic script syntax | PASS | `bash -n artifacts/transport-diagnostic-git-bash.sh` exited 0 |
| `git diff --check` | PASS | command exited 0 in stabilization worktree |
| Remote branch exists | FAIL at last L1 observation | `git ls-remote` returned no ref |
| Remote/local SHA match | NOT RUN | remote ref absent |
| Draft review URL | NOT RUN | remote ref absent |
