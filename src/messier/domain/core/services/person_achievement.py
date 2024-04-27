from messier.domain.core.adapters import AllPersonsAchievements
from messier.domain.core.models.person.achievement import Achievement
from messier.domain.core.models.person.person import Person
from messier.domain.core.services.notification import NotificationService
from messier.infrastructure.bases.service import BaseService


class PersonAchievementService(BaseService):
    def __init__(
            self,
            notification_service: NotificationService,
            all_persons_achievement: AllPersonsAchievements,
    ):
        self.notification_service = notification_service
        self.all_persons_achievement = all_persons_achievement

    async def give_achievement(
            self,
            achievement: Achievement,
            person: Person,
    ):
        await self.all_persons_achievement.create(
            achievement_id=achievement.id,
            person_id=person.id,
        )
        await self.notification_service.notify_person(
            person_id=person.id,
            notification_content=
            f"Вы получили ачивку {achievement.title}!"
        )

    async def get_person_achievements(
            self,
            person: Person,
            page: int = 0,
            limit: int = 0
    ):
        return await self.all_persons_achievement.with_person_id(
            person_id=person.id,
            limit=limit,
            offset=limit * page,
        )
