from datetime import datetime

from messier.infrastructure.repo import BaseEntityRepo
from messier.domain.core.models import UTM


class AllUTMs(BaseEntityRepo[UTM]):
    async def create(
            self,
            value: str | None,
            expire_at: datetime,
            read_limit: int,
    ) -> UTM:
        obj = UTM(
            value=value,
            expire_at=expire_at,
            read_limit=read_limit,
        )
        self.session.add(obj)
        await self.session.flush()
        return obj
