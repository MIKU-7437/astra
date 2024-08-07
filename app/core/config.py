import os
from dataclasses import dataclass
from pydantic_settings import BaseSettings
from pydantic import Field
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class EnvSettings(BaseSettings):
    POSTGRES_USER: str = Field(..., env='POSTGRES_USER')
    POSTGRES_PASS: str = Field(..., env='POSTGRES_PASS')
    POSTGRES_HOST: str = Field(..., env='POSTGRES_HOST')
    POSTGRES_PORT: str = Field(..., env='POSTGRES_PORT')
    POSTGRES_NAME: str = Field(..., env='POSTGRES_NAME')
    POSTGRES_ECHO: bool = Field(..., env='POSTGRES_ECHO')
    POSTGRES_POOL: int = Field(..., env='POSTGRES_POOL')

    APP_HOST: str = Field(..., env='APP_HOST')
    APP_PORT: str = Field(..., env='APP_PORT')
    SECRET_KEY: str = Field(..., env='SECRET_KEY')


    class Config:
        env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env")
        extra = 'allow'


env_settings = EnvSettings()


@dataclass
class PostgresDatabaseConfig:
    POSTGRES_USER: str = env_settings.POSTGRES_USER
    POSTGRES_PASS: str = env_settings.POSTGRES_PASS
    POSTGRES_HOST: str = env_settings.POSTGRES_HOST
    POSTGRES_PORT: str = env_settings.POSTGRES_PORT
    POSTGRES_NAME: str = env_settings.POSTGRES_NAME
    POSTGRES_ECHO: bool = env_settings.POSTGRES_ECHO
    POSTGRES_POOL: int = env_settings.POSTGRES_POOL


    @property
    def async_url(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASS}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_NAME}"

    @property
    def sync_url(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASS}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_NAME}"

    @property
    def async_engine(self):
        return create_async_engine(
            url=self.async_url,
            echo=self.POSTGRES_ECHO,
            future=True,
            pool_size=self.POSTGRES_POOL,
            pool_pre_ping=True,
            pool_timeout=60,
        )

    @property
    def async_session(self):
        return async_sessionmaker(
            self.async_engine,
            expire_on_commit=False,
            autocommit=False
        )

    @property
    def sync_engine(self):
        return create_engine(
            url=self.sync_url,
            echo=False
        )

    @property
    def sync_session(self):
        return sessionmaker(
            self.sync_engine,
            expire_on_commit=False,
            autocommit=False
        )



# @dataclass
# class JWTConfig:
#     SECRET_KEY: str = env_settings.JWT_SECRET_KEY
#     ALGORITHM: str = env_settings.ALGORITHM
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = env_settings.ACCESS_TOKEN_EXPIRE_MINUTES
#     REFRESH_TOKEN_EXPIRE_DAYS: int = env_settings.REFRESH_TOKEN_EXPIRE_DAYS
#
#
# @dataclass
# class RedisConfig:
#     REDIS_USER: str = env_settings.REDIS_USER
#     REDIS_PASS: str = env_settings.REDIS_PASS
#     REDIS_HOST: str = env_settings.REDIS_HOST
#     REDIS_PORT: str = env_settings.REDIS_PORT
#
#
# @dataclass
# class SMTPConfig:
#     DOMAIN_NAME: str = env_settings.SMTP_DOMAIN_NAME
#     SMTP_PORT: str = env_settings.SMTP_PORT
#     API_KEY: str = env_settings.SMTP_API_KEY
#     EMAIL_FROM: str = env_settings.SMTP_EMAIL_FROM
#
#
# @dataclass
# class TwilioConfig:
#     AUTH_TOKEN: str = env_settings.AUTH_TOKEN
#     ACCOUNT_SID: str = env_settings.ACCOUNT_SID
#     TWILIO_PHONE: str = env_settings.TWILIO_PHONE


class Settings:
    def __init__(self):
        self.pg_database = PostgresDatabaseConfig()
        # self.jwt_config = JWTConfig()
        # self.redis_config = RedisConfig()
        # self.smtp_config = SMTPConfig()
        # self.twilio_config = TwilioConfig()


settings: Settings = Settings()
