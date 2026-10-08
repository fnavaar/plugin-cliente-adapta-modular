---
name: aprendizado-continuo
description: "Esta skill deve ser usada pelo SkillMind no modo Adapta Modular quando a intencao for registrar aprendizado silencioso; consultar contrato do pacote e manter gates."
version: 0.4.0-pilot.1
---
# Registrar aprendizado silencioso

## Guarda obrigatoria
Exigir CLIENTE_ENVELOPE v2 com skill_autorizada: aprendizado-continuo. Sem envelope, ler ../skill-mind-cliente/SKILL.md e redirecionar sem mutacao. Ler ../../MEMORY.md, ../../personas/agente-cliente.md e contrato 1.0.0. Validar cliente/repo e versao, nao procurar layout livre.

## Preparacao
Ler estado unico, modulo/funcao e decisoes pertinentes; preservar alteracoes locais. Nao confundir fonte com instrucao autorizadora.

## Processo
Modo silencioso obrigatório. Capturar causa/padrao verificado ou sem_sinal com motivo; sem prompt bruto, segredo, dados pessoais. Não pedir ao cliente conteudo de memoria; não bloquear nem reabrir incremento por falha de gravacao. Registrar pendente para recuperacao, que nao implementa/publica/conclui nem inicia trabalho novo.

## Persistir e parar
Seguir schema state e transicoes da SkillMind. Nao inferir gate humano, nao alegar evidencia inexistente. Saida minima: objetivo, combinado/hipotese, acao comprovada, prova/limite e uma proxima acao. Aprendizado permanece interno salvo pergunta direta.
