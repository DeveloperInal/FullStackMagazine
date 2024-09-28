from pydantic import Field
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from os import getenv

load_dotenv()
class Settings(BaseSettings):
    url_database: str = Field(getenv('URL_DATABASE'))
    bot_token: str = Field(getenv('BOT_TOKEN'))

    class Config:
        env_file = '.env'
        extra = 'forbid'

settings = Settings()