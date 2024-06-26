from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from messier.infrastructure.relational_entity import BaseRelationalEntity
from .achievement import Achievement


class PersonAchievement(BaseRelationalEntity):
    __tablename__ = "person_achievement"

    id: Mapped[int] = mapped_column(primary_key=True)
    achievement_id: Mapped[int] = mapped_column(ForeignKey("achievement.id"))
    person_id: Mapped[int] = mapped_column(ForeignKey("person.id"))
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    achievement: Mapped[Achievement] = relationship(lazy='selectin')
