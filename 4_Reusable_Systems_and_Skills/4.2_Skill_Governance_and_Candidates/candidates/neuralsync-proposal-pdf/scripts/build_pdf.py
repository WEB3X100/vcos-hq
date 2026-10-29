#!/usr/bin/env python3
"""PDF proposal renderer using ReportLab Platypus measured flowables.

Usage: python scripts/build_pdf.py templates/chrome_auto.json --output proposal.pdf
Designed to fail rather than clip when a page or row cannot fit.
"""
import argparse, json, os, sys
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, PageBreak, KeepTogether, Flowable, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

PURPLE = HexColor('#6025e1')  # explicitly supplied by request
INK = HexColor('#1c2330')   # neutral typography, not brand colour
MUTED = HexColor('#586171')
HAIR = HexColor('#d5d7dc')
PALE = HexColor('#f7f7f9')  # neutral table stripe, not additional brand palette
WHITE = HexColor('#ffffff')
MARGIN_X = 44
PAGE_W, PAGE_H = letter
CONTENT_W = PAGE_W - 2*MARGIN_X

class SignatureGrid(Flowable):
    def __init__(self, left, right, height=52):
        super().__init__(); self.left=left; self.right=right; self.height=height; self.width=CONTENT_W
    def wrap(self, aw, ah): return (min(self.width, aw), self.height)
    def draw(self):
        c=self.canv; colw=(self.width-28)/2
        for x,t in ((0,self.left),(colw+28,self.right)):
            c.setStrokeColor(INK); c.setLineWidth(.75); c.line(x,31,x+colw,31)
            c.setFillColor(INK); c.setFont('DejaVu',8)
            c.drawString(x,18,t)
            c.setFillColor(MUTED); c.setFont('DejaVu',7.7)
            c.drawString(x,5,'Date: __________________')

class ProposalDoc:
    def __init__(self,data, root, output):
        self.data=data; self.root=root; self.output=output
        self.d=data['document']; self.styles=self.make_styles()
        self.logo=(root/self.d['logo_file']).resolve()
        if not self.logo.is_file(): raise FileNotFoundError(f'Logo not found: {self.logo}')
        self.expected_pages=len(self.data['pages'])
        self.max_pages=int(self.d.get('max_pages',3))
        if self.expected_pages>self.max_pages: raise ValueError(f'Proposal exceeds the {self.max_pages}-page configured limit')
    @staticmethod
    def make_styles():
        b=dict(fontName='DejaVu',textColor=INK,allowWidows=0,allowOrphans=0)
        def style(name, **kw):
            return ParagraphStyle(name, **(b | kw))
        return {
          'title': style('title',fontName='DejaVu-Bold',fontSize=20.5,leading=26,spaceAfter=4),
          'subtitle':style('subtitle',fontSize=10.7,leading=16,textColor=MUTED,spaceAfter=13),
          'meta':style('meta',fontSize=8.5,leading=12.5,spaceAfter=2),
          'footnote':style('footnote',fontSize=7,leading=10.4,textColor=MUTED,spaceAfter=8),
          'h':style('heading',fontName='DejaVu-Bold',fontSize=10.6,leading=15,textColor=PURPLE,spaceBefore=11,spaceAfter=9,borderColor=PURPLE,borderWidth=0,borderPadding=0),
          'body':style('body',fontSize=9.25,leading=14.2,spaceAfter=8),
          'bullet':style('bullet',fontSize=9.12,leading=13.5,leftIndent=15,firstLineIndent=-11,spaceAfter=5),
          'intro':style('intro',fontSize=8.8,leading=13.3,spaceAfter=7,textColor=MUTED),
          'table':style('table',fontSize=8.24,leading=12.4,spaceAfter=0,wordWrap='LTR'),
          'tableBold':style('tableBold',fontName='DejaVu-Bold',fontSize=8.15,leading=12.2,spaceAfter=0),
          'th':style('tableHeader',fontName='DejaVu-Bold',fontSize=8.0,leading=11,textColor=WHITE),
          'label':style('label',fontSize=8.45,leading=13.0,spaceAfter=5),
          'small':style('small',fontSize=8.1,leading=12.1,spaceAfter=6),
          'number':style('num',fontSize=8.75,leading=13.5,leftIndent=17,firstLineIndent=-14,spaceAfter=5),
        }
    def para(self, text,style='body'):
        # All text from client-specific JSON is escaped, avoiding markup injection.
        return Paragraph(escape(str(text)),self.styles[style])
    def line(self): return HRFlowable(width='100%',thickness=1,color=PURPLE,spaceBefore=0,spaceAfter=6)
    def table(self,block):
        widths=block['widths']; assert abs(sum(widths)-CONTENT_W)<.001, (sum(widths),CONTENT_W)
        cols=len(widths)
        rows=[]
        for head in [block['headers']]:
            assert len(head)==cols
            rows.append([self.para(t,'th') for t in head])
        for i,row in enumerate(block['rows']):
            assert len(row)==cols
            rows.append([self.para(t,'tableBold' if (j==0 and block['headers'][0] in ('You pay','Month','When')) else 'table') for j,t in enumerate(row)])
        t=Table(rows,colWidths=widths,repeatRows=1,hAlign='LEFT',splitByRow=1)
        styles=[
            ('BACKGROUND',(0,0),(-1,0),PURPLE),
            ('VALIGN',(0,0),(-1,-1),'TOP'),
            ('LEFTPADDING',(0,0),(-1,-1),9),
            ('RIGHTPADDING',(0,0),(-1,-1),9),
            ('TOPPADDING',(0,0),(-1,0),7),
            ('BOTTOMPADDING',(0,0),(-1,0),7),
            ('TOPPADDING',(0,1),(-1,-1),8),
            ('BOTTOMPADDING',(0,1),(-1,-1),8),
            ('LINEBELOW',(0,0),(-1,0),.4,PURPLE),
            ('LINEBELOW',(0,1),(-1,-1),.25,HAIR),
        ]
        for i in range(2,len(rows),2): styles.append(('BACKGROUND',(0,i),(-1,i),PALE))
        t.setStyle(TableStyle(styles))
        return t
    def build_block(self,block):
        kind=block['type']; out=[]
        if kind=='cover':
            out += [Spacer(1,46),self.para(self.d['title'],'title'), self.para(self.d['subtitle'],'subtitle'),
                    self.para(f"Prepared for: {self.d['prepared_for']}  |  Prepared by: {self.d['author']}",'meta')]
            if self.d.get('spelling_footnote'):
                out.append(self.para(self.d['spelling_footnote'],'footnote'))
        elif kind=='heading': out=[self.para(block['text'],'h'),self.line()]
        elif kind=='p': out=[self.para(block['text'],'body')]
        elif kind=='intro': out=[self.para(block['text'],'intro')]
        elif kind=='bullets': out=[self.para('•  '+s,'bullet') for s in block['items']]
        elif kind=='numbered': out=[self.para(f'{i}.  {s}','number') for i,s in enumerate(block['items'],1)]
        elif kind=='label_p': out=[Paragraph(f"<font color='#6025e1'><b>{escape(block['label'])}.</b></font>  {escape(block['text'])}",self.styles['label'])]
        elif kind=='decision': out=[self.para(block['text'],'small'),Spacer(1,12)]
        elif kind=='signatures': out=[SignatureGrid(block['left'],block['right'])]
        elif kind=='table': out=[self.table(block),Spacer(1,6)]
        else: raise ValueError(f'Unsupported block type: {kind}')
        return out
    def draw_page(self,c,doc):
        c.saveState()
        page=doc.page
        if page==1:
            # Original image bytes are placed unmodified, preserving aspect ratio.
            im=ImageReader(str(self.logo))
            iw, ih=im.getSize(); width=150.4; height=width*ih/iw
            c.drawImage(im,MARGIN_X,784-height,width=width,height=height,mask='auto')
            c.setFont('DejaVu-Bold',8.1);c.setFillColor(PURPLE)
            c.drawRightString(PAGE_W-MARGIN_X,762,'PROPOSAL  ·  '+self.d['status'])
            c.setFont('DejaVu',7.5);c.setFillColor(MUTED)
            c.drawRightString(PAGE_W-MARGIN_X,746,f"{self.d['client']}  |  {self.d['date']}  |  Draft v{self.d['version']}")
        else:
            c.setFont('DejaVu-Bold',8.3);c.setFillColor(PURPLE)
            c.drawString(MARGIN_X,762,f"NEURALSYNC  /  {self.d['client'].upper()}")
            c.setFont('DejaVu',7.5);c.setFillColor(MUTED)
            c.drawRightString(PAGE_W-MARGIN_X,762,self.d['status'])
            c.setStrokeColor(HAIR);c.setLineWidth(.5);c.line(MARGIN_X,751,PAGE_W-MARGIN_X,751)
        # Separate fixed footer lane, never part of the flow content frame.
        c.setStrokeColor(HAIR);c.setLineWidth(.5);c.line(MARGIN_X,55,PAGE_W-MARGIN_X,55)
        c.setFont('DejaVu',6.9); c.setFillColor(MUTED)
        c.drawCentredString(PAGE_W/2,41,self.d['footer'])
        c.setFont('DejaVu',6.9); c.drawRightString(PAGE_W-MARGIN_X,28,f'{page} / {self.expected_pages}')
        c.restoreState()
    def run(self):
        doc=SimpleDocTemplate(str(self.output),pagesize=letter,
                              leftMargin=MARGIN_X,rightMargin=MARGIN_X,
                              topMargin=68,bottomMargin=75,
                              title=self.d['title']+' (Draft)',author=self.d['author'])
        story=[]
        for i,page_blocks in enumerate(self.data['pages']):
            if i:story.append(PageBreak())
            for blk in page_blocks:
                story.extend(self.build_block(blk))
        doc.build(story,onFirstPage=self.draw_page,onLaterPages=self.draw_page)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('json',type=Path);ap.add_argument('--output',required=True,type=Path)
    args=ap.parse_args();data=json.loads(args.json.read_text(encoding='utf8'))
    font_dir=Path(os.environ.get('DEJAVU_FONT_DIR','/usr/share/fonts/truetype/dejavu'))
    regular=font_dir/'DejaVuSans.ttf'; bold=font_dir/'DejaVuSans-Bold.ttf'
    if not regular.is_file() or not bold.is_file():
        raise FileNotFoundError(f'Rendering fonts not found at {font_dir}; set DEJAVU_FONT_DIR to a directory with locally installed DejaVu Sans fonts. Do not distribute font files.')
    pdfmetrics.registerFont(TTFont('DejaVu',str(regular)))
    pdfmetrics.registerFont(TTFont('DejaVu-Bold',str(bold)))
    pdfmetrics.registerFontFamily('DejaVu',normal='DejaVu',bold='DejaVu-Bold')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    ProposalDoc(data,args.json.parent.parent,args.output).run()
    print(args.output)
if __name__=='__main__':main()
