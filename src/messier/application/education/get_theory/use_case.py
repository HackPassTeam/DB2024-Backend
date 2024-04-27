from messier.application.common.dto import TheoryDTO
from messier.application.education.get_theories.dto import GetTheoriesDTO, GetTheoriesResponseDTO
from messier.application.education.get_theory.dto import GetTheoryDTO
from messier.domain.core.adapters.theory import AllTheory
from messier.infrastructure.use_case import UseCase


class GetTheoryUseCase(UseCase[GetTheoryDTO, TheoryDTO]):

    # noinspection PyProtocol
    def __init__(
            self,
            all_theory: AllTheory
    ):
        self.all_theory = all_theory

    async def __call__(self, payload: GetTheoryDTO) -> TheoryDTO:
        res = await self.all_theory.by_id(
            theory_id=payload.id
        )

        return await TheoryDTO.from_model(res)
