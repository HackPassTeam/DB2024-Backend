from typing import Iterable

from sqlalchemy import update

from messier.domain.telegram.models import TelegramAccount
from messier.infrastructure.repo import BaseEntityRepo


class AllAccounts(BaseEntityRepo[TelegramAccount]):
    async def mark_inactive(self, account_ids: Iterable[int]):
        stmt = (update(TelegramAccount)
                .where(TelegramAccount.id.in_(account_ids))
                .values(is_active=False))
        return await self.session.execute(stmt)

    async def mark_active(self, account_ids: Iterable[int]):
        stmt = (update(TelegramAccount)
                .where(TelegramAccount.id.in_(account_ids))
                .values(is_active=True))
        return await self.session.execute(stmt)
