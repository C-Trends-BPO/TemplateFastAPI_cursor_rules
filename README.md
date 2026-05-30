# Cursor Rules FastAPI

Repositório de rules para padronizar projetos FastAPI no Cursor.

Este pacote foi criado para ser reutilizado pelo time em novos projetos e também em projetos FastAPI já existentes.

## Documentação principal

- [Guia detalhado de aplicação em projetos existentes](./docs/cursor/README.md)
- [Prompts recomendados para usar no Cursor](./docs/cursor/PROMPTS.md)
- [Explicação de cada rule](./.cursor/rules/README.md)

## Estrutura

```text
.cursor/
└── rules/
    ├── README.md
    ├── 000-project-context-always.mdc
    ├── 010-architecture-always.mdc
    ├── 020-fastapi-endpoints-auto.mdc
    ├── 030-services-auto.mdc
    ├── 040-crud-auto.mdc
    ├── 050-schemas-models-auto.mdc
    ├── 060-core-integrations-auto.mdc
    ├── 070-tests-auto.mdc
    ├── 080-security-config-always.mdc
    ├── 090-docs-readme-auto.mdc
    ├── 095-project-readme-sync-auto.mdc
    ├── 100-task-workflow-agent.mdc
    └── 110-python-style-auto.mdc

docs/
└── cursor/
    ├── README.md
    └── PROMPTS.md

AGENTS.md
.cursorrules
```

## Fluxo arquitetural esperado

```text
Endpoint -> Service -> CRUD -> Banco
```

Para integrações externas:

```text
Endpoint -> Service -> Core Client -> API externa
```

## Instalação em um projeto

Copie para a raiz do projeto FastAPI:

```text
.cursor/
AGENTS.md
.cursorrules
docs/cursor/
```

Depois abra o projeto no Cursor pela raiz.

## Observação sobre README do projeto real

Este repositório possui seu próprio `README.md`, mas ao aplicar as rules em um projeto real, o README daquele projeto deve continuar sendo a documentação real da aplicação.

A rule abaixo orienta o Cursor a manter o README do projeto atualizado:

```text
.cursor/rules/095-project-readme-sync-auto.mdc
```

Ela também orienta manter uma seção de alterações recentes no README do projeto.

## Onde entender cada rule

A explicação completa de cada rule está em:

```text
.cursor/rules/README.md
```
