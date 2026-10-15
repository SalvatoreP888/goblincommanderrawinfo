> **Project-wide audit supersedes older status below.** Read the [14 October audit](PROJECT_AUDIT_2026-10-14.md) for V6 corrections, actual committed proof, technical research and outreach. Older references to missing PNGs or V5 as the latest ledger are historical.

# Source and proof status — October 14, 2026

## Source inventory: what GitHub actually hosts

**Stored here:** [Original Prima guide PDF](../Goblin_Commander_Unleash_The_Horde_Strategy_Guide_2004_Book.pdf) and [complete searchable page-indexed text](../prima/Goblin_Commander_Prima_2004_PAGE_INDEXED.md). Source PDF SHA-256 recorded in [prima/README.md](../prima/README.md): `d97aa508cdc14fa0b89df6ee2009484ec6fffac304f4c79280755f9daa4690a7`.

**Not stored here:** [2003 Jaleco manual](https://www.gamesdatabase.org/Media/SYSTEM/Microsoft_Xbox//Manual/formated/Goblin_Commander_-_Unleash_The_Horde_-_2003_-_Jaleco.pdf) and the **41 passage PNG files** mentioned in the historic [V4 report](../evidence/Goblin_Commander_Complete_Evidence_Dossier_v4.md). The images were generated in an earlier separate research package, but the GitHub tree did not contain them when audited. Do **not** cite their local paths as existing GitHub files.

The [renderer](../tools/render_prima_proof.py) can regenerate authentic context screenshots and passage crops from the **stored original PDF** on demand. These are not automatically published or committed by the script; the output becomes a real artifact only after execution and inspection.

## Key claim locations

| Claim | Guide original (printed page) | Indexed searchable proof | Confidence |
|---|---|---|---|
| Fraziel made five races; Grommel aims to unify | p. 4 | [PDF p. 5](../prima/Goblin_Commander_Prima_2004_PAGE_INDEXED.md#pdf-page-005) | Licensed-guide description |
| Opening Fraziel and Naxus collaboration | p. 43 | [PDF p. 44](../prima/Goblin_Commander_Prima_2004_PAGE_INDEXED.md#pdf-page-044) | Licensed-guide prologue description |
| Grax's explosive death | p. 65 | [PDF p. 66](../prima/Goblin_Commander_Prima_2004_PAGE_INDEXED.md#pdf-page-066) | Licensed-guide cinematic description |
| Faine's weather machines and death | pp. 78–81 | [PDF p. 82](../prima/Goblin_Commander_Prima_2004_PAGE_INDEXED.md#pdf-page-082) | Licensed-guide cinematic description |
| Defiler Tree pollutes Soul Fountains | pp. 82–86 | [PDF p. 83](../prima/Goblin_Commander_Prima_2004_PAGE_INDEXED.md#pdf-page-083) | Guide mission objectives |
| Wise One's false truce, payment and ambush | pp. 91–93 | [PDF p. 94](../prima/Goblin_Commander_Prima_2004_PAGE_INDEXED.md#pdf-page-094) | Guide confirms **deception**, not verified peace faction |
| Syst's carnivorous-plant death, Naxus connection | p. 97 | [PDF p. 98](../prima/Goblin_Commander_Prima_2004_PAGE_INDEXED.md#pdf-page-098) | Guide narrative |
| Naxus confesses Fraziel murder | p. 99 | [PDF p. 100](../prima/Goblin_Commander_Prima_2004_PAGE_INDEXED.md#pdf-page-100) | Guide narrative |
| Soulless replicas using Fraziel's Moonstone | p. 101 | [PDF p. 102](../prima/Goblin_Commander_Prima_2004_PAGE_INDEXED.md#pdf-page-102) | Guide narration |
| Genuine Nighthorde defections | p. 102 | [PDF p. 103](../prima/Goblin_Commander_Prima_2004_PAGE_INDEXED.md#pdf-page-103) | Guide narrative |
| Five final bombs in 30 minutes | pp. 107–108 | [PDF p. 109](../prima/Goblin_Commander_Prima_2004_PAGE_INDEXED.md#pdf-page-109) | Guide objectives |
| Purple bomb rearmed if disarmed early | p. 111 | [PDF p. 112](../prima/Goblin_Commander_Prima_2004_PAGE_INDEXED.md#pdf-page-112) | Guide mission warning |
| Naxus defeated; new united goblin nation | p. 112 | [PDF p. 113](../prima/Goblin_Commander_Prima_2004_PAGE_INDEXED.md#pdf-page-113) | Guide ending, not proof of death |
| Soul Wells in GameCube Graveyard | p. 125 | [PDF p. 126](../prima/Goblin_Commander_Prima_2004_PAGE_INDEXED.md#pdf-page-126) | Multiplayer setting, not campaign event |

For manual-specific history and the claims that the Nighthorde sought old wisdom, cite the **original manual's printed pp. 22–23, 32–33**. The 129-page *Prima* guide does **not** supply a named human kingdom or human hometown. The absence of such references is a bounded source observation, not proof that those places never existed.

## Historical source leads, not verified lost lore

- [July 2003 Jaleco site launch](https://www.nintendoworldreport.com/pr/8827/goblin-commander-website-open) advertises monthly clan profiles, first Stonekrusher. **No original Nighthorde profile recovered or authenticated.**
- [Original website Wayback calendar](https://web.archive.org/web/*/http://www.goblincommander.com/) is an index, **not itself a recovered snapshot**.
- [September 26, 2003 Xbox prototype](https://hiddenpalace.org/Goblin_Commander:_Unleash_the_Horde_(Sep_26,_2003_prototype)) is an archival record of a partly corrupted pre-release build; no new story scripts have yet been established from the build.
- [Game Developer 2018](https://www.gamedeveloper.com/design/reversing-the-sunk-cost-fallacy-devs-recount-what-shouldn-t-have-been-cut): Chris Millar's testimony of working online multiplayer removed pre-release.
- [The 2003 E3 preshow preview](https://www.gamespot.com/articles/goblin-commander-e3-2003-preshow-report/1100-6026705/) uses different Fraziel antagonist framing. This is historical press evidence, **not a validated alternate campaign**. Its displayed date metadata is inconsistent with its E3 framing.
- [Spanish magazine scan](https://archive.org/details/Xbox_RO_21): historical source discussing humans and possible sequel ambitions; verify exact original pages before quoting precise sentences.
- [OGDB “Goblin Commander II” listing](https://ogdb.eu/index.php?section=title&titleid=43631) has no independently verified production proof and **must not** be treated as a shipped or demonstrably cancelled sequel.
- [GameFAQs 2003 fan FAQ](https://gamefaqs.gamespot.com/ps2/589779-goblin-commander-unleash-the-horde/faqs/26986) is an author retelling. Its “ruined cities” language is not independent primary-source evidence.

## Required verification standard for the next agent

For each new claim preserve: short **claim**, actual **source URL**, author/date, original/capture status, exact printed/PDF page or footage timestamp or binary file offset, SHA-256 if a file, **unedited screenshot of exact supporting passage when available**, source classification (shipped / original official / licensed guide / period journalism / fan / inference), and next verification step. Do not invent screenshots, transcripts or links.

## Highest-value next tasks

1. Preserve original Jaleco manual pages including the creation chronicle and Nighthorde biography, with actual screenshot + SHA.
2. Recover and authenticate Nighthorde original-site page, if it ever existed, and distinguish it from a promised but unpublished monthly profile.
3. Obtain timecoded retail game dialogue for Fraziel's death, Naxus's revelation and final fate.
4. Compare authenticated prototype and retail files (damaged-sector handling) for unused mission/story changes.
5. Inspect current fan-wiki page revisions before declaring any fact absent.
6. Reproduce authentic Prima proof captures using [the included renderer](../tools/render_prima_proof.py), and **only then** link real image paths.