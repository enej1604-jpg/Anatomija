"""PDF version of the study page: same in-context figures, print layout from template.html."""
import os, html
import build_site as W
B = W.B; S = W.S; esc = B.esc

tpl = open(os.path.join(S, 'template.html')).read()
tpl = tpl.replace('zapiski predavanj 1–4 s slikovnim atlasom', 'zapiski predavanj 1–4 z označenimi slikami')
tpl = tpl.replace('Zapiski sledijo prosojnicam po vrsti. Na koncu vsakega predavanja je <b>slikovni atlas</b>: slike s črtami do struktur, ki jih moraš znati, in tabela izrazov za samopreverjanje.',
                  'Zapiski sledijo prosojnicam po vrsti. <b>Slike stojijo ob besedilu, ki ga razlagajo</b>; črta s piko kaže točno strukturo. Na koncu vsakega predavanja je tabela izrazov za samopreverjanje.')
css = """
:root{--c-r:#2563a6;--c-k:#a86a12;--c-m:#c0362c;--c-s:#0b8578;--c-z:#7a3d9e;--c-t:#3c7a1f;--c-o:#55606b;--halo:#fff;--frame:#d9d4c7}
[data-c="r"]{--cc:var(--c-r)}[data-c="k"]{--cc:var(--c-k)}[data-c="m"]{--cc:var(--c-m)}[data-c="s"]{--cc:var(--c-s)}[data-c="z"]{--cc:var(--c-z)}[data-c="t"]{--cc:var(--c-t)}[data-c="o"]{--cc:var(--c-o)}
.fig{margin:3mm 0 5mm;break-inside:avoid;page-break-inside:avoid;border-top:1px solid #ebe6da;padding-top:2mm}
.fig svg{width:100%;height:auto;display:block}
.frame{fill:none;stroke:var(--frame);stroke-width:1}
.lab .halo{fill:none;stroke:var(--halo);stroke-width:4;stroke-linejoin:round;opacity:.9}
.lab .ln{fill:none;stroke:var(--lc);stroke-width:1.4;stroke-linejoin:round}
.lab .dot{fill:var(--lc);stroke:var(--halo);stroke-width:1.6}
.lab .tx{font:500 15px 'IBM Plex Sans Condensed';fill:#1d1b18}
.lab .la{fill:var(--lc);font-weight:600}
.lab .sl{fill:#3b3732;font-weight:400}
.lab .q,.ftools{display:none}
.fig figcaption{margin:0 6mm;padding-top:1.5mm;border-top:0}
.fn{font:700 8.6pt 'IBM Plex Sans Condensed';color:var(--a);margin-right:1.2mm}
.lgs{display:inline-flex;flex-wrap:wrap;gap:1mm 3mm;margin-left:2.5mm;vertical-align:1px}
.lg{display:inline-flex;align-items:center;gap:1.1mm;font:500 7.6pt 'IBM Plex Sans Condensed';color:#8a8378;white-space:nowrap}
.lg i{width:6.5px;height:6.5px;border-radius:50%;display:inline-block;background:var(--cc)}
.tw{margin:2mm 0 4.5mm}
h2 .sn{display:inline-block;min-width:11mm;color:var(--a);font-weight:700}
"""
tpl = tpl.replace('</style>', css + '</style>')

chapters, tocs = [], []
for num, fname, name, sub in B.TABS:
    body, toc, n = W.render(num, fname, name, sub)
    tocs.append(f'<div class="tc ch{num}"><div class="tcn">{num}</div><div><h3>{esc(name)}</h3><ol>' +
                ''.join(f'<li><a href="#{h}">{esc(t)}</a></li>' for h, t in toc) + '</ol></div></div>')
    chapters.append(f'<section class="chapter ch{num}"><div class="opener"><div class="onum">{num}</div><div><div class="okick">Predavanje {num} · {n} slik</div>'
                    f'<h1>{esc(name)}</h1><div class="osub">{esc(sub)}</div></div></div><div class="body">' + '\n'.join(body) + '</div></section>')
page = tpl.replace('{{TOC}}', ''.join(tocs)).replace('{{CHAPTERS}}', '\n'.join(chapters))
open(os.path.join(W.OUT, 'print.html'), 'w').write(page)
print('ok')
