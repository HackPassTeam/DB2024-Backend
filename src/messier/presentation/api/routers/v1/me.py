from typing import Annotated

from fastapi import APIRouter, Depends

from messier.application.common.dto import PersonDTO, AccountDTO
from messier.application.edit_person import EditPersonDTO, \
    EditPersonResponseDTO
from messier.application.get_my_achievements import \
    GetMyAchievementsResponseDTO, GetMyAchievementsDTO
from messier.presentation.api import dependencies
from messier.presentation.api.dependencies.ioc import CoreIoCDep

router = APIRouter(tags=['Me'])


@router.get(
    '/me/person',
    response_model=PersonDTO,
)
async def get_me(
        person: Annotated[PersonDTO, Depends(dependencies.get_current.get_current_person)]
) -> PersonDTO:
    return person


@router.get(
    "/me/person/achievements",
    response_model=GetMyAchievementsResponseDTO,
)
async def get_my_achievements(
        person: Annotated[PersonDTO, Depends(dependencies.get_current.get_current_person)],
        ioc: CoreIoCDep,
):
    async with ioc.get_my_achievements() as use_case:
        return await use_case(GetMyAchievementsDTO(
            person_id=person.id,
        ))


@router.post(
    '/me/person/edit',
    response_model=EditPersonResponseDTO,
)
async def get_me(
        person: Annotated[PersonDTO, Depends(dependencies.get_current.get_current_person)],
        payload: EditPersonDTO,
        ioc: CoreIoCDep,
) -> EditPersonResponseDTO:
    payload.entity_id = person.id
    async with ioc.edit_person() as use_case:
        response = await use_case(payload)

    return response


@router.get(
    '/me/account',
    response_model=AccountDTO,
)
async def get_my_account(
        account: Annotated[AccountDTO, Depends(dependencies.get_current.get_current_account)]
):
    return account
