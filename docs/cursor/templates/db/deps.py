"""
Template de dependências FastAPI — copiar para api/deps.py no projeto real.

DbDep é o alias padrão para injetar AsyncSession nos endpoints.
"""
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db

DbDep = Annotated[AsyncSession, Depends(get_db)]
