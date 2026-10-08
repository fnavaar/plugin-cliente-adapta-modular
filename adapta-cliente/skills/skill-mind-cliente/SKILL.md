---
name: skill-mind-cliente
description: Entrada unica vinculada ao contrato Adapta Modular 1.0.0; interpretar contexto, necessidade, funcao, interface e incremento no pacote autorizado, preservando autorizacao/teste e retomada sem hooks.
version: 0.4.0-pilot.1
---
# SkillMind Cliente — modo modular

## 1. Interpretar e localizar
Ler ../../MEMORY.md, ../../personas/agente-cliente.md, ../../contrato/contrato.json e schemas.json. Resolver repo/pasta explicitamente fornecidos, conferir projeto.json/client_id/context_repo/contract_version, contrato hash e estado .adapta-cliente/estado-atual.md. Nao caminhar para fase.md como requisito nem procurar outro cliente. Se nao compativel, explicar incompatibilidade e nao alterar app; corrigir pacote por gerador/consultoria, nao adivinhar. Scripts sao apoio opcional; mesmo sem runner cumprir checks do contrato inline.

## 2. Envelope
CLIENTE_ENVELOPE v2
pedido_original: pedido preservado
modo_execucao: modular
rota: contexto|necessidade|funcao|interface|analisar|executar|debugar|comparar|concluir|status|aprender
skill_autorizada: nome da filha
client_id: projeto validado
module_id: modulo ativo ou nenhuma
function_id: funcao ou nenhuma
increment_id: incremento ou nenhuma
contrato_version: 1.0.0
etapa_atual: estado real
autorizacao_implementacao: ausente|confirmada e recorte
teste_humano: pendente|aprovado|falhou|nao_aplicavel

## 3. Rotear por intencao/estado
Contexto→entender-contexto; ideia/problema→explorar-necessidade; definir funcionamento→desenhar-funcao; jornada/tela→desenhar-interface; plano/construir→proxima-task; autorizacao posterior→executar-task; falha→debug-task; comparar→comparar-modulo; teste aprovado/concluir→concluir-task; status→status; manutencao→aprendizado-continuo. Nomes task sao aliases de incremento, nao sequencia tecnica antiga. Selecionar uma filha por etapa, nao misturar fluxos.

Gate pendente impede nova implementacao, nao leitura/consulta/desenho seguro. Funcoes surgem sob demanda dentro de modulo; preferencia do usuario e dependencias reais, nao fila predeterminada. Acesso/regras dados faltantes devem gerar pergunta embutida ao Champion, nunca valor inventado; partes independentes continuam. Risco de seguranca/perda/calculo errado contem dominio afetado. Fora do escopo registrar ideia/decisao do consultor sem criar dependencia artificial.

## 4. Dois hard stops
Depois de proxima-task apresentar plano e parar em aguardando_autorizacao. Relatorio deve estar em resposta anterior; nova mensagem do usuario deve autorizar increment_id/version/recorte. Confirmacao visual/funcao nao vale autorizacao nem teste. Antes da mutacao revalidar pacote, contexto/codigo/ambiente inspecionado e diff. Depois executar-task/debug-task provar e pedir teste humano; encerrar resposta em aguardando_teste_humano. Nao concluir nem abrir proxima task/incremento. Falha vence palavra concluir.

## 5. Estado persistente e fechamento
Usar exclusivamente .adapta-cliente/estado-atual.md com bloco JSON schema state do contrato compartilhado. Registrador valida campos/vinculos/gates; desconhecidos null, nunca fake. Nao manter outro estado JSON independente. etapa/state alterada antes/depois de escrita; snapshots/evidencias sanitizados ligados a criterio+commit+runtime. Antes de incremento_concluido exigir teste explicito e todos os criterios cobertos pela funcao pass reais na versao verificada. Aceite de modulo/fase separado; agente nao aprova gates humanos do consultor.

## 6. Sem dependencia de hooks/agentes
Ler skill autorizada e executar inline quando runtime limitado. Aplicar verificador em serie se sem subagente. Guardas antes de cada escrita; hooks nao concedem publicacao. Aprendizado silencioso nao bloqueia; recuperacao nao inicia trabalho, implementa, publica ou aceita. Relatorio comparativo interno vai ao consultor para validar antes da devolutiva; provas da propria execucao podem ser mostradas ao Champion sem fingir auditoria humana.

## Saida minima
Objetivo, etapa, combinado/hipotese, acao comprovada, evidencia/limite e proxima acao. Conversa em negocio; tecnicamente detalhar o suficiente para implementar/testar, sem exigir siglas ao Champion. Nao mascarar decisao imposta ou negar que ha um contrato de funcionamento.

## Checks prospectivos e manifesto
Registrar checks da funcao antes da implementacao, sem editar criterios do modulo. Conclusao exige evidencia de criterios vinculados E checks da funcao, mesmo code_commit/runtime_version, hash do arquivo e teste humano posterior. Recalcular manifesto local apos alteracao autorizada no pacote com selar.py; selar nao aprova gate nem publica. Arquivos de contrato/contexto/criterios protegidos nao sao alterados pelo construtor. Sem runner, conferir contrato/vinculos/versao/hashes inline e nao afirmar teste automatizado.
