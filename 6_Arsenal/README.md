# 6_Arsenal — Swiss Army Knife

Your personal curated weapon rack. Every gem, repo, tool, framework, API, prompt pack, or reference you've hunted and found lives here. When you're stuck, this is the first place to look.

## What belongs here

| Type | Examples |
|------|---------|
| `repo` | GitHub repos with useful agents, frameworks, components |
| `tool` | SaaS tools, CLIs, browser extensions |
| `framework` | AI frameworks, workflow engines, scraping stacks |
| `api` | APIs you can connect to for data, automation, media |
| `prompt-pack` | Prompt libraries, system prompt templates |
| `tutorial` | Deep guides, courses, walkthroughs worth re-reading |
| `dataset` | Reference data, training sets, curated lists |
| `workflow` | N8n/Make/Zapier templates, automation blueprints |

What does NOT belong here: client-specific files (those live in Drive/ClickUp), active project work (that's `3_Project_Workspaces/`), or packaged VCOS skills (those graduate to `4_Reusable_Systems_and_Skills/`).

---

## Query Protocol

**When you are stuck on a task, say:**
> "Arsenal query: I need to [solve X / build Y / automate Z]"

Claude will read `arsenal-index.md`, match entries by `problem-tags`, and return a ranked shortlist of what you already own that's relevant.

**Trigger phrases that load the arsenal:**
- "what do I have for…"
- "arsenal query:"
- "Swiss Army Knife for…"
- "what tools do I own that can…"
- "check my arsenal"

---

## Add a Gem

**Say:** `"Add gem: [URL or name] — [one-line description]"`

Claude will ask for any missing fields, then append the entry to `arsenal-index.md` using this format:

```
| Name | Type | URL | Problem it solves | problem-tags | Status | Notes |
```

**Status values:** `untested` → `active` → `deprecated`

**Promotion rule:** If you use a gem 3+ times with clear value, flag it as a skill candidate in `4_Reusable_Systems_and_Skills/4.2_Skill_Governance_and_Candidates/vcos-task-skill-map.md`.

---

## File Map

| File | Purpose |
|------|---------|
| `arsenal-index.md` | Master table of all gems — the only file you query |
| `README.md` | This file — query protocol and add instructions |

---

## Agent Instructions

When receiving an arsenal query:
1. Read `6_Arsenal/arsenal-index.md`.
2. Filter rows where `problem-tags` overlap with the user's stated problem.
3. Return a ranked shortlist (most relevant first) with: name, type, URL, and one sentence on why it fits.
4. If nothing matches, say so — do not invent entries.

When receiving "add gem":
1. Confirm name, type, URL, problem-it-solves, and at least two problem-tags.
2. Append a new row to `arsenal-index.md`.
3. Confirm the addition.
