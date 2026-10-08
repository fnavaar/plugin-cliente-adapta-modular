---
name: adapta-cliente:finalizar-task
description: Entrada canonica modular para concluir, mantendo envelope e gates humanos.
argument-hint: "[pedido, modulo ou funcao]"
disable-model-invocation: true
---
Carregar MEMORY.md, personas/agente-cliente.md e skills/skill-mind-cliente/SKILL.md como unica porta. Preservar $ARGUMENTS e criar CLIENTE_ENVELOPE v2 somente apos validar contrato/cliente/repo. Rotear concluir pelo estado do incremento, nao fila task-only. Respeitar plano anterior/autorizacao em nova mensagem e teste humano posterior. Nao publicar por inferencia, nao depender de hooks/subagentes.
