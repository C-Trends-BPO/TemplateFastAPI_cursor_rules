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


Regras complementares:

- antes de criar uma classe nova, avaliar se ela é reutilizável e se deve virar abstração em `core/`;
- quando uma regra de negócio importante for descoberta, criar ou atualizar uma Cursor Rule específica em `.cursor/rules/`;
- para projetos existentes, usar a rule manual `120-business-rules-discovery-manual.mdc` antes de criar endpoints em domínios com regras complexas.


Quando mapear regras de negócio de projetos existentes, use `.cursor/business-rules/` apenas como documentação auxiliar. Rules ativas devem continuar em `.cursor/rules/*.mdc`.
