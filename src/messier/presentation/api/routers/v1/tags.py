from fastapi import APIRouter

from messier.application.get_tags.dto import GetTagsResponseDTO, GetTagsDTO
from messier.presentation.api.dependencies.ioc import CoreIoCDep

router = APIRouter(tags=["Education", "Materials"])


@router.post(
    '/tags',
    response_model=GetTagsResponseDTO,
)
async def get_educational_materials(
        ioc: CoreIoCDep,
        payload: GetTagsDTO
) -> GetTagsResponseDTO:
    async with ioc.get_tags() as use_case:
        return await use_case(payload)
