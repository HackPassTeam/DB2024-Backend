from typing import Iterable

from messier.domain.core.adapters.theory import AllTheory
from messier.domain.core.models.education.educational_material import EducationalMaterial
from messier.domain.core.models.education.theory import Theory
from messier.infrastructure.service import BaseService


class TheoryService(BaseService):
    def __init__(
            self,
            all_theory: AllTheory
    ):
        self.all_theory = all_theory

    async def create(
            self,
            title: str,
            education_material: EducationalMaterial
    ) -> Theory:
        return await self.all_theory.create(title, education_material.id)

    async def all_by_educational_material(
            self,
            education_material: EducationalMaterial
    ) -> list[dict[int, str]]:
        return await self.all_theory.all_by_educational_material(education_material.id)

    async def delete(
            self,
            _id: int
    ) -> None:
        await self.all_theory.delete(_id)
