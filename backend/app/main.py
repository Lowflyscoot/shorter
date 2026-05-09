from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import links
from app.db.init_db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(links.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="192.168.0.12", port=8000, reload=True)
