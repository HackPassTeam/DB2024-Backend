from datetime import datetime

from sqlalchemy import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from messier.infrastructure.relational_entity import BaseRelationalEntity


class Tag(BaseRelationalEntity):
    __tablename__ = 'tag'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(VARCHAR(25))
    color: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    def __repr__(self):
        return self.name
