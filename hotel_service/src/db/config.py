from pydantic import BaseSettings 

class DatabaseSettings(BaseSettings):
    POSTGRES_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_HOST: str
    POSTGRES_DB: str

    class Config:
        env_file = "./.env"

settings = DatabaseSettings()