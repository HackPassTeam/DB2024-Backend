from dataclasses import dataclass, field
from typing import Optional

from messier.application.common.dto import EducationalMaterialDTO


@dataclass
class FullCreateEducationalMaterialDTO:
    name: str
    description: str
    content: str
