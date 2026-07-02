# Instruções para agentes de código

Este projeto segue o padrão:

```text
Endpoint -> Service -> CRUD -> Banco
Endpoint -> Service -> Core Client -> API externa
```

## Documentação

- [Índice das rules](docs/cursor/rules-index.md)
- [Guia projetos existentes](docs/cursor/README.md)
- [Prompts](docs/cursor/PROMPTS.md)

## Skills (workflows longos)

| Skill | Quando |
|-------|--------|
| `aplicar-template-cursor-projeto` | Aplicar template/rules em projeto existente |
| `executar-tarefa-template-fastapi` | Tarefas multi-arquivo, novo módulo |
| `descobrir-regras-negocio` | Mapear projeto legado, rules 2xx |
| `migrar-env-debug-fastapi` | `.env`, launch.json, perfis |
| `configurar-ci-github-actions` | Pipeline GitHub Actions |
| `implementar-otel-loki-fastapi` | OTEL, Tempo, Loki |
| `deploy-swarm-fastapi` | Docker Swarm — Dockerfile, stack, GHCR |
| `auditar-rules-skills-docs` | Reorganizar rules/docs |

Local: `.cursor/skills/<nome>/SKILL.md`

## Regras principais

- Antes de criar rule nova: avaliar Rule vs Skill vs docs (rule `005-rule-vs-skill-gate-always.mdc`)

- endpoint deve ser leve;
- service contém regra de negócio;
- CRUD contém apenas acesso ao banco;
- schemas e models devem ficar separados;
- não versionar secrets;
- manter README do projeto real atualizado com alterações relevantes.


Regras complementares:

- antes de criar uma classe nova, avaliar se ela é reutilizável e se deve virar abstração em `core/`;
- quando uma regra de negócio importante for descoberta, criar ou atualizar uma Cursor Rule específica em `.cursor/rules/`;
- para projetos existentes, usar a rule manual `120-business-rules-discovery-manual.mdc` antes de criar endpoints em domínios com regras complexas;
- para deploy em Docker Swarm, invocar Skill `deploy-swarm-fastapi` ou rule `130-fastapi-swarm-deploy-manual.mdc` (perguntar `APP_PORT` e `STACK_NAME` antes de gerar arquivos); rules `131` e `132` aplicam-se a Dockerfile/stack e workflow `deploy-swarm.yml`.


Quando mapear regras de negócio de projetos existentes, use `.cursor/business-rules/` apenas como documentação auxiliar. Rules ativas devem continuar em `.cursor/rules/*.mdc`.
