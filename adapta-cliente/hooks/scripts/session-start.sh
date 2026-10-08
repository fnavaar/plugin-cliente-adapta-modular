#!/usr/bin/env bash
# Leitura local opcional: nao pull automatico fora de autorizacao.
cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null || exit 0
if [ -f projeto.json ]; then head -40 projeto.json; fi
if [ -f .adapta-cliente/estado-atual.md ]; then head -60 .adapta-cliente/estado-atual.md; fi
exit 0
