# Machine Checks

| Check | Result | Evidence |
| --- | --- | --- |
| Goal packet files exist | PASS | all required binder, dispatch, and contract files exist |
| Diagnostic script syntax | PASS | `bash -n artifacts/transport-diagnostic-git-bash.sh` exited 0 |
| `git diff --check` | PASS | command exited 0 in stabilization worktree |
| Remote branch exists | FAIL at final L1 observation | `git ls-remote --heads origin refs/heads/feature/vcos-stab-03-init-docs` returned no ref; stabilization branch remained visible at `3ca6a2d` |
| Remote/local SHA match | NOT RUN | remote ref absent |
| Draft review URL | NOT RUN | remote ref absent |

## L2 transport diagnostic

| Check | Result | Evidence |
| --- | --- | --- |
| DNS resolution | PASS | L2 `TRANSPORT_DIAGNOSTIC_V2` |
| GitHub HTTPS 443 | PASS | L2 `TRANSPORT_DIAGNOSTIC_V2` |
| GitHub SSH 22 | AUTH_FAILED | L2 `TRANSPORT_DIAGNOSTIC_V2` |
| GitHub SSH 443 fallback | BLOCKED | L2 `TRANSPORT_DIAGNOSTIC_V2` |
| `git ls-remote origin` | TIMEOUT | origin uses unresolved SSH authentication path |
