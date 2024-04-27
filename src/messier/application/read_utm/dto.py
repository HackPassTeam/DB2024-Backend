from dataclasses import dataclass

from messier.application.common.dto import UTMDTO
from messier.domain.core.models.utm import UTMId


@dataclass
class ReadUTMDTO:
    utm_id: UTMId


@dataclass
class ReadUTMResponseDTO:
    utm: UTMDTO
