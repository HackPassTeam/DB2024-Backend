from __future__ import annotations

from random_coffee import application
from random_coffee.infrastructure.bases.interactor_factory import (
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
