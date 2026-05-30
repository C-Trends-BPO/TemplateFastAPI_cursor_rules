# Cursor Rules FastAPI

Repositório com rules e documentação para padronizar projetos FastAPI no Cursor.

O objetivo é facilitar a criação e manutenção de projetos seguindo o fluxo:

```text
Endpoint -> Service -> CRUD -> Banco
Endpoint -> Service -> Core Client -> API externa
```

## Documentação

- [Guia detalhado de aplicação em projetos existentes](./docs/cursor/README.md)
- [Lista de prompts recomendados para o Cursor](./docs/cursor/PROMPTS.md)

## Como usar

Copie para a raiz do projeto FastAPI:

```text
.cursor/
AGENTS.md
.cursorrules
docs/cursor/
```

Depois abra o projeto pela raiz no Cursor.

## Prompts úteis

Este repositório inclui uma lista completa de prompts para:

- iniciar projeto novo
- aplicar rules em projeto existente
- criar módulos completos
- criar/alterar models
- criar/alterar schemas
- criar/alterar CRUDs
- criar/alterar services
- criar/alterar endpoints
- criar testes
- manter README e release notes atualizados

Acesse:

[docs/cursor/PROMPTS.md](./docs/cursor/PROMPTS.md)

## Release notes no README do projeto

Projetos que usam estas rules devem manter uma seção de alterações recentes no próprio README do projeto real:

```md
## Alterações recentes

| Data | Tipo | Módulo/Pasta | Alteração | Impacto |
| ---- | ---- | ------------ | --------- | ------- |
```

Essa regra ajuda o time a entender rapidamente o que mudou e quando uma nova pasta ou camada passou a fazer sentido no projeto.
