---
name: implementar-otel-loki-fastapi
description: Implementa observabilidade completa em FastAPI com OpenTelemetry, Grafana Tempo, Loki e logs correlacionados por trace_id. Use ao adicionar OTEL/Loki, configurar logging_config, telemetry ou corrigir níveis de log por status HTTP.
---

# Implementar OTEL + Loki (FastAPI)

Antes de alterar arquivos, analise a estrutura e apresente plano curto.

Referência completa: [docs/observability/reference.md](../../docs/observability/reference.md).

Rule de princípios (sempre ativa): `.cursor/rules/333-observability-otel-loki-always.mdc`.

## Checklist de implementação

```text
- [ ] Campos OTEL/LOKI em core/config.py (settings, não .env)
- [ ] core/host_info.py — IP e sufixo
- [ ] Properties service_name, loki_app_name no Settings
- [ ] core/logging_config.py — LOG_FORMAT, Loki, helpers HTTP
- [ ] core/telemetry.py — setup_base, logging instrumentation, instrumentadores
- [ ] main.py — ordem correta de setup
- [ ] RequestLoggingMiddleware
- [ ] Handler global de exceções
- [ ] ENABLE_TEST_ROUTES para rotas de teste
- [ ] Dependências em requirements.txt
- [ ] instrument_sqlalchemy(engine) se usar SQLAlchemy
```

## Ordem no main.py

```python
setup_base_telemetry()
setup_logging_instrumentation()
setup_logging()
log_telemetry_status()
# app + middleware + instrument_fastapi
```

## Endpoints

- Traces OTLP: porta **4318** (`OTEL_EXPORTER_OTLP_ENDPOINT` sem `/v1/traces` no config)
- Loki: `LOKI_URL` → `/loki/api/v1/push`
- **Nunca** enviar traces para porta 3200

## Níveis de log

Centralizar em `core/logging_config.py`:

- `log_for_status_code`, `log_http_exception`, `extract_response_status_code`
- Middleware: 5xx ERROR, 4xx WARNING, resto INFO
- 401/403 sempre ERROR

## LoggingInstrumentor

```python
LoggingInstrumentor().instrument(set_logging_format=True, logging_format=LOG_FORMAT)
```

Evita `KeyError: 'otelTraceID'` com dictConfig próprio.

## Validação

1. App sobe; log `OpenTelemetry ativo | service=...`
2. Requisição com trace_id/span_id reais
3. Tempo: Service Name = `<base>-<env>-<ip>`
4. Loki: filtrar por `{app="..."}`
5. 4xx WARNING, 5xx ERROR

## Anti-padrões

- Duplicar app, dictConfig, instrumentadores
- `os.getenv` fora do config
- `logger.error` para todo 4xx
- Stack trace ao cliente
- `/teste-erro-loki` em produção

Código de referência: `docs/observability/reference.md`. Em projetos reais: `core/telemetry.py`, `core/logging_config.py`, `core/host_info.py`, `main.py`.
