#!/usr/bin/env python3
"""Generate authentic direct-PDF proof images from the repository's original Prima guide.

Install: python -m pip install pymupdf
Run:     python tools/render_prima_proof.py

No external calls, OCR, generative edits, automatic Git commits, or file uploads.
Never describe images as existing until the utility has actually run.
"""
from __future__ import annotations
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

try:
    import fitz
except ImportError as exc:
    raise SystemExit("Missing PyMuPDF. Install: python -m pip install pymupdf") from exc

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "Goblin_Commander_Unleash_The_Horde_Strategy_Guide_2004_Book.pdf"
OUTPUT = ROOT / "evidence" / "local_prima_proof"
EXPECTED_SHA = "d97aa508cdc14fa0b89df6ee2009484ec6fffac304f4c79280755f9daa4690a7"
SOURCE_URL = "https://www.ogxbox.co.uk/media/com_eshop/attachments/Goblin_Commander_Unleash_The_Horde_Strategy_Guide_2004_Book.pdf"

# Printed page, literal text anchor, evidence ID. Full original page is always preserved as context.
ANCHORS = [
    (4, "first goblin king", "first_goblin_king"),
    (8, "2.5 souls every second", "fountain_souls"),
    (11, "five moonstones", "moonstone_colors"),
    (15, "Counters Nighthorde", "stonekrusher_counter"),
    (19, "Counters Plaguespitter", "hellfire_counter"),
    (23, "Counters Stonekrusher", "stormbringer_counter"),
    (27, "Dan Russett", "designer_acid"),
    (28, "Counters Stormbringer", "plaguespitter_counter"),
    (33, "Counters Red", "nighthorde_counter"),
    (35, "steals two souls every five seconds", "witch_doctor"),
    (41, "it steals souls", "soul_vortex"),
    (43, "Fraziel working with", "fraziel_prologue"),
    (49, "Master Fraziel appears", "fraziel_death"),
    (65, "gunpowder explosion", "grax_death"),
    (68, "blue moon Trist", "blue_moon"),
    (69, "Master Moongate", "moongate_link"),
    (70, "Titans cannot teleport", "titan_teleport_limit"),
    (78, "weather machines", "weather_machines"),
    (81, "Grommel cheats death", "faine_fate"),
    (82, "Defiler Tree", "defiler_tree"),
    (91, "does not attack you", "messenger"),
    (92, "weary of Syst", "wise_one_claim"),
    (93, "it is a trap", "wise_one_trap"),
    (97, "behind Syst", "naxus_syst"),
    (99, "murdered Master Fraziel", "naxus_confession"),
    (101, "soulless replicas", "moonstone_replicas"),
    (102, "friendly Nighthorde goblins", "nighthorde_defectors"),
    (104, "balloon-like contrap", "machine_structure"),
    (107, "Red Moongate", "five_final_gates"),
    (108, "purpose has always been", "naxus_machine_claim"),
    (108, "30 minutes", "final_countdown"),
    (111, "rearm the bomb", "purple_rearm"),
    (112, "peace and prosperity", "epilogue"),
    (125, "Soul Wells", "graveyard_soul_wells"),
]

def digest(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def run() -> None:
    if not PDF.is_file():
        raise SystemExit(f"Original source missing: {PDF}")
    if digest(PDF) != EXPECTED_SHA:
        raise SystemExit("Source SHA-256 mismatch; refuse to generate evidence from an unknown PDF.")
    doc = fitz.open(PDF)
    if len(doc) != 129:
        raise SystemExit(f"Unexpected source page count {len(doc)} (expected 129)")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    records = []
    for printed, phrase, name in ANCHORS:
        page = doc[printed]  # zero-based index: PDF page = printed page + 1
        hits = page.search_for(phrase)
        if not hits:
            records.append({"name": name, "printed_page": printed, "status": "ANCHOR_NOT_FOUND", "phrase": phrase})
            print(f"SKIP printed page {printed}: {phrase!r} not found in PDF text")
            continue
        context = OUTPUT / f"prima_p{printed:03d}_{name}_context.png"
        passage = OUTPUT / f"prima_p{printed:03d}_{name}_passage.png"
        page.get_pixmap(matrix=fitz.Matrix(1.7, 1.7), alpha=False).save(context)
        rect = max(hits, key=lambda h: h.width)
        crop = fitz.Rect(rect.x0-90, rect.y0-120, rect.x1+95, rect.y1+125) & page.rect
        page.get_pixmap(matrix=fitz.Matrix(2.3, 2.3), clip=crop, alpha=False).save(passage)
        records.append({
            "name": name, "status": "CAPTURED", "phrase": phrase,
            "printed_page": printed, "pdf_page": printed+1,
            "source_url": f"{SOURCE_URL}#page={printed+1}",
            "source_sha256": EXPECTED_SHA,
            "context_path": str(context.relative_to(ROOT)),
            "context_sha256": digest(context),
            "passage_path": str(passage.relative_to(ROOT)),
            "passage_sha256": digest(passage),
            "crop_rect_pdf_points": [round(v,2) for v in crop]
        })
    manifest = {
        "source_file": str(PDF.relative_to(ROOT)),
        "source_sha256": EXPECTED_SHA,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "classification": "direct PDF renders; guide narrative is not verbatim shipped-game dialogue",
        "records": records
    }
    (OUTPUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Rendered {sum(r['status']=='CAPTURED' for r in records)}/{len(records)} evidence pairs to {OUTPUT}")

if __name__ == "__main__":
    run()
