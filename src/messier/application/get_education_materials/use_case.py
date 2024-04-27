from messier.application.common.dto import EducationalMaterialDTO
from messier.application.get_education_materials.dto import GetEducationalMaterialsResponseDTO, \
    GetEducationalMaterialsDTO
from messier.domain.core.services.educational_material import EducationalMaterialService
from messier.infrastructure.use_case import UseCase


class EducationalMaterialDTOself:
    pass


class GetEducationalMaterialsUseCase(UseCase[GetEducationalMaterialsDTO, GetEducationalMaterialsResponseDTO]):
    # noinspection PyProtocol
    def __init__(
            self,
            educational_material: EducationalMaterialService
    ):
        self.educational_material = educational_material

    async def __call__(self, payload: GetEducationalMaterialsDTO) -> GetEducationalMaterialsResponseDTO:
        res = await (
            self.educational_material
            .get_educational_materials(
                tags=payload.tags,
                q=payload.q,
                page=payload.page,
                size=payload.size
            )
        )

        edms = []
        for edm in res:
            edm_dto = await EducationalMaterialDTO.from_model(edm)
            edms.append(edm_dto)

        print(edms)

        return GetEducationalMaterialsResponseDTO(
            educational_material=edms
        )
