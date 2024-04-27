from typing import Union

from fastapi import APIRouter

from messier import application
from messier.domain.core import exceptions
from messier.presentation.api import schemas
from messier.presentation.api.dependencies.ioc import CoreIoCDep

router = APIRouter(tags=['Auth'])


@router.post(
    '/register',
    response_model=application.register.RegisterResponseDTO,
    responses={
        400: {"model": Union[
            schemas.v1.common.err_responses.Schemas.LoginAlreadyOccupiedError,
        ]}
    }
)
async def register(
        ioc: CoreIoCDep,
        payload: application.register.RegisterDTO,
):
    async with ioc.register() as use_case:
        try:
            result = await use_case(
                payload,
            )
        except exceptions.authentication.LoginAlreadyOccupiedError:
            raise schemas.v1.common.err_responses.Exceptions.LoginAlreadyOccupiedError()
        except exceptions.identification.UnknownEmailDomainError:
            raise schemas.v1.common.err_responses.Exceptions.UnknownEmailDomainError()

        return result
