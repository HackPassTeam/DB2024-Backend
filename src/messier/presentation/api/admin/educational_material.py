from sqladmin import ModelView

from messier.domain.core.models.education.educational_material import EducationalMaterial


class EducationalMaterialAdmin(ModelView, model=EducationalMaterial):
    column_list = [
        EducationalMaterial.name,
        EducationalMaterial.description,
        EducationalMaterial.tags,
    ]
