from messier.application.common.dto import AccountDTO
from messier.domain.core.services import (
    AuthenticationService,
    IdentificationService, )
from messier.infrastructure.bases.use_case import UseCase
from .dto import RegisterDTO, RegisterResponseDTO
from ...domain.core.adapters.person import AllPersons


class Register(UseCase[RegisterDTO, RegisterResponseDTO]):
    # noinspection PyProtocol
    def __init__(
            self,
            all_persons: AllPersons,
            authentication_service: AuthenticationService,
            identification_service: IdentificationService,
    ):
        self.all_persons = all_persons
        self.authentication_service = authentication_service
        self.identification_service = identification_service

    async def __call__(self, payload: RegisterDTO) -> RegisterResponseDTO:
        print(payload)

        person = await self.identification_service.create_person(
            full_name=payload.full_name,
        )
        account = await self.authentication_service.register_account(
            email=payload.email,
            password=payload.password,
            person=person,
        )

        result = RegisterResponseDTO(
            account=await AccountDTO.from_model(
                model=account,
            ),
        )
        return result
