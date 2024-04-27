from sqladmin import ModelView

from messier.domain.core.models.education.tag import Tag


class TagAdmin(ModelView, model=Tag):
    column_list = [
        Tag.name,
        Tag.color
    ]
