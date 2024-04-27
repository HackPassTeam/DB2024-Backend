from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, DeclarativeBase

from messier.infrastructure.entity import BaseEntity


class RelationalMapper(DeclarativeBase, AsyncAttrs):
    pass


class BaseRelationalObject(BaseEntity, RelationalMapper):
    __abstract__ = True


class BaseRelationalEntity(BaseRelationalObject):
    __abstract__ = True

    if TYPE_CHECKING:  # I believe in the developers' neatness
        id: Mapped[int]


__all__ = [
    "BaseRelationalObject",
    "BaseRelationalEntity",
]
