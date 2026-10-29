---
name: neuralsync-proposal-pdf
description: Generate and rigorously validate concise NeuralSync client proposal PDFs from isolated, source-grounded JSON without clipped tables, body/footer collisions, altered branding, or unapproved commercial claims.
metadata:
  version: 1.0.0
  updated: 2026-10-28
  status: DRAFT_FOR_INTERNAL_REVIEW
---

# NeuralSync Proposal PDF — Muse Skill

## Trigger
Use when asked to create, revise, diagnose, or QA a client proposal PDF, offer summary, or compact decision document. The skill works with Muse / Claude Code or another Python-capable agent.

## Core rule
**Content truth and physical page layout are different jobs.** Ground every claim in the named client's approved source, store approved content once in JSON, render with a measurement-based flow engine, then inspect every rendered page. Never adjust only fonts in an attempt to fix clipping.

## Authority and approvals
1. Read the named client project context / authoritative proposal. Read only related sources for the job. Sources from another client are patterns only, never commercial facts.
2. Respect any user-specific output contract ahead of a reusable template. Chrome Auto overrides the pre-existing skill's page-1 price convention: its **only numeric prices appear in the final pricing section**.
3. Labels: `VERIFIED`, `USER-DIRECTED`, `INFERRED`, `PROPOSED`, `STALE`. Scope and price not approved are internal **DRAFT**, never invented. Do not send, email, publish or seek signatures without explicit user approval.
4. Extract the exact supplied logo; never recreate, recolour, distort, arbitrarily crop or substitute a text logo. If the original exact logo file is unavailable, either stop or mark the provenance gap for human review and use only a demonstrated identical extracted image.

## Required source record
- Client and intended reader, proposal version/date, prepared-by individual and entity.
- Current version(s) of source documents and authoritative approval state.
- Problems, Phase 1 scope, measurable acceptance checks, explicit exclusions, later phases and approval gates.
- Prices, billing triggers, provider cost basis, currency, applicable tax treatment, recurring service boundaries; unknown fields become reviewer gaps, **not fictional answers**.
- Logo provenance, permitted accent and font status. DejaVu Sans in this package is a technical rendering font, **not an approved NeuralSync brand font**.
- Exact approved page contract: section order, what can appear on each page, maximum length, approved disclaimers, named approval boundary.

## Golden path
1. **SOURCE REVIEW** — Compare new proposal source with prior output; detect name mismatches, superseded terms, commercial inconsistencies. Store discrepancies in the QA handoff. Do not silently correct.
2. **CONTENT CONTRACT** — Copy `templates/chrome_auto.json` as a new, client-isolated file; replace every client-specific statement with verified inputs. Keep `pages` as ordered blocks: `cover`, `heading`, `p`, `bullets`, `intro`, `label_p`, `table`, `numbered`, `decision`, `signatures`. One price table only where authorized. Edit no hard-coded client values in the renderer.
3. **LAYOUT** — Build using ReportLab Platypus `Paragraph`, `Table`, `Spacer`, and `PageBreak`. Its measured wrapped cells define actual row heights. Use a separate 75-point bottom story margin plus a fixed footer strip, consistent column widths, and top-aligned cells. Never estimate row height by character count or draw paragraphs at a fixed y without measuring them.
4. **RENDER** — `python scripts/build_pdf.py templates/chrome_auto.json --output proposal-DRAFT.pdf`. Tool fails on invalid/missing image or unsupported blocks.
5. **GEOMETRY/CONTENT QA** — `python scripts/qa_pdf.py proposal-DRAFT.pdf --contents templates/chrome_auto.json --renders qa/rendered --report qa/qa-report.json`. A nonzero exit code blocks release.
6. **VISUAL QA** — Open `qa/rendered/page-1.png`, `page-2.png`, `page-3.png` individually at normal reading zoom. Check glyphs, text stretching, footer distance, table row fills, signatures, optical balance and legibility. Record a real human or agent visual verdict. A script PASS alone is not release approval.
7. **GRILL / REVIEW** — Confirm with reviewer: names, numbers, currency, deliverables/acceptance, retainer, logo, page count, missing information, and all scope gates. Never label source content VERIFIED simply because the PDF rendered.
8. **HANDOFF** — Provide one draft PDF, the input JSON, the QA report and identified unresolved facts. Approved client send is an explicit separate action.

## Layout engine invariants
- US Letter 612 × 792 pt. Content width 524 pt with 44-pt side margins.
- Text flow is handled by ReportLab Platypus: no manual `cpl = width / constant` or fixed row height guesses.
- All table cells are `Paragraph` flowables with explicit padding, `VALIGN=TOP`, wrapped text, automatic row height and a single table style. Repeating header on page breaks.
- Footer is drawn at the bottom of every page outside the content frame. For the Chrome Auto profile: exact footer string from the input and a visible `DRAFT FOR REVIEW` on every page.
- Brand purple `#6025e1` only because the Chrome Auto instructions explicitly supplied that colour. Other typography and table shades use neutrals, not an invented brand palette.
- Do not justify paragraph text; the default is left alignment. Logo dimensions are fitted preserving exact aspect ratio.
- Keep heading with at least its following content by reviewable page planning. If any block flows onto a fourth page for a three-page profile, the build fails QA. Shortening text takes precedence over reducing text below readable sizes.
- Preserve labels and column definitions: Chrome Auto price table is exactly `You pay | When | What you get in return`.
- Give signature lines separate side-by-side columns and independent date fields.
- PDF uses a real embedded Unicode font so bullets/dashes/name spelling render normally. Do not install or advertise a brand font from these files.

## Non-negotiable QA gates
See `QA-CHECKLIST.md`. Stop delivery on: page count outside contract; body encroaching footer lane; missing draft mark; price leaked outside approved pricing page; missing or incorrect commercial trigger; recalculation failure; source/version confusion; unverified logo swap; visibly overlapped text; clipped glyphs; broken signature labels.

## Chrome Auto profile — fixed client-specific gates
- Reader Chris, prepared by NeuralSync Canada and **Sohaib Sajid**; source v1 uses `Shoaib`, note the discrepancy and obtain confirmation.
- 3 pages target; first page offer/risk/90-day proof, second page Phase 1 scope/exclusions/roadmap/trust, third page pricing/next step/signatures. Price only on page 3. Later phases have no amounts.
- Phone demonstration and approved fallback plan BEFORE paid build. Current revenue systems stay active absent written transition. Retainer starts after Phase 1 acceptance.
- Dealership cost accounting and lender/funding records **NOT** promised in Phase 1. Later phases are gated separately.
- Supplied high-resolution logo image recovered from v5 PDF is in `assets/`. Exact original `ns-logo-color__1.pdf` was not separately provided; the brand-asset source is therefore a pre-send review item.
- $1,500 + $1,750 + $1,750 = $5,000. Provider planning usage is **not** included in that total. Retainer and provider usage are separate; pricing currency is not specified by the source.
- One draft client proposal output only. Do NOT silently produce or send a one-page decision sheet when the instruction requests one PDF.

## Change-control and regression tests
- Every new client starts from an isolated JSON input; never reuse another client's price or approvals.
- Preserve the previous PDF for comparison. Rerender and inspect the **full** PDF after any table-text revision.
- Run a stress test with a long table cell and verify a page-count failure rather than visual clipping.
- Keep source version, renderer code version, logo provenance, and QA JSON with the draft artifact.
- Propose (do not silently write) an update to the NeuralSync skill/ClickUp task once an authorized reviewer approves this skill.

## Exact command
```bash
python scripts/build_pdf.py templates/chrome_auto.json --output Chrome-Auto-Condensed-Proposal-DRAFT-v6-2026-10-28.pdf
python scripts/qa_pdf.py Chrome-Auto-Condensed-Proposal-DRAFT-v6-2026-10-28.pdf --contents templates/chrome_auto.json --renders qa/rendered --report qa/qa-report.json
```

## Failure policy
If verification fails: produce `FAIL` with the exact page, defect, probable cause and changed code or content. Do not say "client-ready". If the source is incomplete: produce a clearly draft-marked file with an explicit uncertainty list, or stop if the missing element is required to render without violating the brief.
