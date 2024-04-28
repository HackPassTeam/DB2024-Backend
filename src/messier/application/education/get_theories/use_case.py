from messier.application.common.dto import ShortTheoryDTO
from messier.application.education.get_theories.dto import GetTheoriesDTO, GetTheoriesResponseDTO
from messier.domain.core.adapters.theory import AllTheory
from messier.infrastructure.use_case import UseCase


class GetTheoriesUseCase(UseCase[GetTheoriesDTO, GetTheoriesResponseDTO]):

    # noinspection PyProtocol
    def __init__(
            self,
            all_theory: AllTheory
    ):
        self.all_theory = all_theory

    async def __call__(self, payload: GetTheoriesDTO) -> GetTheoriesResponseDTO:
        res = await self.all_theory.all_by_educational_material(
            educational_material_id=payload.id
        )

        data = []
        for theory in res:
            data.append(
                ShortTheoryDTO.from_model(theory)
            )

        return GetTheoriesResponseDTO(
            theories=data
        )
