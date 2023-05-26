from functools import lru_cache
from pathlib import Path
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    PROJECT_NAME: str = Field(env='PROJECT_NAME', default='Movies async api')

    API_URL: str = Field(env='API_URL', default='https://pogoda.mail.ru')

    REDIS_HOST: str = Field(env='REDIS_HOST', default='127.0.0.1')
    REDIS_PORT: int = Field(env='REDIS_PORT', default=6379)
    
    class Config:
        __BASE_DIR_PATH = Path(__file__).parent.parent.parent
        __ENV_FILE_PATH = __BASE_DIR_PATH / '.env' / '.env.dev'

        env_file = __ENV_FILE_PATH
        env_file_encoding = 'utf-8'


__settings = Settings()

@lru_cache
def get_settings_instance():
    return __settings