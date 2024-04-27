from fastapi import APIRouter

from messier.application.get_education_materials.dto import GetEducationalMaterialsResponseDTO, \
    GetEducationalMaterialsDTO
from messier.presentation.api.dependencies.ioc import CoreIoCDep

router = APIRouter(tags=["Education", "Materials"])


@router.post(
    '/education/materials/get',
    response_model=GetEducationalMaterialsResponseDTO,
)
async def get_educational_materials(
        ioc: CoreIoCDep,
        payload: GetEducationalMaterialsDTO
) -> GetEducationalMaterialsResponseDTO:
    async with ioc.get_educational_materials() as use_case:
        return await use_case(payload)
