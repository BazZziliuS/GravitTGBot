from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from tgbot.data.config import PATH_DATABASE

engine = create_async_engine(f"sqlite+aiosqlite:///{PATH_DATABASE}")
new_session = async_sessionmaker(engine, expire_on_commit=False)
