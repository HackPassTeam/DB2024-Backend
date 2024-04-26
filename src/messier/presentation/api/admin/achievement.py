from sqladmin import ModelView

from messier.domain.core.models.person.achievement import Achievement


class AchievementAdmin(ModelView, model=Achievement):
    column_list = [
        Achievement.id,
        Achievement.title,
        Achievement.description,
        Achievement.image,
    ]
