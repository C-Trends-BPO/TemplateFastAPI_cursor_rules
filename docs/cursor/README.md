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
