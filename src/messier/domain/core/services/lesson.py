from typing import Iterable

from messier.domain.core.adapters.lesson import AllLessons
from messier.domain.core.models.education.educational_material import EducationalMaterial
from messier.domain.core.models.education.lesson import Lesson
from messier.infrastructure.service import BaseService


class LessonService(BaseService):
    def __init__(
            self,
            all_lessons: AllLessons
    ):
        self.all_lessons = all_lessons

    async def create(
            self,
            education_material: EducationalMaterial,
            title: str,
            content,
            finished: bool
    ) -> Lesson:
        return await self.all_lessons.create(education_material.id)

    async def all_by_course(
            self,
            education_material: EducationalMaterial
    ) -> Iterable[Lesson]:
        return await self.all_lessons.all_by_course(education_material.id)

    async def delete(
            self,
            _id: int
    ) -> None:
        await self.all_lessons.delete(_id)