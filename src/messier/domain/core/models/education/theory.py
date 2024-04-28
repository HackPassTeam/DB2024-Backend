from sqlalchemy import ForeignKey, VARCHAR, Text
from sqlalchemy.orm import mapped_column, Mapped

from messier.infrastructure.relational_entity import BaseRelationalEntity


class Theory(BaseRelationalEntity):
    __tablename__ = 'theory'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    educational_material_id: Mapped[int] = mapped_column(ForeignKey("education_material.id"))
    title: Mapped[str] = mapped_column(VARCHAR(30))
    content: Mapped[str] = mapped_column(Text())

