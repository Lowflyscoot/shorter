from dishka import provide, Provider, Scope
from fastapi.requests import Request
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm.session import Session, sessionmaker

from .models import Base


def init_db(engine):
    Base.metadata.create_all(bind=engine)


def get_engine(db_url):
    return create_async_engine(db_url)


class DBProvider(Provider):
    def __init__(self, db_url):
        super().__init__()
        self.sync_engine = create_engine(db_url)
        self.async_engine = create_async_engine(db_url)

    def create_tables(self):
        Base.metadata.create_all(bind=self.sync_engine)

    @provide(scope=Scope.REQUEST)
    def get_sync_session(self, request: Request) -> Session:
        return sessionmaker(self.sync_engine)

    @provide(scope=Scope.REQUEST)
    async def get_async_session(self, request: Request) -> AsyncSession:
        return async_sessionmaker(self.async_engine)
