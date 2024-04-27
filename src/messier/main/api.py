import locale

import uvicorn
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin

from messier.infrastructure.config import environment
from messier.infrastructure.database import engine, on_startup
from messier.presentation.api.admin import include_admin_views, auth_backend
from messier.presentation.api.routers import v1

app = FastAPI(title="RKSI API")


authentication_backend = auth_backend.SQLAdminAuth(environment.jwt_secret)
admin_app = Admin(
    app,
    engine=engine,
    authentication_backend=authentication_backend,
)
include_admin_views(admin_app)


origins = [
    "*"
    # "http://localhost",
    # "http://localhost:3000",
    # "https://localhost",
    # "https://localhost:3000",
]

if environment.allowed_origin:
    origins.append(environment.allowed_origin)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(v1.router)


@app.on_event("startup")
async def on_application_startup():
    await on_startup()
    scheduler = AsyncIOScheduler()
    scheduler.start()
    # scheduler.add_job()


def main():
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

    if environment.application_protocol == 'HTTP':
        uvicorn.run(
            app=f'{__name__}:app',
            host="0.0.0.0",
            port=8000,
            reload=environment.application_autoreload,
            reload_dirs=['src'],
            proxy_headers=True,
            forwarded_allow_ips="*",
        )
    elif environment.application_protocol == 'HTTPS':
        uvicorn.run(
            app=f'{__name__}:app',
            host="0.0.0.0",
            port=8000,
            ssl_certfile=environment.application_ssl_certfile,
            ssl_keyfile=environment.application_ssl_keyfile,
            reload=environment.application_autoreload,
            reload_dirs=['src'],
            proxy_headers=True,
            forwarded_allow_ips="*",
        )
    else:
        raise KeyError(f"Unknown protocol `{environment.application_protocol}`")


if __name__ == "__main__":
    main()
