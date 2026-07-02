# Templates — sessão async SQLAlchemy

Copiar e adaptar no projeto FastAPI real:

| Arquivo template | Destino no projeto |
|------------------|-------------------|
| `session.py` | `db/session.py` |
| `deps.py` | `api/deps.py` |

Rule correspondente: `.cursor/rules/015-db-session-auto.mdc`

Pré-requisitos:

- `core/config.py` com `DATABASE_URL` (ex.: `postgresql+asyncpg://...`)
- Driver async instalado (ex.: `asyncpg` para PostgreSQL)

Endpoints devem usar `DbDep` importado de `api/deps.py` — ver rule `020-fastapi-endpoints-auto.mdc`.
