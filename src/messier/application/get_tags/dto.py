from dataclasses import dataclass

from messier.application.common.dto import TagDTO


@dataclass
class GetTagsDTO:
    q: str


@dataclass
class GetTagsResponseDTO:
    tags: list[TagDTO]
