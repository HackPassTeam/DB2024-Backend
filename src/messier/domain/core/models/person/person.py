from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from messier.infrastructure.models import BuiltinSubtypeMixin
from messier.infrastructure.relational_entity import BaseRelationalEntity

if TYPE_CHECKING:
    pass


class PersonId(int, BuiltinSubtypeMixin):
    pass


class Person(BaseRelationalEntity):
    __tablename__ = 'person'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    account_id: Mapped[int | None] = mapped_column(ForeignKey('account.id'))
    telegram_account_id: Mapped[int | None] = mapped_column(ForeignKey("telegram_account.id"))
    full_name: Mapped[str] = mapped_column()
    description: Mapped[str | None] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    def __str__(self):  # for admin panel
        return f'{self.full_name}'

    __repr__ = __str__  # for debug
