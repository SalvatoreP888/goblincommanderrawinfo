#!/usr/bin/env python3
"""Fetch public research references into an audit artifact; never fetch game discs.
HTTP success is retrieval evidence, not confirmation of a claim.
"""
import concurrent.futures, csv, hashlib, json, re, urllib.request
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'audit_source_snapshots'
OUT.mkdir(exist_ok=True)
MANUAL = 'https://www.gamesdatabase.org/Media/SYSTEM/Microsoft_Xbox/Manual/formated/Goblin_Commander_-_Unleash_The_Horde_-_2003_-_Jaleco.pdf'
RA = 'https://raw.githubusercontent.com/gdeOo/ra_sets/817632f04b1c769e711eaacacd319b16bef2e29c/Goblin%20Commander%20(PS2)/Goblin%20Commander.rascript'
urls = set()
for filename in ['evidence/Goblin_Commander_All_Source_Links_v3.txt', 'evidence/Goblin_Commander_Master_Sources_v3.csv']:
    text = (ROOT / filename).read_text(encoding='utf-8-sig')
    urls.update(u.rstrip('.,;') for u in re.findall(r'https?://[^\s"<>|]+', text))
urls.update([MANUAL, RA,
 'https://www.chriszirpoli.com/contact', 'https://www.chriszirpoli.com/resume',
 'https://ronmillar.com/resume/', 'https://www.chrishandloser.com/about',
 'https://douglasshuler.com/contact', 'https://www.secondunitgames.com/about',
 'https://www.secondunitgames.com/contact', 'https://gamehistory.org/',
 'https://hiddenpalace.org/Contact_Us',
 'https://retroachievements.org/forums/topic/32991?comment=415058'])

def collect(pair):
    index, url = pair
    row = {'id': f'SNAP-{index:03d}', 'requested_url': url, 'status': 'not_fetched'}
    try:
        if re.search(r'\.(?:iso|bin|xbe|elf|exe|rar|7z)(?:$|\?)',url,re.I):
            row['status']='excluded_game_or_executable'; return row
        req = urllib.request.Request(url, headers={'User-Agent':'GoblinCommanderResearchAudit/1.0 (public historical source preservation)'})
        with urllib.request.urlopen(req, timeout=20) as response:
            data=response.read(16*1024*1024+1)
            if len(data)>16*1024*1024: raise ValueError('source exceeds 16 MiB cap')
            ctype=response.headers.get('content-type','')
            ext='.pdf' if data.startswith(b'%PDF') else ('.rascript' if url==RA else '.html')
            filename='Jaleco_Xbox_Manual.pdf' if url==MANUAL else ('Goblin_Commander_gde.rascript' if url==RA else row['id']+ext)
            (OUT/filename).write_bytes(data)
            row.update(status='retrieved_not_fact_checked', final_url=response.url, http_status=response.status,
                       content_type=ctype, bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), path=filename)
            if url==RA:
                blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
                row['git_blob_sha']=blob
                if blob!='121a0c2472ede57f90fe2872e5bfb022cb7a47a8': raise ValueError('RA source blob differs from inspected GitHub blob')
            if url==MANUAL and not data.startswith(b'%PDF'): raise ValueError('manual response was not a PDF')
    except Exception as exc:
        row.update(status='retrieval_failed', error=str(exc))
    return row
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    records=list(pool.map(collect, enumerate(sorted(urls),1)))
(OUT/'manifest.json').write_text(json.dumps({'warning':'Retrieval does not verify claims. Failed requests do not prove a source never existed.', 'sources':records},indent=2)+'\n')
print(json.dumps({'sources':len(records),'retrieved':sum(x['status']=='retrieved_not_fact_checked' for x in records),'failed':sum(x['status']=='retrieval_failed' for x in records)}))
