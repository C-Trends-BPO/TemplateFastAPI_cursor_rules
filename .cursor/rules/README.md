# Rules do Cursor

Esta pasta contém as **Project Rules** usadas pelo Cursor para orientar geração, refatoração e manutenção de código em projetos FastAPI baseados no padrão do template.

As rules ficam em arquivos `.mdc` porque esse é o formato usado pelo Cursor para aplicar instruções por contexto, tipo de arquivo e escopo.

## Como o Cursor usa esta pasta

O Cursor lê os arquivos dentro de:

```text
.cursor/rules/
```

Cada rule pode conter metadados como:

```yaml
---
description: Descrição curta da rule
globs: api/**/*.py
alwaysApply: false
---
```

## Tipos de rule

### Rules com `alwaysApply: true`

São carregadas sempre que o projeto estiver aberto no Cursor.

Use para regras globais, como:

- contexto do projeto
- arquitetura principal
- segurança
- padrão geral de trabalho

### Rules com `globs`

São aplicadas quando o Cursor trabalha em arquivos compatíveis com o padrão informado.

Exemplo:

```yaml
globs: services/**/*.py
```

Essa rule será considerada principalmente ao editar arquivos dentro de `services/`.

## Fluxo arquitetural esperado

O padrão principal do projeto é:

```text
Endpoint -> Service -> CRUD -> Banco
```

Para integrações externas:

```text
Endpoint -> Service -> Core Client -> API externa
```

## O que cada rule faz

### `000-project-context-always.mdc`

Define o contexto global do projeto.

Explica que o projeto usa:

- FastAPI
- SQLAlchemy
- Pydantic
- HTTPX
- Pytest
- camada `api`
- camada `services`
- camada `crud`
- camada `models`
- camada `schemas`
- camada `core`
- camada `tests`

Também reforça o fluxo principal:

```text
Endpoint -> Service -> CRUD -> Banco
Endpoint -> Service -> Core Client -> API externa
```

Use esta rule para garantir que o Cursor entenda a arquitetura base antes de sugerir alterações.

---

### `010-architecture-always.mdc`

Define as regras gerais de arquitetura.

Ela orienta o Cursor sobre onde cada responsabilidade deve ficar:

| Camada | Responsabilidade |
| ------ | ---------------- |
| `api/` | Rotas HTTP, dependências e response models |
| `services/` | Regra de negócio, validações e orquestração |
| `crud/` | Acesso ao banco de dados |
| `models/` | Tabelas SQLAlchemy e relacionamentos |
| `schemas/` | Schemas Pydantic de entrada e saída |
| `core/` | Configurações, clients externos e recursos compartilhados |
| `tests/` | Testes automatizados |

Também ajuda a evitar import circular e mistura de responsabilidades.

---

### `020-fastapi-endpoints-auto.mdc`

Aplica-se principalmente a:

```text
api/**/*.py
main.py
```

Define que endpoints devem ser leves.

Um endpoint pode:

- receber payload
- declarar `response_model`
- usar `Depends`
- chamar um service
- retornar a resposta

Um endpoint não deve:

- conter regra de negócio pesada
- acessar várias tabelas diretamente
- montar payload complexo de integração externa
- fazer chamadas HTTP externas diretamente
- conter validações complexas que pertencem ao service

Padrão esperado:

```python
@router.post("/", response_model=ExampleResponse)
async def create_example(
    *,
    db: AsyncSession = Depends(deps.get_db),
    payload: ExampleCreate,
):
    return await example_service.create_example(db=db, payload=payload)
```

---

### `030-services-auto.mdc`

Aplica-se principalmente a:

```text
services/**/*.py
```

Define que `services/` é a camada de regra de negócio.

Um service pode conter:

- validações
- normalizações
- checagem de duplicidade
- regras de status
- transições de estado
- orquestração entre múltiplos CRUDs
- chamadas para clients externos em `core/`
- tratamento de erros de negócio

Um service não deve:

- declarar rotas FastAPI
- conter models SQLAlchemy como definição de tabela
- fazer query complexa que deveria estar no CRUD
- expor segredo ou configuração sensível hardcoded

Padrão esperado:

```python
class ExampleService:
    async def create_example(self, db: AsyncSession, payload: ExampleCreate):
        # valida regra
        # chama CRUD
        # retorna resposta
        ...


example_service = ExampleService()
```

---

### `040-crud-auto.mdc`

Aplica-se principalmente a:

```text
crud/**/*.py
```

Define que CRUD deve cuidar apenas do acesso ao banco.

Um CRUD pode conter:

- `get`
- `get_multi`
- `create`
- `update`
- `remove`
- filtros
- paginação
- ordenação
- queries reutilizáveis

Um CRUD não deve conter:

- regra de negócio pesada
- chamada para API externa
- decisão de status de negócio
- tratamento HTTP de endpoint

Padrão esperado:

```python
class CRUDExample(CRUDBase[Example, ExampleCreate, ExampleUpdate]):
    pass


crud_example = CRUDExample(Example)
```

---

### `050-schemas-models-auto.mdc`

Aplica-se principalmente a:

```text
schemas/**/*.py
models/**/*.py
```

Define a separação correta entre schemas Pydantic e models SQLAlchemy.

Em `models/` devem ficar:

- tabelas
- colunas
- relacionamentos
- índices
- constraints

Em `schemas/` devem ficar:

- payload de criação
- payload de atualização
- payload de resposta
- schemas internos quando necessário

Padrão recomendado de schemas:

```text
ExampleBase
ExampleCreate
ExampleUpdate
ExampleResponse ou ExampleInDbBase
```

Regra principal:

```text
Model representa banco.
Schema representa entrada e saída da API.
```

---

### `060-core-integrations-auto.mdc`

Aplica-se principalmente a:

```text
core/**/*.py
services/**/*external*.py
services/**/*client*.py
examples/oauth2_clients/**/*.py
```

Define regras para integrações externas e clients HTTP.

Essa rule cobre o client abstrato para APIs com:

- OAuth2
- API Key
- Bearer Token
- Basic Auth
- Client Secret
- certificado/mTLS
- CA bundle
- headers extras
- timeout
- tratamento padronizado de erro externo

Regra principal:

```text
Endpoint não chama API externa diretamente.
Service chama client em core.
Core centraliza autenticação, headers, timeout e tratamento base.
```

---

### `070-tests-auto.mdc`

Aplica-se principalmente a:

```text
tests/**/*.py
```

Define o padrão de testes automatizados.

Estrutura recomendada:

```text
tests/
├── conftest.py
├── services/
└── api/
    └── api_v1/
        └── endpoints/
```

Regras principais:

- testes de endpoint devem validar contrato HTTP
- testes de service devem validar regra de negócio
- testes de CRUD devem validar acesso ao banco quando houver ambiente apropriado
- usar `pytest`
- usar `pytest-asyncio` para funções async
- usar `AsyncMock` quando não for necessário banco real
- evitar depender de serviços externos reais

---

### `080-security-config-always.mdc`

Rule global de segurança.

Define que o Cursor não deve criar ou versionar:

- senha real
- token real
- API key real
- client secret real
- certificado real
- chave privada real
- `.env` com credenciais reais

Padrão esperado:

```text
.env.example para exemplo
core/config.py para leitura de settings
variáveis reais apenas no ambiente
```

Também orienta a não expor dados sensíveis em logs.

---

### `090-docs-readme-auto.mdc`

Aplica-se principalmente a:

```text
**/README.md
docs/**/*.md
```

Define regras gerais de documentação.

Responsabilidades:

- README principal deve ser visão geral do projeto
- README de subpasta deve explicar detalhes daquela pasta
- documentação deve evitar redundância
- quando possível, referenciar documentos específicos
- exemplos devem ser reais ou claramente marcados como exemplo

Regra principal:

```text
Documentar o suficiente para o time entender e manter o projeto sem repetir tudo em todos os arquivos.
```

---

### `095-project-readme-sync-auto.mdc`

Aplica-se principalmente ao README principal do projeto real.

Essa rule orienta o Cursor a manter o README atualizado quando o template passar a ser usado para desenvolver um projeto específico.

Deve atualizar o README quando houver:

- novo módulo
- novo endpoint
- novo service
- nova integração externa
- nova variável de ambiente
- novo comando de execução
- nova pasta relevante
- alteração arquitetural importante
- novos testes relevantes

Também orienta manter a seção:

```md
## Alterações recentes
```

Com tabela no formato:

```md
| Data | Tipo | Módulo/Pasta | Alteração | Impacto |
| ---- | ---- | ------------ | --------- | ------- |
| 2026-05-30 | Adicionado | `services/` | Criada camada de services. | Endpoints passam a chamar services antes do CRUD. |
```

Essa rule também permite indicar necessidade de novas pastas no template.

Exemplo:

```md
| 2026-05-30 | Sugestão | `workers/` | Projeto passou a ter tarefas assíncronas. | Avaliar criação de pasta própria para jobs/background tasks. |
```

---

### `100-task-workflow-agent.mdc`

Rule voltada para fluxos maiores no Agent Mode.

Orienta o Cursor a trabalhar em etapas:

1. entender o pedido
2. identificar camadas afetadas
3. alterar arquivos necessários
4. manter padrão arquitetural
5. adicionar ou ajustar testes
6. atualizar documentação quando necessário
7. explicar exatamente o que foi criado, alterado ou removido

Também reforça uma regra importante do time:

```text
Quando sugerir alteração em arquivo existente, entregar o arquivo completo já corrigido.
```

---

### `110-python-style-auto.mdc`

Aplica-se principalmente a:

```text
**/*.py
```

Define estilo geral para código Python.

Regras principais:

- usar tipagem sempre que fizer sentido
- manter funções pequenas e objetivas
- usar `async` corretamente
- evitar imports não usados
- evitar `except Exception` genérico sem tratamento claro
- evitar `pass` silencioso
- não misturar português e inglês em nomes internos sem necessidade
- manter nomes claros e consistentes com o projeto

## Quando criar nova rule

Crie uma nova rule quando surgir um padrão repetido para uma pasta, tecnologia ou tipo de tarefa.

Exemplos:

- `120-docker-auto.mdc`
- `130-alembic-auto.mdc`
- `140-celery-workers-auto.mdc`
- `150-django-integration-auto.mdc`

## Quando não criar nova rule

Não crie uma rule nova para um caso muito específico ou temporário.

Nesse caso, prefira documentar no README do módulo ou no prompt usado para aquela tarefa.

## Regras para manter esta pasta organizada

1. Use prefixos numéricos para ordenar as rules.
2. Mantenha nomes claros.
3. Não duplique instruções grandes entre muitos arquivos.
4. Use `alwaysApply: true` apenas quando necessário.
5. Use `globs` para rules específicas.
6. Atualize este README quando criar, remover ou renomear uma rule.
7. Não coloque segredos, tokens ou dados reais nas rules.

## Documentação complementar

Consulte também:

```text
README.md
docs/cursor/README.md
docs/cursor/PROMPTS.md
AGENTS.md
.cursorrules
```
