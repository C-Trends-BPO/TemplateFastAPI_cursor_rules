# AGENTS.md

Este projeto segue o padrão:

```text
Endpoint -> Service -> CRUD -> Banco
Endpoint -> Service -> Core Client -> API externa
```

## Regras principais

- Endpoints devem ser leves.
- Services concentram regra de negócio.
- CRUD acessa banco de dados.
- Models representam tabelas.
- Schemas representam entrada e saída da API.
- Core centraliza recursos compartilhados e clients externos.
- Tests validam endpoints, services e comportamentos principais.
- README do projeto deve ser mantido atualizado com informações reais.
- Alterações relevantes devem ser registradas em `Alterações recentes`.

Para detalhes, consulte:

```text
.cursor/rules/README.md
docs/cursor/README.md
docs/cursor/PROMPTS.md
```
