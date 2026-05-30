# Guia de aplicação das Cursor Rules em projetos existentes

Este guia explica como aplicar as rules em projetos FastAPI já existentes.

Voltar para:

- [README principal](../../README.md)
- [Explicação de cada rule](../../.cursor/rules/README.md)
- [Prompts recomendados](./PROMPTS.md)

## Objetivo

Permitir que projetos já existentes sejam adaptados gradualmente para o padrão:

```text
Endpoint -> Service -> CRUD -> Banco
```

E, para integrações externas:

```text
Endpoint -> Service -> Core Client -> API externa
```

## Como aplicar em projeto existente

1. Copie a pasta `.cursor/` para a raiz do projeto.
2. Copie `AGENTS.md` para a raiz.
3. Copie `.cursorrules` para a raiz.
4. Copie `docs/cursor/` para a pasta `docs/` do projeto.
5. Abra o projeto pelo Cursor usando a raiz.
6. Peça ao Cursor para analisar o projeto antes de alterar arquivos.

Prompt recomendado:

```text
Leia as rules do projeto e o arquivo docs/cursor/README.md.
Analise a estrutura atual deste projeto FastAPI e me diga quais pastas já seguem o padrão e quais precisam ser adaptadas.
Não altere arquivos ainda. Apenas gere um plano de migração incremental.
```

## Estratégia de migração

Não tente migrar tudo de uma vez.

Recomenda-se:

1. escolher um módulo pequeno
2. criar ou ajustar schemas
3. revisar model
4. revisar CRUD
5. criar service
6. simplificar endpoint
7. criar testes
8. atualizar README e alterações recentes

## Mantendo o README atualizado

A rule `095-project-readme-sync-auto.mdc` orienta o Cursor a manter o README real do projeto atualizado conforme novos módulos forem criados.

O README do projeto deve conter apenas informações reais da aplicação.

Também é recomendado manter uma seção:

```md
## Alterações recentes
```

Com tabela:

```md
| Data | Tipo | Módulo/Pasta | Alteração | Impacto |
| ---- | ---- | ------------ | --------- | ------- |
| 2026-05-30 | Adicionado | `services/` | Criada camada de services. | Endpoints passam a chamar services antes do CRUD. |
```

## Quando indicar necessidade de nova pasta

Se o projeto começar a ter uma responsabilidade nova, o Cursor pode sugerir uma nova pasta no README ou na release note.

Exemplos:

```text
workers/      -> tarefas assíncronas
jobs/         -> rotinas agendadas
adapters/     -> adaptação entre sistemas externos
providers/    -> provedores específicos de terceiros
```

A sugestão deve ficar clara como sugestão, não como algo já implementado.
