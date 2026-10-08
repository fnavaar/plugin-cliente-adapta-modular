#!/usr/bin/env python3
"""Validar contrato/projeto/relacoes/gates. CLI: validar.py PACOTE --plugin PLUGIN --client-id ID --repo OWNER/REPO.
Nao executa codigo de pacote. Paths locais sao confinados; nao publica nem altera projeto.
"""
import json,re,hashlib,sys,argparse
from pathlib import Path
from datetime import datetime
from jsonschema import Draft202012Validator
BASE=Path(__file__).resolve().parent

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def timestamp(t):
 d=datetime.fromisoformat(t.replace('Z','+00:00'))
 if d.tzinfo is None:raise ValueError('timestamp sem fuso')
 return d

def validate(root,plugin,expected_client,expected_repo):
 root=Path(root).resolve();plugin=Path(plugin).resolve();errors=[]
 def fail(msg):errors.append(msg)
 def internal(rel):
  p=Path(rel)
  if p.is_absolute() or '..' in p.parts:raise ValueError('path externo: '+rel)
  q=root/p
  if any(a.is_symlink() for a in [q,*q.parents] if a!=root.parent):raise ValueError('symlink: '+rel)
  if not q.resolve().is_relative_to(root):raise ValueError('path fora do pacote: '+rel)
  if not q.is_file():raise ValueError('arquivo ausente: '+rel)
  return q
 try:
  for name in ['contrato.json','schemas.json']:
   p=internal('contrato/'+name)
   for other in [BASE/'contrato'/name,plugin/'adapta-cliente/contrato'/name]:
    if not other.is_file() or digest(p)!=digest(other):fail('contrato nao identico: '+name)
  contract=json.loads(internal('contrato/contrato.json').read_text());schemas=json.loads(internal('contrato/schemas.json').read_text())
  loaded={}
  for kind,key in [('project','project'),('modules','modules'),('criteria','criteria'),('functions','functions'),('decisions','decisions')]:
   loaded[kind]=json.loads(internal(contract['paths'][key]).read_text())
   for e in Draft202012Validator(schemas[kind]).iter_errors(loaded[kind]):fail(kind+': '+e.message)
  md=internal(contract['paths']['state']).read_text();blocks=re.findall(r'```json\s*\n(.*?)\n```',md,re.S)
  if len(blocks)!=1:raise ValueError('estado deve conter um unico bloco JSON')
  state=json.loads(blocks[0]);loaded['state']=state
  for e in Draft202012Validator(schemas['state']).iter_errors(state):fail('state: '+e.message)
  if errors:return {'valid':False,'errors':errors}
  p=loaded['project'];mods=loaded['modules'];cs=loaded['criteria'];fs=loaded['functions'];ds=loaded['decisions']
  if p['client_id']!=expected_client or state['client_id']!=expected_client:fail('cliente incorreto')
  if p['context_repo']!=expected_repo:fail('repositorio incorreto')
  if p['phase']!=state['phase']:fail('fase do estado diverge do projeto')
  if {x['phase'] for x in p['phases']}!={1,2,3,4,5} or len(p['phases'])!=5:fail('exatamente cinco fases')
  for ph in p['phases']:
   if ph['kind']!=('systems' if ph['phase']<4 else 'loops' if ph['phase']==4 else 'validation'):fail('semantica da fase incorreta')
  for rel in p['context_files']:internal(rel)
  for group,name in [(mods,'modulo'),(cs,'criterio'),(fs,'funcao'),(ds,'decisao')]:
   if len({x['id'] for x in group})!=len(group):fail('ID duplicado '+name)
  mi={x['id']:x for x in mods};ci={x['id']:x for x in cs};fi={x['id']:x for x in fs};di={x['id']:x for x in ds}
  sources=json.loads(internal('contexto/fontes.json').read_text());sourceids={x['id'] for x in sources}
  def refs(xs):
   for x in xs:
    if x['kind']=='source' and x['ref'] not in sourceids:fail('fonte inexistente: '+x['ref'])
    if x['kind']=='decision' and x['ref'] not in di:fail('decisao inexistente: '+x['ref'])
  assigned=[]
  for m in mods:
   internal(m['content_path']);refs(m['source_refs'])
   if m['phase']!=p['phase']:fail('modulo detalhado fora da fase atual')
   if not m['criteria_ids']:fail('modulo sem criterio')
   for c in m['criteria_ids']:
    assigned.append(c)
    if c not in ci or ci[c]['module_id']!=m['id']:fail('vinculo modulo/criterio invalido: '+c)
  if len(set(assigned))!=len(assigned) or set(assigned)!=set(ci):fail('cobertura criterios incompleta/duplicada')
  for f in fs:
   refs(f['source_refs'])
   if f['module_id'] not in mi:fail('funcao sem modulo')
   if not f['criteria_ids'] or any(c not in ci or ci[c]['module_id']!=f['module_id'] for c in f['criteria_ids']):fail('funcao com criterio alheio/inexistente')
   if len(set(f['criteria_ids']))!=len(f['criteria_ids']):fail('criterio duplicado da funcao')
   if f['status']=='confirmada' and not f['checks']:fail('funcao confirmada sem prova prospectiva')
   if len({c['id'] for c in f['checks']})!=len(f['checks']) or any(c['id'] in ci for c in f['checks']):fail('ID prova prospectiva duplicado/colide criterio modulo')
   if f['status']=='confirmada' and not(f['confirmed_by'] and f['confirmed_at']):fail('funcao confirmada sem pessoa/data')
  if state['module_id'] is not None and state['module_id'] not in mi:fail('modulo ativo inexistente')
  function=fi.get(state['function_id'])
  if state['function_id'] is not None and not function:fail('funcao ativa inexistente')
  if function and function['module_id']!=state['module_id']:fail('funcao ativa fora do modulo')
  appstages=['implementando','verificando','aguardando_teste_humano','em_correcao','incremento_concluido']
  auth=state['authorization']
  if state['stage'] in appstages:
   if not function or function['status']!='confirmada':fail('implementacao sem funcao confirmada')
   if not state['increment_id'] or not auth:fail('implementacao sem autorizacao')
   else:
    if auth['increment_id']!=state['increment_id'] or (function and auth['function_version']!=function['version']):fail('autorizacao recorte/versao divergente')
    if timestamp(auth['at'])<=timestamp(auth['plan_presented_at']) or auth['message_ref']==auth['plan_message_ref']:fail('autorizacao nao posterior ao plano em nova mensagem')
   if p['environment']['verified_project_id'] is None:fail('projeto nao inspecionado')
  for e in state['evidence']:
   ep=internal(e['path'])
   if digest(ep)!=e['sha256']:fail('hash da evidencia diverge')
   if not function or e['criterion_id'] not in (function['criteria_ids']+[c['id'] for c in function['checks']]):fail('evidencia alheia ao incremento')
  h=state['human_test']
  if state['stage']=='incremento_concluido':
   if auth and h['at'] and timestamp(h['at'])<=timestamp(auth['at']):fail('teste anterior a autorizacao')
   if h['result']!='aprovado' or not h['by'] or not h['at'] or not h['message_ref'] or h['tested_increment_id']!=state['increment_id']:fail('conclusao sem teste humano explicito do incremento')
   if not state['code_commit'] or not state['runtime_version']:fail('conclusao sem versao verificada')
   for c in (function or {}).get('criteria_ids',[])+[x['id'] for x in (function or {}).get('checks',[])]:
    ev=[e for e in state['evidence'] if e['criterion_id']==c]
    if not ev or any(e['result']!='pass' or e['code_commit']!=state['code_commit'] or e['runtime_version']!=state['runtime_version'] for e in ev):fail('criterio sem PASS atual: '+c)
   if h['at'] and state['evidence']:
    if timestamp(h['at'])<=max(timestamp(e['at']) for e in state['evidence']):fail('teste humano anterior a verificacao')
  if (root/'execucao/estado.json').exists():fail('estado concorrente proibido')
  manifest=json.loads(internal('manifest.json').read_text())
  actual={str(x.relative_to(root)) for x in root.rglob('*') if x.is_file() and x.name!='manifest.json'}
  if set(manifest['files'])!=actual:fail('manifesto/inventario divergente')
  for rel,val in manifest['files'].items():
   if digest(internal(rel))!=val:fail('hash divergente: '+rel)
 except Exception as e:fail(str(e))
 return {'valid':not errors,'errors':errors,'counts':{'modules':len(loaded.get('modules',[])),'criteria':len(loaded.get('criteria',[])),'functions':len(loaded.get('functions',[]))},'limit':'Validacao documental, sem prova de runtime/LLM/app.'}

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('package');ap.add_argument('--plugin',required=True);ap.add_argument('--client-id',required=True);ap.add_argument('--repo',required=True);a=ap.parse_args()
 out=validate(a.package,a.plugin,a.client_id,a.repo);print(json.dumps(out,ensure_ascii=False,indent=2));sys.exit(0 if out['valid'] else 1)
