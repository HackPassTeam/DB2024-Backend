from dataclasses import dataclass

from messier.application.common.dto import PersonDTO


@dataclass
class ConfirmIdentificationDTO:
    account_id: int
    confirmation_code: str


@dataclass
class ConfirmIdentificationResponseDTO:
    person: PersonDTO
