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

## Links úteis

- [Explicação de cada rule](../../.cursor/rules/README.md)
- [Prompts recomendados](./PROMPTS.md)
