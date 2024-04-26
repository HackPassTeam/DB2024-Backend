from dataclasses import dataclass

from messier.domain.core.models.utm import UTMId
from messier.application.common.dto import UTMDTO


@dataclass
class ReadUTMDTO:
    utm_id: UTMId


@dataclass
class ReadUTMResponseDTO:
    utm: UTMDTO
