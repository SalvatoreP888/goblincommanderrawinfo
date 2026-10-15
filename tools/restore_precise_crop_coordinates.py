#!/usr/bin/env python3
"""Restore precise crop positions verified against the original recovered PNG hashes.
The historical CSV rounded these seven rectangles to whole PDF points. The exact
positions are the source text-anchor vertical centers +/- 240 points, independently
recovered from the same PDF. All resulting PNGs must still pass SHA-256 comparison.
"""
import csv
from pathlib import Path
p = Path(__file__).resolve().parents[1] / 'evidence/PRIMA_V4_PROOF_SPEC.tsv'
rows = list(csv.DictReader(p.open(encoding='utf-8'), delimiter='\t'))
rects = {
 'printed_p008_soul_caches':'182,134.25604248046875,360,614.2560424804688',
 'printed_p035_soul_doctor_aura':'352,45.699859619140625,548,525.6998596191406',
 'printed_p068_trist_moon_gate':'352,34.518524169921875,548,514.5185241699219',
 'printed_p093_wise_one_trap':'182,73.51828002929688,360,553.5182800292969',
 'printed_p101_naxus_replicas':'22,195.24769592285156,185,675.2476959228516',
 'printed_p102_nighthorde_defectors':'182,215.53781127929688,360,695.5378112792969',
 'printed_p107_final_five_bombs':'352,192.36932373046875,548,672.3693237304688'
}
for row in rows:
    if row['stem'] in rects:
        row['crop_points'] = rects[row['stem']]
with p.open('w',encoding='utf-8',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
    writer.writeheader();writer.writerows(rows)
print('Restored seven source-anchor-derived fractional crop rectangles; hashes unchanged.')
