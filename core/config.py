from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/shop.db"
    db_echo: bool = True

    # model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
