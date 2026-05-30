# Instruções para agentes de código

Este projeto segue o padrão:

```text
Endpoint -> Service -> CRUD -> Banco
Endpoint -> Service -> Core Client -> API externa
```

Consulte:

- `.cursor/rules/README.md` para entender cada rule;
- `docs/cursor/README.md` para aplicar em projetos existentes;
- `docs/cursor/PROMPTS.md` para prompts recomendados.

Regras principais:

- endpoint deve ser leve;
- service contém regra de negócio;
- CRUD contém apenas acesso ao banco;
- schemas e models devem ficar separados;
- não versionar secrets;
- manter README do projeto real atualizado com alterações relevantes.
