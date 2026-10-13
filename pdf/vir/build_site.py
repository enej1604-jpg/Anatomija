"""Build the interactive study page: notes with every labelled diagram placed in its section."""
import json, re, os, html
import xml.etree.ElementTree as ET
from PIL import Image, ImageChops
import numpy as np

import build as B  # reuses ANN (with fix.py applied), BOX, CAT, wrap, spread, inline, render_list, render_table, TABS, R, S

S = B.S
OUT = os.path.join(S, 'site')
os.makedirs(os.path.join(OUT, 'img'), exist_ok=True)
esc = B.esc

# section (substring of h2/h3 heading) -> panels, in reading order
PLACE = {
 '1': [('Orientacijske ravnine', ['1-1-1', '1-1-2']), ('Drugi orientacijski izrazi', ['1-1-3']),
       ('Anatomska poimenovanja gibov', ['1-2-1', '1-2-2', '1-2-3', '1-2-4']), ('predeli telesa', ['1-2-5']),
       ('=Celica', ['1-3-1']), ('Citoplazmatski organeli', ['1-3-3', '1-3-4']), ('Celična membrana', ['1-3-5']),
       ('Prehajanje snovi', ['1-3-6']), ('Skica celice', ['1-3-2']),
       ('Strukture na površini', ['1-4-1', '1-4-2', '1-4-3']), ('Razdelitev krovnih', ['1-4-4', '1-4-5', '1-4-6', '1-4-7']),
       ('Žlezni', ['1-4-9', '1-4-10']), ('Vrste vezivnih celic', ['1-5-1', '1-5-2', '1-5-3', '1-5-4', '1-5-5', '1-5-6']),
       ('Vezivna vlakna', ['1-5-7', '1-5-8']), ('Vrste vezivnega tkiva pri odraslih', ['1-5-9']),
       ('Zgradba kože', ['1-6-1', '1-6-2', '1-6-6']), ('Epidermis', ['1-6-3', '1-6-4', '1-6-5'])],
 '2': [('Lobanja', ['2-1-1']), ('Os occipitale', ['2-1-2']), ('Obrazne kosti', ['2-1-3', '2-1-4']),
       ('Hrbtenica – columna', ['2-2-1']), ('Posebnosti vretenc', ['2-2-2', '2-2-3']), ('Prsni koš', ['2-2-4', '2-2-5']),
       ('Medenica – pelvis', ['2-3-6', '2-3-7']), ('Scapula', ['2-3-1', '2-3-2']), ('Ulna', ['2-3-3']),
       ('Manus', ['2-3-4', '2-3-5']), ('Femur', ['2-3-8']), ('Fibula', ['2-3-9']), ('Ossa tarsi', ['2-3-10'])],
 '3': [('Vrste hrustančevine', ['3-1-2', '3-1-5', '3-1-6']), ('Hialina hrustančevina', ['3-1-1', '3-1-3', '3-1-4']),
       ('Diartroze', ['3-2-1', '3-2-2']), ('Sinartroze', ['3-2-4', '3-2-5']), ('Medvretenčni stiki', ['3-2-3']),
       ('Tipi sklepov po gibljivosti', ['3-3-4', '3-2-6', '3-3-1', '3-3-2', '3-3-3']),
       ('Sklepi glave', ['3-4-1']), ('Sklepi trupa', ['3-4-2', '3-4-3', '3-4-4', '3-4-5']), ('Sklepi prsnega koša', ['3-4-6']),
       ('Sklepi ramenskega obroča', ['3-5-1', '3-5-2']), ('Sklepi zgornjega uda', ['3-5-3', '3-5-4', '3-5-5', '3-5-6', '3-5-7']),
       ('Sklepi medeničnega obroča', ['3-6-1', '3-6-2']), ('Articulatio coxae', ['3-6-3']), ('Articulatio genus', ['3-6-4', '3-6-5']),
       ('Articulatio tibiofibularis', ['3-6-6']), ('Articulatio talocruralis', ['3-6-7']), ('Spodnji skočni', ['3-6-8']),
       ('Zgradba mišice', ['3-7-1', '3-7-11']), ('Deli mišice', ['3-7-2', '3-7-13']), ('Pomožni aparat', ['3-7-3']),
       ('Skeletna (prečnoprogasta)', ['3-7-4', '3-7-5']), ('Mehanizem krčenja', ['3-7-7', '3-7-6']),
       ('Oživčenje skeletnih', ['3-7-8']), ('Srčna mišičnina', ['3-7-9']), ('Gladka mišičnina', ['3-7-10']),
       ('medsebojni odnos', ['3-7-12']), ('Mišice glave – dve', ['3-8-1', '3-8-2']),
       ('Žvekalne mišice', ['3-8-3', '3-8-4', '3-8-5', '3-8-6']), ('Mimične mišice', ['3-8-7', '3-8-11', '3-8-8']),
       ('Vratne mišice', ['3-8-9', '3-8-10'])],
 '4': [('Razdelitev vratnih mišic', ['4-1-1', '4-1-2']), ('Suprahioidne', ['4-1-3']), ('Infrahioidne', ['4-1-4', '4-1-5']),
       ('Prevertebralne', ['4-1-6']), ('Stranska skupina', ['4-1-7', '4-1-8', '4-1-9', '4-1-10']),
       ('Ligamentum nuchae', ['4-2-1']), ('Povrhnje hrbtne', ['4-2-5']),
       ('M. trapezius', ['4-2-2', '4-2-3', '4-2-4', '4-2-6', '4-2-7', '4-2-8', '4-2-9']),
       ('Globoke (avtohtone', ['4-3-1', '4-3-2', '4-3-3', '4-3-4', '4-3-5', '4-3-6', '4-3-7', '4-3-8']),
       ('4.3 Trebušne mišice', ['4-4-1', '4-4-2', '4-4-3', '4-4-4', '4-4-5', '4-4-6']),
       ('Pektoralni mišici', ['4-5-1', '4-5-2', '4-5-3', '4-5-4', '4-5-5']),
       ('Prsnemu košu lastne', ['4-5-6', '4-5-7', '4-5-8']), ('Diaphragma', ['4-5-9', '4-5-10']), ('Dihalne mišice', ['4-5-11']),
       ('Ramenske mišice', ['4-6-1', '4-6-2', '4-6-3']), ('Rotatorna manšeta', ['4-6-9', '4-6-5', '4-6-6', '4-6-4', '4-6-7', '4-6-8']),
       ('M. biceps brachii', ['4-6-10']), ('Ostale mišice nadlakti', ['4-6-11', '4-6-12', '4-6-13'])],
}

def panel_file(pid, crop):
    plate, k = pid.rsplit('-', 1)
    im = Image.open(f'{S}/panels/{plate}-{k}.png').convert('RGB')
    full = im.size; c0 = (0, 0)
    if crop:
        c0 = (int(crop[0]/100*im.width), int(crop[1]/100*im.height))
        im = im.crop((c0[0], c0[1], int(crop[2]/100*im.width), int(crop[3]/100*im.height)))
    diff = ImageChops.difference(im, Image.new('RGB', im.size, (255, 255, 255))).convert('L').point(lambda p: 255 if p > 18 else 0)
    bb = diff.getbbox(); off = c0
    if bb:
        pad = 6
        bb = (max(0, bb[0]-pad), max(0, bb[1]-pad), min(im.width, bb[2]+pad), min(im.height, bb[3]+pad))
        off = (bb[0]+c0[0], bb[1]+c0[1]); im = im.crop(bb)
    w, h = im.size
    if w < 900:
        s = 900 / w; im = im.resize((900, int(h*s)), Image.LANCZOS)
    name = f'img/{pid}.jpg'
    im.save(os.path.join(OUT, name), 'JPEG', quality=84, optimize=True, progressive=True)
    return name, (w, h), off, full

def figure(pid, num, acc):
    plate, k = pid.rsplit('-', 1); k = int(k)
    a = B.ANN[plate]['p'][k-1]
    name, (w, h), off, full = panel_file(pid, a.get('crop'))
    labels = a.get('a', [])
    W = 1000
    iw = min(520, 620*w/h) if labels else min(760, 640*w/h)
    ih = iw*h/w; ix = (W-iw)/2; top = 8; LH = 17.5
    L, Rr = [], []
    for i, (x, y, t, c) in enumerate(labels):
        px = min(max((x/100*full[0]-off[0])/w, 0), 1); py = min(max((y/100*full[1]-off[1])/h, 0), 1)
        X = ix+px*iw; Y = top+py*ih
        lines = B.wrap(t, max(14, int((ix-24)/7.6)))
        d = dict(i=i, X=X, Y=Y, ty=Y, y=Y, t=t, c=c, lines=lines, h=len(lines)*LH)
        (L if px < .5 else Rr).append(d)
    while len(L) > len(Rr)+3:
        m = max(L, key=lambda d: d['X']); L.remove(m); Rr.append(m)
    while len(Rr) > len(L)+3:
        m = min(Rr, key=lambda d: d['X']); Rr.remove(m); L.append(m)
    H = top+ih+8
    for d in L: d['ty'] = d['Y'] + d['X']*1e-4
    for d in Rr: d['ty'] = d['Y'] - d['X']*1e-4
    B.spread(L, 4, H-4, 8); B.spread(Rr, 4, H-4, 8)
    for side in (L, Rr):
        if side: H = max(H, max(d['y']+d['h']/2 for d in side)+6)
    g = []
    for side, sg in ((L, -1), (Rr, 1)):
        for d in sorted(side, key=lambda d: d['y']):
            col = f"var(--c-{d['c']})"
            ex = ix-10 if sg < 0 else ix+iw+10; tx = ix-16 if sg < 0 else ix+iw+16
            pts = f"{d['X']:.1f},{d['Y']:.1f} {ex:.1f},{d['y']:.1f} {tx:.1f},{d['y']:.1f}"
            anchor = 'end' if sg < 0 else 'start'; lx = tx-4 if sg < 0 else tx+4
            y0 = d['y']-d['h']/2+LH*.75
            spans = ''.join(f'<tspan x="{lx:.1f}" y="{y0+j*LH:.1f}">{fmt(ln)}</tspan>' for j, ln in enumerate(d['lines']))
            bx = lx-24 if sg < 0 else lx
            g.append(f'<g class="lab" data-c="{d["c"]}" style="--lc:{col}" tabindex="0">'
                     f'<polyline class="halo" points="{pts}"/><polyline class="ln" points="{pts}"/>'
                     f'<circle class="dot" cx="{d["X"]:.1f}" cy="{d["Y"]:.1f}" r="4"/>'
                     f'<text class="tx" text-anchor="{anchor}">{spans}</text>'
                     f'<g class="q"><rect x="{bx:.1f}" y="{d["y"]-10:.1f}" width="24" height="20" rx="4"/>'
                     f'<text x="{bx+12:.1f}" y="{d["y"]+4.5:.1f}" text-anchor="middle">?</text></g></g>')
    cats = sorted({c for *_, c in labels}, key=lambda c: list(B.CAT).index(c))
    legend = ''.join(f'<span class="lg" data-c="{c}"><i></i>{B.CAT[c][1]}</span>' for c in cats)
    svg = (f'<svg viewBox="0 0 {W} {H:.0f}" role="img" aria-label="{esc(a.get("cap",""))}">'
           f'<image href="{name}" x="{ix:.1f}" y="{top}" width="{iw:.1f}" height="{ih:.1f}" preserveAspectRatio="none"/>'
           f'<rect class="frame" x="{ix:.1f}" y="{top}" width="{iw:.1f}" height="{ih:.1f}"/>' + ''.join(g) + '</svg>')
    tools = ('<div class="ftools"><button class="btn b-quiz" type="button">Skrij oznake</button>'
             '<button class="btn b-zoom" type="button">Povečaj</button></div>') if labels else ''
    return (f'<figure class="fig" id="f{pid}"><div class="fsc">{svg}</div>'
            f'<figcaption><span class="fn">Slika {acc}.{num}</span> {esc(a.get("cap",""))}'
            f'<span class="lgs">{legend}</span>{tools}</figcaption></figure>')

def fmt(ln):
    if ' – ' in ln:
        a, b = ln.split(' – ', 1)
        return f'<tspan class="la">{esc(a)}</tspan><tspan class="sl"> – {esc(b)}</tspan>'
    return f'<tspan class="la">{esc(ln)}</tspan>'

def render(num, fname, name, sub):
    d = json.load(open(f'{B.R}/{fname}'))
    root = ET.fromstring(json.loads(d[-1]['text'])['data']['xml'])
    place = list(PLACE[num]); used = set()
    out, toc = [], []
    pending = []; fig_n = [0]; in_gloss = False

    def flush():
        while pending:
            pid = pending.pop(0)
            plate, k = pid.rsplit('-', 1)
            fig_n[0] += 1
            out.append(figure(pid, fig_n[0], num))

    for el in root:
        if el.tag == 'paragraph' and el.find('media') is not None:
            continue
        if el.tag == 'paragraph' and el.get('heading'):
            h = el.get('heading'); t = B.inline(el); plain = html.unescape(re.sub('<[^>]+>', '', t))
            if h == '1':
                continue
            flush()
            if h == '2':
                in_gloss = plain.startswith('Slikovni')
                hid = f'l{num}-{len(toc)}'
                m = re.match(r'(\d+\.\d+)\s+(.*)', plain)
                if in_gloss:
                    title = 'Ponovi izraze · ' + plain.split('·', 1)[-1].strip()
                    toc.append((hid, title))
                    out.append(f'<h2 id="{hid}" class="gl">{esc(title)}</h2>')
                else:
                    toc.append((hid, plain))
                    out.append(f'<h2 id="{hid}"><span class="sn">{m.group(1)}</span>{esc(m.group(2))}</h2>' if m else f'<h2 id="{hid}">{t}</h2>')
            elif h == '3':
                out.append(f'<h3>{t}</h3>')
            else:
                out.append(f'<h4>{t}</h4>')
            if not in_gloss:
                for i, (key, pids) in enumerate(place):
                    hit = plain.strip() == key[1:] if key.startswith('=') else key.lower() in plain.lower()
                    if i not in used and hit:
                        used.add(i); pending.extend(pids); break
            continue
        if el.tag == 'paragraph':
            t = B.inline(el)
            if not t.strip(): continue
            if in_gloss and 'Pokrij desni stolpec' in t:
                t = 'Pokrij desni stolpec in povej pomen; nato poišči strukturo na sliki zgoraj v poglavju.'
            t = re.sub(r'\s*Na koncu zavihka je slikovni slovar[^.]*\.', ' Slike so ob besedilu, ki ga razlagajo; na koncu je tabela izrazov za ponavljanje.', t)
            t = t.replace('(glej slikovni slovar)', '(slike spodaj)')
            out.append(f'<p class="lede">{t}</p>' if not out else f'<p>{t}</p>')
        elif el.tag == 'list':
            out.append(B.render_list(el))
        elif el.tag == 'table':
            out.append('<div class="tw">' + B.render_table(el, in_gloss) + '</div>')
    flush()
    missing = [k for i, (k, _) in enumerate(place) if i not in used]
    if missing: print('UNPLACED', num, missing)
    return out, toc, fig_n[0]

def main():
    chapters, nav = [], []
    total = 0
    for num, fname, name, sub in B.TABS:
        body, toc, n = render(num, fname, name, sub); total += n
        nav.append(f'<li class="nl ch{num}"><a href="#p{num}"><b>{num}</b>{esc(name)}</a><ol>' +
                   ''.join(f'<li><a href="#{h}">{esc(t)}</a></li>' for h, t in toc) + '</ol></li>')
        chapters.append(f'<section class="chapter ch{num}" id="p{num}"><header class="ch-h"><span class="ch-n">{num}</span>'
                        f'<div><p class="ch-k">Predavanje {num} · {n} slik</p><h1>{esc(name)}</h1><p class="ch-s">{esc(sub)}</p></div></header>'
                        + '\n'.join(body) + '</section>')
    tpl = open(os.path.join(S, 'site_template.html')).read()
    page = tpl.replace('{{NAV}}', ''.join(nav)).replace('{{CHAPTERS}}', '\n'.join(chapters)).replace('{{TOTAL}}', str(total))
    open(os.path.join(OUT, 'index.html'), 'w').write(page)
    print('figures', total, 'html bytes', len(page))

if __name__ == '__main__':
    main()
