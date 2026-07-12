# Next Mission Draft — Correct Mission Control Router Paths

**Status:** ready for L1 issue creation only after stabilization merge, matching L1/L2 SHA check-ins, and reviewed profile installation.
**Not authorization to execute.**

## Mission contract

**Mission ID:** `VCOS-L2-DOC-002`
**Outcome:** `MISSION_CONTROL_PATHS.md` points to the canonical post-restructure Mission Control, session-briefs, and handoff directories.
**Why now:** the verified Wave 1 restructure moved these interfaces, but the root router still names the three pre-restructure paths.

**Base ref:** `origin/main @ <FILL_WITH_MERGED_40_CHARACTER_SHA>`

### Allowed reads

- `AGENTS.md` and its mandatory fast path.
- `MISSION_CONTROL_PATHS.md`.
- Directory names under `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/04_Mission_Control_Dashboard/`.
- Directory names under `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/05_Office_Hours_and_Session_Briefs/`.
- Co-Founder Runtime contracts after they are merged.

### Allowed writes

- `MISSION_CONTROL_PATHS.md` only.

### Required replacements

- `HQ_MC` → `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/04_Mission_Control_Dashboard/mission-control/`
- `HQ_SB` → `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/05_Office_Hours_and_Session_Briefs/session-briefs/`
- `HQ_HANDOFFS` → `1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/05_Office_Hours_and_Session_Briefs/session-briefs/handoffs/`

### Out of scope

- All other files.
- Reformatting or rewriting unrelated router content.
- Castle code, profile files, runtime state, GitHub templates, ClickUp, publishing, deployment, or external messages.
- Multi-agent delegation.

### Acceptance criteria

- [ ] Only `MISSION_CONTROL_PATHS.md` changes.
- [ ] The three canonical paths exactly match the existing directories.
- [ ] No pre-restructure value remains for `HQ_MC`, `HQ_SB`, or `HQ_HANDOFFS`.
- [ ] No placeholders remain after L1 fills the base SHA in the GitHub issue.
- [ ] A single-purpose commit is pushed to an authorized feature branch.
- [ ] A draft PR and standard L2 handoff are produced.

### Validation commands

```bash
test -d '1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/04_Mission_Control_Dashboard/mission-control'
test -d '1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/05_Office_Hours_and_Session_Briefs/session-briefs'
test -d '1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/05_Office_Hours_and_Session_Briefs/session-briefs/handoffs'
git diff --check
git diff --name-only origin/main...HEAD
```

Expected changed-file output: `MISSION_CONTROL_PATHS.md` only.

### Budget and stop conditions

- Wall time: 30 minutes.
- One feature branch and one commit concern.
- Stop if the base SHA differs, tracked tree is dirty before branch creation, any required directory is missing, validation fails, transport fails, or another file would need modification.
- No destructive recovery and no automatic scope expansion.

### Approval boundary

L2 may edit the allowed file, validate, commit, push the feature branch, and open a draft PR. L2 may not merge or perform any external/business-system action.
