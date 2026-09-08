import re, collections
exec(open('geo.py').read().split('def solve')[0])

lm_order, kanto_start = [], None
for line in open('landmark_constants.asm'):
    s=line.strip()
    if s.startswith('const LANDMARK_'): lm_order.append(s.split()[1].split(';')[0])
    elif s.startswith('DEF KANTO_LANDMARK'): kanto_start=len(lm_order)
lm_idx={n:i for i,n in enumerate(lm_order)}

mg,cur=[],None
for line in open('maps_data_maps.asm'):
    s=line.split(';')[0].rstrip()
    if re.match(r'^MapGroup_(\w+):',s): cur=[]; mg.append(cur); continue
    t=s.strip()
    if t.startswith('map ') and cur is not None:
        p=[x.strip() for x in t[4:].split(',')]; cur.append((p[2],p[3]))
dg,cur=[],None
for line in open('map_constants.asm'):
    s=line.split(';')[0].strip()
    if s.startswith('newgroup '): cur=[]; dg.append(cur)
    elif s.startswith('map_const ') and cur is not None:
        cur.append([x.strip() for x in s[10:].split(',')][0])
info={}
for dl,ml in zip(dg,mg):
    for c,(env,lm) in zip(dl,ml): info[c]=(env,lm)

EXCLUDE={'NATIONAL_PARK_BUG_CONTEST','SAFARI_ZONE_BETA'}
M_PER_MI=1609.344
rows=collections.defaultdict(list)
for c,(env,lm) in sorted(info.items()):
    if env not in ('TOWN','ROUTE') or c in EXCLUDE: continue
    reg='Kanto' if lm_idx.get(lm,0)>=kanto_start else 'Johto'
    if c in ('ROUTE_26','ROUTE_27'): reg='Rt26/27'
    w,h=dims[c]; rows[reg].append((c,w*2,h*2))   # blocks -> walkable tiles

def show(name, maps):
    X=sum(m[1] for m in maps); Y=sum(m[2] for m in maps)
    print(f"\n=== {name}: {len(maps)} outdoor maps ===")
    print(f"  total X (sum of widths)  = {X:>6,} tiles = {X:>6,} m = {X/1000:6.3f} km = {X/M_PER_MI:5.3f} mi = {X*3.28084:8,.0f} ft")
    print(f"  total Y (sum of heights) = {Y:>6,} tiles = {Y:>6,} m = {Y/1000:6.3f} km = {Y/M_PER_MI:5.3f} mi = {Y*3.28084:8,.0f} ft")
    print(f"  mean map = {X/len(maps):.1f} x {Y/len(maps):.1f} tiles ; X+Y = {X+Y:,} m = {(X+Y)/M_PER_MI:.3f} mi")
    return X,Y

jx,jy=show("JOHTO", rows['Johto'])
kx,ky=show("KANTO (strict landmark split)", rows['Kanto'])
rx,ry=show("Routes 26 & 27 (Kanto landmarks, on Johto's grid)", rows['Rt26/27'])
print(f"\n  KANTO incl. Rt 26/27: X = {kx+rx:,} m ({(kx+rx)/M_PER_MI:.3f} mi)   Y = {ky+ry:,} m ({(ky+ry)/M_PER_MI:.3f} mi)")
print(f"  BOTH REGIONS:         X = {jx+kx+rx:,} m ({(jx+kx+rx)/M_PER_MI:.3f} mi)   Y = {jy+ky+ry:,} m ({(jy+ky+ry)/M_PER_MI:.3f} mi)")

for reg in ('Johto','Kanto'):
    print(f"\n--- {reg}: widest 5 / tallest 5 (walkable tiles) ---")
    print("   widest: ", ", ".join(f"{c.replace('_',' ').title()} {w}" for c,w,h in sorted(rows[reg],key=lambda r:-r[1])[:5]))
    print("   tallest:", ", ".join(f"{c.replace('_',' ').title()} {h}" for c,w,h in sorted(rows[reg],key=lambda r:-r[2])[:5]))
