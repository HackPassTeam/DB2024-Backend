from typing import Optional

from sqlalchemy import select, or_

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
        print(limit, offset, tags, text)
        stmt = (
            select(EducationalMaterial)
            .limit(limit)
            .offset(offset)
        )

        if tags:
            stmt = stmt.join(EducationalMaterial.tags).where(Tag.id.in_(tags))

        if text:
            stmt = stmt.where(
                or_(
                    EducationalMaterial.name.ilike(f'%{text}%'),
                    EducationalMaterial.description.ilike(f'%{text}%')
                )
            )

        res = await self.session.scalars(stmt)
        return res
