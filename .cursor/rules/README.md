# Rules do Cursor

Esta pasta contém as Project Rules usadas pelo Cursor para orientar a geração, alteração e revisão de código neste padrão FastAPI.

As rules reais são os arquivos `.mdc`. Este `README.md` é apenas documentação para o time.

**Skills de workflow:** `.cursor/skills/` — ver [índice](../../docs/cursor/rules-index.md) e [README das skills](../skills/README.md).

## Como o Cursor aplica as rules

Cada arquivo `.mdc` possui um cabeçalho com:

```yaml
---
description: Descrição da rule
globs: "padrão de arquivos"
alwaysApply: true ou false
---
```

- `alwaysApply: true`: a rule entra como contexto global (stubs curtos para workflows longos).
- `alwaysApply: false`: a rule é aplicada conforme o arquivo/escopo indicado em `globs` ou quando o Agent julgar relevante.
- Workflows operacionais longos: **Skill** em `.cursor/skills/` (rules manuais/auto são stubs que apontam para a Skill).

## Fluxo arquitetural esperado

Para operações de banco:

```text
Endpoint -> Service -> CRUD -> Banco
```

Para integrações externas:

```text
Endpoint -> Service -> Core Client -> API externa
```

## O que cada rule faz

### `005-rule-vs-skill-gate-always.mdc`

Gate global: antes de criar rule operacional grande, avaliar se o conteúdo deve ser **Skill** (`.cursor/skills/`), **docs** ou **Rule**. Questionar o usuário quando o pedido parecer workflow reutilizável.

### `000-project-context-always.mdc`

Define o contexto global do projeto: stack, camadas, fluxo arquitetural e regras gerais.

### `010-architecture-always.mdc`

Define regras de arquitetura, dependência entre camadas e como criar novos módulos.

### `020-fastapi-endpoints-auto.mdc`

Define o padrão para endpoints FastAPI leves, sem regra de negócio pesada.

### `030-services-auto.mdc`

Define como criar services com validações, normalizações, orquestração e regras de negócio.

### `040-crud-auto.mdc`

Define que CRUD deve cuidar apenas de acesso ao banco, filtros, paginação e persistência.

### `050-schemas-models-auto.mdc`

Define separação entre schemas Pydantic e models SQLAlchemy, além do padrão Base/Create/Update/Response.

### `060-core-integrations-auto.mdc`

Define regras para clients externos, OAuth2, API Key, Bearer Token, Basic Auth, certificados, mTLS e tratamento de erro externo.

### `070-tests-auto.mdc`

Define estrutura e padrão de testes usando pytest, AsyncMock e testes por camada.

### `075-github-actions-ci-auto.mdc`

Stub por glob — aponta para Skill `configurar-ci-github-actions`. Princípios: pytest unitário, UTF-8 em requirements, `ci.yml` separado de deploy. Template: `docs/cursor/templates/ci.yml`.

### `080-security-config-always.mdc`

Define regras globais de segurança para não versionar secrets, tokens, senhas, certificados ou `.env` real.

### `085-fastapi-env-debug-manual.mdc`

Stub manual — Skill `migrar-env-debug-fastapi`. Invocar `@085-fastapi-env-debug-manual` para `.env`, `example-config`, `launch.json`.

### `090-docs-readme-auto.mdc`

Define padrões para documentação e READMEs por pasta, evitando redundância.

### `095-project-readme-sync-auto.mdc`

Define regras para manter o README real do projeto atualizado, incluindo uma tabela de `Alterações recentes`.

### `100-task-workflow-agent.mdc`

Stub manual — Skill `executar-tarefa-template-fastapi`. Fluxo para tarefas multi-camada no template.

### `110-python-style-auto.mdc`

Define estilo geral para código Python, imports, async, logs, erros e organização.

### `115-reusable-core-abstractions-auto.mdc`

Stub por glob — princípios curtos; detalhes em `docs/cursor/core-abstractions.md`. Avaliar se nova classe vai para `core/` ou `services/`.

### `120-business-rules-discovery-manual.mdc`

Stub manual — Skill `descobrir-regras-negocio`. Mapear regras de negócio em projeto legado e propor rules `2xx-business-*`.

### `130-fastapi-swarm-deploy-manual.mdc`

Stub manual — Skill `deploy-swarm-fastapi`. Gate: perguntar `APP_PORT`, `STACK_NAME`, ASGI antes de gerar arquivos. Contexto: `docs/contexto_infra_swarm_cursor.md`.

### `131-docker-swarm-stack-auto.mdc`

Stub por glob — Skill `deploy-swarm-fastapi`. Dockerfile, stack, `.dockerignore`, `.env.example`.

### `132-github-actions-swarm-deploy-auto.mdc`

Stub por glob — Skill `deploy-swarm-fastapi`. Workflow `deploy-swarm.yml` separado de `ci.yml`.

### `333-observability-otel-loki-always.mdc`

Rule global (always) com **princípios** OTEL/Tempo/Loki. Implementação: Skill `implementar-otel-loki-fastapi` + `docs/observability/reference.md`.

### Rules de negócio `2xx` (exemplos — não versionadas no template)

Criar no projeto real quando confirmado:

```text
.cursor/rules/2xx-business-<dominio>-auto.mdc
```

Exemplos fictícios:

- `200-business-orders-auto.mdc` — pedidos / ordens de serviço
- `210-business-permissions-auto.mdc` — permissões e grupos
- `220-business-invoices-auto.mdc` — faturamento


## Sobre `.cursor/business-rules/`

É permitido criar uma pasta auxiliar:

```text
.cursor/business-rules/
```

Essa pasta serve para documentação de apoio sobre regras de negócio descobertas em projetos existentes, como perguntas pendentes, decisões e rascunhos.

Ela **não deve substituir** `.cursor/rules/`.

- Rules ativas do Cursor: `.cursor/rules/*.mdc`
- Documentação auxiliar de negócio: `.cursor/business-rules/*.md`

Quando uma regra de negócio for confirmada e precisar orientar o Cursor em futuras alterações, crie ou atualize uma rule `.mdc` em `.cursor/rules/`, normalmente no padrão:

```text
.cursor/rules/2xx-business-<dominio>-auto.mdc
```

## Quando criar uma nova rule

Crie uma nova rule quando houver um padrão recorrente que o time quer aplicar automaticamente, por exemplo:

- padrão específico de autenticação;
- padrão de mensageria;
- padrão de migrations;
- padrão de workers/jobs;
- padrão de deploy;
- padrão de logs/auditoria;
- regra de negócio específica de um domínio;
- regra reutilizável descoberta em projeto existente.

## Quando não criar uma nova rule

Não crie rule para uma orientação pontual ou temporária. Nesse caso, documente em `docs/` ou no README da pasta específica.

## Importante

- Rules **always** e rules por **camada** (020–070) mantêm instruções completas no `.mdc`.
- Rules de **workflow longo** são **stubs** — implementação nas Skills e em `docs/`.
- Índice principal para entry points: `docs/cursor/rules-index.md`.
- Não duplicar workflow inteiro em nova rule — usar Skill (rule `005-rule-vs-skill-gate-always.mdc`).
