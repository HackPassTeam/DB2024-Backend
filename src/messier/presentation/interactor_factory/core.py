from __future__ import annotations

from messier import application
from messier.application.education.create_theory.use_case import CreateTheoryUseCase
from messier.application.education.get_education_materials.use_case import GetEducationalMaterialsUseCase
from messier.application.education.get_theories.use_case import GetTheoriesUseCase
from messier.application.education.get_theory.use_case import GetTheoryUseCase
from messier.application.get_tags.use_case import GetTagsUseCase
from messier.infrastructure.bases.interactor_factory import (
    BaseInteractorFactory,
    use_case_wrapper,
    WiredUseCase,
)


class CoreInteractorFactory(BaseInteractorFactory):
    @use_case_wrapper[application.register.Register]()
    async def register(
            self: CoreInteractorFactory, use_case: application.register.Register,
    ) -> WiredUseCase[application.register.Register]:
        yield use_case

    @use_case_wrapper[application.login.Login]()
    async def login(
            self: CoreInteractorFactory, use_case: application.login.Login,
    ) -> WiredUseCase[application.login.Login]:
        yield use_case

    @use_case_wrapper[application.authorize.Authorize]()
    async def authorize(
            self: CoreInteractorFactory, use_case: application.authorize.Authorize,
    ) -> WiredUseCase[application.authorize.Authorize]:
        yield use_case

    @use_case_wrapper[application.create_utm.CreateUTM]()
    async def create_utm(
            self: CoreInteractorFactory, use_case: application.create_utm.CreateUTM,
    ) -> WiredUseCase[application.create_utm.CreateUTM]:
        yield use_case

    @use_case_wrapper[application.read_utm.ReadUTM]()
    async def read_utm(
            self: CoreInteractorFactory, use_case: application.read_utm.ReadUTM,
    ) -> WiredUseCase[application.read_utm.ReadUTM]:
        yield use_case

    @use_case_wrapper[application.write_utm.WriteUTM]()
    async def write_utm(
            self: CoreInteractorFactory, use_case: application.write_utm.WriteUTM,
    ) -> WiredUseCase[application.write_utm.WriteUTM]:
        yield use_case

    @use_case_wrapper[application.confirm_identification.ConfirmIdentification]()
    async def confirm_identification(
            self: CoreInteractorFactory, use_case: application.confirm_identification.ConfirmIdentification,
    ) -> WiredUseCase[application.confirm_identification.ConfirmIdentification]:
        yield use_case

    @use_case_wrapper[application.edit_person.EditPerson]()
    async def edit_person(
            self: CoreInteractorFactory, use_case: application.edit_person.EditPerson,
    ) -> WiredUseCase[application.edit_person.EditPerson]:
        yield use_case

    @use_case_wrapper[application.passthrough.Passthrough]()
    async def passthrough(
            self: CoreInteractorFactory, use_case: application.passthrough.Passthrough,
    ) -> WiredUseCase[application.passthrough.Passthrough]:
        yield use_case

    @use_case_wrapper[application.get_my_achievements.GetMyAchievements]()
    async def get_my_achievements(
            self: CoreInteractorFactory, use_case: application.get_my_achievements.GetMyAchievements,
    ) -> WiredUseCase[application.get_my_achievements.GetMyAchievements]:
        yield use_case

    @use_case_wrapper[GetEducationalMaterialsUseCase]()
    async def get_educational_materials(
            self: CoreInteractorFactory, use_case: GetEducationalMaterialsUseCase,
    ) -> WiredUseCase[GetEducationalMaterialsUseCase]:
        yield use_case

    @use_case_wrapper[GetTagsUseCase]()
    async def get_tags(
            self: CoreInteractorFactory, use_case: GetTagsUseCase,
    ) -> WiredUseCase[GetTagsUseCase]:
        yield use_case

    @use_case_wrapper[CreateTheoryUseCase]()
    async def create_theory(
            self: CoreInteractorFactory, use_case: CreateTheoryUseCase,
    ) -> WiredUseCase[CreateTheoryUseCase]:
        yield use_case

    @use_case_wrapper[GetTheoriesUseCase]()
    async def get_theories(
            self: CoreInteractorFactory, use_case: GetTheoriesUseCase,
    ) -> WiredUseCase[GetTheoriesUseCase]:
        yield use_case

    @use_case_wrapper[GetTheoryUseCase]()
    async def get_theory(
            self: CoreInteractorFactory, use_case: GetTheoryUseCase,
    ) -> WiredUseCase[GetTheoryUseCase]:
        yield use_case

