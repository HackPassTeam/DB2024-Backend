from messier.infrastructure.repo import BaseEntityRepo
from messier.domain.telegram.models import PhotoSize


class AllPhotoSizes(BaseEntityRepo[PhotoSize]):
    pass
