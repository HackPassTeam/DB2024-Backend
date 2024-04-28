from typing import Annotated

from fastapi import APIRouter, Depends

from messier.application.confirm_identification import (
    ConfirmIdentificationDTO,
    ConfirmIdentificationResponseDTO,
)
from messier.domain.core import models
from messier.infrastructure.dto import BaseDTO
from messier.presentation.api import dependencies
from messier.presentation.api.dependencies.ioc import CoreIoCDep

router = APIRouter(tags=["Me", "Identification"])


class IdentificationConfirmationSchemeDTO(BaseDTO):
    confirmation_code: str


@router.post(
    "/me/account/identification/confirm",
    response_model=ConfirmIdentificationResponseDTO,
)
async def confirm_identification(
        ioc: CoreIoCDep,
        current_account: Annotated[
            models.Account,
            Depends(dependencies.get_current.get_current_account),
        ],
        payload: IdentificationConfirmationSchemeDTO,
):
    async with ioc.confirm_identification() as use_case:
        result = await use_case(ConfirmIdentificationDTO(
            account_id=current_account.id,
            confirmation_code=payload.confirmation_code,
        ))
        return result
