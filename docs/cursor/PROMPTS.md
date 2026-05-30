# Prompts recomendados para usar no Cursor

Este arquivo reúne prompts úteis para iniciar projetos novos, aplicar rules em projetos existentes e criar ou alterar módulos.

Voltar para:

- [README principal](../../README.md)
- [Guia de aplicação](./README.md)
- [Explicação de cada rule](../../.cursor/rules/README.md)

## Iniciar novo projeto com o template

```text
Leia as rules do projeto e analise a estrutura atual do template.
Antes de criar código, me diga quais camadas serão usadas para o módulo que vou pedir.
Siga o padrão Endpoint -> Service -> CRUD -> Banco.
```

## Aplicar rules em projeto existente

```text
Leia as rules do projeto e o arquivo docs/cursor/README.md.
Analise a estrutura atual deste projeto FastAPI e me diga quais pastas já seguem o padrão e quais precisam ser adaptadas.
Não altere arquivos ainda. Apenas gere um plano de migração incremental.
```

## Criar novo módulo completo

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
Crie/ajuste o model [NOME_DO_MODEL] seguindo o padrão do projeto.

Regras:
- model deve representar apenas a tabela e seus relacionamentos
- não colocar regra de negócio no model
- manter nomes de colunas claros
- revisar se será necessário schema, CRUD, service, endpoint e teste
- entregar o arquivo completo ajustado
```

## Criar ou alterar schema

```text
Crie/ajuste os schemas do módulo [NOME_DO_MODULO].

Use o padrão:
- Base
- Create
- Update
- Response ou InDbBase

Regras:
- não misturar schema com model SQLAlchemy
- separar entrada e saída da API
- usar campos opcionais no Update quando fizer sentido
- entregar o arquivo completo ajustado
```

## Criar ou alterar endpoint

```text
Ajuste o endpoint [NOME_DO_ENDPOINT] para seguir o padrão do projeto.

Regras:
- endpoint deve ser leve
- endpoint deve chamar service
- remover regra de negócio da rota
- manter response_model
- usar Depends para dependências
- não chamar API externa diretamente no endpoint
- entregar o arquivo completo ajustado
```

## Criar ou alterar service

```text
Crie/ajuste o service [NOME_DO_SERVICE].

Regras:
- service deve conter regra de negócio
- validar duplicidades e transições de status quando necessário
- chamar CRUD para banco
- chamar core client para API externa
- tratar erros de negócio com mensagens claras
- entregar o arquivo completo ajustado
```

## Criar testes

```text
Crie testes para o módulo [NOME_DO_MODULO].

Regras:
- testes de endpoint em tests/api/api_v1/endpoints
- testes de service em tests/services
- usar pytest e pytest-asyncio quando necessário
- mockar chamadas externas
- não depender de API externa real
- testar sucesso e erro principal
```

## Atualizar README e release notes

```text
Atualize o README do projeto com informações reais sobre as alterações feitas.

Regras:
- não inventar funcionalidades
- documentar apenas o que existe ou foi implementado
- atualizar seção de comandos se necessário
- atualizar variáveis de ambiente se necessário
- adicionar linha em Alterações recentes com Data, Tipo, Módulo/Pasta, Alteração e Impacto
```
