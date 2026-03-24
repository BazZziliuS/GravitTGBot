import aiosqlite

from bot.config import DB_PATH


async def init_db() -> None:
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                text TEXT NOT NULL,
                done INTEGER NOT NULL DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        await db.commit()


async def add_task(user_id: int, text: str) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "INSERT INTO tasks (user_id, text) VALUES (?, ?)",
            (user_id, text),
        )
        await db.commit()
        return cursor.lastrowid


async def get_active_tasks(user_id: int) -> list[tuple[int, str]]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "SELECT id, text FROM tasks WHERE user_id = ? AND done = 0 ORDER BY id",
            (user_id,),
        )
        return await cursor.fetchall()


async def complete_task(task_id: int, user_id: int) -> bool:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "UPDATE tasks SET done = 1 WHERE id = ? AND user_id = ? AND done = 0",
            (task_id, user_id),
        )
        await db.commit()
        return cursor.rowcount > 0
