from tgbot.database.models.base import Base
from tgbot.database.models.tasks import Task  # noqa: F401
from tgbot.database.db_session import engine


async def database_init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def database_close():
    await engine.dispose()
