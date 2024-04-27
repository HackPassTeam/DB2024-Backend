from dataclasses import dataclass

from messier.application.common.dto import TagDTO


@dataclass
class GetTagsResponseDTO:
    tags: list[TagDTO]
