from messier.domain.telegram.models import Chat
from messier.infrastructure.repo import BaseEntityRepo


class AllChats(BaseEntityRepo[Chat]):
    pass
