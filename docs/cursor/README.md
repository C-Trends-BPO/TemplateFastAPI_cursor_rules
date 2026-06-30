# Guia para aplicar as Cursor Rules em projetos existentes

[Voltar para o README principal](../../README.md)

Este guia explica como aplicar as rules em projetos FastAPI já existentes.

## Passo 1: copiar os arquivos

Copie para a raiz do projeto:

```text
.cursor/
AGENTS.md
.cursorrules
```

A pasta `.cursor/rules/` deve conter os arquivos `.mdc` completos.

### Padrão `.env` + debug (FastAPI start manual)

Para projetos que sobem com `uvicorn`/`python main.py`, inclua também:

```text
.cursor/rules/085-fastapi-env-debug-manual.mdc
docs/cursor/templates/launch.json
docs/cursor/templates/env-example-header.env
docs/cursor/templates/ci.yml
```

Prompt recomendado após copiar a rule:

```text
Use a rule 085-fastapi-env-debug-manual.mdc (ou @085-fastapi-env-debug-manual).
Adapte este projeto: migre secrets para .env, crie .env.example, core/example-config.py,
.vscode/launch.json e documente execução + debug no README.
ROOT_PATH prod: /api-{nome}; homolog: /hg-api-{nome}.
PSQL_HOST prod: {host}; homolog: {host}.
Não versionar .env nem core/config.py real.
```

Templates prontos para copiar/adaptar: [`templates/launch.json`](./templates/launch.json), [`templates/env-example-header.env`](./templates/env-example-header.env), [`templates/ci.yml`](./templates/ci.yml).

### Deploy Swarm (FastAPI)

Para projetos que vão para produção no Docker Swarm (`python-app-01/02/03`), inclua também:

```text
.cursor/rules/130-fastapi-swarm-deploy-manual.mdc
.cursor/rules/131-docker-swarm-stack-auto.mdc
.cursor/rules/132-github-actions-swarm-deploy-auto.mdc
docs/contexto_infra_swarm_cursor.md
docs/cursor/templates/Dockerfile.fastapi
docs/cursor/templates/dockerignore
docs/cursor/templates/deploy/stack.yml
docs/cursor/templates/deploy-swarm.yml
docs/cursor/templates/deploy/scripts/force-image-rollout.sh
docs/cursor/templates/env-example-swarm.env
```

Prompt recomendado após copiar as rules:

```text
Use a rule 130-fastapi-swarm-deploy-manual.mdc.
Adapte este projeto FastAPI para Docker Swarm conforme docs/contexto_infra_swarm_cursor.md.
Antes de gerar arquivos, pergunte APP_PORT, STACK_NAME e módulo ASGI.
Crie Dockerfile, deploy/stack.yml, deploy-swarm.yml, /health, .env.example e scripts.
OTEL_APPEND_IP_SUFFIX=False no .env do servidor.
Não versionar .env real.
```

Templates prontos: [`templates/Dockerfile.fastapi`](./templates/Dockerfile.fastapi), [`templates/deploy/stack.yml`](./templates/deploy/stack.yml), [`templates/deploy-swarm.yml`](./templates/deploy-swarm.yml), [`templates/env-example-swarm.env`](./templates/env-example-swarm.env).

## Passo 2: abrir o projeto pela raiz

Abra no Cursor a pasta raiz do projeto, não uma subpasta.

Correto:

```text
meu-projeto-fastapi/
```

Evite abrir diretamente:

```text
meu-projeto-fastapi/api/
```

## Passo 3: analisar antes de refatorar

Use o prompt:

```text
Leia as rules do projeto e analise a estrutura atual. Não altere arquivos ainda. Me diga quais partes já seguem o padrão Endpoint -> Service -> CRUD -> Banco e quais precisam ser adaptadas.
```

## Passo 4: migrar módulo por módulo

Não refatore tudo de uma vez. Escolha um módulo pequeno e aplique:

```text
Endpoint -> Service -> CRUD -> Banco
```

Depois adicione testes e atualize o README.

## Mantendo release notes no README

Quando uma alteração relevante for feita, mantenha a seção:

```md
## Alterações recentes
```

Com tabela:

```md
| Data | Tipo | Módulo/Pasta | Alteração | Impacto |
| ---- | ---- | ------------ | --------- | ------- |
```

Use essa tabela para registrar novas pastas, módulos, endpoints, integrações, variáveis de ambiente e mudanças arquiteturais importantes.



## Descobrir regras de negócio de projeto existente

Depois de copiar as rules para um projeto já em andamento, use a rule manual:

```text
120-business-rules-discovery-manual.mdc
```

Ela deve ser usada antes de criar novos endpoints em projetos que já possuem regras importantes espalhadas pelo código.

Prompt recomendado:

```text
Use a rule 120-business-rules-discovery-manual.mdc.
Analise todo o diretório do projeto atual para entender as regras de negócio principais.
Não altere arquivos ainda.
Liste as regras confirmadas pelo código/documentação, as regras inferidas que precisam de confirmação e faça perguntas objetivas para compor novas Cursor Rules específicas de negócio.
Depois da minha confirmação, crie os arquivos .mdc necessários em .cursor/rules/ seguindo o padrão 2xx-business-<dominio>-auto.mdc.
```

Quando uma nova regra de negócio for confirmada durante o desenvolvimento, atualize uma rule de negócio existente ou crie uma nova rule específica.

## Criar abstrações reutilizáveis no core

A rule `115-reusable-core-abstractions-auto.mdc` orienta o Cursor a avaliar novas classes antes de criá-las.

Se a classe for reutilizável, por exemplo envio de e-mail, storage, PDF, QR Code, mensageria, cache, autenticação externa ou client genérico, considere criar em `core/` como classe abstrata ou base reutilizável.

Se a classe for regra de negócio de um módulo específico, mantenha em `services/`.

## Links úteis

- [Explicação de cada rule](../../.cursor/rules/README.md)
- [Prompts recomendados](./PROMPTS.md)


## Uso opcional de `.cursor/business-rules/`

Em projetos já em andamento, pode ser útil criar a pasta:

```text
.cursor/business-rules/
```

Ela deve ser usada como área de documentação e rascunho para regras de negócio descobertas durante a análise do projeto.

Use essa pasta para:

- regras descobertas ainda não transformadas em rule;
- perguntas pendentes para o usuário ou time de negócio;
- decisões de negócio tomadas durante a implementação;
- lista de rules candidatas.

Atenção: o Cursor carrega as Project Rules a partir de `.cursor/rules/*.mdc`. Portanto, regras confirmadas que precisam orientar novas implementações devem virar `.mdc` dentro de `.cursor/rules/`.

Fluxo recomendado:

```text
Análise do projeto -> .cursor/business-rules/ -> confirmação -> .cursor/rules/2xx-business-<dominio>-auto.mdc
```
