from sqladmin import Admin

from .achievement import AchievementAdmin
from .educational_material import EducationalMaterialAdmin
from .notification_destination import NotificationDestinationAdmin
from .person import PersonAdmin
from .tag import TagAdmin
from .theory import TheoryAdmin


def include_admin_views(admin_app: Admin):
    admin_app.add_view(PersonAdmin)
    admin_app.add_view(NotificationDestinationAdmin)
    admin_app.add_view(AchievementAdmin)
    admin_app.add_view(TagAdmin)
    admin_app.add_view(EducationalMaterialAdmin)
    admin_app.add_view(TheoryAdmin)
