from dataclasses import dataclass


@dataclass
class Settings:
    database_url: str


def get_settings_from_envvars(env: dict) -> Settings:
    url = env.get("DATABASE_URL")
    user = env.get("DATABASE_USER")
    password = env.get("DATABASE_PASSWORD")
    port = env.get("DATABASE_PORT")

    if url is None or user is None or password is None or port is None:
        raise Exception("Where is my database?")

    return Settings(
        database_url=f"postgresql+psycopg://{user}:{password}@{url}:{port}/shorter",
    )
