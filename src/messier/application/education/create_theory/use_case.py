from messier.application.education.create_theory.dto import CreateTheoryDTO
from messier.domain.core.adapters.theory import AllTheory
from messier.infrastructure.use_case import UseCase


class CreateTheoryUseCase(UseCase[CreateTheoryDTO, None]):

    # noinspection PyProtocol
    def __init__(
            self,
            all_theory: AllTheory
    ):
        self.all_theory = all_theory

    async def __call__(
            self,
            payload: CreateTheoryDTO
    ) -> None:
        await self.all_theory.create(
            title=payload.title,
            description=payload.description,
            educational_material_id=payload.educational_material_id
        )
