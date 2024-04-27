from dataclasses import dataclass

from pydantic import EmailStr

from messier.application.common.dto import AccountDTO
from messier.infrastructure.dto import BaseDTO


class RegisterDTO(BaseDTO):
    email: EmailStr
    password: str
    full_name: str


@dataclass
class RegisterResponseDTO:
    account: AccountDTO
