# OpenMaus Access-Recovery Prompt

Use this only after directly attaching/importing the files in `openmaus-import/` or connecting authenticated read-only repository access.

```text
You are Maya. Run an ACCESS-ONLY verification. Do not perform marketing strategy, ICP selection, copywriting, proposal drafting, deck drafting, memory updates, publishing, sending, CRM changes, installs, permission changes, or spending.

Expected canonical source:
WEB3X100/vcos-hq/7_VCOS_Interns/7.1_NeuralSync_Marketing_Intern/

Expected import files:
- README.md
- SOUL.md
- MEMORY-SEED.md
- CLAIMS-AND-APPROVALS.md
- EMAIL-ACTIVATION.md
- SKILL.md
- ONBOARDING-PROMPT.md
- AGENT-ROSTER.md
- TEST-PROMPTS.md

For each file, return:
- exact filename;
- exact location or connector used;
- readable: YES/NO;
- first H1 heading only;
- whether it is canonical, an import snapshot, cached, or provenance unknown;
- last-modified date if visible.

Then return exactly one verdict:
- ACCESS PASS — all required import files are readable and provenance is known;
- ACCESS PARTIAL — identify missing files;
- ACCESS FAIL — no canonical or directly imported snapshot is readable.

Do not cite facts from SOUL.md, MEMORY.md, or any brand file unless you can identify the exact readable copy and provenance in this report. Do not continue beyond this access test.
```
