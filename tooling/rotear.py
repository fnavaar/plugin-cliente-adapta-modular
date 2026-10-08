#!/usr/bin/env python3
"""Roteamento local de referencia: recebe estado e intencao estruturada, nunca escreve/app/tools.
Complementa as instrucoes da SkillMind; nao conecta nem substitui Maestro.
"""
import json,sys
MAP={'contexto':'entender-contexto','necessidade':'explorar-necessidade','funcao':'desenhar-funcao','interface':'desenhar-interface','analisar':'proxima-task','executar':'executar-task','falha':'debug-task','comparar':'comparar-modulo','concluir':'concluir-task','status':'status','aprender':'aprendizado-continuo'}
def route(state,intent):
 if intent not in MAP:return {'allowed':False,'reason':'intencao_desconhecida','skill':None}
 stage=state['stage']
 if intent in ['contexto','necessidade','funcao','interface','status','aprender','comparar']:
  return {'allowed':True,'skill':MAP[intent],'write_app':False,'reason':'consulta_design_seguro_preview_mutante_exige_gate'}
 if intent=='executar':
  if stage!='aguardando_autorizacao' or state['authorization'] is None:return {'allowed':False,'skill':None,'reason':'gate_autorizacao_pendente'}
  return {'allowed':True,'skill':'executar-task','write_app':True,'reason':'revalidar_contrato_recorte_e_autorizacao_posterior_antes_de_escrever'}
 if intent=='concluir':
  if stage!='aguardando_teste_humano' or state['human_test']['result']!='aprovado':return {'allowed':False,'skill':None,'reason':'gate_teste_humano_pendente'}
  return {'allowed':True,'skill':'concluir-task','write_app':False,'reason':'revalidar_todas_provas_atuais_antes_de_concluir'}
 if intent=='falha':
  if not state['increment_id']:return {'allowed':False,'skill':'entender-contexto','reason':'triagem_sem_incremento_ativo','write_app':False}
  return {'allowed':True,'skill':'debug-task','write_app':False,'reason':'diagnosticar_primeiro_confirmar_autorizacao_antes_da_correcao'}
 if stage in ['aguardando_teste_humano','implementando','verificando','em_correcao','aguardando_autorizacao']:
  return {'allowed':False,'skill':None,'reason':'retomar_incremento_ativo_sem_abrir_outro'}
 return {'allowed':True,'skill':'proxima-task','write_app':False,'reason':'analisar_ou_codesenhar_sem_implementar'}
if __name__=='__main__':
 obj=json.load(sys.stdin);print(json.dumps(route(obj['state'],obj['intent']),ensure_ascii=False))
