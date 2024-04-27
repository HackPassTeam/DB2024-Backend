from messier.domain.core.adapters.educational_material import AllEducationalMaterial
from messier.domain.core.adapters.educational_material_tag import AllEducationalMaterialTag
from messier.domain.core.models.education.educational_material import EducationalMaterial
from messier.infrastructure.service import BaseService


class EducationalMaterialService(BaseService):
    def __init__(
            self,
            all_educational_material: AllEducationalMaterial,
            all_educational_material_tag: AllEducationalMaterialTag,
    ):
        self.all_educational_material = all_educational_material
        self.all_educational_material_tag = all_educational_material_tag

    async def get_educational_materials(
            self,
            tags: list[int],
            q: str,
            page: int,
            size: int = 10
    ) -> list[EducationalMaterial]:
        return await self.all_educational_material_tag.get_filtered(
            tags=tags,
            text=q,
            limit=size,
            offset=(page - 1) * size,
        )
