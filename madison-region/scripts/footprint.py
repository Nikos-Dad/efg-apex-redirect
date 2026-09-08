import math
L = {  # approximate WGS84 centroids of candidate anchors
 'Capitol Square':(43.07474,-89.38421), 'Monona Terrace':(43.07161,-89.38058),
 'State St (mid)':(43.07540,-89.39250), 'Memorial Union':(43.07655,-89.39938),
 'Bascom Hall':(43.07566,-89.40477), 'Union South':(43.07159,-89.40817),
 'Camp Randall':(43.07000,-89.41262), 'Picnic Point tip':(43.08889,-89.42389),
 'Vilas Zoo':(43.06639,-89.41083), 'Lake Wingra':(43.05530,-89.42220),
 'Arboretum VC':(43.04278,-89.42472), 'James Madison Pk':(43.08028,-89.37639),
 'Tenney Park':(43.08944,-89.36278), 'Yahara Locks':(43.09060,-89.36060),
 'Willy St/Schenks':(43.08730,-89.34750), 'Olbrich Gardens':(43.09061,-89.33633),
 'Olin Park':(43.05530,-89.37920), 'Turville Point':(43.05250,-89.37330),
 'Warner Park':(43.11940,-89.35720), 'Gov Nelson SP':(43.13720,-89.42780),
}
LAT0, LON0 = 43.0747, -89.3842                      # Capitol = origin
MPD = 111320.0
def xy(p): return ((p[1]-LON0)*MPD*math.cos(math.radians(LAT0)), (p[0]-LAT0)*MPD)
MI = 1609.344

print("=== distances from Capitol Square ===")
for n,p in L.items():
    x,y = xy(p); print(f"  {n:<18} {math.hypot(x,y)/MI:5.2f} mi   E{x:+7.0f}m N{y:+7.0f}m")

# isthmus axis: Bascom Hall -> Olbrich Gardens
bx,by = xy(L['Bascom Hall']); ox,oy = xy(L['Olbrich Gardens'])
th = math.atan2(oy-by, ox-bx)
print(f"\nisthmus axis bearing = {(90-math.degrees(th))%360:.1f}deg from N "
      f"({math.degrees(th):+.1f}deg above due E), Bascom->Olbrich = {math.hypot(ox-bx,oy-by)/MI:.2f} mi")

FOOT = {
 'A  strict 1.0 x 1.0 mi (Capitol-centred, N-up)': dict(w=1.0,h=1.0,rot=0,cx=0,cy=0),
 'B  isthmus corridor 2.6 x 1.0 mi (rotated)'    : dict(w=2.6,h=1.0,rot=math.degrees(th),cx=None,cy=None),
 'C  wide 3.0 x 2.2 mi (N-up)'                   : dict(w=3.0,h=2.2,rot=0,cx=-900,cy=-1500),
}
print()
for name,f in FOOT.items():
    if f['cx'] is None:   # centre the rotated box on the Bascom->Olbrich midpoint
        cx,cy = (bx+ox)/2,(by+oy)/2
    else: cx,cy = f['cx'],f['cy']
    r = math.radians(f['rot']); hw,hh = f['w']*MI/2, f['h']*MI/2
    inside=[]; out=[]
    for n,p in L.items():
        x,y = xy(p); dx,dy = x-cx, y-cy
        u =  dx*math.cos(-r)-dy*math.sin(-r); v = dx*math.sin(-r)+dy*math.cos(-r)
        (inside if abs(u)<=hw and abs(v)<=hh else out).append(n)
    print(f"--- {name}   area={f['w']*f['h']:.2f} sq mi ---")
    print(f"    IN  ({len(inside)}): {', '.join(inside)}")
    print(f"    OUT ({len(out)}): {', '.join(out)}\n")

print("=== tile budget: Gen 2 Johto grid = 470 x 270 walkable tiles ===")
for name,f in FOOT.items():
    long_m = max(f['w'],f['h'])*MI
    print(f"  {name[:3]} long axis {long_m:6.0f} m over 470 tiles -> {long_m/470:5.2f} real m per tile")
