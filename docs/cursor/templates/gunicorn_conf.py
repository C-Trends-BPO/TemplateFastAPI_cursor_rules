# Template gunicorn_conf.py — copiar para a raiz do projeto FastAPI.
# Obrigatório com múltiplos workers: BatchSpanProcessor não é fork-safe.
# Ver docs/observability/reference.md — seção "Gunicorn e fork safety".


def post_fork(server, worker):
    from main import init_observability

    init_observability()
