"""Run with: python -m unittest discover -s tests"""
import unittest,subprocess,sys,os,tempfile,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BUILD=ROOT/'scripts/build_pdf.py'
QA=ROOT/'scripts/qa_pdf.py'
SOURCE=ROOT/'templates/chrome_auto.json'
class ProposalRendererTests(unittest.TestCase):
    def test_reference_proposal_renders_and_passes(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/'good.pdf'
            subprocess.run([sys.executable,str(BUILD),str(SOURCE),'--output',str(p)],check=True,capture_output=True)
            subprocess.run([sys.executable,str(QA),str(p),'--contents',str(SOURCE)],check=True,capture_output=True)
    def test_oversize_content_must_fail_page_contract(self):
        with tempfile.TemporaryDirectory() as t:
            src=json.loads(SOURCE.read_text(encoding='utf8'))
            src['pages'][2][1]['rows'][5][2] += (' A long unsanctioned sentence that would normally flow across rows.'*120)
            (Path(t)/'templates').mkdir()
            sample=Path(t)/'templates/long.json';sample.write_text(json.dumps(src),encoding='utf8')
            # Copy asset into same relative package layout as source since tests intentionally move JSON.
            (Path(t)/'assets').mkdir();
            import shutil
            shutil.copy(ROOT/'assets/neuralsync-logo-recovered-from-v5.png',Path(t)/'assets/neuralsync-logo-recovered-from-v5.png')
            # Renderer may reject oversized table outright, or generate >3 pages.
            pdf=Path(t)/'oversized.pdf'
            proc=subprocess.run([sys.executable,str(BUILD),str(sample),'--output',str(pdf)],capture_output=True)
            if proc.returncode==0:
                gate=subprocess.run([sys.executable,str(QA),str(pdf),'--contents',str(sample)],capture_output=True)
                self.assertNotEqual(gate.returncode,0, 'A long table cell should be a QA failure, not silently accepted')
    def test_wrong_pricing_total_fails(self):
        with tempfile.TemporaryDirectory() as t:
            sample=json.loads(SOURCE.read_text(encoding='utf8'))
            sample['pages'][2][1]['rows'][4][0]='$4,999  Phase 1 total'
            (Path(t)/'templates').mkdir()
            altered=Path(t)/'templates/modified.json';altered.write_text(json.dumps(sample),encoding='utf8')
            (Path(t)/'assets').mkdir()
            import shutil
            shutil.copy(ROOT/'assets/neuralsync-logo-recovered-from-v5.png',Path(t)/'assets/neuralsync-logo-recovered-from-v5.png')
            pdf=Path(t)/'modified.pdf'
            subprocess.run([sys.executable,str(BUILD),str(altered),'--output',str(pdf)],check=True,capture_output=True)
            gate=subprocess.run([sys.executable,str(QA),str(pdf),'--contents',str(altered)],capture_output=True)
            self.assertNotEqual(gate.returncode,0,'Incorrect milestone arithmetic must block QA')
    def test_commercial_math(self):
        inp=json.loads(SOURCE.read_text(encoding='utf8'))
        lines=inp['pages'][2][1]['rows']
        self.assertEqual(1500+1750+1750,5000)
        self.assertIn('$5,000',lines[4][0])
if __name__=='__main__':unittest.main()
