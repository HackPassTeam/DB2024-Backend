from dataclasses import dataclass, field
from typing import Optional

from messier.application.common.dto import EducationalMaterialDTO


@dataclass
class GetEducationalMaterialsDTO:
    tags: list[int] = field(default_factory=list)
    q: Optional[str] = ""
    page: int = 1
    size: int = 10


@dataclass
class GetEducationalMaterialsResponseDTO:
    educational_material: list[EducationalMaterialDTO]
