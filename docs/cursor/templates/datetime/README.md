# Templates — datetime e timezone

Copie para um novo projeto FastAPI junto com a rule `.cursor/rules/055-datetime-timezone-auto.mdc`.

| Arquivo template | Destino no projeto |
|------------------|-------------------|
| `datetime_utils.py` | `core/datetime_utils.py` |
| `datetime_columns.py` | `db/datetime_columns.py` |
| `sp_datetime.py` | `schemas/sp_datetime.py` |

## Configuração

1. Adicione em `core/config.py`: `APP_TIMEZONE: str = "America/Sao_Paulo"`
2. Adicione em `.env.example`: `APP_TIMEZONE=America/Sao_Paulo`
3. Substitua `datetime.utcnow()` por `utc_now()` em services
4. Use `SPDateTime` apenas em schemas `*Response`
5. Crie migration Alembic `timestamp` → `timestamptz` para tabelas existentes

## Prompt para migrar projeto existente

```text
Use a rule 055-datetime-timezone-auto.mdc.
Copie os templates de docs/cursor/templates/datetime/ para core/, db/ e schemas/.
Aplique DateTime(timezone=True) nos models, SPDateTime nas respostas,
substitua datetime.utcnow() por utc_now() e crie migration timestamptz.
Não altere campos date. Documente no README e .env.example.
```
