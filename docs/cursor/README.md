# Guia de aplicação das Cursor Rules em projetos FastAPI

Voltar para o [README principal](../../README.md).

Este guia explica como aplicar as rules em projetos novos ou existentes.

## Prompts recomendados

Para facilitar o uso no dia a dia, este pacote inclui uma lista de prompts prontos para copiar e adaptar:

[Ver lista completa de prompts recomendados](./PROMPTS.md)

Use essa lista para:

- iniciar um projeto novo
- analisar um projeto existente
- migrar endpoints legados para services
- criar models, schemas, CRUDs, services e endpoints
- criar testes automatizados
- atualizar README e release notes

## Aplicando em projeto novo

Copie os arquivos abaixo para a raiz do projeto:

```text
.cursor/
AGENTS.md
.cursorrules
docs/cursor/
```

Depois abra o projeto pela raiz no Cursor.

## Aplicando em projeto existente

Recomendação:

1. Copie as rules para o projeto.
2. Peça ao Cursor para analisar a estrutura sem alterar arquivos.
3. Escolha um módulo pequeno para migrar primeiro.
4. Crie ou ajuste a camada `services/`.
5. Refatore endpoints para chamarem services.
6. Mantenha CRUD apenas com acesso ao banco.
7. Adicione testes gradualmente.
8. Atualize README e release notes.

Prompt recomendado para começar:

```text
Leia as rules em `.cursor/rules/`, o `AGENTS.md` e este guia em `docs/cursor/README.md`.
Analise a estrutura atual deste projeto FastAPI e gere um plano de migração incremental.
Não altere arquivos ainda.
```

## README e release notes

Depois que um projeto começa a evoluir a partir do template, o README principal deve refletir o projeto real, não apenas o template.

Mantenha uma seção:

```md
## Alterações recentes

| Data | Tipo | Módulo/Pasta | Alteração | Impacto |
| ---- | ---- | ------------ | --------- | ------- |
```

Registre apenas mudanças relevantes, como:

- novo módulo
- novo endpoint
- nova integração
- nova pasta
- nova variável de ambiente
- alteração arquitetural
- novos testes
