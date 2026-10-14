# Goblin Commander: Unleash the Horde — Research Archive

Source-backed lore, development history, preserved documentation, and research notes for the 2003 game.

## Read the 2004 Prima Strategy Guide

- **[Page-indexed full guide text (searchable Markdown)](prima/Goblin_Commander_Prima_2004_PAGE_INDEXED.md)** — all 129 PDF pages, with a direct source link on every page.
- **[Full RAW Prima text (TXT)](prima/Goblin_Commander_Prima_2004_RAW_TEXT.txt)** — extracted from the original embedded PDF text layer, not an AI summary.
- **[Original Prima PDF](Goblin_Commander_Unleash_The_Horde_Strategy_Guide_2004_Book.pdf)** — preserves artwork, page layout, screenshots, and maps.
- [How extraction works, page numbers and source integrity](prima/README.md).

## Lore and evidence

- **[Updated Canon & Evidence Dossier v4](evidence/Goblin_Commander_Complete_Evidence_Dossier_v4.md)** — campaign chronology, clan mythology, source references, and corrected Wise One interpretation.
- [Earlier evidence dossier v3](evidence/Goblin_Commander_Complete_Evidence_Dossier_v3.md)
- [v3 claim evidence ledger](evidence/Goblin_Commander_Claims_Evidence_v3.csv)
- [v3 source register](evidence/Goblin_Commander_Master_Sources_v3.csv)

## Verifiable source integrity

Original Prima guide SHA-256:

`d97aa508cdc14fa0b89df6ee2009484ec6fffac304f4c79280755f9daa4690a7`

Generated text is reproducible with `python3 tools/extract_prima_text.py` (requires Poppler's pdftotext), and is automatically updated by the [GitHub Actions workflow](.github/workflows/publish-prima-text.yml) when the PDF or extractor changes.

**Research standard:** Distinguish shipped-game canon from licensed-guide statements, prerelease plans, fan theories, and unresolved claims. Citations should point to exact original page numbers or timestamps.

**Rights notice:** Prima Games material is copyrighted. Public archiving does not itself grant redistribution rights; review rights-holder permissions for reuse.
