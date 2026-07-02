# Prompts recomendados para usar no Cursor

[Voltar para o guia](./README.md)

## Iniciar novo projeto

```text
Leia as rules deste projeto e configure a estrutura inicial seguindo o padrão FastAPI definido.
Crie apenas o necessário para iniciar o projeto, sem inventar módulos de negócio ainda.
Explique quais arquivos foram criados ou alterados.
```

## Aplicar rules em projeto existente

```text
Leia as rules do projeto e analise a estrutura atual.
Não altere arquivos ainda.
Me diga quais pastas e módulos já seguem o padrão Endpoint -> Service -> CRUD -> Banco e quais precisam ser ajustados.
Monte um plano incremental de migração.
```

## Migrar `.env` e debug (FastAPI start manual)

```text
Use a rule 085-fastapi-env-debug-manual.mdc (ou @085-fastapi-env-debug-manual).
Migre secrets do config para .env, crie .env.example e core/example-config.py,
.vscode/launch.json (templates em docs/cursor/templates/) e documente execução + debug no README.

Adaptar para este projeto:
- ROOT_PATH prod: /api-{nome}
- ROOT_PATH homolog: /hg-api-{nome}
- PSQL_HOST prod: {host prod}
- PSQL_HOST homolog: {host homolog}
- APP module: main:app

Não versionar .env nem core/config.py. Não usar --reload no launch.json.
```

## Configurar sessão async SQLAlchemy

```text
Use a rule 015-db-session-auto.mdc (ou @015-db-session-auto).
Configure db/session.py com create_async_engine, async_sessionmaker(expire_on_commit=False) e get_db async.
Crie api/deps.py com DbDep = Annotated[AsyncSession, Depends(get_db)].
Use os templates em docs/cursor/templates/db/ como base.
Não faça auto-commit em get_db se o CRUD já commita (rule 045).
Endpoints devem usar DbDep e chamar service — não acessar CRUD diretamente.
```

## Deploy Docker Swarm (FastAPI)

```text
Use a Skill deploy-swarm-fastapi (ou rule 130-fastapi-swarm-deploy-manual.mdc / @130-fastapi-swarm-deploy-manual).
Adapte este projeto FastAPI para Docker Swarm conforme docs/contexto_infra_swarm_cursor.md.
Antes de gerar arquivos, pergunte APP_PORT, STACK_NAME e módulo ASGI.
Crie Dockerfile, deploy/stack.yml, deploy-swarm.yml, GET /health, .env.example e scripts.
OTEL_APPEND_IP_SUFFIX=False no .env do servidor (/opt/envs/{app}.env).
Não versionar .env real. Manter ci.yml separado de deploy-swarm.yml.
```

## Criar novo módulo

```text
Crie o módulo [NOME_DO_MODULO] seguindo as rules do projeto.

Regras obrigatórias:
- endpoint deve chamar service
- service deve conter regra de negócio
- CRUD deve conter apenas acesso ao banco
- schemas devem separar Create, Update e Response
- models devem conter apenas estrutura da tabela e relacionamentos
- adicionar testes básicos
- atualizar o README com informações reais do módulo
- adicionar uma linha em Alterações recentes

Ao final, explique exatamente quais arquivos foram criados ou alterados.
```

## Criar ou alterar model

```text
Crie/altere o model [NOME_DO_MODEL] seguindo o padrão SQLAlchemy do projeto.
Depois verifique impactos em schemas, CRUD, service, endpoint e testes.
Não coloque regra de negócio dentro do model.
Entregue os arquivos completos alterados.
```

## Criar ou alterar schema

```text
Crie/altere os schemas de [NOME_DO_MODULO] seguindo o padrão Base, Create, Update e Response.
Garanta que campos obrigatórios fiquem no Create, campos opcionais no Update e campos sensíveis não sejam expostos no Response.
Entregue o arquivo completo ajustado.
```

## Criar ou alterar endpoint

```text
Crie/altere o endpoint de [NOME_DO_MODULO] seguindo o padrão do projeto.
O endpoint deve ser leve, usar response_model, DbDep (rule 015) e chamar o service.
Use status_code explícito em POST (ex.: 201). Não coloque regra de negócio no endpoint.
Entregue o arquivo completo ajustado.
```

## Criar ou alterar service

```text
Crie/altere o service de [NOME_DO_MODULO].
Coloque nele as validações, normalizações, regras de negócio e orquestração entre CRUDs ou clients externos.
Não coloque queries complexas no service se elas pertencem ao CRUD.
Entregue o arquivo completo ajustado.
```

## Criar testes

```text
Crie testes para [NOME_DO_MODULO] seguindo as rules.
Inclua testes de service com AsyncMock e testes de endpoint com o service mockado quando fizer sentido.
Não use API externa real nem secrets reais.
```

## Atualizar README e release notes

```text
Revise o README do projeto e atualize apenas com informações reais do que existe.
Se houve alteração relevante, adicione uma linha na seção Alterações recentes com Data, Tipo, Módulo/Pasta, Alteração e Impacto.
Não documente funcionalidades futuras como se já existissem.
```


## Analisar regras de negócio de projeto existente e criar rules específicas

```text
Use a rule 120-business-rules-discovery-manual.mdc.

Analise todo o diretório do projeto atual para entender as regras de negócio principais.
Não altere arquivos ainda.

Quero que você:
1. identifique os módulos principais do projeto;
2. liste as regras de negócio confirmadas pelo código e pela documentação;
3. separe regras apenas inferidas e que precisam de confirmação;
4. faça perguntas objetivas para completar lacunas;
5. sugira quais novas rules devem ser criadas;
6. proponha nomes de arquivos no padrão .cursor/rules/2xx-business-<dominio>-auto.mdc;
7. depois da minha confirmação, crie ou atualize as rules necessárias.

Essas rules devem ajudar o Cursor a criar e alterar novos endpoints sem descumprir regras de negócio existentes.
```

## Registrar uma nova regra de negócio descoberta

```text
Durante esta alteração identificamos uma nova regra de negócio:
[DESCREVA_A_REGRA]

Verifique se já existe alguma rule de negócio que cubra essa regra.
Se existir, atualize a rule existente.
Se não existir, crie uma nova rule em .cursor/rules/ usando o padrão 2xx-business-<dominio>-auto.mdc.

Atualize também docs/cursor/rules-index.md e, se for relevante para o projeto, o README principal e a seção Alterações recentes.
```

## Criar classe reutilizável no core

```text
Preciso criar uma classe para [DESCREVER_CAPACIDADE].

Antes de implementar, use a rule 115-reusable-core-abstractions-auto.mdc e avalie se essa classe pode ser reutilizada futuramente em outros módulos.

Se for reutilizável, crie uma abstração em core/ com classe base/abstrata e uma implementação concreta inicial.
Se for específica do domínio atual, crie no service do módulo.

Ao final, explique por que a classe ficou em core/ ou services/.
```


## Prompt para mapear regras de negócio usando pasta auxiliar

```text
Use a rule 120-business-rules-discovery-manual.mdc.

Analise todo o diretório do projeto atual para entender as regras de negócio principais.
Não altere endpoints, services, schemas, models ou CRUDs ainda.

Use também a pasta .cursor/business-rules/ como área de documentação auxiliar.

Quero que você:
1. identifique os módulos principais do projeto;
2. liste regras confirmadas pelo código e pela documentação;
3. registre hipóteses em .cursor/business-rules/discovered-rules.md;
4. registre perguntas em .cursor/business-rules/pending-questions.md;
5. registre decisões confirmadas em .cursor/business-rules/decisions.md;
6. sugira quais regras devem virar .mdc ativo em .cursor/rules/;
7. proponha nomes no padrão .cursor/rules/2xx-business-<dominio>-auto.mdc;
8. aguarde minha confirmação antes de criar ou atualizar qualquer rule ativa.

Depois da confirmação, crie ou atualize as rules necessárias e atualize os READMEs relacionados.
```
