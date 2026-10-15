# Technical reconstruction: evidence, history and remaining experiments

14 October 2026. This is a research consolidation, **not a report of code changes or a new passing game build**. The actual local browser implementation and wave19 files are not in this repository.

## Goal and boundary

The recorded goal is a browser-native reconstruction of the version already being investigated, derived primarily from the PS2 game. It is not a requirement to switch to GameCube. Emulators can supply reference observations; an emulator, remote stream or disguised emulator-in-WASM is not a substitute for the requested native-browser runtime. Preserve original platform and revision distinctions. Keep source-disc ownership, asset provenance and permission separate from technical success; this research repository does not distribute retail game executables or disc images.

## Recovered historical record

The October 12 session export and research review describe a local `goblin-commander-web` project, followed by a more focused October 13 seven-blocker handoff. These are historical reports, not newly rerun measurements.

| Recorded result or question | Correct interpretation |
|---|---|
| DATA.BAF has 17,235 entries; 4,850 candidate Granny blobs and 8/8 name spot checks | Reported extraction observations; not a demonstration that every name domain, format or asset was decoded correctly. |
| Milestone 10 placed about 200 units using five clan-body meshes | Placed instances are not 200 distinct decoded archetype models. Preserve instance IDs and distinguish mesh coverage from visibility. |
| Earlier 19/19 browser probes and 26 parser tests | Those tests passed at that historical point according to the log; they do not establish current end-to-end gameplay or fidelity. |
| A 65×65 terrain heightfield and 29 archetype/model mappings | Reconstruction findings needing original-file hashes, parser offsets and reference renders. |
| Technology 1–5, `gcclanmgr` costs, `SK_Miner` gating | Shipped costs do not establish roster gates, upgrade multipliers or titan semantics. The current AI lane must not be declared fixed. |
| PS2 texture permutation / palette / VU transfer investigation | Earlier hypotheses, not a completed TruthEngine decoder. Do not restart this old lane automatically when the newer handoff prioritizes seven different blockers. |
| REA, Ghidra and Emotion Engine tooling reportedly installed | Environment history only; do not assume a fresh installation is needed or that those exact versions remain current. |

The original session export is hashed in the recovery inventory. Full current code, local traces and original reference states remain missing from this research-only repository.

## Important new connection: independent PS2 memory research

The [RetroAchievements project thread](https://retroachievements.org/forums/topic/32991?comment=415058) points to **gde / gdeOo**, not an assumed real-person identity. The author's public script is in `gdeOo/ra_sets`, path `Goblin Commander (PS2)/Goblin Commander.rascript`.

Pinned source: [commit 817632f04b1c769e711eaacacd319b16bef2e29c](https://github.com/gdeOo/ra_sets/blob/817632f04b1c769e711eaacacd319b16bef2e29c/Goblin%20Commander%20(PS2)/Goblin%20Commander.rascript).

Inspected blob SHA: `121a0c2472ede57f90fe2872e5bfb022cb7a47a8`. Retrieved-byte SHA-256: `77e1e379a3ff6c412e335ef99fcd0d67b22693359622acb1c209d73c49e247af`. The recovered file has 2,914 split lines. These are researcher-defined structures and conditions, not leaked original source code. Do not assume their addresses match our exact PS2 revision. Confirm the author's serial/build hash and validate each pointer chain against our build before applying it.

| Pinned-script location | Useful connection | What it does NOT establish |
|---|---|---|
| Lines 425–437: `MissionObjective`, `MissionScript`, mission objective tree at `0x70`, script field at `0x84` | Starting points for matching objective records and elapsed-time state to residual objectives. | A complete opcode map or all 21 exact objective conditions. |
| Around lines 799–800: `SoulsUpdate = 0x1000a` | A named resource-update event ID. | `150` is NOT this event ID. |
| Lines 2115–2133: amount-150 resource updates used to detect soul caches; transient event counting | Connects visible cache acquisition to a resource event. The author's comment describes events lasting 1–2 frames and avoids double counting. | A universal statement about every resource event or platform. `amount == 150` is a payload predicate, not the event identifier. |
| Lines 2147–2160: eight Harvest shrine team/group pairs and HP predicates | A concrete independent candidate ownership list, useful to test against extracted entities. | Ownership-by-proximity or a universal natural-defeat predicate. |
| Around lines 2356–2403: Hell Boils Over shrine/team grouping | A comparison target for map ownership mismatches. | A replacement for stable entity IDs and original allocation/ownership traces. |
| Lines 2476–2503: `upgrade_levels` and `locked_units` read separately | Strong reason to keep upgrade state separate from recruitment locks. The achievement expects three upgrade entries at level 3 and selected locks at zero for each of three groups. | The complete original technology unlock policy, all level multipliers, or a proven mapping between tech 1–5 and these arrays. |
| Around line 1737: a destroyed-shrine model string | A candidate visual/state transition for shrine destruction testing. | A complete HP/armor/rebuild state machine. |
| Lines 2801–2818: Moongate achievement has `tally(60, ...)` | The comment explicitly describes an achievement-trigger delay timed to visible arrival. | **Do not port 60 hits as an original-game teleport delay.** This is achievement logic. |

The script is a high-value bridge between our guide-level observations and PS2 state, not permission to call the engine fully reverse engineered. Retain the pinned URL and attribution; check its reuse terms before copying substantial code into another project.

## Seven blocker lanes and acceptance criteria

### T01 — 21 residual campaign objectives

The recorded truth-table breakdown is **0 exact, 6 inferred, 6 fallback, 7 data-absent, 2 mechanic-absent**. This is a dated project status, not a new audit result. Required files are `scratch/wave19/residual/` and `tools/analyze/campaign_residuals.md`; they were not recovered here.

For each residual, preserve mission/platform/build, objective ID, script/bytecode offset, native handler, event writer, state field and a minimal positive/counterexample trace. Trace writes to the condition rather than guessing from the displayed objective text. Check hold-timer pause versus reset, specific-entity destruction versus class-wide counts, exact Slime growth/plate eligibility, and the Wise One's payment plus dialogue/state flag. Completion means causal evidence and negative tests, not a renamed fallback.

### T02 — technology, recruitment, upgrades and titans

Keep at least these dimensions separate: scenario/clan eligibility, ownership, roster/technology gate, paid cage unlock, resource cost, unit capacity, support-slot occupancy and operational building state. Compare `gcclanmgr` configuration with the actual executable consumer and the independent `locked_units` / `upgrade_levels` fields. Test tech 1–5 and zero-based versus one-based indexing explicitly. Do not invent health/damage multipliers. The source guide describes play, not necessarily every internal variable.

### T03 — destructible shrines, rebuilding and natural defeat

Use controlled captures of intact, damaged, destroyed, rebuildable and rebuilding states. Separate HP/armor/damage-state/render model changes. Test the defeat predicate with and without surviving workers/titans, resources, passive income, capturable sources and pending spawn/rebuild actions, including same-frame ordering. A strategic FAQ saying 'you cannot afford an army' is not an exact engine loss threshold. A development-only soul fountain or forced reset must not mask missing natural behavior.

### T04 — ownership on eight maps

Build a crosswalk using original entity ID, file/record offset, start slot, team/group writes and reference capture. Use the RA Harvest list as a candidate cross-check, not a universal owner decoder. Do not assign owners from nearest clan shrine, texture color alone or assumptions about how many enemy teams a map should have.

### T05 — fidelity instrumentation

Distinguish loaded asset, decoded asset, instantiated mesh, visible instance and original-reference match. Preserve the reported 117-versus-131 body discrepancy as an unresolved instance-accounting issue until an ID ledger explains it. Require identical mission, camera, frame/state and visibility set when comparing renders. A luminance average or smoke-test pass is not visual fidelity. Save positive and negative examples, exact tool versions and reproducible commands.

### T06 — matched visuals and cinematics

Retain original clip IDs, aspect ratio, camera, timing and frame hashes. Test decoded skeleton, bind pose, axis order, scale, quaternion ordering, root motion and animation sampling separately. UI, lighting and camera mismatch can invalidate comparisons of otherwise correct assets. Earlier pixel-offset/permutation candidates, VU1 and PATH1/2/3 hypotheses need labeled probes and actual GS transfer observations, not attractive-but-unverified textures.

### T07 — original reference states

Capture the original game's victory, defeat, save overwrite, memory-card formatting, credits, menus and audible effects/music. For formatting tests, use disposable cloned virtual memory cards, never a user's only save. For audio distinguish requested → fetched → decoded → scheduled → mixed → audible → matched. No observed reference means **unobserved**, not pass. Keep gameplay-state coverage separate from asset-extraction coverage.

## Cross-source connections worth testing

The Prima guide gives useful behavioral constraints for the machine's final bombs, purple-bomb rearming, weather machines, Defiler Tree and corrupt Soul Fountains, Moongate capture, Slime growth, Sacrifice reinforcements, and Nighthorde defectors/replicas. These can nominate concrete event/state tests. The original Xbox manual helps distinguish cages, upgrades, titans and structures, but it cannot by itself settle PS2 binary layouts. See [V6](../evidence/Goblin_Commander_Claims_Evidence_v6.csv) for exact publication locators.

The independent memory script supplies candidate state names and pointer chains. The missing local wave19 traces supply the third necessary side of the comparison. Only after all three agree for a named build should an inferred row become executable-traced or original-observed.

## Public technical source register

- [Game Extractor BAF plugin](https://github.com/wattostudios/GameExtractor/blob/master/src/org/watto/ge/plugin/archive/Plugin_BAF.java): a format comparison lead; Xbox support is not automatically a PS2 parser.
- [PCSX2 GS local-memory implementation](https://github.com/PCSX2/pcsx2/blob/master/pcsx2/GS/GSLocalMemory.cpp) and [texture replacement code](https://github.com/PCSX2/pcsx2/blob/master/pcsx2/GS/Renderers/HW/GSTextureReplacements.cpp): references for original-output inspection and memory interpretation, not our native runtime.
- [Ghidra Emotion Engine Reloaded](https://github.com/chaoticgd/ghidra-emotionengine-reloaded): tool lead; compatibility/version claims require current checks.
- [GR2 format notes](https://github.com/rdw-archive/RagnarokFileFormats/blob/master/GR2.MD), [opengr2](https://github.com/arves100/opengr2), [blendergranny](https://github.com/Rasetsuu/blendergranny), [LSLib Granny format code](https://github.com/Norbyte/lslib/blob/master/LSLib/Granny/GR2/Format.cs): distinct format/version leads, not proof of compatibility with every Goblin Commander asset.
- [PJ688 PS2 FAQ](https://gamefaqs.gamespot.com/ps2/589779-goblin-commander-unleash-the-horde/faqs/26986), [tomrace Xbox guide](https://gamefaqs.gamespot.com/xbox/589777-goblin-commander-unleash-the-horde/faqs/29443), [Salasar_2 GameCube guide](https://gamefaqs.gamespot.com/gamecube/589778-goblin-commander-unleash-the-horde/faqs/39083): player accounts with platform and completeness limits.
- [Original publisher material and developer diary](https://www.ladydragon.com/a-2goblin.html): period design descriptions, not a retail executable specification.

## Next handoff contract

A follow-up agent should ingest the audit, V6 ledger and current local code together, then select one blocker lane. For each experiment record the source bytes/hash, command, output files, screenshot or trace, result and a counterexample. Mark each claim `original-observed`, `executable-traced`, `inferred`, `fallback`, or `unobserved`; retain failed experiments. No progress percentage or 'complete' status without defined denominators. Do not resume obsolete texture guesses, substitute emulator playback for the native goal, or treat plausible interpretation as code-derived truth.
