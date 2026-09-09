import json, math
from geo import proj, to_xy, CORE, MI

m = json.load(open('meta.json'))
X0, X1, Y0, Y1 = m['extent']
def S(p): return ((p[0]-X0)/10, (Y1-p[1])/10)
def SL(lat, lon): return S(proj(lat, lon))

# in-core / annexed / out-of-bounds classification drives the dot style
LM = {
 'Capitol Square':      ('core','middle',0,-10),
 'Monona Terrace':      ('core','start',  7,  4),
 'State Street':        ('core','end',   -7, -5),
 'Memorial Union':      ('core','end',   -7,  1),
 'Bascom Hall':         ('core','end',   -7,  5),
 'Union South':         ('core','end',   -7,  5),
 'Camp Randall':        ('core','end',   -7,  5),
 'Henry Vilas Zoo':     ('core','start',  7,  5),
 'James Madison Park':  ('core','start',  7, -3),
 'Picnic Point':        ('annex','start', 8,  3),
 'UW Arboretum':        ('annex','none',  0,  0),
 'Tenney Park':         ('out','end',    -7, -3),
 'Yahara Locks':        ('out','start',   7,  7),
 "Schenk's Corners":    ('out','middle',  0, -9),
 'Olbrich Gardens':     ('out','end',    -7, 11),
 'Olin Park':           ('out','start',   7,  5),
 'Turville Point':      ('out','start',   7,  5),
}
WATER = {'LAKE MENDOTA': (43.0960,-89.4090), 'LAKE MONONA': (43.0580,-89.3600),
         'LAKE WINGRA': (43.0553,-89.4222), 'UNIVERSITY BAY': (43.0855,-89.4130)}

o = []
A = o.append
# --- footprint: core corridor ---
pts = " ".join(f"{x},{y}" for x,y in m['core'])
A(f'<polygon class="core-fill" points="{pts}"/>')
A(f'<polygon class="core-line" points="{pts}"/>')
# --- annex lobes ---
for name, a in m['annex'].items():
    p = " ".join(f"{x},{y}" for x,y in a['pts'])
    A(f'<polygon class="annex-fill" points="{p}"/><polygon class="annex-line" points="{p}"/>')
# --- 73-degree isthmus axis ---
ax = [S(to_xy(u, CORE['cv'])) for u in (-4700, 4900)]
A(f'<line class="axis" x1="{ax[0][0]:.1f}" y1="{ax[0][1]:.1f}" x2="{ax[1][0]:.1f}" y2="{ax[1][1]:.1f}"/>')
ang = -16.6
lx, ly = S(to_xy(3050, CORE['cv']))
A(f'<text class="axis-lbl" x="{lx:.1f}" y="{ly-4:.1f}" transform="rotate({ang} {lx:.1f} {ly-4:.1f})">isthmus axis · 73° from N</text>')
# --- water names (letterspaced caps: standard hydrographic convention) ---
for n,(la,lo) in WATER.items():
    x,y = SL(la,lo)
    cls = "water-lbl" + (" water-lbl-sm" if n=='UNIVERSITY BAY' else "")
    A(f'<text class="{cls}" x="{x:.1f}" y="{y:.1f}">{n}</text>')
# --- preserve + park names ---
for n,(x,y) in m['presLabels']:
    if n in ('Muir Woods','Curtis Prairie'): continue
    A(f'<text class="pres-lbl" x="{x:.1f}" y="{y:.1f}">{n}</text>')
for n,(x,y) in m['parkLabels']:
    if n in ('Law Park','Orton Pk'): continue
    A(f'<text class="park-lbl" x="{x:.1f}" y="{y:.1f}">{n}</text>')
# --- landmark markers ---
for n,(kind, anch, dx, dy) in LM.items():
    x,y = m['landmarks'][n]
    A(f'<circle class="dot dot-{kind}" cx="{x}" cy="{y}" r="{3.0 if kind!="out" else 2.6}"/>')
    if anch != 'none':
        A(f'<text class="lm-lbl lm-{kind}" x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="{anch}">{n}</text>')
# --- scale bar (1 mile) + north arrow ---
u = m['scaleBarUnits']; bx, by = 40, 731
A(f'<g class="scale"><rect x="{bx}" y="{by}" width="{u/2:.1f}" height="5" class="sb-a"/>'
  f'<rect x="{bx+u/2:.1f}" y="{by}" width="{u/2:.1f}" height="5" class="sb-b"/>'
  f'<text class="sb-t" x="{bx}" y="{by-4}">0</text>'
  f'<text class="sb-t" x="{bx+u/2:.1f}" y="{by-4}" text-anchor="middle">½</text>'
  f'<text class="sb-t" x="{bx+u:.1f}" y="{by-4}" text-anchor="start">1 mile = 470 game tiles</text></g>')
A(f'<g class="northarrow"><path d="M960,700 L954,722 L960,716 L966,722 Z"/>'
  f'<text class="sb-t" x="960" y="734" text-anchor="middle">N</text></g>')
open('overlay.svg','w').write("\n".join("  "+l for l in o))
print(f"overlay.svg written, {len(o)} elements")
