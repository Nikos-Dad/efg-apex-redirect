> **Provenance and status.** This brief is the synthesised output of a parallel research pass
> (seven web-research agents plus a synthesis pass, 153 landmarks collected). It is **design
> proposal and unverified secondary research**, not measured fact. The measured numbers in
> `README.md` — the Gold/Silver tile counts and the Madison coordinate geometry — come from
> primary sources (the `pret/pokegold` disassembly and OpenStreetMap) and take precedence
> wherever the two disagree.
>
> Spot-checked and correct: the Johto gym ace levels (9/16/20/25/30/35/31/40) match GSC.
> **Known error:** §5 calls for rotating the map "~30° counter-clockwise" to level the isthmus.
> The measured axis is 73.4° from north, so the correct rotation is **16.6°**, not 30°.
> Other specific figures (building heights, ice-duration records, acreages) are agent-sourced
> and should be checked before anything ships.
>
> §6 raises a constraint worth reading before any design work proceeds: effigy mounds are burial
> sites, the Ho-Chunk Nation holds itself descended from the builders, and the genre's default
> "ancient ruin = dungeon to raid" is not usable here.

---

# MADISON REGION — DESIGN BRIEF
### A Johto-scale Pokémon map built on the Yahara isthmus

---

## 0. THE ONE STRUCTURAL FACT

Madison is a **corridor with hard water edges on both sides and one dominant vertical landmark at its center**. A level designer would have to invent this. Lake Mendota (850 ft) to the north, Lake Monona (845 ft) to the south, a 0.6–1.2 mi neck of land between them, the Capitol on the high point in the middle, and a 1990 state law capping every structure within a mile of it at 1,032.8 ft above sea level — so **the dome is visible from essentially every walkable tile on the map.**

That gives you three things almost no real place gives you at once: a permanent wayfinding beacon, a natural act structure (west end → center → east end), and a legally-enforced lore decree ("no tower in the province may rise above the Dome") that doubles as the villain plot when somebody breaks it.

**Design consequence #1:** the isthmus is not the setting, it is the level. Water is not a border, it is the two long walls of the hallway, and every meaningful barrier on this map is either water, a rail embankment, a causeway, or a piece of paperwork.

**Design consequence #2 (the big one):** at Johto's tile budget this map is *barely compressed*. 470 tiles across 3.4 km of isthmus is ~7.3 m/tile — roughly **7:1**, against Kanto's ~120:1 inside cities and ~1,360:1 on rural routes. State Street's real 1.26 km becomes a **172-tile route**, longer than Cycling Road, at *true length*. Madison's problem is therefore the inverse of Kanto's: not what to shrink, but **what to enlarge.** Period Garden Park is ~930 m² — 18 tiles, a 4×4 room. Half your best landmarks are smaller than a Pokémon Center and must be blown up 3–5×. Plan for a non-uniform **expansion** ratio.

---

## 1. THE SEVEN BIOMES

Not decorative — each is a distinct tileset, encounter table, weather behavior, and traversal grammar. Named in map order, west to east.

**1. Glacial drumlin ridge / oak knoll.** *Anchors: Bascom Hill (86 ft of gain over 850 ft of run, ~10% grade), Bascom Hall, Observatory Hill, Muir Woods, Science Hall.* Madison's only real elevation — total campus relief is 155 ft and this is where most of it is concentrated. Mown lawn, allées, sandstone institutional walls, and a steep north-facing back slope dropping into closed forest. Rock/Ground/Flying/Grass. **This biome is scarce and must be spent carefully: it is your only hill.**

**2. Masonry pedestrian canyon.** *Anchors: State Street 100–800, the Overture Center wall, MMoCA's glass prow, the Orpheum marquee.* Eight blocks, dead straight, walled both sides by continuous 3–6 story brick so it reads as a slot canyon. Buskers, bus air-brakes, skateboards on brick. **Plus its shadow layer:** the mid-block service alleys behind 300–400 and the two-entrance basement under the 600 block (record shop + 1998 speakeasy). Normal/Fairy above, Dark/Poison below.

**3. Granite civic plateau.** *Anchors: the Capitol, the 9.5-acre Square, the Concourse ring road, the Municipal Building's Ionic colonnade, the History Center construction pit.* Cold polished stone, four equal wings, four diagonal walks, six radiating avenues, and — on market days — a full 150-stall ring that moves counterclockwise. Steel/Psychic/Normal.

**4. Soft north littoral (Mendota).** *Anchors: James Madison Park (12.63 acres), the 1915 Bernard-Hoover Boathouse, Tenney Park's Prairie-School lagoons, Memorial Union Terrace.* Grass panels, sand beach, low seawall, cottonwoods, sailboats offshore, geese. Warm, green, informal, and it *freezes*. Water/Flying/Bug → Ice in winter.

**5. Hard south littoral (Monona).** *Anchors: Monona Terrace's 68,000 sq ft rooftop cantilevered ~90 ft over the water, Olin Terrace, the John Nolen causeway, Law Park, Monona Bay's near-sealed lobe.* White concrete arcs, curved parapets, glare, wind, no shade, water on three sides. **Ten minutes from biome 4 and visually its exact opposite** — that contrast is free and you should exploit it ruthlessly.

**6. Canal and lock corridor.** *Anchors: the Yahara's one straightened mile with ~11 crossings, the 1904 Tenney Lock (rebuilt 1959 on a capped landfill), the 5 ft head between the lakes.* No-wake, backyard fences on one bank, boulevard lawn on the other, ten bridges in a mile as a built-in metronome. Water/Poison/Steel.

**7. Brick works and rail row.** *Anchors: Machinery Row (601–627 Williamson, 1898–1912, Romanesque, battlemented corner tower AND a conical turret — a castle silhouette at both ends), Third Lake Ridge's cream-brick worker cottages, Williamson Street, the rail embankments.* Rusticated sandstone bases, heavy timber, line shafts, exposed stone. Steel/Dark/Ghost.

**(8th, off-grid, and you will want it:) fire-managed prairie and marsh.** *Anchors: Curtis Prairie (the world's oldest restored prairie, maintained by prescribed burn), Cherokee Marsh, Gardner Marsh boardwalks, the Lost City Forest's drowned 1911 street grid.* This does not exist on the isthmus and is the single biggest thing the footprint loses. See §5 and §6.

---

## 2. THE TWENTY THAT MUST SURVIVE

Ranked. On-grid unless flagged.

**S-TIER — the map does not exist without these**

1. **Wisconsin State Capitol.** Four equal wings, four front doors, no back; the only granite dome in the US; 284 ft; visible from everywhere by law. This is your League HQ, your beacon, and your lore engine simultaneously. Nothing else in Madison can do that job.
2. **Capitol Square + the Concourse + the Dane County Farmers' Market.** A walkable *ring* at the dead center of an 1836 plat, with four corner walks feeding the endgame and a weekly 150-vendor bazaar that rotates the entire shop layer. Your hub town and your economy, in one geometric object.
3. **State Street, all eight blocks.** The spine. A route made of shops instead of grass, with real segment character (institutional 100–200 → everyday 300–400 → student-loud 500–600 → pedestrian plaza 700–800). At 172 tiles it is your longest route by a wide margin.
4. **Bascom Hill + Bascom Hall.** The only elevation that reads as elevation, and the dome burned off in 1916 and was never rebuilt — a roofless top floor open to weather. The hill *and* its ruin, in one asset.
5. **The Yahara canal + Tenney Park Lock & Dam.** A real, county-operated, permit-gated, hours-limited water elevator that sets the downstream lake's level. You do not have to invent a traversal machine; Dane County built one.

**A-TIER — the biome carriers**

6. **Monona Terrace + Olin Terrace + the John Nolen causeway.** A white circular deck 90 ft out over water, designed 1938, built 1997, by an architect who died in between. Best arena and best ghost story on the map.
7. **James Madison Park + the Bernard-Hoover Boathouse (+ Gates of Heaven, 1863, as shrine).** Your beach, your surf origin, your first soft place. The relocated 1863 sanctuary is the quiet emotional beat — a blessing/rename/heal shrine, never a dungeon.
8. **Machinery Row.** Already shaped like a gym: two towers, a full block, line shafts, National Register, and a real long-running bike shop on the ground floor.
9. **Memorial Union Terrace + the Hoofers piers.** The one place the built city touches open water with nothing in between; ~2,000 chairs in farm-equipment colors, swapped by season. Your social hub and where you learn wind.
10. **Library Mall + Memorial Library + the Hagenah Fountain.** Where downtown stops being commercial and becomes academic. Starting plaza, tutors, and a fountain that is a fixed water encounter dropped implausibly into a paved square.
11. **Williamson Street + the Willy Street Co-op + Third Lake Ridge.** Your co-op Mart (bulk pricing, membership discount), your quest board (the bulletin board *is* one), and the region's cultural counterweight to the Square.
12. **Central Library (2013 skin over 1965 bones) + the vanished Carnegie lot.** Three eras of one institution, the deepest of which is a parking lot. The single best "one location, three timelines" object in Madison.

**B-TIER — flavor, systems, and set pieces**

13. **Overture Center.** Five nested halls of descending size, a custom pipe organ, a free-to-walk atrium. A vertical dungeon with a built-in safe room.
14. **Madison Municipal Building.** The permit office. See §4 — this is load-bearing, not flavor.
15. **Kohl Center.** 17,287 seats, cantilevered decks so the crowd hangs directly overhead, a Chihuly glass wall in the lobby. Your Battle Tower.
16. **Period Garden Park.** ~10,000 sq ft, invisible until you're at its gate, mistaken daily for somebody's front yard. Smallest location on the map holding the rarest thing.
17. **Lake Mendota as a *system*:** 21.6 mi of shore but only 4.3 mi continuously public; long-axis fetch; a 170-year continuous ice record kept since 1852-53; a 105-day median freeze; an 83 ft deep hole.
18. **Lake Monona + Monona Bay.** The tame water. The bay is nearly sealed by the causeway and rail embankment — a wall with one gap.
19. **Muir Woods + Muir Knoll.** Seven acres of closed forest that thousands walk past daily and never enter, reached by an unmarked rustic staircase. Your hidden vertical shortcut.
20. **The Museum Mile + the Wisconsin History Center pit.** As of 2026 that block is fenced hoarding; the $112.3M building opens ~2028. **Ship the hole, and let a late-game questline finish the building.** A museum that gets built while you play is worth the whole gimmick.

**The next five, as off-grid lobe maps (not on the 470×270 grid):** Olbrich's Bolz Conservatory + Royal Thai Pavilion; Garver Feed Mill (1906 "sugar castle," ruin→restored two-state dungeon); the UW Arboretum (Curtis Prairie, Wingra Woods springs, Lost City Forest); Picnic Point; Cherokee Marsh.

**Cut, and I would defend each:** the Beltline (off-map; keep only as the region's edge myth), Hilldale (a mall; redundant with State Street), Regent Street (redundant with State Street), Camp Randall (redundant with Kohl Center; keep as a postgame venue), Governor's Island / Mendota Mental Health Institute (see §6), and the whole lower Yahara chain (Waubesa/Kegonsa = sequel).

---

## 3. THE EIGHT GYMS

Tuned directly against Johto's extracted curve — ace levels **9 / 16 / 20 / 25 / 30 / 35 / 31 / 40**, deltas **+7 / +4 / +5 / +5 / +5 / −4 / +9**, team sizes **2 / 3 / 2 / 4 / 2 / 3 / 3 / 4**, four-unit chapter-break teams at gyms 4 and 8, boss ace 3–6 levels above the local wild ceiling.

**The Capitol is not a gym. It is the League** — four wings, four Elite Four members, then the rotunda puzzle and the Champion on the dome observation deck in open air.

| # | Site | Type | Ace / Size | Grants | Biome | Scale |
|---|---|---|---|---|---|---|
| 1 | **Bascom Hall** | Flying | Lv 9 / 2 | BEAM (Flash) | drumlin ridge | campus village |
| 2 | **Overture Center** | Fairy | Lv 16 / 3 | SHEAR (Cut) | masonry canyon | dense strip |
| 3 | **Capitol Square Market** | Normal | Lv 20 / 2 | HAUL permission (Strength) | civic plateau | metropolis |
| 4 | **Central Library** | Ghost | Lv 25 / 4 | PADDLE (Surf) | subterranean archive | single building |
| 5 | **James Madison Park** | Fighting | Lv 30 / 2 | PORTAGE | soft north littoral | waterfront nbhd |
| 6 | **Monona Terrace** | Psychic | Lv 35 / 3 | **nothing** (+Def) | hard south littoral | megastructure |
| 7 | **Tenney Park Locks** | Ice | Lv 31 / 3 | SLUICE (Whirlpool) | canal / frozen lagoon | small park town |
| 8 | **Machinery Row** | Steel | Lv 40 / 4 | CLIMB (Waterfall) | brick works | warehouse district |

**Gym 1 — Bascom Hall, Flying, "the Domeless Gym."** Leader: a student orator on the roofless top floor where the 1916 dome burned off, all "sifting and winnowing." Overworld weather carries into the battle. Pre-gym dungeon is the hill itself — trainers tiered by altitude so the fight gets harder with elevation, with the Lincoln statue as the heal point that only activates once you've cleared every tier below. Frail type, lowest ace you'll ever ship, and its badge unlocks a *non-blocking* tool. The headlamp itself is found in Muir Woods, not given by the leader — key and permission split from move one.

**Gym 2 — Overture Center, Fairy.** Leader: a conductor whose team attacks on the beat of the pipe organ. Five halls of descending size = five nested tiers; the organ stops open passages between them; the free-to-walk glass atrium is a deliberate no-battle safe room inside the dungeon. Grants SHEAR — the first *hard* gate, opening the boarded 100-block storefronts, chained alley gates, and the rail-side lots. Fairy answered by Steel/Poison, which shares nothing with Flying's Rock/Electric/Ice.

**Gym 3 — the Farmers' Market ring, Normal. The Whitney slot.** Leader: the Market Master, a dairy vendor whose ace is the obvious Wisconsin Miltank. This is the deliberate difficulty spike, placed in the richest location on the map, where a stuck player has the most alternatives — 150 stalls, the Overture, the Municipal Building, the department-store equivalent, the Underground. Gym-adjacent dungeon: the **History Center construction pit** across the Square, a fenced excavation full of Ground and Steel. Grants HAUL *permission*; the pry bar isn't found until Machinery Row, five gyms later. Copy Johto exactly here.

**Gym 4 — Central Library, Ghost. The structural midpoint.** Two doors from the Market. **Normal → Ghost, two blocks apart, a market and a library** — Johto's mutual-immunity adjacency, but the two buildings are so ordinary and so close that the lesson lands as a joke rather than a lecture. Dungeon: descend the 2013 light wells into the retained 1965 concrete stacks; the late-game payoff is an item that lets you see and enter the 1906 Carnegie building's ghost standing on what is now a parking lot on N. Carroll. Four-unit team, chapter break. Grants **PADDLE** — the largest single unlock in the game, and it happens *at the hub*, so the map explodes open in both directions at once from the Square. Obedience to 50.

**Gyms 5 & 6 — the two-lane lobe.** After Surf, the Square's corner avenues give you two lanes east, and you may run them in either order:
- **North lane → Gym 5, James Madison Park, Fighting.** Leader: a boathouse coach. Two full basketball courts, a sand volleyball court, and rowers — the type is sitting there already. Dungeon: the three-room 1915 boathouse, Water/Ghost resident. Grants **PORTAGE** — carry your boat overland, the real Paddle-and-Portage verb, which lets you move between the Mendota tier and the Monona tier *anywhere*, slowly, instead of only at the lock. It is the Fly slot in function (it changes your whole relationship to the map) without being flight.
- **South lane → Gym 6, Monona Terrace, Psychic. The Jasmine slot: the refused boss, and the only badge that grants no field move.** Leader: an architect-medium who will not battle you until the original 1938 drawings are found — a building dreamed sixty years before it existed. She sends you across to the *other* lane (the boathouse archive, the Gates of Heaven caretaker) to get them. Arena: the rooftop, a white ring 90 ft over open water where knockback genuinely sends a Pokémon off the edge. Below deck, the exhibition hall's layout changes with an in-game event calendar, so the dungeon is never the same twice.

This is Johto's Olivine/Cianwood trick with the geography Madison actually has. It costs you the classic out-and-back peninsula, but it buys something better: the two lanes are the map's two *opposite* biomes, so order-freedom also means "which Madison do you meet first — the green one or the white one."

**Gym 7 — Tenney Park Lock & Dam, Ice. The Pryce regression, −4.** Leader: **the Lockmaster, who has kept the ice-on/ice-off ledger since 1852.** She is under-leveled on purpose, because the two-lane lobe may have over-leveled you by an unknowable amount, and that is the price of the branch. The gym room is the puzzle by this point: the frozen lagoon as a sliding-ice maze, and the lock chamber as a vertical water elevator you ride. Gated not by level but by faction — the villains have jammed the gates. Grants **SLUICE**: operate the locks, raise and lower Monona, expose lakebed passages and submerged side channels. Like Whirlpool, this is mostly an *optional-content* key plus the road east.

**Gym 8 — Machinery Row, Steel. +9, four units, two beats.** The approach consumes every tool you own: Paddle down the canal, Sluice through the lock, Shear the yard fence, Haul the line shafts. A de facto exam on the entire gating system, exactly like the road to Clair. Leader: a machinist in the conical turret office, timber beams and lake windows. Then he **refuses the badge** and sends you to the Third Lake Ridge preservationists, who test how you treat what you inherit — the Dragon's Den quiz, relocated. The CLIMB kit is found earlier, inside the frozen lagoon, so you carry it unusable for twenty minutes.

*One rule I break, deliberately:* Ice → Steel share Fire and Fighting as answers, which Johto never allows. Fix it in the team, not the type — the gym 8 ace is **Steel/Flying**, so the Fighting sweeper that beat Pryce-analog comes in neutral. Everything else holds: **no starter type gets a gym** (Fire/Water/Grass are absent from all eight, and the Water specialist goes to the Elite Four), **no two adjacent gyms share an answer**, **one new biome per gym with no repeats in a row**, and **settlement scale zig-zags** village → strip → metropolis → single building → neighborhood → megastructure → village → district → the crown.

**Wild bands** (boss sits +3 to +6 over local ceiling, jagged like Johto's because Surf opens deep water early): State Street Lv 2–6 → campus ridge Lv 4–9 → Square + pit Lv 5–13 → alley/basement layer Lv 10–16 → **both shores Lv 13–24** (the spike) → canal Lv 15–19 (the dip) → Machinery Row/rail row Lv 20–27.

**The faction, used three times as a non-level gate** (Johto's pattern): a development consortium named for the real, failed 1911 Lake Forest subdivision that sank into the marsh. They occupy the Municipal Building's permit office before gym 4 (freezing everyone's paperwork), the Tenney locks before gym 7, and the History Center pit before gym 8. Their goal is to fill the wetlands and repeal the height limit. **The endgame beat: they build something taller than the dome.** Madison's villain is a zoning variance, and that is more interesting than it sounds.

---

## 4. TRAVERSAL: BADGES ONTO REAL BARRIERS

Seven of eight badges grant a field move; three of the seven tools are found in the world *before* the badge that licenses them.

| Real barrier | Verb | Gate | Notes |
|---|---|---|---|
| Boarded storefronts, chained gates, rail-side lots | **SHEAR** | Badge 2 | First hard gate. Opens the 100-block vacancies as procedurally re-dressed dungeon rooms. |
| Line shafts, lock gates, drawbridge counterweights, construction barriers | **HAUL** | Badge 3 permission / tool at Machinery Row | Five-gym delay, copied straight from Plain Badge. |
| **Lakes Mendota & Monona** | **PADDLE** | Badge 4 / boat from Hoofers | Mendota is the hard water (long-axis fetch, tacking against wind); Monona is tame. Monona Bay is your teaching harbor — nearly sealed by the causeway, one gap. |
| **The isthmus itself** (5 ft of head between two lakes) | **PORTAGE** | Badge 5 | Carry the boat overland. Slow, vulnerable, always available. This is the answer to "why can't I just sail everywhere" — a cost, not a wall. |
| **The Yahara lock** (Mendota tier → Monona tier) | **SLUICE** | Badge 7 + **Tenney Lock Permit** | A staffed, ticketed, hours-limited county facility. Toll NPC, time gate, and 48-hour off-hours sidequest, all real. Also the single control on Monona's water level — make it a **player-controllable global**: drop it to expose lakebed passages, raise it to float over barriers. |
| **Bascom Hill's 10% grade**, fire escapes, rail embankments, the dome stair | **CLIMB** | Badge 8 / kit found in the frozen lagoon | Opens the Capitol's observation deck and the Muir Woods back-slope shortcut. |
| Dark basements, culverts, library light wells | **BEAM** | Badge 1 | Softest gate, blocks no critical path. |
| **Rail corridors & the John Nolen causeway** | *none* | crossable only at named gaps | Your on-grid Beltline: hard walls with two or three bridges. Off-grid, the actual Beltline is crossable only where the Capital City Trail and Southwest Commuter Path duck under — those two underpasses are the keys to the whole southern half of the region. |
| **The ~11 bridges over one mile of canal** | *none* | rhythm, not gate | Ten crossings in a mile is a built-in metronome: perches, ambushes, and two rail-to-trail conversions you can climb onto with CLIMB. |
| **Everything civic** | **PERMITS** | purchased at the Municipal Building | See below. |

**Madison's signature gate is paperwork, and I would build the whole item economy around it.** These are all real: the Tenney Lock Permit, the DNR state trail pass required for nine miles of the Capital City Trail, the Lake Access Permit at Olbrich, the after-hours ranger permit for the Lakeshore Preserve (open 4am–10pm), the fishing license. The old post office at 215 MLK becomes the region's permit office, mail depot, trade hub, and lost-and-found — and Madison's Snorlax is a form that hasn't been stamped. That is funnier, more local, and less resented than a sleeping obstacle.

**No Fly. Opinionated and load-bearing.** Fast travel is the Metro bus along State Street's block gates (unlocked one at a time; riding skips encounters and buskers, so speedrunners lose items) and, later, the bike-path network with trailhead nodes. Madison is genuinely one of America's bike cities; more importantly, **if you can fly, the isthmus stops being an isthmus** and every chokepoint you spent the game building evaporates. The dome must stay visible-and-unreachable for twenty hours.

**Winter is the endgame's traversal reversal.** Mendota's median ice duration is 105 days; Monona 107; the record runs unbroken to 1852-53. In the ice state Paddle is disabled, the locks are irrelevant because you walk over them, the lagoons become sliding-ice puzzle floors, Bascom Hill glazes into an unwalkable slope requiring traction, and the entire lake surface becomes a new walkable tier. **Iceboats use the same wind vector field as summer sailing — one mechanic, two seasons.** Vary ice thickness by depth and inflow: shallow Wingra safe long before deep Mendota.

---

## 5. THE FOOTPRINT TO ACTUALLY BUILD

**Bascom Hill in the WSW to the Yahara River / Tenney Locks in the ENE, lake shore to lake shore. ~3.4 km × 2.0 km = 6.8 km² ≈ 2.6 sq mi. Rotate the whole map ~30° counter-clockwise** so the isthmus axis is horizontal, Mendota is the top edge and Monona the bottom. This is documented series practice — Hoenn is Kyushu rotated 90° for the GBA's horizontal screen; Galar is Britain rotated 180° so the capital lands at the end of the difficulty ramp.

At 470 × 270 that is **7.3 m/tile**. Sanity check: land is ~45% of the box (~3.1 km²), of which roughly half is building mass you walk *around* rather than on — Gen 1's rule of about one enterable door per two to three screens of city — leaving ~29–35k walkable outdoor tiles, plus ~55k surfable water. It closes.

**Tile budget for the ~35,000:** State Street + Library Mall 3,200 · Capitol Square + the four corner avenues 2,800 · Bascom/Observatory ridge + Muir Woods + the Kohl apron 4,500 · Mansion Hill + E. Gorham + James Madison Park 4,000 · MLK/Law Park/Monona Terrace/John Nolen 3,500 · the E. Washington mid-isthmus grid (Tenney-Lapham) 5,000 · Williamson/Third Lake Ridge/Machinery Row 4,500 · Yahara banks + Tenney Park + the locks 3,500 · the alley/basement/rail second sheet 2,000 · gatehouses and margin 2,000.

**What it wins:** every S-tier landmark, all seven core biomes, the four-wing hub with six radiating spokes, the full 172-tile State Street canyon, the only real hill, both shores in their opposing materials, the lock, and — decisively — **hard water edges on both long sides**, so you never author a fake mountain range to keep the player in.

**What it loses, and this is real:** no prairie, no marsh, no savanna, no springs, no effigy mounds, no Arboretum, no Olbrich, no Garver, no Picnic Point, no Cherokee Marsh, no Beltline. **Roughly a third of Madison's biome variety is outside this box.** Recover it the way the series always has — as **off-grid lobe maps**, not as grid extensions: Olbrich + Garver reached east through the Yahara lock (the Blackthorn-behind-the-Ice-Path shape); the Arboretum and Lake Wingra reached south by paddling Monona Bay into Wingra Creek and gated by the DNR trail pass; Picnic Point west by boat from the Union; Cherokee Marsh north up the river as the source of the region's water quality.

**Alternatives considered and rejected:**
- **Campus-only (936 acres = 1.46 sq mi).** Fits beautifully, has the best relief (155 ft), the best wilderness (300 acres of Lakeshore Preserve), a mile-long peninsula, and four mound groups. Loses the Capitol, the isthmus, and the whole civic register — and every location is one institution, so all eight gyms end up wearing the same lanyard. Monotone verbs.
- **Arboretum + Wingra basin.** Best biome diversity by a mile: burn-cycle prairie, oak savanna, spring-fed dark woods, boardwalk marsh, a drowned 1911 street grid. But it is a basin, not a corridor — no spine, no hub, no beacon — and it is zero percent urban in a game whose best material is urban.
- **East side / Yahara corridor (Willy → Olbrich).** The best *dungeons* in the city (Garver's two-state sugar castle, Goodman's Ironworks/Brassworks, the Barrymore's painted starfield). But no dominant landmark, no elevation, and no center.
- **The whole "two lakes + Arboretum" wedge (~5 sq mi).** Blows the budget, halves the tile scale to ~15 m, and makes Capitol Square a nine-tile blob. Compress this map and you lose the one thing it has that Kanto never did: near-literal city blocks.

---

## 6. HONEST RISKS

**1. There are no caves.** Madison has essentially no natural rock. A third of the genre's dungeon vocabulary — Mt. Moon, Rock Tunnel, Union Cave, Diglett's — has no source material. Every cave must be an *enclosure* substitute: the 600-block basement, the library's 1965 stacks, Machinery Row's cellars, Starkweather's culverts, Warner Park's 6-ft concrete lagoon-to-lake pipe, a Beltline underpass. That works, but it means every dark space in your game is man-made, and the map will feel less ancient than a Pokémon map usually does.

**2. There is almost no vertical relief.** 155 ft across the entire campus; Bascom Hill is the only slope that reads as a slope. Ledges — the genre's cheapest one-way movement rule — have nearly nothing to attach to. Mitigate with the drumlin grain (whaleback ridges running NE-SW with wetland in the troughs) for micro-relief, and put your verticality in *buildings*: the Capitol's 284 ft, Kohl's cantilevered decks, Machinery Row's two towers, Monona Terrace's ramps, the library's light wells.

**3. A corridor is a hallway.** The isthmus's legibility is also its confinement. Johto's strength was branching; this map will read closer to Unova's linear circuit. The two-lane shore lobe, the Square's six spokes, and the alley/basement second sheet are your mitigations, and they are not fully sufficient. Accept it and lean into the loop shape — final content at the *center* rather than the far end is unusual and genuinely better here.

**4. Eight gyms in 2.6 sq mi.** Johto's eight span a prefecture. Yours span a 45-minute walk. Gyms will sit 300–600 tiles apart. The Gen-1 lesson applies: **tiles follow intended playtime, not kilometers** — Route 1 got 36 steps for 49 km, Cycling Road got 144 for 80 km. Budget by seconds, put content where you want time spent, and use the off-grid lobes for the long hauls.

**5. Water everywhere, but no Water gym.** Two lakes, a river, three locks, 4.3 miles of public Mendota shoreline — and the Johto balance rule says keep starter types out of the gym roster. So the lakes carry Ice, Fighting-on-a-pier, and traversal instead, and the Water specialist goes to the Elite Four. If you overrule me and ship a Water gym, you privilege the Grass and Electric starters for a third of the game and you will feel it.

**6. Effigy mounds are a live ethical constraint, not set dressing.** Madison had 1,500+; about 200 survive; 230+ ring Lake Wingra, the densest concentration in North America; four groups survive on campus, three on Eagle Heights. They are burial sites, the Ho-Chunk hold themselves descendants of the builders, and tobacco offerings are still tied to trees at Eagle Heights today. **The genre's default — ancient ruin = dungeon to raid — is unusable.** The isthmus footprint is nearly mound-free, which is one quiet argument for it; the moment you extend west or south you inherit the obligation. If you go there: no battle, no dig, no capture, stepping on one is refused outright, offerings and blessings only, a combat-free questline, the destroyed panther and linear mounds present as *absences* on the map — and consult the Ho-Chunk Nation before shipping a line of it. The 2019 renaming of Squaw Bay to **Wicawak** (muskrat), first requested in 2005, is a good, respectful beat about maps being wrong and names being restored.

**7. Some real buildings should not be dungeons.** The Royal Thai Pavilion is a royal gift and an active cultural site — it can be an honored arena, but nothing gets smashed there. The Gates of Heaven is the eighth-oldest surviving synagogue building in the country and a working wedding venue — shrine, never dungeon. **Cut Governor's Island and Mendota Mental Health Institute entirely.** "Eerie asylum grounds" is the single worst trope available in Madison, and the sandstone outcrop is not worth it.

**8. Madison has no antagonist geography.** No volcano, no desert, no wasteland, no ruin. Your closest things are a drowned 1911 subdivision (off-grid), reed canary grass blight, algal blooms, and a freeway. The villain plan — fill the marsh, repeal the height limit — is thematically perfect and *visually undramatic*. You will have to make blight tiles, construction hoarding, and a rising tower do the work that Team Magma got from a volcano.

**9. Winter is the best idea here and the most expensive.** A seasonal flip that disables Surf, opens the lake surface, freezes the lagoons, glazes the hill, and swaps every encounter table is effectively a second map. Commit to it in preproduction or cut it in preproduction. A half-implemented winter is worse than none, and the ice record, the iceboats, and the 105-day timer are too good to do badly.

**10. Everything is green, flat and low-rise.** Without the season system and without the height law paying off, large stretches will read as one tileset. Your contrast budget is *materials*, not terrain: white Bethel granite, cream city brick, rusticated sandstone, white cast concrete, lawn, sand, black water. Use them hard, and keep the north shore soft and the south shore hard.

**11. The map dates fast.** As of 2026 the History Center is a pit until ~2028, John Nolen Drive is under reconstruction through 2027, the engineering campus is mid-demolition, and State Street's pedestrian extent has changed year to year. Turn that into the feature — a region that visibly rebuilds itself between acts — rather than pretending to a fixed present.

**12. And the smallest risk, worth naming: there is nowhere to hide.** 35,000 walkable tiles, hard water edges, and a dome you can see from every one of them. There is no "over there" on this map. All your secrecy has to live in interiors, basements, alleys, and the one quarter-acre Victorian garden that nobody notices they're walking past.