"""Check relative links and Markdown/Mermaid source consistency; no network access."""
from pathlib import Path
import re,sys
from urllib.parse import unquote
ROOT=Path(__file__).resolve().parents[1];errors=[];diagrams=0
for p in sorted(ROOT.rglob('*.md')):
 s=p.read_text()
 for raw in re.findall(r'\]\(([^)]+)\)',s):
  link=raw.split('#',1)[0]
  if not link or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:',link):continue
  dest=p.parent/unquote(link)
  if not dest.exists():errors.append(f'{p.relative_to(ROOT)}: missing {raw}')
 blocks=re.findall(r'```mermaid\n(.*?)\n```',s,re.S)
 if blocks:
  prefix='sop-' if p.parent.name=='sops' else 'example-' if p.parent.name=='walkthroughs' else ''
  source=ROOT/'diagrams/sources'/f'{prefix}{p.stem}.mmd'
  if not source.exists() or source.read_text().strip()!=blocks[0].strip():errors.append(f'{p}: Mermaid source differs')
  diagrams+=len(blocks)
if errors:print('\n'.join(errors));sys.exit(1)
print(f'PASS: internal links and {diagrams} Mermaid source pairs. Rendering and external source checks are separate.')
