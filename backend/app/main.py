from contextlib import asynccontextmanager
from os import environ

from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka, FastapiProvider
from fastapi import FastAPI

from core import get_settings_from_envvars
from db import DBProvider
from routes import links_router


settings = get_settings_from_envvars(environ)


db_provider = DBProvider(settings.database_url)
container = make_async_container(
    db_provider,
    FastapiProvider(),
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_provider.create_tables()
    yield
    await app.state.dishka_container.close()


shorter_app = FastAPI(lifespan=lifespan)
shorter_app.include_router(links_router)

setup_dishka(container=container, app=shorter_app)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:shorter_app", host="127.0.0.1", port=80, reload=True)
