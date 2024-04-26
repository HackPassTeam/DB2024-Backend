from typing import Annotated, TypeAlias

from fastapi import Depends

from messier.presentation.interactor_factory import \
    TelegramInteractorFactory
from messier.presentation.interactor_factory.core import CoreInteractorFactory


async def get_ioc() -> CoreInteractorFactory:
    yield CoreInteractorFactory()


CoreIoCDep: TypeAlias = Annotated[CoreInteractorFactory, Depends(get_ioc)]


async def get_telegram_ioc() -> CoreInteractorFactory:
    yield TelegramInteractorFactory()


TelegramIoCDep: TypeAlias = Annotated[TelegramInteractorFactory, Depends(get_telegram_ioc)]
