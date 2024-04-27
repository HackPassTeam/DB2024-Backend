from typing import Optional

from sqlalchemy import select, or_, and_, any_

from messier.domain.core.models.education.educational_material import EducationalMaterial
from messier.domain.core.models.education.educational_material_tag import EducationalMaterialTag
from messier.domain.core.models.education.tag import Tag
from messier.infrastructure.repo import BaseEntityRepo


class AllEducationalMaterialTag(BaseEntityRepo[EducationalMaterialTag]):
    async def create_link(
            self,
            edm_id: int,
            tag_id: int
    ):
        obj = EducationalMaterialTag(
            educational_material_id=edm_id,
            tag_id=tag_id
        )

        await self.save(obj)
        return obj

    async def get_filtered(
            self,
            tags: list[int],
            limit: int,
            offset: int,
            text: Optional[str] = None
    ):
        stmt = (
            select(EducationalMaterial)
            .where(Tag.id.in_(tags))
            .limit(limit)
            .offset(offset)
        )

        if text:
            stmt.where(
                and_(
                    or_(
                        EducationalMaterial.name.contains(text),
                        EducationalMaterial.name.contains(text)
                    )
                )
            )

        res = await self.session.scalars(stmt)
        return res
