# Prompts recomendados para usar com as Cursor Rules

Este arquivo reúne prompts prontos para usar no Cursor ao trabalhar com projetos FastAPI que seguem esta arquitetura:

```text
Endpoint -> Service -> CRUD -> Banco
Endpoint -> Service -> Core Client -> API externa
```

Use estes prompts como ponto de partida. Ajuste nomes de módulos, entidades, endpoints e regras de negócio conforme o projeto.

---

## 1. Iniciando um novo projeto com o template

### Analisar o template antes de começar

```text
Leia todas as rules em `.cursor/rules/`, o `AGENTS.md`, o `README.md` principal e os READMEs das subpastas.

Depois, me explique a estrutura atual do projeto e confirme o fluxo arquitetural esperado para criar novos módulos.
Não altere nenhum arquivo ainda.
```

### Planejar o primeiro módulo do projeto

```text
Leia as rules do projeto e me ajude a planejar o primeiro módulo chamado `[NOME_DO_MODULO]`.

O módulo precisa ter:
- model SQLAlchemy
- schemas Pydantic
- CRUD
- service
- endpoint FastAPI
- testes de service
- testes de endpoint
- documentação no README

Antes de alterar arquivos, gere um plano com a lista de arquivos que serão criados ou alterados.
```

### Criar estrutura inicial de um módulo completo

```text
Crie o módulo `[NOME_DO_MODULO]` seguindo as rules do projeto.

Regras obrigatórias:
- endpoint deve chamar service
- service deve conter regra de negócio
- CRUD deve conter apenas acesso ao banco
- schemas devem separar Create, Update e Response
- models devem conter apenas estrutura da tabela e relacionamentos
- adicionar testes básicos
- atualizar o README com informações reais do módulo
- adicionar uma linha em "Alterações recentes"

Ao final, explique exatamente quais arquivos foram criados ou alterados.
```

---

## 2. Aplicando as rules em projeto existente

### Diagnóstico inicial sem alterar arquivos

```text
Leia as rules em `.cursor/rules/`, o `AGENTS.md` e o guia em `docs/cursor/README.md`.

Analise a estrutura atual deste projeto FastAPI e identifique:
- quais pastas já seguem o padrão
- quais camadas estão misturadas
- quais endpoints possuem regra de negócio demais
- quais módulos deveriam ter service
- quais testes estão faltando
- quais READMEs precisam ser atualizados

Não altere arquivos ainda. Gere apenas um plano de migração incremental.
```

### Migrar um endpoint legado para service

```text
Analise o endpoint `[CAMINHO_DO_ENDPOINT]` e refatore seguindo o padrão:

Endpoint -> Service -> CRUD -> Banco

Regras:
- remova regra de negócio pesada do endpoint
- crie ou atualize o service correspondente
- mantenha o CRUD apenas para banco
- preserve o comportamento atual da API
- atualize testes se existirem
- atualize o README do projeto se a mudança for relevante
- registre a alteração em "Alterações recentes"

Quando alterar arquivo existente, entregue o arquivo completo ajustado.
```

### Adaptar um módulo existente sem quebrar compatibilidade

```text
Refatore o módulo `[NOME_DO_MODULO]` para seguir as rules do projeto sem quebrar compatibilidade com os endpoints atuais.

Faça em etapas:
1. identificar responsabilidades misturadas
2. criar ou ajustar service
3. manter schemas compatíveis
4. manter response_model atual
5. ajustar testes
6. atualizar documentação real do projeto

Antes de editar, liste os arquivos afetados.
Depois de editar, explique o que mudou.
```

---

## 3. Criação de models

### Criar uma nova model

```text
Crie a model SQLAlchemy `[NOME_DA_ENTIDADE]` seguindo o padrão do projeto.

Campos necessários:
- `[CAMPO_1]`: `[TIPO]`
- `[CAMPO_2]`: `[TIPO]`
- `[CAMPO_3]`: `[TIPO]`

Regras:
- usar tipagem compatível com SQLAlchemy do projeto
- manter apenas estrutura de tabela e relacionamentos
- não adicionar regra de negócio na model
- adicionar relacionamentos se necessário
- revisar imports e evitar circular import
- indicar se será necessário criar migration

Entregue o arquivo completo da model.
```

### Alterar uma model existente

```text
Altere a model `[NOME_DA_MODEL]` para adicionar/remover/ajustar os seguintes campos:

- `[CAMPO]`: `[DESCRIÇÃO_DA_MUDANÇA]`

Regras:
- preserve os campos existentes que não foram citados
- não coloque regra de negócio na model
- ajuste relacionamentos se necessário
- informe se a mudança exige migration
- atualize schemas, CRUD, service, endpoints e testes se forem impactados
- atualize o README e "Alterações recentes" se a mudança afetar o uso do projeto

Entregue os arquivos completos alterados.
```

### Revisar model existente

```text
Revise a model `[NOME_DA_MODEL]` e verifique se ela segue as rules do projeto.

Procure por:
- regra de negócio indevida dentro da model
- imports desnecessários
- nomes inconsistentes
- campos sem tipo adequado
- relacionamentos incompletos
- risco de circular import

Não altere o arquivo ainda. Primeiro me dê um diagnóstico e sugestões.
```

---

## 4. Criação de schemas

### Criar schemas para uma entidade

```text
Crie os schemas Pydantic para a entidade `[NOME_DA_ENTIDADE]` seguindo o padrão do projeto.

Preciso dos seguintes schemas:
- `[Nome]Base`
- `[Nome]Create`
- `[Nome]Update`
- `[Nome]Response` ou `[Nome]InDbBase`

Campos:
- `[CAMPO_1]`: `[TIPO]`
- `[CAMPO_2]`: `[TIPO]`
- `[CAMPO_3]`: `[TIPO]`

Regras:
- separar entrada e saída
- campos de Create devem representar o payload obrigatório
- campos de Update devem ser opcionais quando fizer sentido
- Response deve conter os campos retornados pela API
- não expor campos sensíveis
- usar Config/from_attributes conforme padrão do projeto

Entregue o arquivo completo.
```

### Alterar schemas existentes

```text
Ajuste os schemas de `[NOME_DA_ENTIDADE]` para refletir a seguinte mudança:

[MUDANÇA]

Regras:
- preserve compatibilidade quando possível
- não exponha campos sensíveis no response
- ajuste Create, Update e Response separadamente
- verifique se endpoints e testes precisam ser atualizados
- atualize README/release notes se afetar contrato da API

Entregue os arquivos completos alterados.
```

### Criar schema de response customizado

```text
Crie um schema de response customizado para o endpoint `[NOME_DO_ENDPOINT]`.

O response deve retornar:
- `[CAMPO_1]`
- `[CAMPO_2]`
- `[CAMPO_3]`

Regras:
- não retornar diretamente model SQLAlchemy se o contrato precisa ser customizado
- criar schema claro e nomeado
- aplicar o schema no `response_model` do endpoint
- ajustar service para montar o retorno se necessário
- adicionar ou ajustar teste do endpoint

Entregue os arquivos completos alterados.
```

---

## 5. Criação e alteração de CRUD

### Criar CRUD para entidade

```text
Crie o CRUD da entidade `[NOME_DA_ENTIDADE]` seguindo o padrão `CRUDBase` do projeto.

Regras:
- usar herança de `CRUDBase[Model, CreateSchema, UpdateSchema]`
- CRUD deve conter apenas acesso ao banco
- não colocar regra de negócio no CRUD
- métodos customizados devem ser consultas reutilizáveis
- filtros devem seguir o padrão já usado no projeto

Entregue o arquivo completo.
```

### Adicionar método de consulta no CRUD

```text
Adicione no CRUD de `[NOME_DA_ENTIDADE]` um método para consultar por `[CAMPO/FILTRO]`.

Regras:
- método deve apenas consultar o banco
- não lançar regra de negócio se isso pertencer ao service
- retornar objeto, lista ou None conforme necessidade
- manter padrão async/sync já usado no projeto
- ajustar service para usar esse método se necessário

Entregue o arquivo completo alterado.
```

---

## 6. Criação e alteração de services

### Criar service para entidade

```text
Crie o service `[NOME_DA_ENTIDADE]Service` seguindo as rules do projeto.

Ele deve conter lógicas para:
- criar registro
- buscar por ID
- listar com paginação/filtros
- atualizar registro
- remover ou desativar registro

Regras:
- service deve conter regra de negócio
- usar CRUD para acessar banco
- normalizar campos quando necessário
- validar duplicidade quando necessário
- lançar HTTPException ou exceção padronizada conforme o padrão do projeto
- não acessar request diretamente se não for necessário

Entregue o arquivo completo.
```

### Adicionar regra de negócio em service existente

```text
Adicione a seguinte regra de negócio no service `[NOME_DO_SERVICE]`:

[REGRA]

Regras:
- não colocar essa regra no endpoint
- não colocar essa regra no CRUD
- preservar comportamento existente
- adicionar ou ajustar testes do service
- atualizar README/release notes se a regra afetar o uso do módulo

Entregue os arquivos completos alterados.
```

### Criar service com integração externa

```text
Crie ou ajuste um service para integrar com a API externa `[NOME_DA_API]`.

Regras:
- o service deve orquestrar a integração
- o consumo HTTP deve usar o client em `core/`
- autenticação deve usar o padrão de OAuth2/API Key/mTLS já definido no projeto
- não expor secrets no código
- usar variáveis de ambiente/configurações do projeto
- tratar erros externos de forma padronizada
- adicionar exemplo ou teste com mock

Entregue os arquivos completos alterados.
```

---

## 7. Criação e alteração de endpoints

### Criar endpoint completo para entidade

```text
Crie os endpoints para `[NOME_DA_ENTIDADE]` seguindo as rules do projeto.

Preciso das rotas:
- GET lista
- GET por ID
- POST criação
- PUT/PATCH atualização
- DELETE remoção ou desativação

Regras:
- endpoint deve ser leve
- endpoint deve chamar service
- usar `response_model`
- usar `Depends` para banco e autenticação quando necessário
- não colocar regra de negócio no endpoint
- adicionar logs úteis sem expor dados sensíveis
- adicionar testes de endpoint
- atualizar README e "Alterações recentes"

Entregue os arquivos completos criados/alterados.
```

### Ajustar endpoint existente

```text
Ajuste o endpoint `[CAMINHO_DO_ENDPOINT]` para seguir o padrão do projeto.

Regras:
- remover regra de negócio do endpoint
- mover lógica para service
- manter contrato de entrada e saída se possível
- aplicar `response_model` correto
- revisar status codes
- revisar tratamento de erro
- ajustar testes
- atualizar documentação se houver mudança de uso

Entregue o arquivo completo ajustado e os arquivos dependentes alterados.
```

### Adicionar filtros e paginação

```text
Adicione filtros e paginação no endpoint `[CAMINHO_DO_ENDPOINT]`.

Filtros necessários:
- `[FILTRO_1]`
- `[FILTRO_2]`

Regras:
- parâmetros devem usar `Query`
- endpoint deve repassar filtros para o service
- service deve montar a regra de filtro
- CRUD deve executar a consulta
- manter limite máximo seguro
- adicionar testes cobrindo filtros principais
- atualizar README se o endpoint for documentado nele

Entregue os arquivos completos alterados.
```

---

## 8. Testes

### Criar testes para service

```text
Crie testes para o service `[NOME_DO_SERVICE]`.

Cenários mínimos:
- criação com sucesso
- busca com sucesso
- erro 404 quando não encontra
- validação de duplicidade
- atualização com sucesso
- remoção/desativação com sucesso

Regras:
- usar pytest
- usar pytest-asyncio se o projeto for async
- usar AsyncMock para CRUD e integrações externas
- não depender de API externa real
- não depender de banco real se o teste for unitário

Entregue o arquivo completo de teste.
```

### Criar testes para endpoint

```text
Crie testes para os endpoints de `[NOME_DA_ENTIDADE]`.

Cenários mínimos:
- GET lista
- GET por ID
- POST criação
- PUT/PATCH atualização
- DELETE remoção/desativação
- erro 404
- erro de validação de payload

Regras:
- usar httpx AsyncClient ou TestClient conforme padrão do projeto
- mockar service quando o foco for rota
- validar status_code e JSON retornado
- não chamar API externa real

Entregue o arquivo completo de teste.
```

---

## 9. README, documentação e release notes

### Atualizar README após criar módulo

```text
Atualize o README principal com informações reais sobre o módulo `[NOME_DO_MODULO]` que acabou de ser criado.

Regras:
- não inventar funcionalidades futuras
- documentar apenas o que existe
- incluir comandos úteis se houver
- incluir variáveis de ambiente novas se houver
- adicionar entrada na tabela "Alterações recentes"
- se a explicação ficar longa, criar ou atualizar README na subpasta correspondente e referenciar no README principal

Entregue o README completo atualizado.
```

### Criar ou atualizar README de subpasta

```text
Crie ou atualize o README da pasta `[PASTA]`.

Ele deve explicar:
- responsabilidade da pasta
- o que deve ficar nela
- o que não deve ficar nela
- exemplos de uso
- regras principais
- relação com outras camadas do projeto

Evite repetir conteúdo que já existe no README principal.
```

### Atualizar release notes

```text
Atualize a seção "Alterações recentes" do README com a mudança abaixo:

[MUDANÇA]

Use a tabela:
| Data | Tipo | Módulo/Pasta | Alteração | Impacto |

Regras:
- registrar apenas mudanças relevantes
- não registrar typos ou formatação simples
- usar a data atual
- indicar nova pasta quando a mudança sugerir expansão da estrutura
```

---

## 10. Revisão de qualidade antes de finalizar

### Revisão geral de módulo

```text
Revise o módulo `[NOME_DO_MODULO]` de ponta a ponta.

Verifique:
- model
- schemas
- CRUD
- service
- endpoint
- testes
- README/release notes

Confirme se segue o padrão:
Endpoint -> Service -> CRUD -> Banco

Não altere arquivos ainda. Primeiro liste problemas encontrados e sugestões.
```

### Corrigir módulo após revisão

```text
Aplique as correções sugeridas no módulo `[NOME_DO_MODULO]`.

Regras:
- manter arquitetura das rules
- não mudar contrato da API sem necessidade
- entregar arquivos completos alterados
- atualizar testes
- atualizar README/release notes se houver impacto

Ao final, explique exatamente o que foi alterado.
```

---

## 11. Prompts curtos para o dia a dia

### Criar módulo rápido

```text
Crie o módulo `[NOME]` completo seguindo as rules do projeto: model, schemas, CRUD, service, endpoint, testes e README.
```

### Refatorar endpoint

```text
Refatore este endpoint para mover regra de negócio para service e manter o CRUD apenas para banco.
```

### Criar schema de response

```text
Crie um schema de response para este endpoint e aplique no `response_model`, ajustando o service se necessário.
```

### Adicionar filtro

```text
Adicione o filtro `[FILTRO]` neste endpoint seguindo o fluxo endpoint -> service -> CRUD.
```

### Revisar arquitetura

```text
Revise este módulo e diga onde ele viola as rules do projeto antes de alterar qualquer arquivo.
```

### Atualizar documentação

```text
Atualize o README principal e a seção "Alterações recentes" com base nas mudanças reais feitas neste módulo.
```

---

## 12. Checklist para usar depois de qualquer alteração grande

Use este prompt ao final de uma implementação maior:

```text
Revise as alterações feitas nesta tarefa e confirme:

- endpoints continuam leves
- services concentram regra de negócio
- CRUDs só acessam banco
- schemas estão separados entre entrada e saída
- models não possuem regra de negócio
- integrações externas usam core client
- testes foram criados ou ajustados
- README foi atualizado com informações reais
- seção "Alterações recentes" foi atualizada quando necessário
- não há secrets, tokens ou senhas no código

Se encontrar problema, corrija e entregue os arquivos completos alterados.
```
