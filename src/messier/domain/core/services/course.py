from typing import Iterable

from sqlalchemy import select

from messier.domain.core.adapters.course import AllCourses
from messier.domain.core.adapters.lesson import AllLessons
from messier.domain.core.models.education.course import Course
from messier.domain.core.models.education.educational_material import EducationalMaterial
from messier.domain.core.models.person.person import Person
from messier.infrastructure.service import BaseService


class CourseService(BaseService):

    def __init__(
            self,
            all_courses: AllCourses,
            all_lessons: AllLessons
    ):
        self.all_courses = all_courses

    async def create(
            self,
            educational_material: EducationalMaterial,
            person: Person
    ) -> Course:
        return await self.all_courses.create(educational_material.id, person.id)

    async def get_person_courses(
            self,
            person: Person,
            finished: bool = None
    ) -> Iterable[Course]:
        return await self.all_courses.all_by_person(person.id, finished)

    async def delete(
            self,
            course: Course
    ) -> None:
        return await self.all_courses.delete(course.id)
