from messier.infrastructure.config import environment

imports = ('messier.infrastructure.notifier.backends.telegram.tasks',
           'messier.infrastructure.notifier.backends.email.tasks',)
broker_url = f"redis://{environment.redis_host}:{environment.redis_port}"
broker_connection_retry_on_startup = True
