# Índice das Cursor Rules

Documentação das Project Rules em `.cursor/rules/*.mdc`. As rules reais são os arquivos `.mdc`; este índice é referência para o time.

**Skills de workflow:** `.cursor/skills/` — workflows longos (env/debug, CI, OTEL, Swarm, descoberta de negócio, auditoria).

## Como o Cursor aplica as rules

Cada `.mdc` possui cabeçalho YAML:

```yaml
---
description: Descrição da rule
globs: "padrão de arquivos"
alwaysApply: true ou false
---
```

- `alwaysApply: true` — contexto global (stubs curtos; implementação nas Skills/docs).
- `alwaysApply: false` — conforme `globs` ou relevância do Agent.
- Rules **manual** — invocar no chat ou usar a Skill correspondente.

## Fluxo arquitetural

```text
Endpoint -> Service -> CRUD -> Banco
Endpoint -> Service -> Core Client -> API externa
```

## Rules globais (always)

| Arquivo | Função |
|---------|--------|
| `005-rule-vs-skill-gate-always.mdc` | Gate Rule vs Skill — perguntar antes de criar rule operacional grande |
| `000-project-context-always.mdc` | Stack, camadas, regras globais resumidas |
| `010-architecture-always.mdc` | Dependências entre camadas, novo módulo |
| `080-security-config-always.mdc` | Secrets, `.env`, credenciais |
| `333-observability-otel-loki-always.mdc` | Princípios OTEL/Loki (implementação na Skill + docs) |

## Rules por camada (auto)

| Arquivo | Função |
|---------|--------|
| `020-fastapi-endpoints-auto.mdc` | Endpoints leves |
| `030-services-auto.mdc` | Regras de negócio em services |
| `040-crud-auto.mdc` | CRUD só acesso ao banco |
| `045-crud-transaction-commit-auto.mdc` | `commit: bool`, transação única |
| `046-alembic-version-table-auto.mdc` | Tabela de versão Alembic |
| `050-schemas-models-auto.mdc` | Schemas vs models |
| `060-core-integrations-auto.mdc` | Clients externos, OAuth, mTLS |
| `070-tests-auto.mdc` | Pytest por camada |
| `075-github-actions-ci-auto.mdc` | Stub CI → Skill `configurar-ci-github-actions` |
| `090-docs-readme-auto.mdc` | READMEs por pasta |
| `095-project-readme-sync-auto.mdc` | README + Alterações recentes |
| `110-python-style-auto.mdc` | Estilo Python |
| `115-reusable-core-abstractions-auto.mdc` | Stub abstrações → `docs/cursor/core-abstractions.md` |
| `131-docker-swarm-stack-auto.mdc` | Stub stack → Skill `deploy-swarm-fastapi` |
| `132-github-actions-swarm-deploy-auto.mdc` | Stub workflow deploy Swarm |

## Rules / Skills manuais

| Rule (stub) | Skill | Quando usar |
|-------------|-------|-------------|
| `085-fastapi-env-debug-manual.mdc` | `migrar-env-debug-fastapi` | `.env`, `launch.json`, perfis homolog/prod |
| `100-task-workflow-agent.mdc` | `executar-tarefa-template-fastapi` | Tarefas maiores no template |
| `120-business-rules-discovery-manual.mdc` | `descobrir-regras-negocio` | Mapear regras em projeto legado |
| `130-fastapi-swarm-deploy-manual.mdc` | `deploy-swarm-fastapi` | Deploy Docker Swarm (gate APP_PORT/STACK_NAME) |

Skills adicionais em `.cursor/skills/`:

- `aplicar-template-cursor-projeto` — aplicar template/rules em projeto existente
- `auditar-rules-skills-docs` — auditoria de rules/skills/docs
- `configurar-ci-github-actions` — pipeline GitHub Actions
- `implementar-otel-loki-fastapi` — implementação completa OTEL+Loki
- `deploy-swarm-fastapi` — Dockerfile, stack, workflow GHCR

## Rules de negócio (padrão — não versionadas no template)

Criar no projeto real quando a regra for confirmada:

```text
.cursor/rules/2xx-business-<dominio>-auto.mdc
```

Exemplos fictícios (substituir pelo domínio real):

| Arquivo exemplo | Domínio |
|-----------------|---------|
| `200-business-orders-auto.mdc` | Pedidos / ordens de serviço |
| `210-business-permissions-auto.mdc` | Permissões e grupos |
| `220-business-invoices-auto.mdc` | Faturamento |

## `.cursor/business-rules/`

Documentação auxiliar (hipóteses, perguntas, decisões). **Não substitui** `.cursor/rules/*.mdc`.

Fluxo: análise → `.cursor/business-rules/` → confirmação → `.cursor/rules/2xx-business-<dominio>-auto.mdc`

## Quando criar nova rule

Crie quando houver padrão recorrente: auth, mensageria, migrations, workers, logs, regra de domínio.

Não crie para orientação pontual — use `docs/` ou README da pasta.

Workflow operacional longo → **Skill** (rule `005-rule-vs-skill-gate-always.mdc` orienta a questionar o usuário antes de criar `.mdc`).

## Links

- [Guia projetos existentes](./README.md)
- [Prompts](./PROMPTS.md)
- [Observabilidade — referência](../observability/reference.md)
- [Abstrações core](./core-abstractions.md)
- [Skills do projeto](../../.cursor/skills/)
- [Índice detalhado das rules](../../.cursor/rules/README.md)
