from messier.application.common.dto import (
    UTMDTO,
)
from messier.domain.core.services import (
    UTMService,
)
from messier.infrastructure.bases.use_case import UseCase
from .dto import CreateUTMDTO, CreateUTMResponseDTO


class CreateUTM(UseCase[CreateUTMDTO, CreateUTMResponseDTO]):
    # noinspection PyProtocol
    def __init__(
            self,
            utm_service: UTMService,
    ):

        self.utm_service = utm_service

    async def __call__(
            self, payload: CreateUTMDTO
    ) -> CreateUTMResponseDTO:
        result = await self.utm_service.create_utm(
            value=payload.value,
            expire_seconds=payload.expire_seconds,
            read_limit=payload.read_limit,
        )

        return CreateUTMResponseDTO(
            utm=await UTMDTO.from_model(result)
        )
