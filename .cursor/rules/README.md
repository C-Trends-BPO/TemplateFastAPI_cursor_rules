# Rules do Cursor

Esta pasta contém as Project Rules usadas pelo Cursor para orientar a geração, alteração e revisão de código neste padrão FastAPI.

As rules reais são os arquivos `.mdc`. Este `README.md` é apenas documentação para o time.

## Como o Cursor aplica as rules

Cada arquivo `.mdc` possui um cabeçalho com:

```yaml
---
description: Descrição da rule
globs: "padrão de arquivos"
alwaysApply: true ou false
---
```

- `alwaysApply: true`: a rule entra como contexto global.
- `alwaysApply: false`: a rule é aplicada conforme o arquivo/escopo indicado em `globs` ou quando o Agent julgar relevante.
- `globs`: define os arquivos/pastas onde a rule faz sentido.

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

Define pipeline GitHub Actions para pytest unitário: template `ci.yml`, env fictício de CI, cópia de `example-config.py`, marker `integration` fora do pipeline e **UTF-8 obrigatório** em `requirements.txt` (com step de verificação e comando de correção). Template em `docs/cursor/templates/ci.yml`.

### `080-security-config-always.mdc`

Define regras globais de segurança para não versionar secrets, tokens, senhas, certificados ou `.env` real.

### `085-fastapi-env-debug-manual.mdc`

Rule **manual** para FastAPI com start manual: `core/config.py` lendo `.env`, `core/example-config.py` para CI, `.env.example` com perfis prod/homolog e `.vscode/launch.json`. Invocar com `@085-fastapi-env-debug-manual`. Globs limitados aos arquivos de config/debug; `alwaysApply: false`. Templates em `docs/cursor/templates/`.

### `090-docs-readme-auto.mdc`

Define padrões para documentação e READMEs por pasta, evitando redundância.

### `095-project-readme-sync-auto.mdc`

Define regras para manter o README real do projeto atualizado, incluindo uma tabela de `Alterações recentes`.

### `100-task-workflow-agent.mdc`

Define um fluxo de trabalho para o Agent executar tarefas maiores com consistência.

### `110-python-style-auto.mdc`

Define estilo geral para código Python, imports, async, logs, erros e organização.

### `115-reusable-core-abstractions-auto.mdc`

Define que, antes de criar uma nova classe Python, o Cursor deve avaliar se ela pode ser reutilizada futuramente. Se a classe representar uma capacidade técnica genérica, como envio de e-mail, storage, geração de PDF, QR Code, mensageria, autenticação externa ou client reutilizável, ela deve ser considerada para criação em `core/` como abstração ou classe base.

Essa rule ajuda a evitar duplicação e impede que capacidades reutilizáveis fiquem presas dentro de um service específico.

### `120-business-rules-discovery-manual.mdc`

Rule manual para projetos já em andamento. Ela orienta o Cursor a analisar o diretório inteiro do projeto, identificar regras de negócio reais, fazer perguntas ao usuário e propor novas rules específicas para garantir que novos endpoints respeitem as regras existentes.

Use essa rule manualmente quando for mapear um projeto legado ou quando uma nova regra de negócio importante for descoberta durante o desenvolvimento.

### `130-fastapi-swarm-deploy-manual.mdc`

Rule **manual** para adaptar FastAPI a produção no Docker Swarm (HAProxy → Swarm em `192.168.0.223/224/225`). Invocar com `@130-fastapi-swarm-deploy-manual`. **Gate obrigatório:** perguntar `APP_PORT`, `STACK_NAME`, módulo ASGI e domínio/CORS antes de gerar arquivos. Orquestra Dockerfile, `deploy/stack.yml`, `deploy-swarm.yml`, `/health` e `.env.example`. Complementa `085` (dev) e `333` (OTEL; no Swarm `OTEL_APPEND_IP_SUFFIX=False`). Contexto: `docs/contexto_infra_swarm_cursor.md`.

### `131-docker-swarm-stack-auto.mdc`

Rule por glob para `Dockerfile`, `deploy/**`, `.dockerignore`, `.env.example`, `.editorconfig` e `.gitattributes`. Define stack com `mode: host`, `stop-first`, rede `app_network`, healthcheck `/health`, `CACHE_BUST` e script `force-image-rollout.sh`. Templates em `docs/cursor/templates/`.

### `132-github-actions-swarm-deploy-auto.mdc`

Rule por glob para `.github/workflows/deploy*.yml` e `*swarm*.yml`. Pipeline separado de `ci.yml`: runner `[self-hosted, linux, swarm]`, build GHCR com `CACHE_BUST`, `docker pull`, `stack deploy --with-registry-auth`, wait 600s com validação `3/3` na mesma tag SHA. Alembic opcional (sem `manage.py migrate`). Template: `docs/cursor/templates/deploy-swarm.yml`.

### `200-business-auth-token-auto.mdc`

Regras de autenticação JWT: login, refresh, validate, arquitetura multi-sistema, validade de 1 hora, erros unificados, logs e rate limit.

### `210-business-auth-permissions-auto.mdc`

Regras de resolução de permissões Django: grupos, permissões diretas, `is_staff`, `content_type_id` por sistema integrado.

### `220-business-arancia-messager-auto.mdc`

Regras do endpoint Arancia Messager: `content_type_id=31`, contrato de resposta sem `is_staff`.


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

Não substitua o conteúdo das rules por uma frase apontando para este README. O Cursor precisa das instruções completas dentro de cada `.mdc` para aplicar corretamente os padrões durante a geração de código.
