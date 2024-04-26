from dataclasses import dataclass

from messier.domain.core.models.utm import UTMId
from messier.application.common.dto import UTMDTO


@dataclass
class WriteUTMDTO:
    utm_id: UTMId
    value: str


@dataclass
class WriteUTMResponseDTO:
    utm: UTMDTO
