from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing_extensions import Annotated

from messier.application.login import (
    LoginDTO,
)
from messier.domain.core import exceptions
from messier.presentation.api.dependencies.ioc import CoreIoCDep
from messier.presentation.api.schemas.v1 import token as schemas

router = APIRouter(tags=["Auth"])


@router.post(
    '/token',
    response_model=schemas.Token,
)
async def login(
        ioc: CoreIoCDep,
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    async with ioc.login() as use_case:
        try:
            result = await use_case(LoginDTO(
                login=form_data.username,
                password=form_data.password,
                security_scopes=form_data.scopes,
            ))
        except exceptions.authentication.AuthenticationError:
            raise HTTPException(status_code=400,
                                detail="Incorrect username or password")

        return {"access_token": result.access_token, "token_type": "bearer"}
