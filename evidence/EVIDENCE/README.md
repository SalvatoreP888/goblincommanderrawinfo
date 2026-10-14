# Goblin Commander — evidence status and capture queue

Evidence baseline: 14 October 2026.

This package contains an **auditable source ledger**, not fabricated screenshots or unpermitted reuploads. Each claim in `Goblin_Commander_Claims_Evidence_v3.csv` includes URLs and exact locators where known. Source files hosted by third parties were **not downloaded locally** because the original PDF servers were not accessible from the artifact container. The source PDFs remain linked in the report and source index.

## Evidence standard for later archival runs

1. Create `EVIDENCE/<claim_id>/` for the claim.
2. Capture a faithful, permitted original source or official archived version as `source_original.<ext>` (never recreate it from memory).
3. Capture the **exact supporting passage**, with visible source identity/page context, as `passage_screenshot.png` and preserve the original untouched.
4. Record the direct public URL, Wayback URL if relevant, capture date, printed page/PDF page or timestamp, uploader provenance and SHA-256 of each captured file.
5. Link both files to the corresponding claim ID in the CSV.
6. Do not mark screenshots `captured` until both files exist and were visually inspected. Do not silently treat an indexed excerpt as a page screenshot.
7. Where reproducing whole copyrighted media is not authorized, preserve metadata, a short lawful excerpt, and a locator; do not bypass access restrictions.

## Target priorities

- Original Xbox manual: printed pp. 17, 20, 22–33; chronology/clans/Titans.
- Prima strategy guide: printed pp. 4, 90–92, 101, 107–109; Wise One/replicas/bombs/king.
- Original Spanish *Official Xbox Magazine* interview: find exact issue page and verify sequel/online-play sentence in Spanish.
- Prototype preservation record: Hidden Palace build metadata, damaged-disc warning.
- Current Fandom wiki: article-by-article snapshot before claiming a gap.
- Original 2003 official site: verify each actual Wayback capture rather than saving an index page alone.
