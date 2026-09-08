import json, math, os

LAT0, LON0 = 43.0747, -89.3842            # Wisconsin State Capitol = origin
MPD = 111320.0
KX = MPD * math.cos(math.radians(LAT0))
MI = 1609.344
def proj(lat, lon): return ((lon - LON0) * KX, (lat - LAT0) * MPD)   # metres E, N

def load(name):
    p = name + '.json'
    if not os.path.exists(p) or os.path.getsize(p) < 500: return []
    try: return json.load(open(p))['elements']
    except Exception: return []

def rings_of(el):
    """Return list of projected rings (lists of (x,y)) for a way or multipolygon relation."""
    out = []
    if el['type'] == 'way' and 'geometry' in el:
        out.append([proj(p['lat'], p['lon']) for p in el['geometry']])
    elif el['type'] == 'relation':
        segs = [[proj(p['lat'], p['lon']) for p in m['geometry']]
                for m in el.get('members', [])
                if m.get('role') in ('outer', '') and m.get('geometry')]
        eps = 1.0
        while segs:                                   # stitch member ways into rings
            cur = segs.pop(0)
            changed = True
            while changed:
                changed = False
                for i, s in enumerate(segs):
                    if math.dist(cur[-1], s[0]) < eps:  cur += s[1:];        segs.pop(i); changed=True; break
                    if math.dist(cur[-1], s[-1]) < eps: cur += s[::-1][1:];  segs.pop(i); changed=True; break
                    if math.dist(cur[0], s[-1]) < eps:  cur = s[:-1] + cur;  segs.pop(i); changed=True; break
                    if math.dist(cur[0], s[0]) < eps:   cur = s[::-1][:-1]+cur; segs.pop(i); changed=True; break
            out.append(cur)
    return [r for r in out if len(r) >= 3]

def simplify(pts, tol):
    """Douglas-Peucker."""
    if len(pts) < 3: return pts
    a, b = pts[0], pts[-1]
    dx, dy = b[0]-a[0], b[1]-a[1]; L = math.hypot(dx, dy)
    worst, wi = -1, 0
    for i in range(1, len(pts)-1):
        p = pts[i]
        d = abs(dy*p[0]-dx*p[1]+b[0]*a[1]-b[1]*a[0])/L if L > 1e-9 else math.dist(p, a)
        if d > worst: worst, wi = d, i
    if worst <= tol: return [a, b]
    return simplify(pts[:wi+1], tol)[:-1] + simplify(pts[wi:], tol)

# ---- isthmus frame: u = along the Bascom->Olbrich axis, v = across it ----
TH = math.radians(16.6)
def to_uv(x, y): return ( x*math.cos(TH)+y*math.sin(TH), -x*math.sin(TH)+y*math.cos(TH))
def to_xy(u, v): return ( u*math.cos(TH)-v*math.sin(TH),  u*math.sin(TH)+v*math.cos(TH))

CORE = dict(cu=-760, cv=200, w=2.2*MI, h=1.2*MI)      # recommended isthmus corridor
def core_corners():
    hw, hh = CORE['w']/2, CORE['h']/2
    return [to_xy(CORE['cu']+su*hw, CORE['cv']+sv*hh) for su, sv in ((-1,-1),(1,-1),(1,1),(-1,1))]

ANNEX = {                                              # axis-aligned lobes, metres E/N of Capitol
  'Lakeshore Preserve / Picnic Point': dict(x0=-3600, x1=-2250, y0=850,   y1=1900),
  'Arboretum / Lake Wingra / Vilas'  : dict(x0=-3900, x1=-1900, y0=-3900, y1=-700),
}

LM = {
 'Capitol Square':(43.07474,-89.38421),'Monona Terrace':(43.07161,-89.38058),
 'State Street':(43.07540,-89.39250),'Memorial Union':(43.07655,-89.39938),
 'Bascom Hall':(43.07566,-89.40477),'Union South':(43.07159,-89.40817),
 'Camp Randall':(43.07000,-89.41262),'Picnic Point':(43.08976,-89.41518),
 'Henry Vilas Zoo':(43.06639,-89.41083),'Lake Wingra':(43.05530,-89.42220),
 'UW Arboretum':(43.04278,-89.42472),'James Madison Park':(43.08028,-89.37639),
 'Tenney Park':(43.08944,-89.36278),'Yahara Locks':(43.09060,-89.36060),
 "Schenk's Corners":(43.08730,-89.34750),'Olbrich Gardens':(43.09061,-89.33633),
 'Olin Park':(43.05530,-89.37920),'Turville Point':(43.05250,-89.37330),
}

if __name__ == '__main__':
    hw, hh = CORE['w']/2, CORE['h']/2
    print("=== membership of the recommended 2.2 x 1.2 mi isthmus corridor ===")
    for n,(la,lo) in LM.items():
        x,y = proj(la,lo); u,v = to_uv(x,y)
        du, dv = abs(u-CORE['cu']), abs(v-CORE['cv'])
        inc = du <= hw and dv <= hh
        ann = [k for k,a in ANNEX.items() if a['x0']<=x<=a['x1'] and a['y0']<=y<=a['y1']]
        tag = 'CORE' if inc else ('ANNEX: '+ann[0].split('/')[0].strip() if ann else '--')
        print(f"  {n:<22} u={u:+6.0f} v={v:+6.0f}   {tag}")
    print(f"\ncore area   = {CORE['w']*CORE['h']/MI**2:.2f} sq mi")
    for k,a in ANNEX.items():
        print(f"annex {k[:28]:<30} {(a['x1']-a['x0'])*(a['y1']-a['y0'])/MI**2:.2f} sq mi")
