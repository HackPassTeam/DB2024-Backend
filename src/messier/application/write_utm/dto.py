from dataclasses import dataclass

from messier.application.common.dto import UTMDTO
from messier.domain.core.models.utm import UTMId


@dataclass
class WriteUTMDTO:
    utm_id: UTMId
    value: str


@dataclass
class WriteUTMResponseDTO:
    utm: UTMDTO
