from typing import Iterable

from numpy import select

from messier.domain.core.models.education.educational_material import EducationalMaterial
from messier.domain.core.models.education.educational_material_tag import EducationalMaterialTag
from messier.domain.core.models.education.tag import Tag
from messier.infrastructure.repo import BaseEntityRepo


class AllEducationalMaterialTag(BaseEntityRepo[EducationalMaterialTag]):
    async def create_link(
            self,
            edm: EducationalMaterial,
            tag: Tag
    ):
        obj = EducationalMaterialTag(
            educational_material_id=edm.id,
            tag_id=tag.id
        )
        await self.save(obj)
        return obj
