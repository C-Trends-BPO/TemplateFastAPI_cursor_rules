# Referência — OpenTelemetry + Tempo + Loki (FastAPI)

Implementação completa de observabilidade. Use com a Skill `implementar-otel-loki-fastapi` e a rule stub `333-observability-otel-loki-always.mdc`.

## Infra de observabilidade

O Grafana consulta o Tempo pela porta 3200:

```text
http://tempo:3200
```

As aplicações FastAPI devem enviar traces para o Tempo via OTLP HTTP na porta 4318:

```text
http://192.168.0.213:4318
```

Endpoint final usado pelo exporter:

```text
http://192.168.0.213:4318/v1/traces
```

Logs devem ser enviados para Loki:

```text
http://192.168.0.213:3100/loki/api/v1/push
```

Nunca usar a porta `3200` na aplicação para enviar traces.

### Endpoint OTLP — base URL vs `/v1/traces`

No `settings`, guardar apenas a **base URL** (sem `/v1/traces`):

```python
OTEL_EXPORTER_OTLP_ENDPOINT: str = "http://192.168.0.213:4318"
```

No `core/telemetry.py`, ao passar o endpoint explicitamente ao `OTLPSpanExporter`, concatenar o path:

```python
endpoint = settings.OTEL_EXPORTER_OTLP_ENDPOINT.rstrip("/")
exporter = OTLPSpanExporter(endpoint=f"{endpoint}/v1/traces")
```

O SDK só auto-anexa `/v1/traces` quando lê de variáveis de ambiente (`OTEL_EXPORTER_OTLP_ENDPOINT`) **sem** passar `endpoint` ao construtor. Com construtor explícito, a URL é usada como está.

**Anti-padrão:** base URL com `/v1/traces` no `settings` **e** concatenação no código → `.../v1/traces/v1/traces`.

Definir o endpoint como campo do `config` (`settings`):

Correto:

```python
OTEL_EXPORTER_OTLP_ENDPOINT: str = "http://192.168.0.213:4318"
```

Errado:

```python
OTEL_EXPORTER_OTLP_ENDPOINT: str = "http://tempo:3200"
OTEL_EXPORTER_OTLP_ENDPOINT: str = "http://192.168.0.213:3200"
```

## Configurações obrigatórias no config

Valores em `core/config.py` via classe `Settings` (Pydantic). Ler sempre de `settings` — não espalhar `os.getenv` no código.

Em **desenvolvimento local**, defaults podem ficar no `Settings`. Em **produção (Swarm)**, o `.env` do servidor (`/opt/envs/{app}.env`) alimenta o `settings` via variáveis de ambiente; o arquivo real não vai para o Git.

```python
class Settings(BaseSettings):
    OTEL_ENABLED: bool = True
    OTEL_SERVICE_NAME: str = "NomeAplicacaoFastAPI"
    OTEL_APPEND_ENV: bool = True
    OTEL_APPEND_IP_SUFFIX: bool = True
    OTEL_EXPORTER_OTLP_ENDPOINT: str = "http://192.168.0.213:4318"
    OTEL_ENVIRONMENT: str = type_name
    OTEL_HOST_NAME: str = ""

    LOKI_ENABLED: bool = True
    LOKI_URL: str = "http://192.168.0.213:3100/loki/api/v1/push"
    LOKI_APP_NAME: str = "NomeAplicacaoFastAPI"
    LOKI_HOST_NAME: str = ""

    LOG_LEVEL: str = "INFO"
    ENABLE_TEST_ROUTES: bool = False
    OTEL_DEFER_INIT: bool = False  # True no Swarm — init no post_fork do Gunicorn
```

`OTEL_SERVICE_NAME` e `LOKI_APP_NAME` são nome BASE. Properties `service_name`/`loki_app_name` anexam ambiente (`type_name`) e octeto IP.

## Separação de ambiente (type_name)

- `type_name` é fonte única do ambiente (`homologacao`/`producao`).
- Não repetir ambiente hardcoded em `OTEL_SERVICE_NAME` ou `LOKI_APP_NAME`.
- Nome final: `<base>-<ambiente>-<octeto_ip>`.

## Identificação por IP — `core/host_info.py`

```python
import socket
from typing import Optional


def get_local_ip() -> str:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(("8.8.8.8", 80))
        return sock.getsockname()[0]
    except OSError:
        try:
            return socket.gethostbyname(socket.gethostname())
        except OSError:
            return "127.0.0.1"
    finally:
        sock.close()


def get_ip_suffix(ip: Optional[str] = None) -> str:
    ip = ip or get_local_ip()
    parts = ip.split(".")
    if len(parts) == 4 and parts[-1].isdigit():
        return parts[-1]
    digits = "".join(char for char in ip if char.isdigit())
    return digits[-3:] if digits else "000"
```

Properties no `Settings`:

```python
from core.host_info import get_ip_suffix, get_local_ip

LOCAL_IP = get_local_ip()
IP_SUFFIX = get_ip_suffix(LOCAL_IP)


class Settings(BaseSettings):
    OTEL_SERVICE_NAME: str = "NomeAplicacaoFastAPI"
    OTEL_APPEND_ENV: bool = True
    OTEL_APPEND_IP_SUFFIX: bool = True
    OTEL_ENVIRONMENT: str = type_name
    OTEL_HOST_NAME: str = ""
    LOKI_APP_NAME: str = "NomeAplicacaoFastAPI"
    LOKI_HOST_NAME: str = ""

    @property
    def name_suffix(self) -> str:
        parts: list[str] = []
        if self.OTEL_APPEND_ENV and self.OTEL_ENVIRONMENT:
            parts.append(self.OTEL_ENVIRONMENT)
        if self.OTEL_APPEND_IP_SUFFIX:
            parts.append(IP_SUFFIX)
        return ("-" + "-".join(parts)) if parts else ""

    @property
    def service_name(self) -> str:
        return f"{self.OTEL_SERVICE_NAME}{self.name_suffix}"

    @property
    def loki_app_name(self) -> str:
        return f"{self.LOKI_APP_NAME}{self.name_suffix}"

    @property
    def host_name(self) -> str:
        return self.OTEL_HOST_NAME or LOCAL_IP

    @property
    def loki_host_name(self) -> str:
        return self.LOKI_HOST_NAME or LOCAL_IP
```

## Dependências

```txt
opentelemetry-api
opentelemetry-sdk
opentelemetry-exporter-otlp-proto-http
opentelemetry-instrumentation-fastapi
opentelemetry-instrumentation-httpx
opentelemetry-instrumentation-sqlalchemy
opentelemetry-instrumentation-psycopg2
opentelemetry-instrumentation-logging
python-logging-loki
```

Projetos que ainda usam `requests` (não `httpx`): adicionar `opentelemetry-instrumentation-requests`. Com `asyncpg`: instrumentar `sync_engine` do SQLAlchemy.

## Estrutura

```text
core/telemetry.py
core/logging_config.py
core/host_info.py
```

## `core/logging_config.py`

```python
import logging
import logging.config
import time

from fastapi import HTTPException, Request
from starlette.middleware.base import BaseHTTPMiddleware

from core.config import settings

LOG_FORMAT = (
    "%(asctime)s %(levelname)s "
    "[%(name)s] "
    "[%(filename)s:%(lineno)d] "
    "[trace_id=%(otelTraceID)s "
    "span_id=%(otelSpanID)s "
    "resource.service.name=%(otelServiceName)s] "
    "- %(message)s"
)


def get_logging_config() -> dict:
    log_level = settings.LOG_LEVEL
    handlers = {
        "default": {
            "level": log_level,
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        }
    }
    root_handlers = ["default"]
    if settings.LOKI_ENABLED:
        handlers["loki"] = {
            "level": log_level,
            "class": "logging_loki.LokiHandler",
            "url": settings.LOKI_URL,
            "tags": {
                "app": settings.loki_app_name,
                "host": settings.loki_host_name,
                "env": settings.OTEL_ENVIRONMENT,
            },
            "auth": None,
            "version": "1",
        }
        root_handlers.append("loki")
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {"standard": {"format": LOG_FORMAT}},
        "handlers": handlers,
        "loggers": {
            "": {"handlers": root_handlers, "level": log_level, "propagate": False},
            "uvicorn": {"handlers": root_handlers, "level": log_level, "propagate": False},
            "uvicorn.access": {"handlers": root_handlers, "level": log_level, "propagate": False},
            "uvicorn.error": {"handlers": root_handlers, "level": log_level, "propagate": False},
        },
    }


def setup_logging() -> None:
    logging.config.dictConfig(get_logging_config())


_AUTH_ERROR_CODES = frozenset({401, 403})


def is_auth_error(status_code: int | None) -> bool:
    return status_code in _AUTH_ERROR_CODES


def is_client_error(status_code: int | None) -> bool:
    return status_code is not None and 400 <= status_code < 500


def resolve_log_level(status_code: int | None, *, common_business: bool = False) -> str:
    if status_code is None:
        return "warning" if common_business else "error"
    if status_code >= 500 or is_auth_error(status_code):
        return "error"
    if is_client_error(status_code) or common_business:
        return "warning"
    return "error"


def log_for_status_code(
    logger: logging.Logger,
    status_code: int | None,
    msg: str,
    *args,
    exc_info: bool = False,
    common_business: bool = False,
    **kwargs,
) -> None:
    level = resolve_log_level(status_code, common_business=common_business)
    if level == "warning":
        logger.warning(msg, *args, **kwargs)
    else:
        logger.error(msg, *args, exc_info=exc_info, **kwargs)


def log_http_exception(
    logger: logging.Logger,
    exc: HTTPException,
    msg: str,
    *args,
    **kwargs,
) -> None:
    log_for_status_code(logger, exc.status_code, msg, *args, **kwargs)


def extract_response_status_code(exc: Exception) -> int | None:
    response = getattr(exc, "response", None)
    if response is not None:
        status_code = getattr(response, "status_code", None)
        if status_code is not None:
            return status_code
    return None


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logger = logging.getLogger("http.request")
        start = time.perf_counter()
        response = await call_next(request)
        duration_ms = (time.perf_counter() - start) * 1000
        status = response.status_code
        msg = "http.request method=%s path=%s status=%s duration_ms=%.2f"
        args = (request.method, request.url.path, status, duration_ms)
        if status >= 500:
            logger.error(msg, *args)
        elif 400 <= status < 500:
            logger.warning(msg, *args)
        else:
            logger.info(msg, *args)
        return response
```

## Níveis de log por status HTTP

| Situação | Nível |
|----------|-------|
| 2xx/3xx | `INFO` |
| 4xx comum | `WARNING` |
| 401/403 | `ERROR` |
| 5xx | `ERROR` |
| Exceção não tratada | `ERROR` |

Usar `log_for_status_code` / `log_http_exception` em integrações e services — não `logger.error` fixo para todo 4xx.

## `core/telemetry.py`

```python
import logging

from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from core.config import settings
from core.logging_config import LOG_FORMAT

logger = logging.getLogger(__name__)
_engines_instrumentados: set[int] = set()


def setup_logging_instrumentation() -> None:
    LoggingInstrumentor().instrument(
        set_logging_format=True,
        logging_format=LOG_FORMAT,
    )


def setup_base_telemetry() -> None:
    if not settings.OTEL_ENABLED:
        return
    endpoint = settings.OTEL_EXPORTER_OTLP_ENDPOINT.rstrip("/")
    resource = Resource.create(
        {
            "service.name": settings.service_name,
            "deployment.environment": settings.OTEL_ENVIRONMENT,
            "host.name": settings.host_name,
        }
    )
    provider = TracerProvider(resource=resource)
    exporter = OTLPSpanExporter(endpoint=f"{endpoint}/v1/traces")
    provider.add_span_processor(BatchSpanProcessor(exporter))
    trace.set_tracer_provider(provider)
    HTTPXClientInstrumentor().instrument()


def log_telemetry_status() -> None:
    if not settings.OTEL_ENABLED:
        logger.info("OpenTelemetry desativado via OTEL_ENABLED.")
        return
    endpoint = settings.OTEL_EXPORTER_OTLP_ENDPOINT.rstrip("/")
    logger.info(
        "OpenTelemetry ativo | service=%s | host=%s | env=%s | endpoint=%s/v1/traces",
        settings.service_name,
        settings.host_name,
        settings.OTEL_ENVIRONMENT,
        endpoint,
    )


def instrument_fastapi(app: FastAPI) -> None:
    if settings.OTEL_ENABLED:
        FastAPIInstrumentor.instrument_app(app)


def instrument_sqlalchemy(engine) -> None:
    if not settings.OTEL_ENABLED:
        return
    target = getattr(engine, "sync_engine", engine)
    if id(target) in _engines_instrumentados:
        return
    SQLAlchemyInstrumentor().instrument(engine=target)
    _engines_instrumentados.add(id(target))
```

Ordem crítica: `setup_base_telemetry()` → `setup_logging_instrumentation()` → `setup_logging()` → `log_telemetry_status()`.

## Gunicorn e fork safety

O `BatchSpanProcessor` **não é fork-safe**. Com Gunicorn + múltiplos workers (`UvicornWorker`), inicializar telemetria no import do `main.py` no processo master pode causar deadlocks ou traces perdidos após o `fork`.

**Padrão recomendado (Swarm/produção):**

1. `OTEL_DEFER_INIT=True` no `.env` do servidor — adia o init no import.
2. `gunicorn_conf.py` na raiz com hook `post_fork` que chama `init_observability()`.
3. Comando Gunicorn com `-c gunicorn_conf.py`.

Template: `docs/cursor/templates/gunicorn_conf.py`.

```python
# gunicorn_conf.py
def post_fork(server, worker):
    from main import init_observability

    init_observability()
```

```python
# main.py — função reutilizável
def init_observability() -> None:
    setup_base_telemetry()
    setup_logging_instrumentation()
    setup_logging()
    log_telemetry_status()


if not settings.OTEL_DEFER_INIT:
    init_observability()
```

**Desenvolvimento local (uvicorn direto):** manter `OTEL_DEFER_INIT=False` (default) — init no import funciona com processo único.

**Alternativas** (menos comuns neste template): `opentelemetry-instrument` como wrapper do comando; `SimpleSpanProcessor` (trade-off de performance).

## `main.py`

```python
import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from opentelemetry import trace

from core.config import settings
from core.logging_config import RequestLoggingMiddleware, setup_logging
from core.telemetry import (
    instrument_fastapi,
    instrument_sqlalchemy,
    log_telemetry_status,
    setup_base_telemetry,
    setup_logging_instrumentation,
)


def init_observability() -> None:
    setup_base_telemetry()
    setup_logging_instrumentation()
    setup_logging()
    log_telemetry_status()


if not settings.OTEL_DEFER_INIT:
    init_observability()

logger = logging.getLogger(settings.service_name)

app = FastAPI(title=settings.OTEL_SERVICE_NAME)
app.add_middleware(RequestLoggingMiddleware)
instrument_fastapi(app)
# instrument_sqlalchemy(engine)  # se usar SQLAlchemy


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception("Erro não tratado na rota %s %s", request.method, request.url.path)
    return JSONResponse(status_code=500, content={"detail": "Erro interno do servidor"})


if settings.ENABLE_TEST_ROUTES:

    @app.get("/teste-erro-loki")
    def teste_erro_loki():
        raise Exception("Teste de erro para Loki")

    @app.get("/telemetry-test")
    def telemetry_test():
        tracer = trace.get_tracer(__name__)
        with tracer.start_as_current_span("teste-manual-opentelemetry") as span:
            span.set_attribute("app.name", settings.service_name)
            return {"status": "ok", "message": "Trace manual gerado"}
```

Não criar segundo `app = FastAPI(...)`. Rotas de teste só com `ENABLE_TEST_ROUTES=False` em produção.

## Validações

1. App sobe sem erro.
2. Log de startup com `service=<base>-<env>-<ip>`.
3. Logs de requisição com `trace_id`/`span_id` reais (não `0`).
4. Tempo: Service Name correto.
5. Loki: `{app="NomeAPI-homologacao-213"}`.
6. 4xx→WARNING, 5xx/401/403→ERROR.

## Regras de qualidade

- Não duplicar `app`, `dictConfig`, `LoggingInstrumentor`, `FastAPIInstrumentor`.
- Não hardcodar nome/host fora do config.
- Não quebrar startup se Loki/Tempo indisponíveis.
- Não expor stack trace ao cliente.
- Níveis por status só em `core/logging_config.py`.

## LogQL úteis

```logql
{app="NomeAplicacaoFastAPI-homologacao-213"} |= "ERROR"
{app="NomeAplicacaoFastAPI-homologacao-213"} |= "WARNING" |= "status=4"
{app="NomeAplicacaoFastAPI-homologacao-213"} |= "http.request" |= "status=5"
{app="NomeAplicacaoFastAPI-homologacao-213"} |= "Erro não tratado"
```
