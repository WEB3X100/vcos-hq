# Installation and execution handoff for Muse (Claude Code / CoWork)

## Objective
Replace the failing hand-rolled fpdf2 row-height/pagination implementation with the tested measurable-flow renderer in this package. Preserve the existing proposal skill's source and approval gates. Do not modify production or client systems and do not send to Chrome Auto without approval.

## One-time installation
1. Make a backup of `~/workspace/neuralsync-skills/pdf-proposal-generation/SKILL.md` and the existing `build_chrome_condensed_v5.py`.
2. Review `SKILL.md` and `MUSE_UPGRADE_NOTES.md` in this package. Bring the renderer and QA gates into your existing skill; do **not** reintroduce character-count estimates or fixed table cell heights.
3. Copy `scripts/`, `templates/`, `assets/`, `requirements.txt`, `QA-CHECKLIST.md` and `SKILL.md` into the existing skill directory after approval. Preserve the recovered logo file as an interim reference; prefer a verified exact copy of `ns-logo-color__1.pdf` before final issuance.
4. Install requirements in the intended isolated Python environment. Ensure DejaVu Sans is installed locally as a rendering font; do not bundle font files.
5. Use a client-specific JSON input under `templates/` and run:

```bash
python scripts/build_pdf.py templates/chrome_auto.json --output Chrome-Auto-Condensed-Proposal-DRAFT-v6-2026-10-28.pdf
python scripts/qa_pdf.py Chrome-Auto-Condensed-Proposal-DRAFT-v6-2026-10-28.pdf \
  --contents templates/chrome_auto.json --renders qa/rendered --report qa/qa-report.json
python -m unittest discover -s tests -v
```

## Reviewer checklist
- Show all three PNGs to the reviewer, not just a successful PDF-write console message.
- Confirm the exact logo source, author spelling, currency, retainer boundaries, Chris's full name, decision date, and relevant taxes.
- Confirm written phone-plan approval is the build gate and later phases are not pre-approved.
- If a change makes 4 pages, FAIL. Fix content structure/spacing with legibility intact and rerun all checks.

## Suggested task update (PROPOSED, not applied)
Task `86e3t8vpq` — "Build the PDF and proposal generation skill".
Status: `READY FOR MUSE INTEGRATION / USER REVIEW`, not `COMPLETE` until the skill is installed, tested in Muse's environment, and the brand/commercial gaps are reviewed.
Evidence: v6 draft PDF; full-page rendered PNGs; `qa-report.json`; three regression tests, including long-cell overflow failure.
Owner: NeuralSync skill maintainer / Muse integrator (individual not verified).
Due date: not supplied; leave blank.
Next action: install in Muse workspace and run the Chrome Auto acceptance test with real brand logo asset.
