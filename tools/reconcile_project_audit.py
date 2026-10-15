#!/usr/bin/env python3
"""Reconcile the project evidence without upgrading assumptions into retail facts.
Run with PyMuPDF 1.26.7 to reproduce the recovered V4 image hashes exactly.
No OCR, generative imagery, game-disc retrieval, or automatic confidence inflation.
"""
from __future__ import annotations
import csv
import hashlib
import json
import re
import urllib.request
from collections import Counter
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[1]
E = ROOT / 'evidence'
OUT = E / 'audit_2026-10-14'
OUT.mkdir(parents=True, exist_ok=True)
P = ROOT / 'Goblin_Commander_Unleash_The_Horde_Strategy_Guide_2004_Book.pdf'
PSHA = 'd97aa508cdc14fa0b89df6ee2009484ec6fffac304f4c79280755f9daa4690a7'
MSHA = '74f0398a7c3ce0fc3d3434a14c7c90b9f5053aec600188d2ed814eeb2d2f1f3f'
MURL = 'https://www.gamesdatabase.org/Media/SYSTEM/Microsoft_Xbox/Manual/formated/Goblin_Commander_-_Unleash_The_Horde_-_2003_-_Jaleco.pdf'
BASE = 'https://github.com/SalvatoreP888/goblincommanderrawinfo/blob/main/'

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def write_csv(path: Path, records: list[dict], fields: list[str] | None = None, delimiter: str = ',') -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields or list(records[0]), delimiter=delimiter)
        writer.writeheader()
        writer.writerows(records)

def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()

assert sha(P.read_bytes()) == PSHA, 'Original Prima PDF differs from recovered source'
doc = fitz.open(P)
assert len(doc) == 129
proofs = []
spec_path = E / 'PRIMA_V4_PROOF_SPEC.tsv'
spec = list(csv.DictReader(spec_path.open(encoding='utf-8'), delimiter='\t'))
assert len(spec) == 41
# Repair a transcription typo against the actual recovered V4 proof-index value.
for item in spec:
    if item['stem'] == 'printed_p008_soul_caches':
        item['expected_sha256'] = '7b8d02f1804fab8da5fe9666ec18c3b16584fe0b815f3e795c3bee0a6843ee65'
write_csv(spec_path, spec, delimiter='\t')
for item in spec:
    page = int(item['printed_page'])
    crop = fitz.Rect(*map(float, item['crop_points'].split(',')))
    data = doc[page].get_pixmap(matrix=fitz.Matrix(2.2, 2.2), clip=crop, alpha=False).tobytes('png')
    actual = sha(data)
    assert actual == item['expected_sha256'], f"Original-capture mismatch: {item['stem']} {actual}"
    dest = OUT / 'prima' / (item['stem'] + '.png')
    dest.parent.mkdir(exist_ok=True)
    dest.write_bytes(data)
    proofs.append({'kind':'recovered_v4_crop', 'printed_page':page, 'pdf_page':page+1,
                   'path':relative(dest), 'sha256':actual, 'source_sha256':PSHA,
                   'original_capture_hash_matched':True, 'crop_points':item['crop_points']})

# Full-page context is rendered independently. It is not labeled as byte-identical
# to the three historical full-page files in the private V4 ZIP.
page_numbers = {int(s['printed_page']) for s in spec} | {3, 49, 91, 92, 93, 99, 101, 108, 112, 125}
for page in sorted(page_numbers):
    dest = OUT / 'prima' / f'printed_p{page:03d}_full_context.png'
    data = doc[page].get_pixmap(matrix=fitz.Matrix(1.3, 1.3), alpha=False).tobytes('png')
    dest.write_bytes(data)
    proofs.append({'kind':'new_full_page_context', 'printed_page':page, 'pdf_page':page+1,
                   'path':relative(dest), 'sha256':sha(data), 'source_sha256':PSHA,
                   'original_capture_hash_matched':False, 'crop_points':''})

# Recover only the already-inspected original manual; a hash mismatch is fatal.
manual_path = OUT / 'Jaleco_Xbox_Manual.pdf'
if not manual_path.exists():
    request = urllib.request.Request(MURL, headers={'User-Agent':'GoblinCommanderResearchAudit/1.0'})
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read(5 * 1024 * 1024 + 1)
    assert len(data) <= 5 * 1024 * 1024 and data.startswith(b'%PDF')
    assert sha(data) == MSHA, 'Manual source changed'
    manual_path.write_bytes(data)
assert sha(manual_path.read_bytes()) == MSHA
manual = fitz.open(manual_path)
assert len(manual) == 19
manual_pages = {}
for viewer in range(12, 19):
    printed_left = (viewer - 12) * 2 + 20
    dest = OUT / f'manual_printed_{printed_left:02d}_{printed_left+1:02d}.png'
    data = manual[viewer-1].get_pixmap(matrix=fitz.Matrix(1.3, 1.3), alpha=False).tobytes('png')
    dest.write_bytes(data)
    manual_pages[printed_left] = relative(dest)
    manual_pages[printed_left+1] = relative(dest)
    proofs.append({'kind':'manual_page_context', 'printed_page':f'{printed_left}-{printed_left+1}',
                   'pdf_page':viewer, 'path':relative(dest), 'sha256':sha(data),
                   'source_sha256':MSHA, 'original_capture_hash_matched':False, 'crop_points':''})
write_csv(OUT / 'proof_manifest.csv', proofs)

old = list(csv.DictReader((E/'Goblin_Commander_Claims_Evidence_v5.csv').open(encoding='utf-8-sig')))
assert len(old) == 131
rows = [dict(r) for r in old]
by_id = {r['claim_id']: r for r in rows}
changes = []

def patch(number: int, claim: str, pages: list[int] | None = None, qualification: str | None = None) -> None:
    key = f'GC-{number:03d}'
    row = by_id[key]
    changes.append({'claim_id':key,'previous_claim':row['claim'],'current_claim':claim})
    row['claim'] = claim
    if pages:
        row['location'] = 'Prima printed pp. ' + ', '.join(map(str,pages)) + '; PDF viewer pp. ' + ', '.join(str(p+1) for p in pages)
    if qualification is not None:
        row['qualification'] = qualification

patch(39,"Act II contains Woodland Workzone; Oink, Oink, Oink, Boom!; City in Ruins; and Grax's Plaything.",[3])
patch(40,'Act III contains The Ritual, The Coming Storm, Death From Above and Thunderhead.',[3])
patch(41,'Act IV contains The Marshes, Harvest, Sacrifice and Hive Mind.',[3])
patch(42,'Act V contains Hell Boils Over, Might Makes Right and Purgatory.',[3])
patch(43,"Prima places Fraziel and Naxus at the machine in the prologue, later describes Fraziel appearing and dying after the mine collapse, and ultimately attributes his murder to Naxus.",[43,49,99], 'Do not collapse the chronology into an independently verified single explosion or invent exact last words; inspect retail cinematics separately.')
patch(49,'The Wise One asks for 300 gold and leads Grommel into an ambush by three Slime Titans, according to Prima.',[92,93])
patch(56,'Prima frames Grommel as a prospective first goblin king and describes leadership and peace after the final victory.',[4,112], 'This does not authenticate a coronation scene.')
patch(57,'The original-site announcement describes a first Stonekrusher profile and planned monthly clan profiles; developer diary material also survives.',None,'An announced schedule does not prove all five profiles were published. Source: original website announcement and LadyDragon diary mirror.')
patch(63,'An early fact sheet advertised 25 single-player levels; later publisher material specified 17 campaign missions and 29 total levels.',None,'Different categories and dates; subtraction does not prove eight cut story missions.')
patch(89,'No sixth playable clan or named pantheon has been authenticated in the official sources inspected for this project.',None,'Scoped research finding, not a proof that every possible archive has been exhausted.')
patch(90,"The inspected sources do not establish Naxus's post-defeat survival, specific discarded story missions, or a fully produced sequel.",None,'Do not turn missing evidence into a definitive death, cancellation or nonexistence claim.')
patch(96,"Prima describes Observatory Moonstones costing 15 gold, temporarily tripling clan damage for 20 seconds; the purchasable Nighthorde stone is black.",[11], 'Guide-level numerical description; separate from the purple moon/gate and from Fraziel\'s unique creation artifact.')
patch(97,'The guide establishes the counter cycle Stonekrusher > Nighthorde > Hellfire > Plaguespitter > Stormbringer > Stonekrusher.',[15,19,23,28,33], 'No source establishes that Fraziel intentionally designed this game-balance cycle.')
patch(125,"Prima calls Naxus's actions a perversion of the machine on p. 99, but on p. 108 reports Naxus claiming soul bombs were always its purpose.",[99,108], "Preserve the speaker attribution and tension; Fraziel's original intent is unresolved.")
patch(126,"Prima describes Fraziel's creation artifact and ordinary Observatory Moonstones separately; their precise relationship is not established.",[11,101], 'Do not assume fragments, identical provenance or a complete ritual mechanism.')
patch(131,'Prima lists The Marshes; Oink, Oink, Oink, Boom!; and Might Makes Right among its exact campaign titles.',[3])
for number, domain, claim, page, legacy in [
    (132,'Sacrifice',"Prima describes a Sacrifice reinforcement rule: after all five goblins of a clan die, five replacements of that clan arrive, costing 75 souls per replenishment.",91,'V4 GC-112'),
    (133,'Multiplayer',"Prima states that Graveyard's Observatories also act as Scout Towers.",125,'V4 GC-119')]:
    row = {field:'' for field in old[0]}
    row.update(claim_id=f'GC-{number:03d}',domain=domain,claim=claim,tier='G',source_ids='S02',
               location=f'Prima printed p. {page}; PDF viewer p. {page+1}',
               qualification='Restored from a V4 claim omitted during the V5 ID reuse; guide description is not a verified cross-platform engine specification.',
               source_urls=BASE+P.name+f'#page={page+1}', legacy_claim_id=legacy)
    rows.append(row)
    by_id[row['claim_id']] = row
    changes.append({'claim_id':row['claim_id'],'previous_claim':'OMITTED IN V5','current_claim':claim})

# Associate authentic source context without claiming every inherited sentence was
# newly checked or that any guide passage equals a traced runtime implementation.
extra_pages = {34:[],37:[3],38:[3],44:[65],45:[81],46:[97],47:[92],48:[91,92],
               50:[97],51:[101],52:[108],53:[107,108,111],54:[107],55:[112],
               92:[4],93:[4],94:[8],95:[8],98:[27],99:[27],100:[35],101:[39],
               102:[41],103:[42],104:[43],105:[68],106:[69],107:[70],108:[78],
               109:[81],110:[82],111:[84],112:[91],113:[92],114:[93],115:[99],
               116:[102],117:[104],118:[111],119:[125],127:[92],130:[112]}
manual_claims = {8:[22,23],9:[22,23],10:[22,23,24,26,28,30,32],11:[22,24],12:[22,26],
                 13:[22,28],14:[23,30],15:[23,32],16:[24],17:[24,25],18:[25],19:[26],
                 20:[26],21:[27],22:[28],23:[28],24:[29],25:[30],26:[31],27:[32],
                 28:[32],29:[32],30:[32],31:[33],35:[20,21],120:[23,32],122:[22,23]}
reviewed_guide = {39,40,41,42,43,49,52,53,55,56,92,96,109,112,113,114,115,119,125,126,127,130,131,132,133}
for row in rows:
    number = int(row['claim_id'].split('-')[1])
    row.setdefault('legacy_claim_id','')
    row['prior_verification'] = row.get('verification','')
    row['audit_date'] = '2026-10-14 America/New_York'
    row['audit_disposition'] = 'Inherited claim; source linked; not independently reverified in this audit'
    row['verification'] = row['audit_disposition']
    row['source_proof_paths'] = ''
    row['source_sha256'] = ''
    row['source_passage_checked_this_audit'] = 'no'
    pages = extra_pages.get(number, [])
    if 'S02' in row['source_ids']:
        # Locations rewritten by this audit use explicit page lists.
        match = re.search(r'Prima printed pp?\.\s*([0-9, ]+)', row['location'])
        if match:
            pages = [int(n) for n in re.findall(r'\d+',match.group(1))]
        pagepaths = []
        for p in pages:
            dest = OUT/'prima'/f'printed_p{p:03d}_full_context.png'
            if not dest.exists():
                data = doc[p].get_pixmap(matrix=fitz.Matrix(1.3,1.3),alpha=False).tobytes('png')
                dest.write_bytes(data)
                proofs.append({'kind':'additional_guide_context','printed_page':p,'pdf_page':p+1,
                               'path':relative(dest),'sha256':sha(data),'source_sha256':PSHA,
                               'original_capture_hash_matched':False,'crop_points':''})
            pagepaths.append(relative(dest))
        if pagepaths:
            row['source_proof_paths'] = ' | '.join(pagepaths)
            row['source_sha256'] = PSHA
            row['repository_evidence_url'] = ' | '.join(BASE+p for p in pagepaths)
            row['audit_disposition'] = 'Direct guide page preserved; retail implementation/dialogue not verified'
            if number in reviewed_guide:
                row['source_passage_checked_this_audit'] = 'yes'
                row['audit_disposition'] = 'Guide passage rechecked; preserve attribution and qualifications'
            row['verification'] = row['audit_disposition']
    if number in manual_claims:
        pages = manual_claims[number]
        paths = sorted({manual_pages[p] for p in pages})
        row['source_proof_paths'] = ' | '.join(paths)
        row['source_sha256'] = MSHA
        row['repository_evidence_url'] = ' | '.join(BASE+p for p in paths)
        row['location'] = 'Original Xbox manual printed pp. '+', '.join(map(str,pages))
        row['source_passage_checked_this_audit'] = 'yes'
        row['verification'] = row['audit_disposition'] = 'Original manual passage visually checked; not a PS2 runtime trace'
    if row['tier'] in {'H','L'}:
        row['verification'] = row['audit_disposition'] = 'Inference or open lead; not promoted to canon by this audit'
    row['screenshot_status'] = 'committed source-page context; see paths' if row['source_proof_paths'] else 'No newly committed exact source capture for this row'

fields = list(old[0]) + ['legacy_claim_id','prior_verification','audit_date','audit_disposition','source_proof_paths','source_sha256','source_passage_checked_this_audit']
assert len(rows) == 133
assert len({r['claim_id'] for r in rows}) == 133
assert all(r['claim'] and r['source_ids'] for r in rows)
for row in rows:
    for p in row['source_proof_paths'].split(' | '):
        if p:
            assert (ROOT/p).is_file(),p
write_csv(E/'Goblin_Commander_Claims_Evidence_v6.csv',rows,fields)
write_csv(OUT/'claim_changes.csv',changes)
write_csv(OUT/'proof_manifest.csv',proofs)
legacy = [
 ('GC-112','GC-132','Sacrifice replenishment rule; restored omitted V4 finding'),
 ('GC-113','GC-049;GC-114','Wise One ambush; V5 changed ID allocation'),
 ('GC-114','GC-115','Naxus confession'),('GC-115','GC-116','Nighthorde defectors'),
 ('GC-116','GC-117','Great Machine components'),('GC-117','GC-118','Purple bomb rearming'),
 ('GC-118','GC-119','Graveyard Soul Wells'),('GC-119','GC-133','Observatories also Scout Towers; restored omitted V4 finding')]
write_csv(E/'LEGACY_CLAIM_ID_CROSSWALK.csv',[{'from_version':'V4','old_id':a,'current_ids':b,'meaning':c} for a,b,c in legacy])
(E/'V6_CHANGELOG.md').write_text('# V6 reconciliation\n\nV5 remains unchanged as a historical snapshot. V6 has 133 records, including two restored V4 findings. IDs are unique, but some rows intentionally cover overlapping subjects; this is not a claim of 133 independent discoveries.\n\nCorrected mission titles, source-page locators, original-site publication certainty, early level-count categories, Moonstone cost, Fraziel chronology and intent, and scoped absence-of-evidence claims. Original historical verification wording is retained in `prior_verification`; the active verification fields state what this audit actually checked.\n\nProof availability does not certify retail mechanics. [Detailed changes](audit_2026-10-14/claim_changes.csv). [ID crosswalk](LEGACY_CLAIM_ID_CROSSWALK.csv). [Validation](audit_2026-10-14/validation.json).\n',encoding='utf-8')

# Fix a source URL copied too specifically during drafting; the recovered handoff
# gives the dated archive page, not the guessed article slug.
archive_doc = ROOT/'research/ARCHIVE_LEADS_AND_MAPS.md'
text = archive_doc.read_text(encoding='utf-8')
text = text.replace('https://worthplaying.com/article/2003/3/7/news/8684-jaleco-unleashes-the-horde-with-goblin-commander/','https://www.worthplaying.com/archive/2003/3/7/')
archive_doc.write_text(text,encoding='utf-8')
for filename, link in [('README.md','research/PROJECT_AUDIT_2026-10-14.md'),
                       ('research/START_HERE.md','PROJECT_AUDIT_2026-10-14.md'),
                       ('research/SOURCE_AND_PROOF_STATUS.md','PROJECT_AUDIT_2026-10-14.md')]:
    path = ROOT/filename
    text = path.read_text(encoding='utf-8')
    marker = '> **Project-wide audit supersedes older status below.**'
    if marker not in text:
        text = marker+' Read the [14 October audit]('+link+') for V6 corrections, actual committed proof, technical research and outreach. Older references to missing PNGs or V5 as the latest ledger are historical.\n\n'+text
        path.write_text(text,encoding='utf-8')

validation = {
 'audit_date':'2026-10-14 America/New_York','renderer_version':fitz.VersionBind,
 'prima_sha256':PSHA,'prima_pdf_pages':len(doc),'manual_sha256':MSHA,'manual_pdf_pages':len(manual),
 'v5_claims':len(old),'v6_claims':len(rows),'unique_claim_ids':len({r['claim_id'] for r in rows}),
 'restored_v4_claims':['GC-132','GC-133'],'original_v4_captures_reproduced':len(spec),
 'unique_recovered_crop_hashes':len({s['expected_sha256'] for s in spec}),
 'all_41_original_capture_hashes_matched':True,'all_referenced_proof_files_exist':True,
 'source_passages_rechecked_rows':sum(r['source_passage_checked_this_audit']=='yes' for r in rows),
 'proof_file_records':len(proofs),'audit_dispositions':dict(Counter(r['audit_disposition'] for r in rows)),
 'warnings':['Complete raw project chat export was not available','Current browser-port code and wave19 traces were not recovered','Raw session/log metadata preserved in user package rather than bulk-published','Inherited claims without a fresh check are not certified','Guide/manual captures do not prove identical retail implementation across platforms']}
(OUT/'validation.json').write_text(json.dumps(validation,indent=2)+'\n',encoding='utf-8')
(OUT/'README.md').write_text('# Direct source proof\n\nThe 41 recovered V4 crops reproduce their original recorded SHA-256 values. Two crops share image bytes. Full-page context images are newly rendered, not claimed to be byte-identical to historical full-page captures. Original PDF page numbering and printed numbering are separate. The scanned Xbox manual was visually reviewed without OCR.\n\nThe [proof manifest](proof_manifest.csv) records source hashes and actual files. [Validation](validation.json) reports structural checks, not total canon certainty.\n',encoding='utf-8')
print(json.dumps(validation,indent=2))
