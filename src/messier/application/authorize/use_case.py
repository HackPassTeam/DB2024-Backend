from messier.application.authorize.dto import AuthorizeDTO, AuthorizeResponseDTO
from messier.application.common.dto import AccountDTO
from messier.domain.core.adapters.account import AllAccounts
from messier.domain.core.exceptions.authorization import \
    InvalidCredentialsError
from messier.domain.core.services import (
    AuthorizationService, AuthenticationService,
)
from messier.infrastructure.bases.use_case import UseCase
from messier.infrastructure.security.token import decode_access_token, \
    InvalidCredentialsError as SubdomainInvalidCredentialsError


class Authorize(UseCase[AuthorizeDTO, AuthorizeResponseDTO]):
    """Authorize use case

    This use case processes authorization, based on JWT tokens.
    Caller must pass all access scopes to check, is token allows
    to access this scopes. Token can encapsulate any information.
    Typically, token encapsulates prove of person's authorization.
    So, in this case, will be checked if token is correct and person
    steel have allocated permissions.

    """

    # noinspection PyProtocol
    def __init__(
            self,
            authorization_service: AuthorizationService,
            all_accounts: AllAccounts,
            authentication_service: AuthenticationService,
    ):
        self.authorization_service = authorization_service
        self.all_accounts = all_accounts
        self.authentication_service = authentication_service

    async def __call__(self, payload: AuthorizeDTO) -> AuthorizeResponseDTO:
        access_token = payload.access_token

        try:
            decoded_access_token = decode_access_token(access_token)
        except SubdomainInvalidCredentialsError:
            raise InvalidCredentialsError()

        login = decoded_access_token.sub.login
        print(login)
        account = await self.all_accounts.with_login(login=login)

        await self.authorization_service.authorize_account(
            account=account,
            access_scopes=payload.access_scopes,
        )

        account_dto = await AccountDTO.from_model(
            model=account,
        )
        return AuthorizeResponseDTO(
            account=account_dto,
        )
