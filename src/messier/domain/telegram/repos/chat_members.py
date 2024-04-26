from sqlalchemy import select

from messier.infrastructure.repo import BaseEntityRepo
from messier.domain.telegram.models import ChatMember


class AllChatMembers(BaseEntityRepo[ChatMember]):
    async def with_chat_and_account(
            self,
            telegram_chat_id: int,
            telegram_account_id: int,
    ) -> ChatMember | None:
        stmt = (select(ChatMember)
                .where(ChatMember.telegram_chat_id == telegram_chat_id)
                .where(ChatMember.telegram_account_id == telegram_account_id))

        return await self.session.scalar(stmt)
