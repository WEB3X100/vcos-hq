#!/usr/bin/env python3
"""Automated geometry and source-content checks for proposal PDFs.

Usage: qa_pdf.py document.pdf --contents templates/client.json --renders qa/rendered
A nonzero exit status blocks release. Visual human/agent review remains required.
"""
import argparse, json, re, sys
from pathlib import Path
import fitz
from PIL import Image


def spans(page):
    result=[]
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines',[]):
            for span in line.get('spans',[]):
                txt=span.get('text','').strip()
                if txt:result.append((fitz.Rect(span['bbox']),txt))
    return result

def check(path,contents=None,render_dir=None):
    errors=[]; doc=fitz.open(path)
    config=json.loads(Path(contents).read_text(encoding='utf8')) if contents else None
    d=config['document'] if config else {}
    expected=len(config['pages']) if config else None
    max_pages=int(d.get('max_pages',3))
    pricing_page=int(d.get('pricing_page',expected or len(doc)))
    footer=d.get('footer','DRAFT FOR REVIEW')
    status=d.get('status','DRAFT FOR REVIEW')
    output={'file':str(path),'checks':{},'pages':[]}
    if expected and len(doc)!=expected:errors.append(f'Expected {expected} pages, got {len(doc)}. The content overflowed its declared frame.')
    if len(doc)>max_pages:errors.append(f'Page-count limit {max_pages} exceeded: {len(doc)}.')
    if pricing_page<1 or pricing_page>len(doc):errors.append('Pricing page is not present.')
    for i,p in enumerate(doc):
        no=i+1; text=p.get_text(sort=True); ss=spans(p)
        output['pages'].append({'page':no,'text_spans':len(ss),'image_count':len(p.get_images())})
        if tuple(map(round,(p.rect.width,p.rect.height)))!=(612,792): errors.append(f'Page {no}: expected Letter 612 × 792 pt.')
        if status not in text:errors.append(f'Page {no}: missing draft status.')
        if footer not in text:errors.append(f'Page {no}: missing/truncated footer.')
        if config and i<len(config['pages']):
            for b in config['pages'][i]:
                if b['type']=='heading' and re.sub(r'\s+',' ',b['text']) not in re.sub(r'\s+',' ',text):
                    errors.append(f'Page {no}: section heading missing or on wrong page: {b["text"]!r}.')
            if i==0 and d['title'] not in text:
                errors.append(f'Page {no}: proposal title missing.')
        for r,t in ss:
            if r.x0<38 or r.x1>574:errors.append(f'Page {no}: text beyond horizontal safe zone: {t[:25]!r}.')
            if r.y0<9 or r.y1>775:errors.append(f'Page {no}: text beyond vertical safe zone: {t[:25]!r}.')
            if 721<r.y0<738:errors.append(f'Page {no}: text encroaches on footer gap: {t[:25]!r}.')
        for k,(r1,t1) in enumerate(ss):
            for r2,t2 in ss[k+1:]:
                inter=r1 & r2
                if not inter.is_empty and inter.width>2 and inter.height>1.2:
                    errors.append(f'Page {no}: text overlap {t1[:22]!r} / {t2[:22]!r}.')
                    break
        if no!=pricing_page and re.search(r'\$\s*\d',text):
            errors.append(f'Page {no}: monetary amount leaked outside authorized pricing page {pricing_page}.')
        if '�' in text or '■' in text:errors.append(f'Page {no}: broken font replacement glyph.')
        if no==1 and d.get('logo_file') and not p.get_images():errors.append('Page 1: missing logo.')
    if config:
        prices=[(i+1,b) for i,page in enumerate(config['pages']) for b in page if b['type']=='table' and b['headers'][0]=='You pay']
        if len(prices)!=1:errors.append('Exactly one table beginning with You pay required for this content profile.')
        elif prices[0][0]!=pricing_page:errors.append('Pricing table declared on the wrong page.')
        check=d.get('payment_check')
        if check and len(prices)==1:
            rows=prices[0][1]['rows']
            def amount(row_idx):
                raw=rows[row_idx][0]
                match=re.search(r'\$\s*([0-9][0-9,]*(?:\.[0-9]{2})?)',raw)
                if not match:raise ValueError(f'No dollar amount in payment row {row_idx}: {raw}')
                return round(float(match.group(1).replace(',','')),2)
            try:
                component_total=sum(amount(i) for i in check['component_rows'])
                printed_total=amount(check['total_row'])
                if component_total!=printed_total:errors.append(f'Phase 1 milestone arithmetic mismatch: {component_total} vs {printed_total}.')
            except (IndexError,ValueError,TypeError,KeyError) as exc:
                errors.append(f'Commercial arithmetic configuration invalid: {exc}')
    if render_dir:
        rd=Path(render_dir);rd.mkdir(parents=True,exist_ok=True); images=[]
        for i,p in enumerate(doc):
            pix=p.get_pixmap(matrix=fitz.Matrix(1.75,1.75),alpha=False)
            fn=rd/f'page-{i+1}.png';pix.save(fn)
            im=Image.open(fn).convert('RGB');im.thumbnail((510,660));images.append(im)
        montage=Image.new('RGB',(sum(im.width for im in images)+40*(len(images)+1),max(im.height for im in images)+80),'#e8e8e8')
        x=40
        for im in images:montage.paste(im,(x,40));x+=im.width+40
        montage.save(rd/'all-pages-contact-sheet.png')
    output['checks']={'letter_pages':not any('Letter' in v for v in errors),'page_count':len(doc)==expected if expected else len(doc)<=max_pages,'footer_and_draft':not any('footer' in v or 'draft' in v for v in errors),'pricing_segregation':not any('pricing' in v or 'monetary amount' in v for v in errors),'geometry':not any('safe zone' in v or 'footer gap' in v or 'overlap' in v for v in errors),'commercial_arithmetic':not any('arithmetic' in v for v in errors)}
    output['status']='PASS' if not errors else 'FAIL';output['failures']=errors
    return output

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('pdf');ap.add_argument('--contents');ap.add_argument('--renders');ap.add_argument('--report');a=ap.parse_args()
    result=check(a.pdf,a.contents,a.renders)
    output=json.dumps(result,ensure_ascii=False,indent=2)
    print(output)
    if a.report:Path(a.report).write_text(output+'\n',encoding='utf8')
    sys.exit(0 if result['status']=='PASS' else 1)
