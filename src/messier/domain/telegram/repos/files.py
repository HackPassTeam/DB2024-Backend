from messier.infrastructure.repo import BaseEntityRepo
from messier.domain.telegram.models import File


class AllFiles(BaseEntityRepo[File]):
    pass
