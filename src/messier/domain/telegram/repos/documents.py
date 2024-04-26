from messier.infrastructure.repo import BaseEntityRepo
from messier.domain.telegram.models import Document


class AllDocuments(BaseEntityRepo[Document]):
    pass
