from messier.infrastructure.repo import BaseEntityRepo
from messier.domain.telegram.models import Chat


class AllChats(BaseEntityRepo[Chat]):
    pass
