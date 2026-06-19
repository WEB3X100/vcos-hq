# Weekly Research Calibration Prompt

You are improving my Research Agent calibration.

Read all morning briefs from the past week and extract the `MY NOTES ON THIS BRIEF` sections. Compare those notes against the items included in each brief, the sources used, and the topics searched.

Propose updates to my research context:

1. Sources that consistently produced useful signal should be added to the priority list.
2. Topics that consistently produced noise should be added to `What I Specifically Do Not Want`.
3. Missing search angles should become explicit future search queries.
4. Patterns in what I found useful should become explicit significance criteria.
5. Sources that repeatedly produced weak or stale items should be demoted or ignored.

Return proposed changes in this format:

```markdown
# Proposed Research Context Updates

## Add To Trusted Sources

- [Source] - [reason]

## Add To Do Not Want

- [Noise pattern] - [reason]

## Add Search Queries

- [Query] - [what it should catch]

## Update Significance Criteria

- [Criterion] - [reason]

## Demote Or Ignore

- [Source/topic] - [reason]
```

Do not edit the persistent research context until a human approves the proposed changes.
