from typing import Iterable

from sqlalchemy import select

from messier.domain.core.models.education.theory import Theory
from messier.infrastructure.repo import BaseEntityRepo


class AllTheory(BaseEntityRepo[Theory]):
    async def create(
            self,
            title: str,
            description: str,
            educational_material_id: int
    ) -> Theory:
        obj = Theory(
            title=title,
            content=description,
            educational_material_id=educational_material_id
        )
        await self.save(obj)
        return obj

    async def all_by_educational_material(
            self,
            educational_material_id: int
    ) -> list[tuple[int, str]]:
        stmt = (
            select(Theory.id, Theory.title)
            .where(Theory.educational_material_id == educational_material_id)
            .order_by(Theory.id)
        )

        res = await self.session.execute(stmt)
        return res

    async def by_id(
            self,
            theory_id: int
    ) -> Theory:
        stmt = (
            select(Theory)
            .where(Theory.id == theory_id)
        )

        res = await self.session.scalars(stmt)
        return res.one()


    async def delete(
            self,
            _id: int
    ) -> None:
        return await self.delete_by_id(_id)
