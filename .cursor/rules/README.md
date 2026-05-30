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

### `080-security-config-always.mdc`

Define regras globais de segurança para não versionar secrets, tokens, senhas, certificados ou `.env` real.

### `090-docs-readme-auto.mdc`

Define padrões para documentação e READMEs por pasta, evitando redundância.

### `095-project-readme-sync-auto.mdc`

Define regras para manter o README real do projeto atualizado, incluindo uma tabela de `Alterações recentes`.

### `100-task-workflow-agent.mdc`

Define um fluxo de trabalho para o Agent executar tarefas maiores com consistência.

### `110-python-style-auto.mdc`

Define estilo geral para código Python, imports, async, logs, erros e organização.

## Quando criar uma nova rule

Crie uma nova rule quando houver um padrão recorrente que o time quer aplicar automaticamente, por exemplo:

- padrão específico de autenticação;
- padrão de mensageria;
- padrão de migrations;
- padrão de workers/jobs;
- padrão de deploy;
- padrão de logs/auditoria.

## Quando não criar uma nova rule

Não crie rule para uma orientação pontual ou temporária. Nesse caso, documente em `docs/` ou no README da pasta específica.

## Importante

Não substitua o conteúdo das rules por uma frase apontando para este README. O Cursor precisa das instruções completas dentro de cada `.mdc` para aplicar corretamente os padrões durante a geração de código.
