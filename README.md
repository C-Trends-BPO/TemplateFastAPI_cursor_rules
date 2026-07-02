# Cursor Rules FastAPI

Repositório de rules para padronizar projetos FastAPI no Cursor.

Este pacote ajuda o time a aplicar uma arquitetura consistente baseada em:

```text
Endpoint -> Service -> CRUD -> Banco
Endpoint -> Service -> Core Client -> API externa
```

## Documentações importantes
- [Rules criadas para usar com o TemplateFastAPI](https://github.com/IgorSantRocha/TemplateFastAPI_v2)
- [Índice das rules](./docs/cursor/rules-index.md)
- [Índice detalhado das rules](./.cursor/rules/README.md)
- [Skills de workflow](./.cursor/skills/README.md)
- [Guia detalhado para aplicar em projetos existentes](./docs/cursor/README.md)
- [Prompts recomendados para o Cursor](./docs/cursor/PROMPTS.md)

## Estrutura

```text
.cursor/
├── rules/
│   ├── README.md
│   ├── 000-project-context-always.mdc
│   └── ...
└── skills/
    ├── README.md
    ├── aplicar-template-cursor-projeto/
    ├── auditar-rules-skills-docs/
    ├── configurar-ci-github-actions/
    ├── descobrir-regras-negocio/
    ├── executar-tarefa-template-fastapi/
    ├── implementar-otel-loki-fastapi/
    ├── deploy-swarm-fastapi/
    └── migrar-env-debug-fastapi/

docs/
├── contexto_infra_swarm_cursor.md
├── observability/
│   └── reference.md
└── cursor/
    ├── README.md
    ├── PROMPTS.md
    ├── rules-index.md
    ├── core-abstractions.md
    └── templates/

AGENTS.md
.cursorrules
README.md
```

## Como aplicar em um projeto

Copie para a raiz do projeto FastAPI:

```text
.cursor/
AGENTS.md
.cursorrules
```

Opcionalmente, copie também:

```text
docs/cursor/
```

A pasta `.cursor` precisa ficar na raiz aberta pelo Cursor.

## README do projeto real

Quando essas rules forem usadas em um projeto real, o README desse projeto deve ser mantido atualizado com informações reais, incluindo a seção:

```md
## Alterações recentes
```

Exemplo:

```md
| Data | Tipo | Módulo/Pasta | Alteração | Impacto |
| ---- | ---- | ------------ | --------- | ------- |
| 2026-05-30 | Adicionado | `services/` | Criada camada de services para regras de negócio. | Endpoints passam a chamar services antes do CRUD. |
```

## Alterações recentes

| Data | Tipo | Módulo/Pasta | Alteração | Impacto |
| ---- | ---- | ------------ | --------- | ------- |
| 2026-07-02 | Atualizado | `docs/observability/`, skills OTEL/Swarm, `.cursor/rules/333-*`, templates deploy | Validação Context7: fork safety Gunicorn (`OTEL_DEFER_INIT`, `gunicorn_conf.py`), vars OTEL/LOKI no stack, endpoint `/v1/traces`, `httpx` em vez de `requests`. | Traces confiáveis no Swarm; settings vs `.env` esclarecido. |
| 2026-07-02 | Adicionado | `.cursor/rules/015-*`, `docs/cursor/templates/db/`, rules 020/045/070 | Rule e templates para sessão SQLAlchemy async (`get_db`, `DbDep`); endpoints com `Annotated`; testes com `dependency_overrides`. | Padrão async alinhado ao FastAPI/SQLAlchemy 2.0; commit permanece no CRUD/service (rule 045). |
| 2026-07-02 | Corrigido | `.cursor/rules/055-*`, `050-*`, `migrar-env-debug-fastapi`, `docs/cursor/templates/datetime/` | Rule 055 movida para `.cursor/rules/` (globs, não always); exemplos Pydantic v2 (`ConfigDict`, `SettingsConfigDict`); referências apontam para templates. | Datetime/timezone ativo por glob; sem sintaxe Pydantic v1 nos exemplos. |
| 2026-07-02 | Refatorado | `.cursor/rules/`, `.cursor/skills/`, `docs/` | Auditoria rules/skills/docs: rules longas viraram stubs + Skills; rule 333 renomeada e enxugada; Skill `deploy-swarm-fastapi`; contexto global reduzido. | Workflows invocáveis por `@skill`; princípios globais curtos; implementação em `docs/observability/reference.md` e skills. |
| 2026-07-02 | Adicionado | `.cursor/skills/`, `docs/cursor/rules-index.md`, `docs/observability/`, `005-rule-vs-skill-gate` | Skills de workflow do projeto fulfillment + docs de suporte e gate Rule vs Skill. | Workflows longos (env, CI, OTEL, negócio, auditoria) invocáveis por `@skill`; AGENTS.md atualizado. |
| 2026-06-29 | Adicionado | `.cursor/rules/130-132`, `docs/cursor/templates/deploy*` | Rules e templates para deploy FastAPI em Docker Swarm (Dockerfile, stack, workflow GHCR, `/health`). | Projetos podem adaptar produção no Swarm com gate de `APP_PORT` e pipeline separado do CI. |

## Novas rules importantes

### Classes reutilizáveis no `core/`

A rule `115-reusable-core-abstractions-auto.mdc` orienta o Cursor a avaliar toda nova classe antes de criá-la. Se a classe puder ser reutilizada em outros módulos, como uma classe de envio de e-mail, storage, PDF, QR Code, mensageria ou client externo, o Cursor deve considerar criá-la como abstração em `core/`.

### Descoberta de regras de negócio em projetos existentes

A rule `120-business-rules-discovery-manual.mdc` deve ser chamada manualmente quando o time quiser mapear um projeto já em andamento. Ela induz o Cursor a analisar o diretório do projeto, identificar regras de negócio reais, fazer perguntas ao usuário e criar novas rules específicas para novos endpoints.

### Deploy Docker Swarm (FastAPI)

As rules `130-fastapi-swarm-deploy-manual.mdc`, `131-docker-swarm-stack-auto.mdc` e `132-github-actions-swarm-deploy-auto.mdc` são stubs que apontam para a Skill `deploy-swarm-fastapi`. Invocar `@deploy-swarm-fastapi` ou `@130` — é obrigatório perguntar `APP_PORT` e `STACK_NAME`. Contexto: `docs/contexto_infra_swarm_cursor.md`.

Prompt recomendado:

```text
Use a rule 120-business-rules-discovery-manual.mdc.
Analise todo o diretório do projeto atual para entender as regras de negócio principais.
Não altere arquivos ainda.
Liste as regras confirmadas pelo código/documentação, as regras inferidas que precisam de confirmação e faça perguntas objetivas para compor novas Cursor Rules específicas de negócio.
Depois da minha confirmação, crie os arquivos .mdc necessários em .cursor/rules/ seguindo o padrão 2xx-business-<dominio>-auto.mdc.
```


## Pasta auxiliar de regras de negócio

Além das rules ativas em `.cursor/rules/`, este pacote pode incluir a pasta:

```text
.cursor/business-rules/
```

Essa pasta é opcional e serve para registrar descobertas, perguntas pendentes e decisões sobre regras de negócio durante a análise de projetos existentes.

Ela não substitui as rules `.mdc`. As instruções que o Cursor deve aplicar automaticamente continuam em:

```text
.cursor/rules/*.mdc
```

Leia também:

- [Índice das rules](./docs/cursor/rules-index.md)
- [Índice detalhado das rules](./.cursor/rules/README.md)
- [Guia de aplicação em projetos existentes](./docs/cursor/README.md)
- [Prompts recomendados](./docs/cursor/PROMPTS.md)
