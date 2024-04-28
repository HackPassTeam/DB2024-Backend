from dataclasses import dataclass

from messier.application.common.dto import AccountDTO
from messier.infrastructure.security.scopes import AccessScopeEnum


@dataclass
class AuthorizeDTO:
    access_token: str
    access_scopes: set[AccessScopeEnum]


@dataclass
class AuthorizeResponseDTO:
    account: AccountDTO
