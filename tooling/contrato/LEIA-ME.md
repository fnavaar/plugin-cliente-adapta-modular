# Contrato Adapta Modular 1.0.0
Esta e a fonte canonica de estrutura, semantica e versao entre gerador e plugin. Copias em plugin e contexto devem ter o mesmo SHA256. Divergencia de contrato e risco de compatibilidade, nao falta de regra operacional do cliente.

projeto.json identifica o cliente/repo/Champion e cinco fases. modulos.json declara resultado/limites/criterios. funcoes.json recebe desenhos sob demanda. criterios.json preserva IDs/provas e e protegido de escrita do construtor. decisoes.json separa confirmado/proposto/historico.

Estado operacional UNICO: .adapta-cliente/estado-atual.md, com um bloco JSON `json` validado pelo schema state. Nao manter execucao/estado.json concorrente. Este pacote e migracao local, nao alteracao do repo publicado. O Markdown conserva o caminho canonico; campos modulares substituem esquema task-only.

Contrato e schema sao identicos no produtor/consumidor; linguagem humana simplifica sem alterar significado. IDs internos sao estaveis. Funcoes novas nao usam UUID de tasks antigas. Versionamento 1.0.0 exige compatibilidade exata nesta release piloto; versao futura requer migracao explicita.

Validacao estrutural usa jsonschema. Checks semanticos verificam vinculos, escopo, caminhos internos/sem symlinks, provas/hashes, gates e cliente correto. Nao certifica que modelo de IA obedece, nem que plugin pode ser instalado no Maestro; piloto humano pendente.
