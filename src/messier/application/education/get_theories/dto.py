from dataclasses import dataclass

from messier.application.common.dto import TheoryDTO, ShortTheoryDTO


@dataclass
class GetTheoriesDTO:
    id: int


@dataclass
class GetTheoriesResponseDTO:
    theories: list[ShortTheoryDTO]
