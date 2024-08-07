from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base


POSTGRES_USER = settings.pg_database.POSTGRES_USER
POSTGRES_PASS = settings.pg_database.POSTGRES_PASS
POSTGRES_HOST = settings.pg_database.POSTGRES_HOST
POSTGRES_PORT = settings.pg_database.POSTGRES_PORT
POSTGRES_NAME = settings.pg_database.POSTGRES_NAME
POSTGRES_ECHO = settings.pg_database.POSTGRES_ECHO
POSTGRES_POOL = settings.pg_database.POSTGRES_POOL


async_url = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}"

async_engine = create_async_engine(
    url=async_url,
    echo=POSTGRES_ECHO,
    future=True,
    pool_size=POSTGRES_POOL,
    pool_pre_ping=True,
    pool_timeout=60,
)

async_session = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
    autocommit=False
)

sync_url = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}"

sync_engine = create_engine(
    url=sync_url,
    echo=False
)

sync_session = sessionmaker(
    sync_engine,
    expire_on_commit=False,
    autocommit=False
)

Base = declarative_base()
