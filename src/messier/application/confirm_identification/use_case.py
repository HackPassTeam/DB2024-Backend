from messier.application.common.dto import PersonDTO
from messier.application.confirm_identification.dto import (
    ConfirmIdentificationDTO,
    ConfirmIdentificationResponseDTO,
)
from messier.domain.core.adapters import AllAccounts
from messier.domain.core.services import (
    AuthorizationService, AuthenticationService,
    IdentificationService,
)
from messier.infrastructure.bases.use_case import UseCase


class ConfirmIdentification(
    UseCase[ConfirmIdentificationDTO, ConfirmIdentificationResponseDTO],
):
    # noinspection PyProtocol
    def __init__(
            self,
            authorization_service: AuthorizationService,
            all_accounts: AllAccounts,
            authentication_service: AuthenticationService,
            identification_service: IdentificationService,
    ):
        self.authorization_service = authorization_service
        self.all_accounts = all_accounts
        self.authentication_service = authentication_service
        self.identification_service = identification_service

    async def __call__(
            self, payload: ConfirmIdentificationDTO
    ) -> ConfirmIdentificationResponseDTO:
        account = await self.all_accounts.with_id(payload.account_id)

        person = await self.identification_service.confirm_identification(
            account=account,
            confirmation_code=payload.confirmation_code,
        )
        return ConfirmIdentificationResponseDTO(
            person=await PersonDTO.from_model(person)
        )
