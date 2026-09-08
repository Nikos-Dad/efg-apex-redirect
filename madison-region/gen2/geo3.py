import re, collections
exec(open('geo.py').read().split('def solve')[0])

def fwd(root):
    pos={root:(0,0)}; q=collections.deque([root]); bad=[]
    while q:
        a=q.popleft(); ax,ay=pos[a]; aw,ah=dims[a]
        for d,b,off in conns.get(a,[]):
            bw,bh=dims[b]
            p={'north':(ax+off,ay-bh),'south':(ax+off,ay+ah),
               'west':(ax-bw,ay+off),'east':(ax+aw,ay+off)}[d]
            if b in pos:
                if pos[b]!=p: bad.append((a,d,b,pos[b],p))
            else: pos[b]=p; q.append(b)
    return pos,bad

for root in ('NEW_BARK_TOWN','PALLET_TOWN'):
    pos,bad=fwd(root)
    xs=[pos[m][0] for m in pos]; ys=[pos[m][1] for m in pos]
    w=max(pos[m][0]+dims[m][0] for m in pos)-min(xs); h=max(pos[m][1]+dims[m][1] for m in pos)-min(ys)
    land=sum(dims[m][0]*dims[m][1] for m in pos)
    print(f"\n### from {root}: {len(pos)} maps, {len(bad)} inconsistencies")
    print(f"    bbox {w}x{h} blocks = {w*2}x{h*2} tiles ; land in component = {land} blocks = {land*4} tiles")
    for e in bad: print("    MISMATCH", e)
    print("    maps:", ", ".join(sorted(pos)))
