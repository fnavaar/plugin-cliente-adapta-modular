#!/usr/bin/env python3
"""Gerador de pacote Adapta Modular a partir de entrada estruturada e assets autorizados.
CLI: gerar-pasta.py entrada.json --assets DIR --dest DIR --plugin DIR --client-id ID --repo OWNER/REPO
Contrato/paths/semantica FIXOS; conteudo vem da entrada, nunca adivinhado. Sem overwrite/remoto.
"""
from pathlib import Path
import json,argparse,shutil,importlib.util,re
BASE=Path(__file__).resolve().parent
for n,file in [('v','validar.py'),('g','selar.py')]:
 sp=importlib.util.spec_from_file_location(n,BASE/file);globals()[n]=importlib.util.module_from_spec(sp);sp.loader.exec_module(globals()[n])
def generate(inputfile,assets,dest,plugin,client,repo):
 data=json.loads(Path(inputfile).read_text());assets=Path(assets).resolve();dest=Path(dest)
 if dest.exists():raise ValueError('Destino existente: gerador nao sobrescreve trabalho')
 if set(data)!={'project','modules','criteria','functions','decisions','sources','state','asset_paths'}:raise ValueError('entrada deve conter exatamente os campos canonicos')
 if data['project']['client_id']!=client or data['project']['context_repo']!=repo:raise ValueError('identidade fornecida nao corresponde a entrada')
 reserved=['contrato/','projeto.json','produto/modulos.json','produto/funcoes.json','validacao/criterios.json','contexto/decisoes.json','contexto/fontes.json','.adapta-cliente/estado-atual.md','manifest.json','execucao/estado.json']
 for rel in data['asset_paths']:
  p=Path(rel)
  if p.is_absolute() or '..' in p.parts or any(rel==x or (x.endswith('/') and rel.startswith(x)) for x in reserved):raise ValueError('asset path invalido/reservado: '+rel)
  q=assets/p
  if not q.is_file() or q.is_symlink() or not q.resolve().is_relative_to(assets):raise ValueError('asset ausente/externo: '+rel)
 dest.mkdir(parents=True);shutil.copytree(BASE/'contrato',dest/'contrato')
 for rel in data['asset_paths']:
  p=dest/rel;p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(assets/rel,p)
 paths={'project':'projeto.json','modules':'produto/modulos.json','criteria':'validacao/criterios.json','functions':'produto/funcoes.json','decisions':'contexto/decisoes.json','sources':'contexto/fontes.json'}
 for key,rel in paths.items():
  p=dest/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(data[key],ensure_ascii=False,indent=2)+'\n')
 p=dest/'.adapta-cliente/estado-atual.md';p.parent.mkdir(parents=True,exist_ok=True);p.write_text('# Estado atual — Adapta Cliente\n\nFonte unica do pacote.\n\n```json\n'+json.dumps(data['state'],ensure_ascii=False,indent=2)+'\n```\n')
 g.seal(dest);result=v.validate(dest,plugin,client,repo)
 if not result['valid']:raise ValueError('Pacote gerado NAO COMPATIVEL; nao publicar: '+json.dumps(result['errors'],ensure_ascii=False))
 return result
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('--assets',required=True);ap.add_argument('--dest',required=True);ap.add_argument('--plugin',required=True);ap.add_argument('--client-id',required=True);ap.add_argument('--repo',required=True);a=ap.parse_args()
 print(json.dumps(generate(a.input,a.assets,a.dest,a.plugin,a.client_id,a.repo),ensure_ascii=False,indent=2))
