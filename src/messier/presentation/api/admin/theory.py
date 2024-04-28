from sqladmin import ModelView

from messier.domain.core.models.education.theory import Theory


class TheoryAdmin(ModelView, model=Theory):
    column_list = [
        Theory.id,
        Theory.educational_material_id,
        Theory.title,
        Theory.content
    ]
