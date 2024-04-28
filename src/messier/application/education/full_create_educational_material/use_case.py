from messier.application.common.dto import EducationalMaterialDTO
from messier.application.education.full_create_educational_material.dto import FullCreateEducationalMaterialDTO
from messier.application.education.get_education_materials.dto import GetEducationalMaterialsDTO, \
    GetEducationalMaterialsResponseDTO
from messier.domain.core.adapters.educational_material import AllEducationalMaterial
from messier.domain.core.services.educational_material import EducationalMaterialService
from messier.infrastructure.use_case import UseCase


class EducationalMaterialDTOself:
    pass


class FullCreateEducationalMaterialsUseCase(UseCase[FullCreateEducationalMaterialDTO, EducationalMaterialDTO]):

    # noinspection PyProtocol
    def __init__(
            self,
            educational_material_service: EducationalMaterialService,
            all_educational_material: AllEducationalMaterial
    ):
        self.educational_material = educational_material_service
        self.all = all_educational_material

    async def __call__(self, payload: GetEducationalMaterialsDTO) -> GetEducationalMaterialsResponseDTO:



        # res = await (
        #     self.all.create(
        #
        #     )
        # )

        edms = []
        for edm in res:
            edm_dto = await EducationalMaterialDTO.from_model(edm)
            edms.append(edm_dto)

        print(edms)

        return GetEducationalMaterialsResponseDTO(
            educational_material=edms
        )
