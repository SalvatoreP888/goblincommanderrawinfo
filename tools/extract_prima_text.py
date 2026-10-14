#!/usr/bin/env python3
"""Reproduce the Prima strategy guide's embedded selectable PDF text.

Usage: python3 tools/extract_prima_text.py
Requires the poppler pdftotext command. No OCR or generated passages.
"""
import hashlib
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "Goblin_Commander_Unleash_The_Horde_Strategy_Guide_2004_Book.pdf"
OUT = ROOT / "prima"
EXPECTED_SHA256 = "d97aa508cdc14fa0b89df6ee2009484ec6fffac304f4c79280755f9daa4690a7"
PAGES = 129
SOURCE_URL = "https://www.ogxbox.co.uk/media/com_eshop/attachments/Goblin_Commander_Unleash_The_Horde_Strategy_Guide_2004_Book.pdf"

def main():
    if not PDF.is_file():
        raise SystemExit(f"Missing source PDF: {PDF}")
    digest = hashlib.sha256(PDF.read_bytes()).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"Source PDF changed: {digest}; expected {EXPECTED_SHA256}")
    result = subprocess.run(
        ["pdftotext", "-raw", "-enc", "UTF-8", str(PDF), "-"],
        check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    raw = result.stdout.decode("utf-8")
    pages = raw.rstrip("\f\r\n").split("\f")
    if len(pages) != PAGES:
        raise SystemExit(f"Expected {PAGES} PDF pages; found {len(pages)}")
    OUT.mkdir(parents=True, exist_ok=True)
    raw_file = OUT / "Goblin_Commander_Prima_2004_RAW_TEXT.txt"
    raw_file.write_text(raw, encoding="utf-8")
    header = [
        "# Prima's Official Strategy Guide (2004) - Page-Indexed Extracted Text",
        "",
        "> Machine-extracted text from the embedded selectable PDF text layer (not OCR).",
        "> Original illustrations, maps, and text baked into images may be absent.",
        f"> Original 129-page PDF: {SOURCE_URL}",
        f"> PDF SHA-256: {digest}",
        "> Page mapping: PDF p. 3 = printed p. 2; subsequent pages follow printed = PDF - 1.",
        "",
        "## Jump to a PDF page",
        "",
    ]
    for start in range(1, PAGES+1, 10):
        ends = min(start + 9, PAGES)
        header.append(" · ".join(f"[{i}](#pdf-page-{i:03d})" for i in range(start, ends+1)) + "  ")
    header.extend(["", "---", ""])
    for i, txt in enumerate(pages, 1):
        printed = f"Printed page {i - 1}" if i >= 3 else ("Front cover" if i == 1 else "Inside title")
        header.extend([
            f'<a id="pdf-page-{i:03d}"></a>',
            f"## PDF page {i:03d} - {printed}",
            f"[View original PDF page]({SOURCE_URL}#page={i})",
            "",
            "~~~text",
            txt.rstrip(),
            "~~~",
            "",
            "---",
            "",
        ])
    out_file = OUT / "Goblin_Commander_Prima_2004_PAGE_INDEXED.md"
    out_file.write_text("\n".join(header), encoding="utf-8")
    print(f"Original sha256: {digest}")
    print(f"Pages: {len(pages)}")
    print(f"Raw: {raw_file} ({raw_file.stat().st_size} bytes)")
    print(f"Indexed: {out_file} ({out_file.stat().st_size} bytes)")
if __name__ == "__main__":
    main()
