from fastapi import APIRouter

from messier.application.common.dto import TheoryDTO
from messier.application.education.create_theory.dto import CreateTheoryDTO
from messier.application.education.get_education_materials.dto import GetEducationalMaterialsDTO, \
    GetEducationalMaterialsResponseDTO
from messier.application.education.get_theories.dto import GetTheoriesDTO, GetTheoriesResponseDTO
from messier.application.education.get_theory.dto import GetTheoryDTO
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


@router.post(
    '/education/theories/create',
    response_model=None,
)
async def create_theory(
        ioc: CoreIoCDep,
        payload: CreateTheoryDTO
) -> None:
    async with ioc.create_theory() as use_case:
        await use_case(payload)


@router.post(
    '/education/theories/',
    response_model=GetTheoriesResponseDTO,
)
async def get_theories(
        ioc: CoreIoCDep,
        payload: GetTheoriesDTO
) -> GetTheoriesResponseDTO:
    async with ioc.get_theories() as use_case:
        return await use_case(payload)


@router.post(
    '/education/theory/',
    response_model=None,
)
async def get_theories(
        ioc: CoreIoCDep,
        payload: GetTheoryDTO
) -> TheoryDTO:
    async with ioc.get_theory() as use_case:
        return await use_case(payload)
