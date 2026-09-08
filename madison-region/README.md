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
authored yet — no tile maps, no routes, no gym siting. That is the next job.

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

## 5. The unresolved annex problem

The two must-have clusters **are not inside the chosen corridor**, and this is the single most
important open item.

- The **Arboretum and Lake Wingra** hang south-west, off-axis.
- **Picnic Point** juts north into Lake Mendota.

Drawn honestly on real ground they are separate lobes (the dashed boxes on the map: 2.47 mi² and
0.55 mi²). The intended fix is the fidelity setting already chosen — **fold the lobes onto the
corridor's axis** rather than reproduce them in place, so the Arboretum swings from south-west to
west and *extends* the strip instead of widening it. Real bearings bend; identity, adjacency and
travel order survive.

This is standard for the genre: Johto renders Kansai's ~10,000 mi² in 0.05 mi² of map by keeping
about thirty places and discarding the space between them.

**Not yet decided: where the fold seam goes.** Folding the Arboretum lobe west means choosing
which real adjacency to break — Vilas→Wingra, or Wingra→Arboretum.

---

## 6. Files

```
survey-map.html      the published survey map, self-contained (fonts from Google Fonts)
data/
  *.json.gz          raw OSM extracts: water, park, road, named (Arboretum + Lakeshore Preserve)
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

1. **Tenney Park and the Yahara Locks are outside the line.** They are the only place Mendota and
   Monona physically connect, which makes them the most natural Surf/Whirlpool gate in the city.
   Extending the corridor east costs ~0.4 mi² and drops something on the west end.
2. **Is the Capitol the final gym or the villain's tower?** It cannot be both, and the answer
   reorders the whole progression.
3. **Where does the fold seam go?** (§5)
4. **Winter.** Both lakes freeze solid and locals walk across them. That is a traversal mechanic
   the series has never used, and it is sitting right there.
5. **Gym siting and type spread** — completely open. Gen 2's benchmark for comparison: 8 gyms
   spanning Flying/Bug/Normal/Ghost/Fighting/Steel/Ice/Dragon, gating movement through
   Cut/Surf/Strength/Whirlpool/Fly/Waterfall.

---

## 8. Sources and licensing

- Base geometry © OpenStreetMap contributors, **ODbL** — retrieved via Overpass
  (`overpass.kumi.systems`; `overpass-api.de` was unreliable and repeatedly returned 504).
  Lake, park, preserve, road and river outlines are unmodified OSM data.
- Gold/Silver map tables from the `pret/pokegold` disassembly.
- The corridor, annex boxes and isthmus axis are proposals drawn on top of the real data.
- Anchor coordinates are approximate centroids, except Picnic Point and the Arboretum which are
  real OSM nodes/centroids.
