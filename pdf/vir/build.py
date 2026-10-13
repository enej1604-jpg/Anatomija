import json, re, sys, os, base64, html, io
import xml.etree.ElementTree as ET
from PIL import Image

S = os.path.dirname(os.path.abspath(__file__))
R = '/root/.claude/projects/-home-user-Anatomija/9e55e80f-ee32-5b4f-8f4f-970e761a6b93/tool-results'
TABS = [
    ('1', 'mcp-Claude_Docs-read-1791905722769.txt', 'Uvod', 'Izrazoslovje · celica · tkiva · koža'),
    ('2', 'mcp-Claude_Docs-read-1791905723757.txt', 'Osteologija', 'Kostnina · okostje trupa, glave in udov'),
    ('3', 'mcp-Claude_Docs-read-1791905724815.txt', 'Miologija I', 'Hrustanec · sklepi · mišično tkivo · glava'),
    ('4', 'mcp-Claude_Docs-read-1791905725646.txt', 'Miologija II', 'Vrat · hrbet · trup · rama · nadlaket'),
]
ANN = {}
for f in sorted(os.listdir(S)):
    if re.match(r'ann\d+\.py$', f):
        ns = {}
        exec(open(os.path.join(S, f)).read(), ns)
        ANN.update(ns['A'])
BOX = json.load(open(os.path.join(S, 'boxes.json')))

# category -> (line colour, label tag)
CAT = {
    'r': ('#2563a6', 'smer / ravnina'),
    'k': ('#b7791f', 'kost'),
    'm': ('#c0392b', 'mišica'),
    's': ('#0f8a7e', 'sklep / vez'),
    'z': ('#7b3fa0', 'živec / žila'),
    't': ('#3f7d20', 'tkivo / celica'),
    'o': ('#4a5568', 'drugo'),
}

def esc(s):
    return html.escape(s, quote=True)

# ---------- figures ----------
def panel_uri(plate, k, crop=None):
    im = Image.open(f'{S}/panels/{plate}-{k}.png').convert('RGB')
    full0 = im.size; c0 = (0, 0)
    if crop:
        c0 = (int(crop[0]/100*im.width), int(crop[1]/100*im.height))
        im = im.crop((c0[0], c0[1], int(crop[2]/100*im.width), int(crop[3]/100*im.height)))
    # trim pure-white margins so pictures sit tight
    bg = Image.new('RGB', im.size, (255, 255, 255))
    from PIL import ImageChops
    diff = ImageChops.difference(im, bg).convert('L').point(lambda p: 255 if p > 18 else 0)
    bb = diff.getbbox()
    off = (0, 0)
    if bb:
        pad = 6
        bb = (max(0, bb[0]-pad), max(0, bb[1]-pad), min(im.width, bb[2]+pad), min(im.height, bb[3]+pad))
        off = (bb[0] + c0[0], bb[1] + c0[1])
        im = im.crop(bb)
    else:
        off = c0
    full = full0
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=86)
    return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode(), im.size, off, full

def wrap(t, n):
    words = t.split(' '); lines = ['']
    for w in words:
        if len(lines[-1]) + len(w) + 1 > n and lines[-1]:
            lines.append(w)
        else:
            lines[-1] = (lines[-1] + ' ' + w).strip()
    return lines

def spread(items, lo, hi, gap):
    # items: list of dicts with 'y' desired and 'h'; resolve overlaps keeping order
    items.sort(key=lambda d: d['ty'])
    for i in range(1, len(items)):
        prev = items[i-1]
        mn = prev['y'] + prev['h']/2 + gap + items[i]['h']/2
        items[i]['y'] = max(items[i]['ty'], mn)
    # push back up if overflowing bottom
    if items and items[-1]['y'] + items[-1]['h']/2 > hi:
        items[-1]['y'] = hi - items[-1]['h']/2
        for i in range(len(items)-2, -1, -1):
            mx = items[i+1]['y'] - items[i+1]['h']/2 - gap - items[i]['h']/2
            items[i]['y'] = min(items[i]['y'], mx)
    if items and items[0]['y'] - items[0]['h']/2 < lo:
        d = lo - (items[0]['y'] - items[0]['h']/2)
        for it in items: it['y'] += d

def figure_svg(plate, k, ann):
    uri, (w, h), off, full = panel_uri(plate, k, ann.get('crop'))
    labels = ann.get('a', [])
    W = 1000
    if labels:
        iw = min(500, 600 * w / h)
    else:
        iw = min(760, 620 * w / h)
    ih = iw * h / w
    ix = (W - iw) / 2
    pad_top = 8
    LH = 17.5  # line height
    left, right = [], []
    for x, y, t, c in labels:
        # x,y are % of the un-trimmed panel; map into trimmed image
        px = (x/100*full[0] - off[0]) / w
        py = (y/100*full[1] - off[1]) / h
        px = min(max(px, 0), 1); py = min(max(py, 0), 1)
        X = ix + px*iw; Y = pad_top + py*ih
        colw = ix - 22
        lines = wrap(t, max(14, int(colw / 7.6)))
        d = {'X': X, 'Y': Y, 'ty': Y, 'y': Y, 't': t, 'c': c, 'lines': lines, 'h': len(lines)*LH}
        (left if px < 0.5 else right).append(d)
    # balance if one side is overloaded
    while len(left) > len(right) + 3:
        m = max(left, key=lambda d: d['X']); left.remove(m); right.append(m)
    while len(right) > len(left) + 3:
        m = min(right, key=lambda d: d['X']); right.remove(m); left.append(m)
    H = pad_top + ih + 8
    spread(left, 4, H - 4, 7); spread(right, 4, H - 4, 7)
    for side in (left, right):
        if side:
            H = max(H, max(d['y'] + d['h']/2 for d in side) + 6)
    out = [f'<svg viewBox="0 0 {W} {H:.0f}" xmlns="http://www.w3.org/2000/svg" class="fig">',
           f'<image href="{uri}" x="{ix:.1f}" y="{pad_top}" width="{iw:.1f}" height="{ih:.1f}" preserveAspectRatio="none"/>',
           f'<rect x="{ix:.1f}" y="{pad_top}" width="{iw:.1f}" height="{ih:.1f}" fill="none" stroke="#d9d4c7" stroke-width="1"/>']
    lines_svg, dots_svg, text_svg = [], [], []
    for side, d0 in ((left, -1), (right, 1)):
        for d in side:
            col = CAT[d['c']][0]
            ex = ix - 10 if d0 < 0 else ix + iw + 10       # elbow at image edge
            tx = ix - 16 if d0 < 0 else ix + iw + 16
            pts = f"{d['X']:.1f},{d['Y']:.1f} {ex:.1f},{d['y']:.1f} {tx:.1f},{d['y']:.1f}"
            lines_svg.append(f'<polyline points="{pts}" fill="none" stroke="#fff" stroke-width="3.6" stroke-linejoin="round" opacity=".9"/>')
            lines_svg.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="1.3" stroke-linejoin="round"/>')
            dots_svg.append(f'<circle cx="{d["X"]:.1f}" cy="{d["Y"]:.1f}" r="3.6" fill="{col}" stroke="#fff" stroke-width="1.4"/>')
            anchor = 'end' if d0 < 0 else 'start'
            lx = tx - 4 if d0 < 0 else tx + 4
            y0 = d['y'] - d['h']/2 + LH*0.75
            ts = []
            for i, ln in enumerate(d['lines']):
                # Latin part (before ' – ') in italic-ish colour; Slovene after
                ts.append(f'<tspan x="{lx:.1f}" y="{y0 + i*LH:.1f}">{fmt_label(ln, col)}</tspan>')
            text_svg.append(f'<text text-anchor="{anchor}" class="lb">{"".join(ts)}</text>')
    out += lines_svg + dots_svg + text_svg + ['</svg>']
    return '\n'.join(out)

def fmt_label(ln, col):
    if ' – ' in ln:
        a, b = ln.split(' – ', 1)
        return f'<tspan class="la" fill="{col}">{esc(a)}</tspan><tspan class="sl"> – {esc(b)}</tspan>'
    return f'<tspan class="la" fill="{col}">{esc(ln)}</tspan>'

PLATE_OF = {}  # blob order per tab -> plate id
def blank(plate, k):
    im = Image.open(f'{S}/panels/{plate}-{k}.png').convert('L')
    import numpy as np
    return np.array(im).mean() > 253.5

def plate_html(plate, letter, alt):
    ann = ANN.get(plate, {})
    title = ann.get('title', alt)
    ps = ann.get('p', [])
    out = [f'<section class="plate"><div class="plate-h"><span class="pl">{letter}</span><h3>{esc(title)}</h3></div>']
    n = len(BOX[plate])
    for k in range(1, n+1):
        a = ps[k-1] if k-1 < len(ps) else {}
        if a.get('skip') or blank(plate, k):
            out.append(f'<p class="nofig"><b>{letter}{k}</b> {esc(a.get("cap", ""))} <i>(slika v izvirni plošči manjka)</i></p>')
            continue
        cats = sorted({c for *_, c in a.get('a', [])}, key=lambda c: list(CAT).index(c))
        legend = ''.join(f'<span class="lg"><i style="background:{CAT[c][0]}"></i>{CAT[c][1]}</span>' for c in cats)
        out.append('<figure>' + figure_svg(plate, k, a) +
                   f'<figcaption><b>{letter}{k}</b> {esc(a.get("cap", ""))}<span class="lgs">{legend}</span></figcaption></figure>')
    out.append('</section>')
    return '\n'.join(out)

# ---------- text ----------
def inline(el):
    out = []
    for c in el:
        if c.tag == 'text':
            b = c.find('bold'); i = c.find('italic')
            if b is not None:
                out.append(f'<strong>{esc("".join(b.itertext()))}</strong>')
            elif i is not None:
                out.append(f'<em>{esc("".join(i.itertext()))}</em>')
            else:
                out.append(esc(c.text or ''))
        elif c.tag == 'mention':
            out.append(esc(c.get('label') or c.get('name') or ''))
        elif c.tag == 'date':
            out.append(esc(c.get('value')))
    s = ''.join(out)
    s = s.replace('→', '<span class="ar">→</span>')
    return s

def render_tab(num, fname, name, sub):
    d = json.load(open(f'{R}/{fname}'))
    x = json.loads(d[-1]['text'])['data']['xml']
    root = ET.fromstring(x)
    out = []
    media_i = 0
    toc = []
    in_gloss = False
    first_h1 = True
    for el in root:
        if el.tag == 'paragraph' and el.find('media') is not None:
            el = el.find('media')
        if el.tag == 'paragraph':
            h = el.get('heading'); t = inline(el)
            if h == '1':
                continue  # chapter opener renders the title
            if h == '2':
                hid = f'c{num}-{len(toc)}'
                plain = re.sub('<[^>]+>', '', t)
                toc.append((hid, plain))
                in_gloss = plain.startswith('Slikovni')
                m = re.match(r'(\d+\.\d+)\s+(.*)', html.unescape(plain))
                if m:
                    out.append(f'<h2 id="{hid}"><span class="sn">{m.group(1)}</span>{esc(m.group(2))}</h2>')
                else:
                    cls = ' class="gl"' if in_gloss else ''
                    out.append(f'<h2 id="{hid}"{cls}>{t}</h2>')
            elif h == '3':
                if in_gloss:
                    continue  # plate header replaces "A · …" subheads
                out.append(f'<h3>{t}</h3>')
            elif h:
                out.append(f'<h4>{t}</h4>')
            else:
                if not t.strip():
                    continue
                if len(out) == 0:
                    out.append(f'<p class="lede">{t}</p>')
                else:
                    out.append(f'<p>{t}</p>')
        elif el.tag == 'list':
            out.append(render_list(el))
        elif el.tag == 'table':
            out.append(render_table(el, in_gloss))
        elif el.tag == 'media':
            media_i += 1
            plate = f'{num}-{media_i}'
            out.append(plate_html(plate, f'{num}{chr(64+media_i)}', el.get('alt')))
    return out, toc

def render_list(el):
    tag = 'ol' if el.get('kind') == 'ordered' else 'ul'
    items = []
    for li in el:
        parts = []
        for c in li:
            if c.tag == 'paragraph':
                parts.append(inline(c))
            elif c.tag == 'list':
                parts.append(render_list(c))
        items.append('<li>' + ''.join(parts) + '</li>')
    return f'<{tag}>' + ''.join(items) + f'</{tag}>'

def render_table(el, gloss):
    rows = list(el)
    out = [f'<table class="{"gls" if gloss else "tb"}">']
    for ri, r in enumerate(rows):
        cells = []
        for c in r:
            tag = 'th' if c.get('header') == 'true' else 'td'
            content = '<br>'.join(inline(p) for p in c if p.tag == 'paragraph')
            cells.append(f'<{tag}>{content}</{tag}>')
        if ri == 0 and all(c.get('header') == 'true' for c in r):
            out.append('<thead><tr>' + ''.join(cells) + '</tr></thead><tbody>')
        else:
            out.append('<tr>' + ''.join(cells) + '</tr>')
    out.append('</tbody></table>')
    return ''.join(out)

def main(only=None):
    chapters = []
    tocs = []
    for num, fname, name, sub in TABS:
        if only and num not in only:
            continue
        body, toc = render_tab(num, fname, name, sub)
        tocs.append((num, name, sub, toc))
        chapters.append(f'''<section class="chapter ch{num}">
<div class="opener"><div class="onum">{num}</div><div><div class="okick">Predavanje {num}</div><h1>{esc(name)}</h1><div class="osub">{esc(sub)}</div></div></div>
<div class="body">{"".join(body)}</div></section>''')
    toc_html = []
    for num, name, sub, toc in tocs:
        items = ''.join(f'<li><a href="#{hid}">{esc(html.unescape(t))}</a></li>' for hid, t in toc)
        toc_html.append(f'<div class="tc ch{num}"><div class="tcn">{num}</div><div><h3>{esc(name)}</h3><ol>{items}</ol></div></div>')
    tpl = open(f'{S}/template.html').read()
    page = tpl.replace('{{TOC}}', ''.join(toc_html)).replace('{{CHAPTERS}}', '\n'.join(chapters))
    open(f'{S}/out.html', 'w').write(page)
    print('html ok', len(page))

if __name__ == '__main__':
    main(sys.argv[1:] or None)
