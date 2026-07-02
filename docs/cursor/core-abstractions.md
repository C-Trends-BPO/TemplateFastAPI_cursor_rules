# Abstrações reutilizáveis em `core/`

Detalhes e exemplos extraídos da rule stub `115-reusable-core-abstractions-auto.mdc`.

## Candidatas a `core/`

Envio de e-mail/SMS/WhatsApp, storage, PDF, QR Code, parser de arquivos, mensageria, cache, criptografia, clients HTTP genéricos, autenticação externa.

## Checklist antes de criar classe

1. Pode ser usada por mais de um módulo?
2. Capacidade técnica genérica ou regra de negócio específica?
3. Depende de model/schema/CRUD de um módulo?
4. Pode ser interface/contrato abstrato?
5. Terá múltiplas implementações (SMTP, S3, etc.)?

## Padrão de pacote

```text
core/
├── email/
│   ├── base.py
│   ├── smtp.py
│   └── schemas.py
├── storage/
│   ├── base.py
│   └── local.py
└── integrations/
```

## Exemplo — classe abstrata

```python
from abc import ABC, abstractmethod


class AbstractEmailClient(ABC):
    @abstractmethod
    async def send_email(
        self,
        *,
        to: list[str],
        subject: str,
        body: str,
        cc: list[str] | None = None,
        bcc: list[str] | None = None,
    ) -> None:
        raise NotImplementedError
```

```python
class SMTPEmailClient(AbstractEmailClient):
    async def send_email(self, *, to, subject, body, cc=None, bcc=None) -> None:
        ...
```

## Quando ficar em `services/`

`UserService`, `OrderService` — regra de domínio. Podem usar abstrações de `core/`.

## Dependências permitidas

```text
Service -> Core abstraction
Service -> CRUD
Endpoint -> Service
```

Evitar: `Core -> Service`, `Core -> CRUD/model de domínio`.

## Quando não abstrair

Uma implementação simples, específica de módulo, ou abstração prematura. Extrair para `core/` quando houver reutilização real.

## Como explicar a decisão

Ao criar uma nova classe, informe no resumo final:

- onde a classe foi criada;
- por que ficou em `core/` ou em `services/`;
- se foi abstrata ou concreta;
- quais módulos podem reutilizá-la;
- se README ou **Alterações recentes** foram atualizados.

## Documentação

Ao criar abstração em `core/`: atualizar `core/README.md` (se existir), README principal e **Alterações recentes**.
