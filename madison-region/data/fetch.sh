#!/bin/sh
# Re-pull the Madison OSM extracts (only needed if the .json.gz files are missing).
# overpass-api.de was unreliable during the original pull; kumi.systems worked.
set -e
H=${OVERPASS:-https://overpass.kumi.systems/api/interpreter}
for q in water park road named; do
  echo "fetching $q ..."
  curl -sS --max-time 180 -o "$q.json" -X POST "$H" --data-binary "@q_$q.ql"
done
