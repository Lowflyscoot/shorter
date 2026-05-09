from pydantic_settings import BaseSettings
from pathlib import Path


BACKEND_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    database_url: str

    class Config():
        env_file = BACKEND_DIR / ".env"

settings = Settings()
