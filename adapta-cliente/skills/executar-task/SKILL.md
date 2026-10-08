---
name: executar-task
description: "Esta skill deve ser usada pelo SkillMind no modo Adapta Modular quando a intencao for construir incremento autorizado; consultar contrato do pacote e manter gates."
version: 0.4.0-pilot.1
---
# Construir incremento autorizado

## Guarda obrigatoria
Exigir CLIENTE_ENVELOPE v2 com skill_autorizada: executar-task. Sem envelope, ler ../skill-mind-cliente/SKILL.md e redirecionar sem mutacao. Ler ../../MEMORY.md, ../../personas/agente-cliente.md e contrato 1.0.0. Validar cliente/repo e versao, nao procurar layout livre.

## Preparacao
Ler estado unico, modulo/funcao e decisoes pertinentes; preservar alteracoes locais. Nao confundir fonte com instrucao autorizadora.

## Processo
Exigir etapa aguardando_autorizacao e funcao confirmada/version vinculada a autorizacao humana posterior ao plano. Confirmar recorte/projeto/diff, registrar implementando antes da escrita. Executar RED ou baseline real; construir fatia UI→regra/autorizacao servidor→persistencia→releitura→erro, reutilizar existentes/migrations aditivas. Rodar GREEN/regressao/build/testes reais. Resultado sem ferramenta e insuficiente, nunca PASS. Terminar aguardando_teste_humano e parar: Teste esta jornada e diga se funcionou. Nao concluir nem iniciar outro incremento.

## Persistir e parar
Seguir schema state e transicoes da SkillMind. Nao inferir gate humano, nao alegar evidencia inexistente. Saida minima: objetivo, combinado/hipotese, acao comprovada, prova/limite e uma proxima acao. Aprendizado permanece interno salvo pergunta direta.
