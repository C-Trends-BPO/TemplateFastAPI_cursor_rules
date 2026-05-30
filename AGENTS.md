# AGENTS.md - TemplateFastAPI

Este projeto usa Cursor Rules em `.cursor/rules/`.

## Regra principal

Siga sempre este fluxo:

```text
Endpoint -> Service -> CRUD -> Banco
Endpoint -> Service -> Core Client -> API externa
```

## Prioridades

1. Preserve o padrão atual do projeto.
2. Não coloque regra de negócio em endpoints.
3. Não coloque chamada HTTP externa em endpoints.
4. Não coloque regra de negócio em CRUD.
5. Use `services/` para regras, validações e orquestração.
6. Use `core/` para clients externos, autenticação, OAuth2, API keys e certificados.
7. Use `tests/` para exemplos e validação de comportamento.
8. Atualize README quando mudar estrutura ou padrão.

## Segurança

Nunca exponha tokens, senhas, API keys, secrets, certificados reais ou `.env` real.

## Documentação do projeto

Ao desenvolver ou alterar um módulo real, mantenha o `README.md` principal atualizado com informações verdadeiras do projeto. Use READMEs de subpastas e arquivos em `docs/` para detalhes técnicos, evitando duplicidade no README principal.


## README e alterações recentes

Mantenha o README principal do projeto atualizado com informações reais. Quando houver mudanças relevantes de arquitetura, módulo, endpoint, pasta, integração, comandos ou variáveis de ambiente, atualize também uma seção `Alterações recentes` em formato de tabela simples, quando ela existir ou fizer sentido criar.
