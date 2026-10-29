# Muse upgrade notes — why the v5 attempts failed

**Evidence reviewed**
- `Chrome Auto Next Decade Proposals.docx` (28 October 2026 original source)
- `Chrome-Auto-Condensed-Proposal-DRAFT-v5-2026-10-28.pdf` (3 pages, fpdf2 output)
- Uploaded `SKILL (9).md` (NeuralSync PDF/proposal skill in progress)
- The user-supplied v5 snippet using `cpl = max(10, int(w/1.9))` as a proxy for wrapped line count.

**Observed v5 defects**
- Page 1, Month 2 row: alternating row-fill background covers only the first line while wrapped second-line text protrudes below it. This is a computed-row-height error, not a font error.
- Page 3 commercial table: rows have inconsistent heights and narrow columns; the lowest recurring-fee row contains much more text than the shortcut can measure.
- Page 3 signature line labels run together, even though lines are physically separate. These need independent grid cells.
- Footer is fixed to a page edge while body table grows unpredictably. With longer text, footer collision is likely without a reserved flow region.
- A prior default cell alignment justified body text; adding `align='L'` changes justification but does NOT fix line count, row height or pagination.

**Fix implemented**
- Replaced the custom fpdf2 hand-rolled table/pagination with ReportLab Platypus `Paragraph` and `Table` flowables; line wrapping is measured by the real font metrics, and row height is set to the largest actual cell.
- Document `pages` + body frame plus fixed footer lane; no body writing in footer strip.
- Explicit column widths, padding, top-aligned cells, neutral alternating background covering full row.
- Two-column signature flowable; explicit review date placeholders.
- Separate JSON content contract, rendering script and PDF-text geometry/content QA script.
- Every page rendered as PNG; user can review the contact sheet + individual pages.

**Conflict detected in old skill**
- Old `SKILL (9).md` requires page-1 pricing and typically a 2-page decision document; the **current explicit Chrome Auto brief** instead requires pricing *only at the end* and accepts 3 pages. Specific approved client requirements supersede the generic outline.
- Old skill asks for a second decision sheet by default. This request asks for **one** proposal PDF. Do not add a companion page/sheet unless separately asked.
- Existing skill primarily controls content truth and human review. It does not provide a tested renderer or geometry gate; this new skill provides both and can be incorporated without discarding the content gates.

**Safeguards**
- All logos remain client-supplied assets. The high-resolution PNG is unmodified extraction from v5 PDF, not represented as the original `ns-logo-color__1.pdf` file.
- `#6025e1` is user-supplied for the Chrome Auto use case; black, gray and neutral table striping are not labeled brand colours. DejaVu is a technical rendering font.
- Human commercial approval required before any client communication. No Google Drive, ClickUp, repo or client-side system was modified by this local package.

**Suggested integration path**
1. Copy this folder to `~/workspace/neuralsync-skills/pdf-proposal-generation/` after review, retaining the existing original skill as a backup.
2. Merge the new `SKILL.md` rendering/QA sections into Muse's existing proposal skill, preserving the existing source, commercial and human approval gates.
3. Replace the old build script's table implementation; do not patch its character-count approximation.
4. Run the included Chrome Auto gold-standard regression. Keep generated QA artifacts in the client's review folder.
5. After approval, record `Skill verified; renderer rebuilt; QA pass` against the related ClickUp task with the actual evidence link. Do not mark a tracker done based on the package alone.
