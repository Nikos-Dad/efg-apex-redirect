layers  = open('layers.svg').read()
overlay = open('overlay.svg').read()

HTML = r'''<title>Madison Isthmus Survey</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo+Narrow:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap">
<style>
:root{
  --paper:#E9EDEF; --panel:#F5F8F9; --ink:#16252C; --ink2:#516B74; --rule:#C7D3D8;
  --water:#A6C6D6; --waterEdge:#6F9FB6; --waterInk:#37697F;
  --green:#C7D6B6; --preserve:#A6BE90; --preserveEdge:#7C9A66; --presInk:#4B6839;
  --road:#CFD7DB; --roadHi:#AEBCC3; --rail:#B7C3C8;
  --core:#C0421F; --coreFill:rgba(192,66,31,.10);
  --annex:#63509A; --annexFill:rgba(99,80,154,.11);
  --shadow:0 1px 2px rgba(22,37,44,.07),0 8px 26px -14px rgba(22,37,44,.28);
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --paper:#0D1418; --panel:#141F24; --ink:#DBE6EA; --ink2:#8AA2AB; --rule:#25353C;
  --water:#1D3D4A; --waterEdge:#3A6A79; --waterInk:#83B8CC;
  --green:#25352A; --preserve:#2E4332; --preserveEdge:#4B6A4F; --presInk:#9CBE8D;
  --road:#22313A; --roadHi:#35484F; --rail:#2A3941;
  --core:#F2734B; --coreFill:rgba(242,115,75,.13);
  --annex:#A48DDC; --annexFill:rgba(164,141,220,.14);
  --shadow:0 1px 2px rgba(0,0,0,.5),0 10px 30px -16px rgba(0,0,0,.8);
}}
:root[data-theme="dark"]{
  --paper:#0D1418; --panel:#141F24; --ink:#DBE6EA; --ink2:#8AA2AB; --rule:#25353C;
  --water:#1D3D4A; --waterEdge:#3A6A79; --waterInk:#83B8CC;
  --green:#25352A; --preserve:#2E4332; --preserveEdge:#4B6A4F; --presInk:#9CBE8D;
  --road:#22313A; --roadHi:#35484F; --rail:#2A3941;
  --core:#F2734B; --coreFill:rgba(242,115,75,.13);
  --annex:#A48DDC; --annexFill:rgba(164,141,220,.14);
  --shadow:0 1px 2px rgba(0,0,0,.5),0 10px 30px -16px rgba(0,0,0,.8);
}
*{box-sizing:border-box}
body{background:var(--paper);color:var(--ink);
  font-family:"Source Serif 4",Georgia,serif;font-size:16px;line-height:1.6;
  -webkit-font-smoothing:antialiased;padding:0}
.wrap{max-width:1120px;margin:0 auto;padding:34px 22px 70px;display:flex;flex-direction:column;gap:30px}
h1,h2,h3,.ui{font-family:"Archivo Narrow",Arial Narrow,sans-serif}
.mono{font-family:"IBM Plex Mono",ui-monospace,monospace}

/* ---- masthead ---- */
.mast{display:flex;flex-direction:column;gap:11px;border-bottom:2px solid var(--ink);padding-bottom:16px}
.eyebrow{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.18em;
  text-transform:uppercase;color:var(--core);font-weight:500}
h1{font-size:clamp(34px,6vw,58px);line-height:.96;margin:0;font-weight:700;
  letter-spacing:-.015em;text-wrap:balance}
.deck{margin:0;max-width:64ch;color:var(--ink2);font-size:17px}
.meta{display:grid;grid-template-columns:repeat(auto-fit,minmax(158px,1fr));gap:1px;
  background:var(--rule);border:1px solid var(--rule);margin-top:5px}
.meta div{background:var(--panel);padding:9px 11px}
.meta dt{font-family:"IBM Plex Mono",monospace;font-size:9.5px;letter-spacing:.13em;
  text-transform:uppercase;color:var(--ink2);margin:0 0 3px}
.meta dd{margin:0;font-family:"IBM Plex Mono",monospace;font-size:12.5px;font-weight:500;
  font-variant-numeric:tabular-nums}

/* ---- map ---- */
.mapwrap{border:1px solid var(--rule);background:var(--panel);box-shadow:var(--shadow)}
.bar{display:flex;flex-wrap:wrap;gap:6px;align-items:center;padding:10px 12px;
  border-bottom:1px solid var(--rule)}
.bar .lbl{font-family:"IBM Plex Mono",monospace;font-size:10px;letter-spacing:.13em;
  text-transform:uppercase;color:var(--ink2);margin-right:3px}
button.chip{font-family:"Archivo Narrow",sans-serif;font-size:13px;font-weight:600;
  padding:4px 11px;border:1px solid var(--rule);background:var(--paper);color:var(--ink2);
  cursor:pointer;border-radius:2px;transition:background .13s,color .13s,border-color .13s}
button.chip[aria-pressed="true"]{background:var(--ink);color:var(--paper);border-color:var(--ink)}
button.chip:hover{border-color:var(--ink2)}
button.chip:focus-visible{outline:2px solid var(--core);outline-offset:2px}
.mapscroll{overflow-x:auto}
svg.map{display:block;width:100%;min-width:640px;height:auto;background:var(--paper)}

/* map lettering */
.map text{font-family:"Archivo Narrow",sans-serif;paint-order:stroke;
  stroke:var(--paper);stroke-width:2.6px;stroke-linejoin:round}
.water-lbl{font-size:12.5px;font-style:italic;letter-spacing:.22em;fill:var(--waterInk);
  text-anchor:middle;font-weight:500}
.water-lbl-sm{font-size:8.5px;letter-spacing:.16em;opacity:.85}
.pres-lbl{font-size:9px;fill:var(--presInk);text-anchor:middle;font-weight:600;letter-spacing:.02em}
.park-lbl{font-size:8px;fill:var(--presInk);text-anchor:middle;opacity:.8}
.lm-lbl{font-size:9.5px;font-weight:600;fill:var(--ink);dominant-baseline:middle}
.lm-out{fill:var(--ink2);font-weight:500}
.dot{stroke:var(--paper);stroke-width:1.3}
.dot-core{fill:var(--core)} .dot-annex{fill:var(--annex)}
.dot-out{fill:none;stroke:var(--ink2);stroke-width:1.5}
.core-fill{fill:var(--coreFill);stroke:none}
.core-line{fill:none;stroke:var(--core);stroke-width:2}
.annex-fill{fill:var(--annexFill);stroke:none}
.annex-line{fill:none;stroke:var(--annex);stroke-width:1.6;stroke-dasharray:7 4}
.axis{stroke:var(--core);stroke-width:.8;stroke-dasharray:2 5;opacity:.6}
.axis-lbl{font-size:8px;fill:var(--core);letter-spacing:.1em;text-anchor:middle;opacity:.9}
.sb-a{fill:var(--ink)} .sb-b{fill:var(--paper);stroke:var(--ink);stroke-width:.8}
.sb-t{font-family:"IBM Plex Mono",monospace;font-size:8px;fill:var(--ink2);stroke:none}
.northarrow path{fill:var(--ink)}
/* layer toggles */
.hide-roads #roads,.hide-roads #major,.hide-roads #rail{display:none}
.hide-parks #parks,.hide-parks .park-lbl{display:none}
.hide-core .core-fill,.hide-core .core-line,.hide-core .axis,.hide-core .axis-lbl{display:none}
.hide-annex .annex-fill,.hide-annex .annex-line{display:none}
.hide-out .dot-out,.hide-out .lm-out{display:none}

/* ---- legend ---- */
.legend{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:9px 20px;
  padding:12px;border-top:1px solid var(--rule);font-size:13.5px}
.legend div{display:flex;gap:9px;align-items:baseline}
.key{width:15px;height:11px;flex:none;border:1px solid var(--rule);position:relative;top:1px}
.k-core{background:var(--coreFill);border:2px solid var(--core)}
.k-annex{background:var(--annexFill);border:1.6px dashed var(--annex)}
.k-pres{background:var(--preserve);border-color:var(--preserveEdge)}
.k-park{background:var(--green);border-color:var(--preserveEdge)}
.k-water{background:var(--water);border-color:var(--waterEdge)}
.k-dot{width:9px;height:9px;border-radius:50%;background:var(--core);border:none;margin:0 3px}
.k-hollow{width:9px;height:9px;border-radius:50%;background:none;border:1.6px solid var(--ink2);margin:0 3px}

/* ---- prose + tables ---- */
section h2{font-size:13px;letter-spacing:.15em;text-transform:uppercase;margin:0 0 3px;
  color:var(--core);font-weight:700}
section > p:first-of-type{margin-top:0}
p{max-width:66ch}
table{width:100%;border-collapse:collapse;font-size:14px;margin-top:10px}
th,td{text-align:left;padding:8px 11px;border-bottom:1px solid var(--rule);vertical-align:top}
th{font-family:"Archivo Narrow",sans-serif;font-size:11px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--ink2);font-weight:600;border-bottom:1.5px solid var(--ink)}
td.n{font-family:"IBM Plex Mono",monospace;font-variant-numeric:tabular-nums;
  white-space:nowrap;font-size:13px}
.tag{font-family:"Archivo Narrow",sans-serif;font-size:11px;font-weight:600;padding:1px 7px;
  border-radius:2px;letter-spacing:.03em;white-space:nowrap}
.t-core{background:var(--coreFill);color:var(--core);box-shadow:inset 0 0 0 1px var(--core)}
.t-annex{background:var(--annexFill);color:var(--annex);box-shadow:inset 0 0 0 1px var(--annex)}
.t-out{color:var(--ink2);box-shadow:inset 0 0 0 1px var(--rule)}
.scroller{overflow-x:auto}
.cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(272px,1fr));gap:20px}
.note{border-left:2.5px solid var(--core);padding:2px 0 2px 15px;margin:0}
.note p{margin:0 0 7px}
.note p:last-child{margin:0}
ul{padding-left:19px;margin:8px 0;max-width:64ch}
li{margin-bottom:6px}
strong{font-weight:600}
code{font-family:"IBM Plex Mono",monospace;font-size:.88em;background:var(--panel);
  padding:1px 4px;border:1px solid var(--rule);border-radius:2px}
footer{border-top:1px solid var(--rule);padding-top:14px;color:var(--ink2);font-size:13px}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
</style>

<div class="wrap">
<header class="mast">
  <div class="eyebrow">Field survey · region reconnaissance</div>
  <h1>Madison Isthmus Survey</h1>
  <p class="deck">Real geography for a Gold/Silver-scale region built on Madison, Wisconsin — drawn from
  OpenStreetMap, with the proposed playfield boundary laid over it. Everything here is the actual city;
  no game geometry has been invented yet.</p>
  <dl class="meta">
    <div><dt>Projection</dt><dd>Equirect., lat₀ 43.0747</dd></div>
    <div><dt>Origin</dt><dd>State Capitol dome</dd></div>
    <div><dt>Sheet</dt><dd>6.21 × 4.66 mi</dd></div>
    <div><dt>Core footprint</dt><dd>2.64 mi²</dd></div>
    <div><dt>With annexes</dt><dd>5.66 mi²</dd></div>
    <div><dt>Sources</dt><dd>OSM · Overpass</dd></div>
  </dl>
</header>

<div class="mapwrap">
  <div class="bar">
    <span class="lbl">Layers</span>
    <button class="chip" aria-pressed="true" data-t="core">Core corridor</button>
    <button class="chip" aria-pressed="true" data-t="annex">Annex lobes</button>
    <button class="chip" aria-pressed="true" data-t="out">Out-of-bounds pins</button>
    <button class="chip" aria-pressed="true" data-t="parks">Parks</button>
    <button class="chip" aria-pressed="true" data-t="roads">Roads &amp; rail</button>
  </div>
  <div class="mapscroll">
  <svg class="map" id="map" viewBox="0 0 1000 750" role="img"
       aria-label="Map of Madison, Wisconsin showing Lakes Mendota, Monona and Wingra, the UW Arboretum and Lakeshore Nature Preserve, with a proposed 2.2 by 1.2 mile game-region corridor along the isthmus and two annexed greenspace lobes.">
__LAYERS__
<g id="overlay">
__OVERLAY__
</g>
  </svg>
  </div>
  <div class="legend">
    <div><span class="key k-core"></span><span><strong>Core corridor</strong> — 2.2 × 1.2 mi, on the isthmus axis</span></div>
    <div><span class="key k-annex"></span><span><strong>Annex lobes</strong> — your two must-have clusters</span></div>
    <div><span class="key k-pres"></span><span>Nature preserve (real OSM boundary)</span></div>
    <div><span class="key k-park"></span><span>City park</span></div>
    <div><span class="key k-water"></span><span>Open water</span></div>
    <div><span class="key k-dot"></span><span>Anchor inside the footprint</span></div>
    <div><span class="key k-hollow"></span><span>Anchor left outside</span></div>
  </div>
</div>

<section>
  <h2>Why this shape</h2>
  <p>Madison's isthmus runs <strong>73° from north</strong> — Bascom Hall to Olbrich Gardens is a 3.61-mile
  strip pinched between two lakes. That is already a Pokémon route: a long, thin corridor with hard water
  edges on both flanks and no way to leave it except through gated crossings. The corridor drawn above is
  rotated onto that axis rather than squared to north, which is why it catches nine anchors in 2.64 mi²
  where a north-up box of the same area catches four.</p>
  <div class="note">
    <p><strong>The conflict worth knowing about.</strong> A strict 1 × 1 mile box on the Capitol — the size
    you first asked for — holds Capitol Square, State Street, Monona Terrace and James Madison Park, and
    nothing else. Bascom Hall is 1.04 mi out, Picnic Point 2.23 mi, Olbrich 2.66 mi, the Arboretum 3.01 mi.
    Campus begins roughly where that box ends.</p>
  </div>
</section>

<section>
  <h2>Anchor inventory</h2>
  <p>Distances are straight-line from the Capitol dome. <em>u</em> is displacement along the isthmus axis,
  <em>v</em> across it — the coordinate system the corridor is cut in.</p>
  <div class="scroller">
  <table>
    <thead><tr><th>Anchor</th><th>Distance</th><th>u / v (m)</th><th>Status</th><th>Why it matters</th></tr></thead>
    <tbody>
      <tr><td>Capitol Square</td><td class="n">0.00 mi</td><td class="n">0 / +4</td><td><span class="tag t-core">core</span></td><td>Natural central hub; the one place every route can radiate from</td></tr>
      <tr><td>Monona Terrace</td><td class="n">0.28 mi</td><td class="n">+184 / −414</td><td><span class="tag t-core">core</span></td><td>Frank Lloyd Wright lakefront deck — the south-shore gateway</td></tr>
      <tr><td>State Street</td><td class="n">0.42 mi</td><td class="n">−625 / +267</td><td><span class="tag t-core">core</span></td><td>A ready-made pedestrian route corridor, Capitol to campus</td></tr>
      <tr><td>Memorial Union</td><td class="n">0.78 mi</td><td class="n">−1124 / +550</td><td><span class="tag t-core">core</span></td><td>Terrace on Mendota; the obvious Surf launch point</td></tr>
      <tr><td>Bascom Hall</td><td class="n">1.04 mi</td><td class="n">−1572 / +580</td><td><span class="tag t-core">core</span></td><td>Real elevation — a hill climb, so a natural gated ascent</td></tr>
      <tr><td>Union South</td><td class="n">1.23 mi</td><td class="n">−1967 / +225</td><td><span class="tag t-core">core</span></td><td>West campus counterweight to Memorial Union</td></tr>
      <tr><td>Henry Vilas Zoo</td><td class="n">1.46 mi</td><td class="n">−2339 / −268</td><td><span class="tag t-core">core</span></td><td>A free zoo. Hard to imagine a better in-world creature facility</td></tr>
      <tr><td>Camp Randall</td><td class="n">1.47 mi</td><td class="n">−2364 / +159</td><td><span class="tag t-core">core</span></td><td>80,000-seat bowl; reads as an arena without any redesign</td></tr>
      <tr><td>James Madison Park</td><td class="n">0.55 mi</td><td class="n">+786 / +414</td><td><span class="tag t-core">core</span></td><td>North-shore beach; the corridor's east shoulder</td></tr>
      <tr><td>Picnic Point</td><td class="n">2.23 mi</td><td class="n">−2642 / +2436</td><td><span class="tag t-annex">annex</span></td><td>Wooded peninsula with effigy mounds — the strongest route material on the sheet</td></tr>
      <tr><td>Lake Wingra</td><td class="n">2.34 mi</td><td class="n">−3578 / −1187</td><td><span class="tag t-annex">annex</span></td><td>A third, small, spring-fed lake — different water from the two big ones</td></tr>
      <tr><td>UW Arboretum</td><td class="n">3.01 mi</td><td class="n">−4173 / −2464</td><td><span class="tag t-annex">annex</span></td><td>1,200 acres: tallgrass prairie, oak savanna, restored woods</td></tr>
      <tr><td>Tenney Park / Yahara Locks</td><td class="n">1.49 mi</td><td class="n">+2138 / +1075</td><td><span class="tag t-out">out</span></td><td>The lock system physically joining Mendota to Monona — a real loss</td></tr>
      <tr><td>Olbrich Gardens</td><td class="n">2.66 mi</td><td class="n">+4236 / +585</td><td><span class="tag t-out">out</span></td><td>Botanical gardens and Thai pavilion; strong, but far east</td></tr>
      <tr><td>Olin Park / Turville Point</td><td class="n">1.37 mi</td><td class="n">−227 / −2186</td><td><span class="tag t-out">out</span></td><td>South-shore woods with the skyline view back across Monona</td></tr>
    </tbody>
  </table>
  </div>
</section>

<section>
  <h2>The annex problem, and the fix</h2>
  <div class="cols">
    <div>
      <p>The two clusters you marked non-negotiable do not sit inside the corridor. The Arboretum and Lake
      Wingra hang <strong>south-west</strong>, off-axis; Picnic Point juts <strong>north</strong> into
      Mendota. Drawn honestly on real ground, they are separate lobes — the dashed boxes.</p>
      <p>Held literally, the footprint grows from 2.64 mi² to 5.66 mi², and at a Johto-sized tile budget
      that is about 10 real metres per tile: a house becomes one tile, and the city stops being legible.</p>
    </div>
    <div>
      <p>Better than folding: keep the corridor tight and reach the lobes as <strong>off-grid maps</strong> —
      separate areas entered through a transition rather than stitched into the same grid. Picnic Point by
      boat from the Union; the Arboretum by paddling Monona Bay into Wingra Creek.</p>
      <p>Gold/Silver does exactly this. Measured from the disassembly, Johto and Kanto are two
      <em>disconnected</em> components of the map graph — 31 and 35 outdoor maps that never touch, joined
      only through cave interiors. Off-grid lobes are native to the engine, and they cost the corridor
      no area at all.</p>
    </div>
  </div>
</section>

<section>
  <h2>Proposed gym siting</h2>
  <p>A first pass, tuned against Gold/Silver's own curve — Johto's aces run
  <span class="mono">9 · 16 · 20 · 25 · 30 · 35 · 31 · 40</span>, with the deliberate regression at seven.
  The Capitol is deliberately <em>not</em> a gym: four equal wings make it the League, one wing per Elite
  Four member, with the Champion on the dome observation deck.</p>
  <div class="scroller">
  <table>
    <thead><tr><th>#</th><th>Site</th><th>Type</th><th>Ace</th><th>Grants</th><th>Why there</th></tr></thead>
    <tbody>
      <tr><td class="n">1</td><td>Bascom Hall</td><td>Flying</td><td class="n">Lv 9</td><td>Flash</td><td>The only real hill; trainers tier by altitude</td></tr>
      <tr><td class="n">2</td><td>Overture Center</td><td>Fairy</td><td class="n">Lv 16</td><td>Cut</td><td>Five nested halls; first hard gate</td></tr>
      <tr><td class="n">3</td><td>Capitol Square market</td><td>Normal</td><td class="n">Lv 20</td><td>Strength (permission)</td><td>The Whitney spike, sited where a stuck player has the most alternatives</td></tr>
      <tr><td class="n">4</td><td>Central Library</td><td>Ghost</td><td class="n">Lv 25</td><td>Surf</td><td>Normal→Ghost two blocks apart; opens the map at the hub</td></tr>
      <tr><td class="n">5</td><td>James Madison Park</td><td>Fighting</td><td class="n">Lv 30</td><td>Portage</td><td>Boathouse and courts; north lane of a two-lane branch</td></tr>
      <tr><td class="n">6</td><td>Monona Terrace</td><td>Psychic</td><td class="n">Lv 35</td><td>— none —</td><td>The Jasmine slot: refuses to battle until you fetch the 1938 drawings</td></tr>
      <tr><td class="n">7</td><td>Tenney Park locks</td><td>Ice</td><td class="n">Lv 31</td><td>Whirlpool</td><td>The Pryce regression; frozen lagoon as sliding-ice maze</td></tr>
      <tr><td class="n">8</td><td>Machinery Row</td><td>Steel</td><td class="n">Lv 40</td><td>Waterfall</td><td>Approach consumes every tool you own — the road to Clair</td></tr>
    </tbody>
  </table>
  </div>
  <p>Constraints held: no starter type gets a gym, no two adjacent gyms share an answer, one new biome per
  gym, and settlement scale zig-zags village → strip → metropolis → single building → neighbourhood →
  megastructure → village → district. Note this puts <strong>gyms 7 and 8 outside the current corridor</strong>,
  at Tenney and Machinery Row — the strongest argument yet for extending east.</p>
</section>

<section>
  <h2>Settled so far</h2>
  <div class="scroller">
  <table>
    <thead><tr><th>Decision</th><th>Value</th><th>Consequence</th></tr></thead>
    <tbody>
      <tr><td>Tile budget</td><td class="n">470 × 270</td><td>~35,000 walkable tiles, identical to Johto's outdoor grid</td></tr>
      <tr><td>Real footprint</td><td class="n">2.2 × 1.2 mi</td><td>2.64 mi² core, rotated to the 73° isthmus axis</td></tr>
      <tr><td>Compression</td><td class="n">~7.5 m/tile</td><td>Across the core corridor's long axis at that budget</td></tr>
      <tr><td>Fidelity</td><td>Recognizable, rearranged</td><td>Bearings may bend; landmark identity and order may not</td></tr>
      <tr><td>Must-haves</td><td>Arboretum + Wingra + Vilas; Picnic Point</td><td>Folded in as annexes, not reproduced in place</td></tr>
      <tr><td>Gyms</td><td class="n">8</td><td>Not yet sited — next decision</td></tr>
    </tbody>
  </table>
  </div>
</section>

<section>
  <h2>Open questions for whoever picks this up</h2>
  <ul>
    <li><strong>Tenney Park and the Yahara locks are currently outside the line.</strong> They are the only
    place where Mendota and Monona physically connect, which makes them the most natural
    Surf/Whirlpool gate in the whole city. Extending the corridor east costs roughly 0.4 mi² and drops
    something on the west end.</li>
    <li><strong>Does the Capitol become the final gym or the villain's tower?</strong> It cannot be both, and
    the answer reorders the whole progression.</li>
    <li><strong>Which lobes are off-grid, and what's the transition?</strong> Boat, trail pass, or lock
    passage each imply a different badge gate and a different point in the progression.</li>
    <li><strong>Winter.</strong> Both lakes freeze solid and locals walk across them. That is a traversal
    mechanic Pokémon has never had, and it is sitting right there.</li>
  </ul>
</section>

<footer>
  Base geometry © OpenStreetMap contributors (ODbL), retrieved via Overpass. Lake, park, preserve, road and
  river outlines are unmodified OSM data; the corridor, annex boxes and isthmus axis are proposals drawn on
  top. Anchor coordinates are approximate centroids.
</footer>
</div>

<script>
(function(){
  var map = document.getElementById('map');
  document.querySelectorAll('button.chip').forEach(function(b){
    b.addEventListener('click', function(){
      var on = b.getAttribute('aria-pressed') === 'true';
      b.setAttribute('aria-pressed', String(!on));
      map.classList.toggle('hide-' + b.dataset.t, on);
    });
  });
})();
</script>
'''
HTML = HTML.replace('__LAYERS__', layers).replace('__OVERLAY__', overlay)
open('madison-isthmus-survey.html','w').write(HTML)
print("written:", len(HTML), "bytes")
