from dataclasses import dataclass

import aiogram.types

from messier.infrastructure.dto import BaseDTO


class UpsertTelegramEntitiesDTO(BaseDTO):
    user: aiogram.types.User | None = None
    chat: aiogram.types.Chat | None = None


@dataclass
class UpsertTelegramEntitiesResponseDTO:
    pass
