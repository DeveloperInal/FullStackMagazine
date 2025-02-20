from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()
class Settings(BaseSettings):
    url_database: str = Field(alias='URL_DATABASE')
    bot_token: str = Field(alias='BOT_TOKEN')

    model_config = SettingsConfigDict(
        env_file='.env',
        extra='forbid'
    )

settings = Settings()