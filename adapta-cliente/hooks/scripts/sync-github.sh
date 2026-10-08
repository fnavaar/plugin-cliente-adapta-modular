#!/usr/bin/env bash
# Hook opcional informativo. Sem staging/commit/push automatico: publicacao exige autorizacao explicita de alvo e arquivos.
cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null || exit 0
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git status --short
fi
exit 0
