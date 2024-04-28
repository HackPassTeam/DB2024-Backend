from sqlalchemy import select

from messier.domain.core.models.education.tag import Tag
from messier.infrastructure.repo import BaseEntityRepo


class AllTag(BaseEntityRepo[Tag]):
    async def create(
            self,
            name: str,
            color: int,
    ):
        obj = Tag(
            name=name,
            color=color
        )
        await self.save(obj)
        return obj

    async def get_all(
            self,
            text: str
    ):
        stmt = (
            select(Tag)
            .order_by(Tag.name)
        )

        if text:
            stmt = stmt.where(Tag.name.ilike(f"%{text}%"))

        return await self.session.scalars(stmt)
