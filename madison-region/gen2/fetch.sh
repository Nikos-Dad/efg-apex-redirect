#!/bin/sh
# Pull the Gold/Silver map tables the measurements in ../README.md are derived from.
set -e
B=https://raw.githubusercontent.com/pret/pokegold/master
curl -sS -o map_constants.asm       $B/constants/map_constants.asm
curl -sS -o landmark_constants.asm  $B/constants/landmark_constants.asm
curl -sS -o maps_data_maps.asm      $B/data/maps/maps.asm
curl -sS -o attributes_data_maps.asm $B/data/maps/attributes.asm
echo "fetched. now: python3 calc.py && python3 stack.py && python3 geo3.py"
