from fastapi import APIRouter

from messier.application.create_utm import (
    CreateUTMDTO, CreateUTMResponseDTO
)
from messier.application.write_utm import (
    WriteUTMDTO, WriteUTMResponseDTO,
)
from messier.presentation.api.dependencies.ioc import CoreIoCDep


router = APIRouter(tags=["UTM"])


@router.post(
    '/utm',
    response_model=CreateUTMResponseDTO,
)
async def create_utm(
        ioc: CoreIoCDep,
        payload: CreateUTMDTO,
):
    async with ioc.create_utm() as use_case:
        result = await use_case(payload)

    return result


@router.put(
    '/utm',
    response_model=WriteUTMResponseDTO,
)
async def write_utm(
        ioc: CoreIoCDep,
        payload: WriteUTMDTO,
):
    async with ioc.write_utm() as use_case:
        result = await use_case(payload)

    return result
