"""Regera o index.html após editar data.json: python build_index.py"""
import json
from pathlib import Path
root=Path(__file__).parent
raw=json.loads((root/'data.json').read_text(encoding='utf-8'))
html=(root/'index.template.html').read_text(encoding='utf-8')
html=html.replace('__ROTEIRO_DATA__',json.dumps(raw,ensure_ascii=False,separators=(',',':')).replace('</','<\\/'))
(root/'index.html').write_text(html,encoding='utf-8')
print('index.html atualizado com',sum(len(sec['items']) for sec in raw),'itens')
