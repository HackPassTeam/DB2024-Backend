from dataclasses import dataclass, field
from typing import Optional

from messier.application.common.dto import EducationalMaterialDTO, TagDTO


@dataclass
class GetTagsResponseDTO:
    tags: list[TagDTO]
