from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import mapped_column, Mapped, relationship

from messier.domain.core.models.person.person import Person
from messier.infrastructure.notifier.interface import NotifierBackendEnum
from messier.infrastructure.relational_entity import BaseRelationalEntity


class NotificationDestinationRelPerson(BaseRelationalEntity):
    __tablename__ = 'notification_destination_rel_person'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    notification_destination_id: Mapped[int] = mapped_column(ForeignKey("notification_destination.id"))
    person_id: Mapped[int] = mapped_column(ForeignKey("person.id"))


class NotificationDestination(BaseRelationalEntity):
    __tablename__ = 'notification_destination'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    notifier_backend: Mapped[NotifierBackendEnum] = mapped_column(Enum(NotifierBackendEnum))
    internal_identifier: Mapped[str] = mapped_column()
    priority: Mapped[int] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    deleted_at: Mapped[Optional[datetime]] = mapped_column()

    persons: Mapped[list[Person]] = relationship(secondary=NotificationDestinationRelPerson.__table__)
