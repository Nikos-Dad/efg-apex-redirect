# Madison game region — geographic bounds

Reference frame for the proposed Pokémon Gold/Silver-scale region on the Madison isthmus.
All coordinates WGS 84 (EPSG:4326), decimal degrees.

- **Origin:** Wisconsin State Capitol dome — `43.0747, -89.3842`
- **Isthmus axis:** bearing **73.4° from north** (16.6° above due east)
- **Projection used:** local equirectangular about lat 43.0747 (sub-metre error at this extent)

---

## 1. Core corridor — 2.2 × 1.2 mi, rotated to the isthmus axis

Rotated rectangle, **not** a north-up box. 3,541 × 1,931 m = **6.838 km² / 2.640 mi²**.
Centroid `43.074471, -89.393859`.

| Corner | Latitude | Longitude | Lands near |
|---|---|---|---|
| W | 43.061615 | -89.411330 | Vilas / Camp Randall |
| S | 43.070702 | -89.369604 | Lake Monona shore, S of Monona Terrace |
| E | 43.087327 | -89.376389 | Lake Mendota, NE of James Madison Park |
| N | 43.078241 | -89.418115 | Lake Mendota, off University Bay |

WKT:
```
POLYGON((-89.411330 43.061615 , -89.369604 43.070702 , -89.376389 43.087327 , -89.418115 43.078241 , -89.411330 43.061615))
```

## 2. Annex lobes — axis-aligned

Both hold must-have greenspace that falls **outside** the corridor. Current plan is to reach them
as off-grid maps rather than extend the grid.

| Lobe | South | West | North | East | Area |
|---|---|---|---|---|---|
| Lakeshore Preserve / Picnic Point | 43.082336 | -89.428472 | 43.091768 | -89.41187 | 0.55 mi² |
| Arboretum / Lake Wingra / Vilas | 43.039666 | -89.432161 | 43.068412 | -89.407566 | 2.47 mi² |

## 3. Bounding boxes

Order is `south, west, north, east` (Overpass / Leaflet order).

| Extent | Bounds | Size |
|---|---|---|
| Core + both annexes | `43.039666, -89.432161, 43.091768, -89.369604` | 5,087 × 5,800 m |
| Rendered survey sheet | `43.036073, -89.448149, 43.103446, -89.325170` | 10,000 × 7,500 m (6.21 × 4.66 mi) |

Overpass bbox for re-pulling source data:
```
(43.030,-89.460,43.115,-89.320)
```

## 4. Anchors

| Anchor | Latitude | Longitude | In |
|---|---|---|---|
| Lake Wingra | 43.05530 | -89.42220 | annex |
| Picnic Point | 43.08976 | -89.41518 | annex |
| UW Arboretum | 43.04278 | -89.42472 | annex |
| Bascom Hall | 43.07566 | -89.40477 | core |
| Camp Randall | 43.07000 | -89.41262 | core |
| Capitol Square | 43.07474 | -89.38421 | core |
| Henry Vilas Zoo | 43.06639 | -89.41083 | core |
| James Madison Park | 43.08028 | -89.37639 | core |
| Memorial Union | 43.07655 | -89.39938 | core |
| Monona Terrace | 43.07161 | -89.38058 | core |
| State Street | 43.07540 | -89.39250 | core |
| Union South | 43.07159 | -89.40817 | core |
| Olbrich Gardens | 43.09061 | -89.33633 | outside |
| Olin Park | 43.05530 | -89.37920 | outside |
| Schenk's Corners | 43.08730 | -89.34750 | outside |
| Tenney Park | 43.08944 | -89.36278 | outside |
| Turville Point | 43.05250 | -89.37330 | outside |
| Yahara Locks | 43.09060 | -89.36060 | outside |

## 5. Caveats

- The corridor is **rotated 16.6°**; treating it as a north-up bbox loses campus at the west end
  and gains open water at the east.
- Anchor coordinates are approximate centroids, except **Picnic Point** and the **UW Arboretum**,
  which come from real OSM nodes/relation centroids.
- Gyms 7 and 8 in the current design sit at the Tenney locks and Machinery Row — both **outside**
  these bounds. Extending the corridor east is the open decision.
- Base geometry © OpenStreetMap contributors (ODbL).
