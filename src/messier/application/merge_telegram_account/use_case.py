from messier.application.common.dto import TelegramAccountDTO
from messier.application.merge_telegram_account.dto import MergeTelegramAccountDTO, MergeTelegramAccountResponseDTO
from messier.domain.telegram.services import DatabaseSyncService
from messier.infrastructure.bases.use_case import UseCase


class MergeTelegramAccount(UseCase[MergeTelegramAccountDTO, MergeTelegramAccountResponseDTO]):
    # noinspection PyProtocol
    def __init__(
            self,
            telegram_service: DatabaseSyncService,
    ) -> None:
        self.telegram_service = telegram_service

    async def __call__(self, payload: MergeTelegramAccountDTO) -> MergeTelegramAccountResponseDTO:
        telegram_account = await self.telegram_service.find_telegram_account_by_telegram_id(
            telegram_id=payload.telegram_id,
        )

        if telegram_account is None:
            telegram_account = await self.telegram_service.create_telegram_account(
                telegram_id=payload.telegram_id,
                first_name=payload.first_name,
                last_name=payload.last_name,
                username=payload.username,
            )

        result = MergeTelegramAccountResponseDTO(
            telegram_account=await TelegramAccountDTO.from_model(
                telegram_account,
            )
        )
        return result
