# NeuralSync — reusable proposal PDF generation / QA package

This package includes a **reusable ReportLab Platypus renderer**, a JSON input for the Chrome Auto draft, the unmodified raster logo recovered from the provided v5 PDF, geometric/content QA, a proposal-generation skill, and documented review blockers.

## Local setup

Python 3.10+ with `reportlab`, `PyMuPDF` (`fitz`), and `Pillow`:

```bash
python -m pip install -r requirements.txt
python scripts/build_pdf.py templates/chrome_auto.json --output Chrome-Auto-DRAFT.pdf
python scripts/qa_pdf.py Chrome-Auto-DRAFT.pdf --contents templates/chrome_auto.json --renders qa/rendered --report qa/qa-report.json
```

`DejaVuSans.ttf` and `DejaVuSans-Bold.ttf` must be available as rendering fonts; the current package uses typical Linux font paths. This is a render-font dependency, not a brand-font requirement.

## Portability

- Keep `assets/` and `templates/` relative to the root of this folder.
- Copy `templates/chrome_auto.json` to a new client-specific JSON and replace **all client-specific facts** before a different proposal is generated.
- A client-specific PDF output should never be used as a source of truth for another client's price or approvals.
- For workstations without DejaVu at `/usr/share/fonts/truetype/dejavu/`, adjust font paths in `scripts/build_pdf.py` or supply equivalent licensed rendering fonts. Do not distribute the font files.
- The exact original logo PDF (`ns-logo-color__1.pdf`) is not contained in the uploaded inputs; the included extracted image is only a source-preserving fallback until the original is verified.

## Visual review

Open `qa/rendered/page-1.png`, `page-2.png` and `page-3.png`, check all tables and signatures, and record human approval. Automated QA passing does not constitute permission to send to Chris.
