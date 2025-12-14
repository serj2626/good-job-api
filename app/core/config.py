from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/work.db"
    db_echo: bool = True

    # model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
