import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import (
    RedisStorage, RedisEventIsolation, DefaultKeyBuilder
)
from redis.asyncio import Redis

from messier.infrastructure.config import environment
from messier.presentation.telegram import routers, middlewares, error_handlers


def main():
    bot = Bot(environment.telegram_bot_token)

    redis = Redis(
        host=environment.redis_host, port=environment.redis_port,
    )
    key_builder = DefaultKeyBuilder(with_destiny=True)
    storage = RedisStorage(
        redis=redis,
        key_builder=key_builder,
    )
    events_isolation = RedisEventIsolation(
        redis=redis,
        key_builder=key_builder,
    )
    dp = Dispatcher(
        storage=storage, event_isolation=events_isolation,
    )

    mw = middlewares

    auth_fsm_middleware = mw.AuthenticationFSMContextOuterMiddleware(
        storage=storage, events_isolation=events_isolation,
    )

    dp.include_router(routers.router)
    dp.include_router(error_handlers.router)

    # additional core aiogram infrastructure
    dp.update.outer_middleware(auth_fsm_middleware)
    # aiogram infrastructure
    dp.message.outer_middleware(mw.StartPayloadOuterMiddleware())
    # application
    dp.update.outer_middleware(mw.IoCInjectionMiddleware())
    # domain
    dp.update.outer_middleware(mw.TelegramAccountMiddleware())
    dp.message.outer_middleware(mw.UTMInterceptorOuterMiddleware())
    dp.update.outer_middleware(mw.AuthorizationMiddleware())

    asyncio.run(dp.start_polling(bot))


if __name__ == '__main__':
    main()
