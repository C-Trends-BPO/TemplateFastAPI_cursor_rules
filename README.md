# Cursor Rules FastAPI

Repositório de rules para padronizar projetos FastAPI no Cursor.

Este pacote ajuda o time a aplicar uma arquitetura consistente baseada em:

```text
Endpoint -> Service -> CRUD -> Banco
Endpoint -> Service -> Core Client -> API externa
```

## Documentações importantes
- [Rules criadas para usar com o TemplateFastAPI](https://github.com/C-Trends-BPO/TemplateFastAPI)
- [Explicação de cada rule](./.cursor/rules/README.md)
- [Guia detalhado para aplicar em projetos existentes](./docs/cursor/README.md)
- [Prompts recomendados para o Cursor](./docs/cursor/PROMPTS.md)

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
