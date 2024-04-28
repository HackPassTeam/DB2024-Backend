from messier.infrastructure.config import Environment
from .backends import (
    TelegramNotifierBackend,
    EmailNotifierBackend,
)
from .interface import Notifier


def build_notifier(environment: Environment) -> Notifier:
    result = Notifier(
        [
            TelegramNotifierBackend(
                bot_token=environment.telegram_bot_token,
            ),
            EmailNotifierBackend(),
        ],
    )
    return result
