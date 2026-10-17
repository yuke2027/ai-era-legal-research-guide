"""Extract Mermaid sources and attach stable SVG/source links to Markdown."""
from pathlib import Path
import re,os
ROOT=Path(__file__).resolve().parents[1]
def diagram_name(p):
 if p.parent.name=='sops':return 'sop-'+p.stem
 if p.parent.name=='walkthroughs':return 'example-'+p.stem
 return p.stem
for p in sorted((ROOT/'docs').rglob('*.md')):
 s=p.read_text();blocks=re.findall(r'```mermaid\n(.*?)\n```',s,re.S)
 if not blocks:continue
 if len(blocks)!=1:raise ValueError(f'Expected one diagram: {p}')
 name=diagram_name(p);target=ROOT/'diagrams/sources'/f'{name}.mmd';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(blocks[0]+'\n')
 src=os.path.relpath(target,p.parent);svg=os.path.relpath(ROOT/'diagrams/previews'/f'{name}.svg',p.parent)
 s=re.sub(r'\n<!-- diagram-links -->.*?<!-- /diagram-links -->\n','\n',s,flags=re.S)
 end=s.index('\n```',s.index('```mermaid'))+4
 s=s[:end]+f'\n\n<!-- diagram-links -->\n[独立 SVG 图谱]({svg}) · [Mermaid 源文件]({src})\n<!-- /diagram-links -->\n'+s[end:]
 p.write_text(s)
print('Diagram sources synchronized.')
