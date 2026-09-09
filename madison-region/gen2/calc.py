import re

# --- landmark order + Johto/Kanto split marker ---
lm_order, kanto_start = [], None
for line in open('landmark_constants.asm'):
    s = line.strip()
    if s.startswith('const LANDMARK_'):
        lm_order.append(s.split()[1].split(';')[0].strip())
    elif s.startswith('DEF KANTO_LANDMARK'):
        kanto_start = len(lm_order)          # next const declared is first Kanto landmark
lm_idx = {n: i for i, n in enumerate(lm_order)}
print(f"landmarks: {len(lm_order)}, kanto starts at index {kanto_start} = {lm_order[kanto_start]}")

# --- dimensions in blocks, grouped ---
dim_groups, cur = [], None
for line in open('map_constants.asm'):
    s = line.split(';')[0].strip()
    if s.startswith('newgroup '):
        cur = []; dim_groups.append((s.split()[1], cur))
    elif s.startswith('map_const ') and cur is not None:
        p = [x.strip() for x in s[len('map_const '):].split(',')]
        cur.append((p[0], int(p[1]), int(p[2])))

# --- environment + landmark, grouped (same table order) ---
map_groups, cur = [], None
for line in open('maps_data_maps.asm'):
    s = line.split(';')[0].rstrip()
    m = re.match(r'^MapGroup_(\w+):', s)
    if m:
        cur = []; map_groups.append((m.group(1), cur)); continue
    t = s.strip()
    if t.startswith('map ') and cur is not None:
        p = [x.strip() for x in t[4:].split(',')]
        cur.append((p[0], p[2], p[3]))       # name, environment, landmark

assert len(dim_groups) == len(map_groups), (len(dim_groups), len(map_groups))
rows = []
for (gn, dims), (gn2, mps) in zip(dim_groups, map_groups):
    assert len(dims) == len(mps), (gn, gn2, len(dims), len(mps))
    for (cname, w, h), (mname, env, lm) in zip(dims, mps):
        rows.append(dict(const=cname, name=mname, w=w, h=h, env=env, lm=lm))
print(f"joined {len(rows)} maps across {len(rows and dim_groups)} groups\n")

def region(lm):
    i = lm_idx.get(lm)
    if i is None or lm == 'LANDMARK_SPECIAL': return 'SPECIAL'
    return 'Kanto' if i >= kanto_start else 'Johto'

OUTDOOR = {'TOWN', 'ROUTE'}
SQM_PER_SQMI = 2589988.110336

# 1 block = 4x4 background tiles (32x32 px) = 2x2 walkable steps (16x16 px each)
for r in rows:
    r['blocks'] = r['w'] * r['h']
    r['walk_tiles'] = r['blocks'] * 4
    r['region'] = region(r['lm'])

print("=== outdoor maps with SPECIAL landmark (need manual check) ===")
for r in rows:
    if r['env'] in OUTDOOR and r['region'] == 'SPECIAL':
        print(f"  {r['const']:<34} {r['w']:>3}x{r['h']:<3} {r['lm']}")

print("\n=== TOTALS (surface / outdoor only: TOWN + ROUTE) ===")
for reg in ('Johto', 'Kanto'):
    sub = [r for r in rows if r['env'] in OUTDOOR and r['region'] == reg]
    t = sum(r['walk_tiles'] for r in sub)
    print(f"{reg:<6} {len(sub):>3} maps  {sum(r['blocks'] for r in sub):>6} blocks  "
          f"{t:>8} tiles(=m^2)  {t/SQM_PER_SQMI:9.5f} sq mi  ({t/1e6:.4f} km^2)")

print("\n=== TOTALS (every map incl. interiors, caves, gates) ===")
for reg in ('Johto', 'Kanto', 'SPECIAL'):
    sub = [r for r in rows if r['region'] == reg]
    t = sum(r['walk_tiles'] for r in sub)
    print(f"{reg:<8} {len(sub):>3} maps  {t:>8} tiles(=m^2)  {t/SQM_PER_SQMI:9.5f} sq mi")

print("\n=== largest outdoor maps ===")
for r in sorted([x for x in rows if x['env'] in OUTDOOR], key=lambda x: -x['blocks'])[:8]:
    print(f"  {r['const']:<28} {r['w']:>3}x{r['h']:<3} blocks = {r['w']*2:>3}x{r['h']*2:<3} tiles  {r['region']}")
