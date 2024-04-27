from messier.domain.core.models.education.educational_material import EducationalMaterial
from messier.infrastructure.repo import BaseEntityRepo


class AllEducationalMaterial(BaseEntityRepo[EducationalMaterial]):
    async def create(
            self,
            name: str,
            description: str,
    ):
        obj = EducationalMaterial(
            name=name,
            description=description
        )
        await self.save(obj)
        return obj
