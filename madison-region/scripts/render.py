import json, math, os
from geo import proj, rings_of, simplify, load, to_uv, to_xy, core_corners, CORE, ANNEX, LM, MI

# map extent in metres E/N of the Capitol
X0, X1, Y0, Y1 = -5200, 4800, -4300, 3200
W, H = (X1-X0)/10, (Y1-Y0)/10          # 1 svg unit = 10 m  -> 1000 x 750
def S(p): return ((p[0]-X0)/10, (Y1-p[1])/10)   # project to svg space (y down)

def clipbox(pts, pad=600):
    return any(X0-pad<=x<=X1+pad and Y0-pad<=y<=Y1+pad for x,y in pts)

def path(rings, tol, close=True):
    out=[]
    for r in rings:
        if len(r)<2 or not clipbox(r): continue
        r = simplify(r, tol)
        if len(r)<2: continue
        d = "M" + " L".join(f"{S(p)[0]:.1f},{S(p)[1]:.1f}" for p in r)
        out.append(d + ("Z" if close else ""))
    return " ".join(out)

# ---------- water ----------
water = load('water')
BIG = {'Lake Mendota','Lake Monona','Lake Wingra','Monona Bay','Upper Mud Lake','Lake Waubesa'}
lake_d, pond_d, river_d = [], [], []
for e in water:
    t = e.get('tags', {}); n = t.get('name','')
    if t.get('waterway') == 'river':
        river_d.append(path(rings_of(e), 8, close=False)); continue
    rs = rings_of(e)
    if not rs: continue
    area = max(abs(sum(r[i][0]*r[i-1][1]-r[i-1][0]*r[i][1] for i in range(len(r))))/2 for r in rs)
    (lake_d if (n in BIG or area > 60000) else pond_d).append(path(rs, 12 if n in BIG else 6))

# ---------- parks ----------
parks = load('park')
park_d, park_labels = [], []
KEY = {'Brittingham Park':'Brittingham','Yahara Place Park':'Yahara Place',
       'Marshall Park':'Marshall Pk','Warner Park':'Warner Park'}
seen=set()
for e in parks:
    t = e.get('tags', {}); n = t.get('name','')
    rs = rings_of(e)
    if not rs: continue
    park_d.append(path(rs, 6))
    if n in KEY and KEY[n] and n not in seen:
        seen.add(n)
        pts=[p for r in rs for p in r]
        cx=sum(p[0] for p in pts)/len(pts); cy=sum(p[1] for p in pts)/len(pts)
        if X0<cx<X1 and Y0<cy<Y1: park_labels.append((KEY[n], S((cx,cy))))

# ---------- preserves (real boundaries for the must-have greenspace) ----------
PRES = {'Lakeshore Nature Preserve':'Lakeshore Nature Preserve',
        'University of Wisconsin Arboretum':'UW Arboretum',
        'Curtis Prairie':'Curtis Prairie','Wingra Woods':'Wingra Woods','Muir Woods':'Muir Woods',
        'Gallistel Woods':None,'Frautschi Point':None,'Eagle Heights Woods':None,'Picnic Point Marsh':None}
pres_d, pres_labels = [], []
for e in load('named'):
    n = e.get('tags', {}).get('name','')
    if n not in PRES or e['type'] == 'node': continue
    rs = rings_of(e)
    if not rs: continue
    pres_d.append(path(rs, 6))
    if PRES[n]:
        pts=[p for r in rs for p in r]
        cx=sum(p[0] for p in pts)/len(pts); cy=sum(p[1] for p in pts)/len(pts)
        pres_labels.append((PRES[n], S((cx,cy))))

# ---------- roads ----------
roads = load('road')
major_d, minor_d, rail_d = [], [], []
for e in roads:
    t = e.get('tags', {}); hw = t.get('highway'); rw = t.get('railway')
    rs = rings_of(e)
    if not rs: continue
    d = path(rs, 10, close=False)
    if not d: continue
    if rw == 'rail': rail_d.append(d)
    elif hw in ('motorway','trunk'): major_d.append(d)
    else: minor_d.append(d)

def emit(f, d_list, **attrs):
    d = " ".join(x for x in d_list if x)
    if not d.strip(): return
    a = " ".join(f'{k.replace("_","-")}="{v}"' for k,v in attrs.items())
    f.write(f'  <path d="{d}" {a}/>\n')

with open('layers.svg','w') as f:
    f.write(f'<!-- viewBox 0 0 {W:.0f} {H:.0f} ; 1 unit = 10 m ; origin = WI State Capitol -->\n')
    f.write('<g id="parks">\n');  emit(f, park_d,  fill="var(--green)", stroke="none");           f.write('</g>\n')
    f.write('<g id="preserve">\n'); emit(f, pres_d, fill="var(--preserve)", stroke="var(--preserveEdge)", stroke_width="0.6"); f.write('</g>\n')
    f.write('<g id="lakes">\n');  emit(f, lake_d,  fill="var(--water)", stroke="var(--waterEdge)", stroke_width="0.8"); f.write('</g>\n')
    f.write('<g id="ponds">\n');  emit(f, pond_d,  fill="var(--water)", stroke="none");           f.write('</g>\n')
    f.write('<g id="rail">\n');   emit(f, rail_d,  fill="none", stroke="var(--rail)", stroke_width="0.7", stroke_dasharray="3 3"); f.write('</g>\n')
    f.write('<g id="roads">\n');  emit(f, minor_d, fill="none", stroke="var(--road)",  stroke_width="0.7"); f.write('</g>\n')
    f.write('<g id="major">\n');  emit(f, major_d, fill="none", stroke="var(--roadHi)",stroke_width="1.6"); f.write('</g>\n')
    f.write('<g id="river">\n');  emit(f, river_d, fill="none", stroke="var(--water)", stroke_width="2.2"); f.write('</g>\n')

meta = dict(
  viewW=round(W), viewH=round(H), mPerUnit=10, extent=[X0,X1,Y0,Y1],
  core=[list(map(lambda v: round(v,1), S(p))) for p in core_corners()],
  coreArea=round(CORE['w']*CORE['h']/MI**2, 2),
  annex={k: dict(pts=[list(map(lambda v: round(v,1), S(p))) for p in
                      [(a['x0'],a['y0']),(a['x1'],a['y0']),(a['x1'],a['y1']),(a['x0'],a['y1'])]],
                 area=round((a['x1']-a['x0'])*(a['y1']-a['y0'])/MI**2,2)) for k,a in ANNEX.items()},
  landmarks={n: [round(v,1) for v in S(proj(la,lo))] for n,(la,lo) in LM.items()},
  parkLabels=[[n, [round(p[0],1), round(p[1],1)]] for n,p in park_labels],
  presLabels=[[n, [round(p[0],1), round(p[1],1)]] for n,p in pres_labels],
  scaleBarUnits=round(MI/10, 1),
)
json.dump(meta, open('meta.json','w'), indent=1)
print(f"layers.svg {os.path.getsize('layers.svg'):,} bytes ; viewBox {W:.0f}x{H:.0f}")
print(f"lakes={len(lake_d)} ponds={len(pond_d)} parks={len(park_d)} roads={len(minor_d)} major={len(major_d)} rail={len(rail_d)} river={len(river_d)}")
print("park labels:", [n for n,_ in park_labels])
print("preserve layer:", len(pres_d), "polys;", [n for n,_ in pres_labels])
print("1 mile =", round(MI/10,1), "svg units")
