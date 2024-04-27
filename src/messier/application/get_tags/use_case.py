from messier.application.common.dto import TagDTO
from messier.application.get_tags.dto import GetTagsResponseDTO
from messier.domain.core.adapters.tag import AllTag
from messier.infrastructure.use_case import UseCase


class EducationalMaterialDTOself:
    pass


class GetTagsUseCase(UseCase[None, GetTagsResponseDTO]):
    # noinspection PyProtocol
    def __init__(
            self,
            all_tag: AllTag
    ):
        self.all_tag = all_tag

    async def __call__(self, payload: None) -> GetTagsResponseDTO:
        res = await self.all_tag.get_all()

        tags = []
        for tag in res:
            tag_dto = await TagDTO.from_model(tag)
            tags.append(tag_dto)

        print(tags)

        return GetTagsResponseDTO(
            tags=tags
        )
