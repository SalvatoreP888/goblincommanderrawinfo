# Goblin Commander — project-wide evidence audit

Audit date: 14 October 2026, US Eastern (execution continued into 15 October UTC).

## Start here

This audit covers **the whole Goblincommander project**, not only the lore branch: narrative, characters, ancient Ogriss, maps, historical sources, development history, the PS2-derived browser reconstruction, technical blockers, agent handoffs and outreach. It does not include unrelated personal or Precision Exteriors material.

Use this document together with:

- [V6 claims register](../evidence/Goblin_Commander_Claims_Evidence_v6.csv), its [change log](../evidence/V6_CHANGELOG.md), and [legacy-ID crosswalk](../evidence/LEGACY_CLAIM_ID_CROSSWALK.csv).
- [Technical research and open experiments](TECHNICAL_RESEARCH_AND_GAPS.md).
- [People, public contact routes and role-specific questions](OUTREACH_CONTACTS_AND_QUESTIONS.md).
- [Archive leads, geography and exact mission index](ARCHIVE_LEADS_AND_MAPS.md).
- [Recovered-file inventory and completeness limits](RECOVERY_INVENTORY_2026-10-14.csv).
- [Machine-generated validation report](../evidence/audit_2026-10-14/validation.json). A proposed output is not an existing proof until this report and its files actually exist.

The older V3/V4 reports and V5 ledger remain historical snapshots. They are not silently rewritten into primary evidence. The V6 ledger reconciles 131 V5 records with two substantive V4 findings that had disappeared, for an expected 133 records. That is a count of recorded claims, **not 133 independently verified retail-game facts**.

## What was actually recovered

The live research repository was read and archived. Its original Prima guide matches SHA-256 `d97aa508cdc14fa0b89df6ee2009484ec6fffac304f4c79280755f9daa4690a7`: 10,526,865 bytes and 129 PDF pages. The user Library also yielded the V4 proof ZIP, text-extraction ZIP, earlier reports, developer-contact document, October 12 session export, two October 12 technical documents, October 13 agent handoff, October 14 archive leads and a later generated lore-research report. File hashes and dispositions are in the recovery inventory.

The V4 archive really contains 41 indexed passage-capture files and three additional full-page images. Two of the indexed captures share the same crop/image bytes but support different statements. The reproduction specification preserves the 41 original capture names, crop rectangles and SHA-256 values. Direct-PDF reproduction must match those values rather than invent screenshots or substitute generated illustrations.

A fresh public-source retrieval recovered the original Xbox manual, SHA-256 `74f0398a7c3ce0fc3d3434a14c7c90b9f5053aec600188d2ed814eeb2d2f1f3f`, and the independent PS2 achievement research described in the technical document. Retrieval is not a factual endorsement. The HTTP collection also returned failures and duplicate/malformed URL candidates; its raw request count must not be described as a count of verified independent sources.

## Corrections that govern earlier material

| Earlier wording/problem | Corrected finding and evidence |
|---|---|
| Original release in 2006 | The original release belongs to 2003. A later webpage timestamp is not the game's original release date. [Publisher launch statement](https://www.nintendoworldreport.com/pr/9213/the-horde-is-unleashed). |
| Fraziel certainly intended planetary genocide and Naxus's new race | The guide calls Naxus's actions a perversion on printed p. 99, but on p. 108 reports Naxus's claim that soul bombs were always the machine's purpose. Preserve that tension and the speaker attribution. Naxus's plan is not independent proof of Fraziel's original intent. |
| The manual never mentions other humans; only Fraziel and goblins inhabit the world | Incorrect. The Chronicle uses a collective reference to humans, and Stone Ogre lore describes another population. The manual does not locate or explain a wider human civilization. Printed pp. 22–25. |
| Nighthorde discovered a human empire or taught Fraziel creation magic | Ancient battlefields, crypts and lost wisdom are described, but their builders/species are not identified. Creation precedes the clan's search; that ordering does not establish the source of Fraziel's learning. Manual pp. 22–23, 32–33. |
| Wise One proves a genuine peace faction | He claims dissent and asks 300 gold, then leads Grommel into a three-Slime trap. His assertion is not independently verified. Prima pp. 91–93. |
| Nighthorde was uniformly loyal to Naxus | Friendly defectors join Grommel. Prima p. 102. |
| All hostile members of earlier clans must be traitors, or must all be replicas | Naxus uses the Moonstone to produce soulless replicas, but individual identities are not exhaustively established. Prima p. 101. |
| Four final bombs | The licensed guide specifies five and a 30-minute limit; the purple bomb can be rearmed. Prima pp. 107–111. Retain the fan-walkthrough discrepancy when comparing versions. |
| Naxus permanently dies; Grommel has a documented coronation | Defeat and subsequent peace are described; a permanent death and coronation scene have not been authenticated. Prima pp. 4, 112. |
| `The Blight`, `Night Makes Right`, shortened `Oink Oink Boom` | Prima's contents give **The Marshes**, **Might Makes Right**, and **Oink, Oink, Oink, Boom!** Printed p. 3. These wrong titles survived in V5 despite a later corrective note. |
| All five monthly official-site profiles are preserved/proven published | A monthly schedule beginning with Stonekrusher was announced. This does not establish publication or recovery of every later profile. [Website announcement](https://www.nintendoworldreport.com/pr/8827/goblin-commander-website-open). |
| An increased ledger count proves nothing was lost | V4 identifiers were reused for different statements in V5. The Sacrifice reinforcement rule and Graveyard Observatory/Scout Tower function were omitted. Both are restored under new stable IDs, with a crosswalk. Prima pp. 91 and 125. |
| A generated UHD map is a 1:1 canon map | No generated reconstruction is source evidence. A faithful map requires the original map image, provenance, projection/layout and a feature-by-feature comparison. See the map document. |

## Evidence classes

**Retail observation** requires a named platform/build, source capture or executable trace, and a precise locator. **Official manual/publisher material** establishes its own wording. **Licensed guide** material is attributed to the guide, not passed off as verbatim cinematic dialogue. **Developer recollection** is firsthand historical testimony but may differ from the final product. **Fan research** can guide experiments but requires platform-aware validation. **Hypothesis/open question** remains explicitly unresolved.

A page screenshot proves that the publication contains the passage; it does not prove that a numerical mechanic is implemented identically in every console revision. An achievement-script condition does not automatically define the original game's engine behavior. A current search failure does not prove an archive never existed. An unlocated source is not a negative fact about the fictional world.

## Completeness boundary — not a claim of literal full export

1. **Conversation coverage:** visible project-thread excerpts and retrieved Library artifacts were reconciled. A full raw export of every message in every project branch was not provided by the available retrieval surface. No fabricated transcripts were created to fill that gap.
2. **Native-browser implementation:** the accessible GitHub repository is a research archive, not the actual browser-port codebase. The local `scratch/wave19/residual/`, current executable traces, build hashes, test runs and `tools/analyze/campaign_residuals.md` were not present. Historical counts and statuses therefore remain dated reports, not current passing tests.
3. **Private/raw material:** the recovered 1,551,076-byte session export and generated research JSON are preserved in the user's local audit package with hashes. Their raw metadata and potentially sensitive log content are not bulk-published into this public repository. Relevant project findings are consolidated here; byte-for-byte publication of those raw files is not claimed.
4. **Visual/archive coverage:** the generated visualization drafts, an authenticated master world-map image, unrecovered videos, complete official-site backups and the older named agent-wave packet were not all retrieved. The inventory names these gaps instead of treating a mentioned filename as an available file.
5. **Contact status:** public routes are distinguished from historical/profile-only leads. No interview was conducted and no outreach was sent during this audit.

## What remains investigable

The unresolved questions are research targets, not declarations that they cannot be solved. Source-script recovery, period website/media preservation, targeted developer interviews and platform-matched experiments may resolve them. Each answer should carry a source URL or artifact hash, an exact page/time/offset, its revision, and permission to quote or reproduce where relevant. Do not upgrade confidence just because several generated reports repeat the same sentence.
