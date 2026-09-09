# Madison Region — Pokémon-style game map, design handoff

> **This directory is unrelated to the apex-redirect site in this repo.** It lives on a
> scratch branch only because that is where the working session was pinned. Do not merge
> it into `main`; the redirect site is `index.html` / `404.html` / `CNAME` at the repo root
> and nothing here touches it.

Working notes for a Pokémon Gold/Silver-style game with 8 gyms, set in Madison, Wisconsin.
Everything below is either measured from primary sources or an explicitly-flagged proposal.

**Published survey map:** https://claude.ai/code/artifact/acee6a15-02c3-4f6a-8244-702a31c1faf5
(same content as `survey-map.html`)

---

## 1. Where this stands

Real-world reconnaissance is **done**: the region is measured, the footprint is drawn on
actual OpenStreetMap geometry, and the scale question is settled. No game geometry has been
authored yet — no tile maps, no routes.

A research pass (7 parallel web surveys, 153 landmarks, plus a synthesis) has since produced
`design-brief.md`: a full first-pass proposal covering seven biomes, the twenty locations that
must survive, **eight sited gyms with types and level curve**, badge-gated traversal mapped onto
real barriers, and a risk list. It is proposal, not measurement — read its provenance header.

Two things from that pass are worth knowing immediately:

- It independently converged on **essentially this exact footprint** (6.8 km² vs. the 6.84 km²
  already drawn here), which is decent evidence the corridor is right.
- It **supersedes the "fold the lobes" plan** in §5 with a better one. See below.

---

## 2. Decisions already made

These came from the person driving the project. Treat them as settled unless they say otherwise.

| Decision | Value | Notes |
|---|---|---|
| Tile budget | **470 × 270 grid, ~35,000 walkable tiles** | Deliberately identical to Johto's outdoor grid |
| Real footprint | **2.2 × 1.2 mi**, rotated to the isthmus axis | 2.64 mi² core |
| Fidelity | **Recognizable but rearranged** | Bearings may bend; landmark identity and travel order may not |
| Must-have greenspace | UW Arboretum + Lake Wingra + Vilas Zoo; Picnic Point + Lakeshore Nature Preserve | Both fall **outside** the core corridor — see §5 |
| Gyms | 8 | Not yet sited |

The original ask was "1 mile × 1 mile or slightly smaller." That was relaxed once the
measurements showed a 1 mi² box on the Capitol excludes the entire university.

---

## 3. Gold/Silver reference measurements

Derived from the [`pret/pokegold`](https://github.com/pret/pokegold) disassembly, not from
fan estimates. Regenerate with `gen2/fetch.sh` then the scripts beside it.

**Unit chain:** 1 block = 4×4 background tiles (32×32 px) = **2×2 walkable tiles** of 16×16 px.
Confirmed by screen geometry — the Game Boy's 160×144 screen is exactly 10×9 walkable tiles,
and a Pokémon Center interior (5×4 blocks) is exactly one screen wide.

**Scale convention:** 1 walkable tile ≈ 1 metre. Sanity checks: doors are 1 m wide, a Pokémon
Center is 10×8 m, a house footprint is 8×8 m. This is a convention, not canon — at 1 yard/tile
everything shrinks ~16%.

| Metric | Johto | Kanto |
|---|---|---|
| Outdoor maps | 34 | 39 (41 counting Routes 26–27) |
| Walkable tiles (= m²) | 36,720 | 32,220 |
| Area | 0.0142 mi² (9.07 acres) | 0.0124 mi² (7.96 acres) |
| Connected grid bounding box | 235 × 135 blocks = **470 × 270 tiles** | 140 × 135 blocks = 280 × 270 tiles |
| Stacked total X (sum of widths) | 1,120 m | 1,250 m |
| Stacked total Y (sum of heights) | 1,206 m | 1,062 m |

Both regions total ~0.028 mi² of walkable outdoor surface — about 18 acres, roughly a seventh
of Vatican City. Johto is portrait (1,120 × 1,206), Kanto is landscape (1,250 × 1,062), and
their total linear extent differs by only 0.6%.

**Method notes.** Outdoor = `TOWN` + `ROUTE` environments in `data/maps/maps.asm`. Region split
at the `KANTO_LANDMARK` marker in `constants/landmark_constants.asm`. `NATIONAL_PARK_BUG_CONTEST`
(a duplicate of National Park) and `SAFARI_ZONE_BETA` (cut content) are excluded. Map coordinates
were reconstructed by BFS over the `connection` macros in `data/maps/attributes.asm`: Johto placed
31 maps with **zero** inconsistencies, Kanto placed 35 with one genuine 1-block asymmetry in the
Celadon↔Route 7 pair (a quirk in the shipped data, not a parse error).

**Caveat:** these are map *extents*. Some tiles inside them are water, cliff or tree border you
cannot stand on, so the true walkable count is lower. Filtering by real passability would mean
decoding each map's `.blk` layout against its tileset collision attributes — not yet done.

---

## 4. Madison geometry

Origin for all local coordinates is the **Wisconsin State Capitol dome (43.0747 N, 89.3842 W)**.
Projection is equirectangular about that latitude; `scripts/geo.py` is the single source of truth.

**The defining fact:** Madison's isthmus runs **73° from north**. Bascom Hall → Olbrich Gardens
is a 3.61 mi strip pinched between Lake Mendota and Lake Monona. It is already a Pokémon route —
a long thin corridor with hard water edges and no exit except through gated crossings. The
corridor is cut in a rotated frame: `u` = along that axis, `v` = across it.

| Anchor | From Capitol | u / v (m) | Status |
|---|---|---|---|
| Capitol Square | 0.00 mi | 0 / +4 | core |
| Monona Terrace | 0.28 mi | +184 / −414 | core |
| State Street | 0.42 mi | −625 / +267 | core |
| James Madison Park | 0.55 mi | +786 / +414 | core |
| Memorial Union | 0.78 mi | −1124 / +550 | core |
| Bascom Hall | 1.04 mi | −1572 / +580 | core |
| Union South | 1.23 mi | −1967 / +225 | core |
| Henry Vilas Zoo | 1.46 mi | −2339 / −268 | core |
| Camp Randall | 1.47 mi | −2364 / +159 | core |
| Picnic Point | 2.23 mi | −2642 / +2436 | **annex** |
| Lake Wingra | 2.34 mi | −3578 / −1187 | **annex** |
| UW Arboretum | 3.01 mi | −4173 / −2464 | **annex** |
| Tenney Park / Yahara Locks | 1.49 mi | +2138 / +1075 | out |
| Olbrich Gardens | 2.66 mi | +4236 / +585 | out |
| Olin Park / Turville Point | 1.37 mi | −227 / −2186 | out |

**Why rotated:** the 2.64 mi² corridor on the isthmus axis catches **nine** anchors. A north-up
box of the same area centred on the Capitol catches **four**.

**Compression:** 3,540 m along the core's long axis over 470 tiles ≈ **7.5 real m per tile**.
Held literally with both annexes (5.66 mi²) it degrades to ~10 m/tile, at which point a house is
one tile and the city stops being legible. Hence §5.

---

## 4b. Proposed gym siting (first pass)

From `design-brief.md`, tuned against Johto's own curve (aces 9 / 16 / 20 / 25 / 30 / 35 / 31 / 40,
with the deliberate regression at seven). **The Capitol is not a gym — it is the League**, four equal
wings for four Elite Four members, Champion on the dome observation deck.

| # | Site | Type | Ace | Grants |
|---|---|---|---|---|
| 1 | Bascom Hall | Flying | 9 | Flash |
| 2 | Overture Center | Fairy | 16 | Cut |
| 3 | Capitol Square market | Normal | 20 | Strength (permission only) |
| 4 | Central Library | Ghost | 25 | Surf |
| 5 | James Madison Park | Fighting | 30 | Portage |
| 6 | Monona Terrace | Psychic | 35 | *nothing* |
| 7 | Tenney Park locks | Ice | 31 | Whirlpool |
| 8 | Machinery Row | Steel | 40 | Waterfall |

Constraints held: no starter type gets a gym, no two adjacent gyms share an answer, one new biome
per gym, settlement scale zig-zags. **Gyms 7 and 8 sit outside the current corridor** — see §7.1.

No Fly, deliberately: if you can fly, the isthmus stops being an isthmus and every chokepoint
evaporates. Fast travel is the State Street bus and the bike-path network instead.

---

## 5. The unresolved annex problem

The two must-have clusters **are not inside the chosen corridor**, and this is the single most
important open item.

- The **Arboretum and Lake Wingra** hang south-west, off-axis.
- **Picnic Point** juts north into Lake Mendota.

Drawn honestly on real ground they are separate lobes (the dashed boxes on the map: 2.47 mi² and
0.55 mi²).

**Current best answer — off-grid lobes, not grid extensions.** Keep the corridor tight and reach
the lobes as *separate maps* entered through a transition: Picnic Point by boat from the Union;
the Arboretum by paddling Monona Bay into Wingra Creek, gated behind a trail pass; Olbrich east
through the Yahara lock (the Blackthorn-behind-the-Ice-Path shape).

This costs the corridor **no area at all**, and it is exactly how the engine already works.
Measured from the disassembly: Johto and Kanto are two *disconnected components* of Gold/Silver's
map graph — 31 and 35 outdoor maps that never touch, joined only through cave interiors. Off-grid
lobes are native to the format.

*(An earlier plan here was to fold the lobes onto the corridor axis so the Arboretum swung from
south-west to west. That works but breaks a real adjacency for no benefit the off-grid approach
doesn't give free. Superseded.)*

---

## 6. Files

```
survey-map.html      the published survey map, self-contained (fonts from Google Fonts)
design-brief.md      first-pass design proposal: biomes, 8 sited gyms, traversal, risks
geographic-bounds.md corner coordinates, bboxes and WKT for the corridor and both annexes
data/
  *.json.gz          raw OSM extracts: water, park, road, named (Arboretum + Lakeshore Preserve)
  surveys.json       153 researched landmarks with character notes and per-site game ideas
  footprint.geojson  the corridor and annex polygons, ready for any GIS or map tool
  q_*.ql             the exact Overpass queries used
  meta.json          derived SVG-space geometry: footprint corners, landmark pins, labels
  fetch.sh           re-pull the OSM data if needed
scripts/
  geo.py             projection, ring stitching, simplification, footprint definition — start here
  render.py          OSM JSON -> layers.svg (parks, preserves, lakes, roads, river)
  overlay.py         footprint boxes, isthmus axis, landmark pins, labels, scale bar
  build.py           inlines both SVGs into the final HTML page
  footprint.py       candidate-footprint comparison and anchor distance table
gen2/
  fetch.sh           pull the pokegold disassembly tables
  calc.py            per-region outdoor area
  stack.py           stacked X/Y extents
  geo3.py            connection-graph BFS -> grid bounding boxes
```

Rebuild the map with: `cd scripts && python3 render.py && python3 overlay.py && python3 build.py`
(expects the `data/*.json` files un-gzipped in the working directory).

---

## 7. Open questions

1. **Extend the corridor east — probably yes.** Tenney Park and the Yahara Locks are outside the
   current line, and they are the only place Mendota and Monona physically connect. The brief's
   gym siting puts **gyms 7 and 8 out there** (Tenney locks, Machinery Row), which makes this the
   most pressing boundary decision. Costs ~0.4 mi²; something on the west end gives way.
2. **Neither, on the Capitol.** The brief argues it should be *the League* rather than a gym or the
   villain's tower — four equal wings, one Elite Four member each, Champion on the dome. That puts
   the endgame at the map's centre instead of its far end, which is unusual and probably right for
   a corridor. Worth accepting or rejecting explicitly.
3. **Which lobes go off-grid, and what is the transition?** Boat, trail pass, or lock passage each
   imply a different badge gate at a different point in the progression.
4. **Winter — commit or cut in preproduction.** Both lakes freeze (median ~105 days) and locals
   walk across them. It disables Surf, opens the lake surface as a walkable tier, and swaps every
   encounter table: effectively a second map. A half-built winter is worse than none.
5. **The mound constraint.** Effigy mounds are burial sites and the isthmus footprint is nearly
   mound-free — one quiet argument for it. Extending west or south inherits an obligation that
   rules out the genre's default treatment of ancient sites entirely. See `design-brief.md` §6.6.

---

## 8. Sources and licensing

- Base geometry © OpenStreetMap contributors, **ODbL** — retrieved via Overpass
  (`overpass.kumi.systems`; `overpass-api.de` was unreliable and repeatedly returned 504).
  Lake, park, preserve, road and river outlines are unmodified OSM data.
- Gold/Silver map tables from the `pret/pokegold` disassembly.
- The corridor, annex boxes and isthmus axis are proposals drawn on top of the real data.
- Anchor coordinates are approximate centroids, except Picnic Point and the Arboretum which are
  real OSM nodes/centroids.
