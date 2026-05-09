from sqlalchemy.ext.asyncio import create_async_engine
from app.core.config import settings
from app.db.base import Base

from app.db.models import links  

async def init_db():
    engine = create_async_engine(settings.database_url)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()
