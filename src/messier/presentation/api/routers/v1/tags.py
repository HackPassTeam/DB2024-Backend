from fastapi import APIRouter

from messier.application.get_tags.dto import GetTagsResponseDTO
from messier.presentation.api.dependencies.ioc import CoreIoCDep

router = APIRouter(tags=["Education", "Materials"])


@router.get(
    '/tags/',
    response_model=GetTagsResponseDTO,
)
async def get_educational_materials(
        ioc: CoreIoCDep
) -> GetTagsResponseDTO:
    async with ioc.get_tags() as use_case:
        return await use_case(None)
