# Guia de aplicação das Cursor Rules em projetos FastAPI existentes

Este guia explica como aplicar as rules deste repositório em projetos FastAPI novos ou já existentes.

O README principal do repositório apresenta a visão rápida das rules. Este documento entra no detalhe de implantação, migração gradual e manutenção da documentação.

Voltar para o início: [README principal](../../README.md)

## 1. Objetivo das rules

As rules foram criadas para orientar o Cursor a seguir uma arquitetura consistente:

```text
Endpoint -> Service -> CRUD -> Banco
Endpoint -> Service -> Core Client -> API externa
```

O objetivo não é obrigar todo projeto existente a ser refatorado de uma vez. A recomendação é migrar aos poucos, módulo por módulo.

## 2. Como copiar para um projeto existente

Na raiz do projeto de destino, copie:

```text
.cursor/
AGENTS.md
.cursorrules
docs/cursor/
```

Exemplo:

```bash
cp -r .cursor AGENTS.md .cursorrules docs /caminho/do/projeto-existente/
```

Depois, abra o projeto no Cursor pela raiz onde está a pasta `.cursor/`.

## 3. Cuidados antes de aplicar em projeto legado

Antes de pedir alterações automáticas, peça uma análise:

```text
Leia as rules do projeto e analise a estrutura atual.
Identifique quais partes já seguem o padrão Endpoint -> Service -> CRUD -> Banco e quais precisam ser adaptadas.
Não altere arquivos ainda. Apenas gere um plano incremental.
```

Isso evita que o Cursor tente refatorar o projeto inteiro de uma vez.

## 4. Estratégia recomendada de migração

Use esta ordem:

1. Escolha um módulo pequeno.
2. Analise endpoint, schema, model e CRUD existentes.
3. Crie `services/` se ainda não existir.
4. Mova regra de negócio do endpoint para o service.
5. Mantenha CRUD apenas para acesso ao banco.
6. Ajuste imports e responses.
7. Adicione testes para service.
8. Adicione testes para endpoint se possível.
9. Atualize o README do projeto com informações reais do módulo.

## 5. Como criar `services/` em projeto existente

Estrutura mínima:

```text
services/
├── __init__.py
├── base_service.py
└── nome_do_modulo_service.py
```

O service deve concentrar:

```text
validações
normalizações
regras de negócio
duplicidades
transições de status
orquestração entre CRUDs
chamadas para core clients
```

O endpoint deve apenas chamar o service.

## 6. Como aplicar a regra de README atualizado

Este pacote inclui a rule:

```text
.cursor/rules/095-project-readme-sync-auto.mdc
```

Ela orienta o Cursor a manter o `README.md` principal do projeto sincronizado com o que realmente existe no código.

Essa rule deve ser considerada principalmente quando forem criados ou alterados:

```text
módulos
endpoints
services
integrações externas
fluxos de autenticação
variáveis de ambiente
testes
estrutura de pastas
comandos de execução
```

## 7. Como o README deve ser atualizado em projetos reais

O README principal deve deixar de ser apenas o README do template e passar a documentar o projeto real.

Ele deve responder:

```text
O que este projeto faz?
Quais módulos existem?
Como rodar localmente?
Como configurar variáveis de ambiente?
Como executar testes?
Quais integrações externas existem?
Onde estão as documentações específicas?
```

Evite duplicar detalhes longos. Use links para documentos específicos.

Exemplo:

```md
## Documentação

- [Arquitetura de services](./services/README.md)
- [Integrações externas](./core/README.md)
- [Testes](./tests/README.md)
- [Cursor Rules](./docs/cursor/README.md)
```

## 8. Exemplo de prompt para implementar módulo e atualizar README

```text
Crie o módulo de clientes seguindo as rules do projeto.
Use o padrão Endpoint -> Service -> CRUD -> Banco.
Crie model, schema, crud, service, endpoint e testes básicos.
Depois atualize o README.md principal com informações reais do módulo criado e adicione links para READMEs específicos se necessário.
Entregue os arquivos completos alterados.
```

## 9. Exemplo de prompt para projeto legado

```text
Refatore apenas o módulo de cars.
Mova regra de negócio do endpoint para services/car_service.py.
Mantenha crud/crud_cars.py apenas com acesso ao banco.
Não altere outros módulos.
Ao final, atualize o README.md principal somente com informações reais sobre o módulo de cars.
```

## 10. O que não fazer

Evite pedir:

```text
Refatore todo o projeto de uma vez.
```

Prefira:

```text
Refatore somente este módulo.
```

Também evite documentar funcionalidades futuras como se já existissem.

Se algo ainda não foi implementado, use uma seção como:

```md
## Próximos passos sugeridos
```

## 11. Checklist ao terminar uma alteração

Depois de cada módulo importante, confira:

```text
endpoint chama service?
service concentra regra de negócio?
crud está limitado a banco?
schemas estão separados de models?
testes foram adicionados ou ajustados?
README principal foi atualizado se necessário?
README de subpasta/docs foram usados para detalhes?
nenhum segredo real foi documentado?
```

## 12. Relação entre README principal e este guia

No repositório de rules:

```text
README.md = visão rápida e explicação das rules
docs/cursor/README.md = guia detalhado de aplicação em projetos existentes
```

No projeto de destino:

```text
README.md = documentação real do projeto
docs/cursor/README.md = guia de uso das rules no projeto
.cursor/rules/*.mdc = rules usadas pelo Cursor
```
