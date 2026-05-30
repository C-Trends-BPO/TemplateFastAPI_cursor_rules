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
O endpoint deve ser leve, usar response_model, Depends e chamar o service.
Não coloque regra de negócio no endpoint.
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
