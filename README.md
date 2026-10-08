# Adapta Cliente Modular — piloto 0.4.0-pilot.1
Réplica estrutural da base 0.3.0 commit 36154ba. Nao instalada/publicada neste run. Caminhos da base preservados; manifests identificam variante isolada. Nao carregar ambos os plugins/memorias no mesmo assistente.

Pacote cliente deve cumprir contrato Adapta Modular 1.0.0 e client_id/context_repo fornecidos explicitamente; plugin nao interpreta estrutura livre. Ler adapta-cliente/contrato/LEIA-ME.md. Co-desenhar funcao → interface → plano → autorizacao posterior → construir → provar → teste humano. Nao fila tecnica predeterminada.

No ETHOS/MAESTRO, usar mecanismo real disponivel de carregar bundle, ainda nao validado; copiar adapta-cliente/MEMORY.md integralmente para personalizacao apos remover regras legadas conflitantes. Nao presumir autodiscovery, cron ou hooks. Conferir versao/modo/contexto lidos com pedido de status antes de qualquer escrita. Não afirmar instalacao no Maestro a partir de ZIP/documentos.

npm test verifica estrutura/contratos da replica. Python validar.py no kit valida pacote/relacoes/gates. Passes locais nao certificam obediencia do LLM, instalacao ou app. Publicar/plugin externo requer confirmacao nova. Repo Holder antigo e app intactos.

## Ferramentas compartilhadas
`tooling/` contém gerador e validador; o contexto fica somente no repo do cliente. Usar `python3 tooling/validar.py CAMINHO_CONTEXTO --plugin . --client-id ID --repo OWNER/REPO`. Instalar jsonschema; contrato da pasta deve corresponder ao bundle. Repo privado fnavaar/plugin-cliente-adapta-modular; publicação não equivale a instalação no Maestro.
