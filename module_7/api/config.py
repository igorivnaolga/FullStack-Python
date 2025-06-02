from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 9000
    debug: bool = True
    database_uri: str = "postgresql://test:test@localhost:5432/pew"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls,
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
    ) -> tuple:
        return (
            env_settings,
            dotenv_settings,
            file_secret_settings,
            init_settings,
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()
