from sqlalchemy import select, update

from tgbot.database.models.tasks import Task
from tgbot.database.db_session import new_session


class Tasksx:
    @staticmethod
    async def add(user_id: int, text: str) -> int:
        async with new_session() as session:
            task = Task(user_id=user_id, text=text)
            session.add(task)
            await session.commit()
            return task.id

    @staticmethod
    async def get_active(user_id: int) -> list[tuple[int, str]]:
        async with new_session() as session:
            result = await session.execute(
                select(Task.id, Task.text)
                .where(Task.user_id == user_id, Task.done == False)
                .order_by(Task.id)
            )
            return list(result.tuples().all())

    @staticmethod
    async def complete(task_id: int, user_id: int) -> bool:
        async with new_session() as session:
            result = await session.execute(
                update(Task)
                .where(Task.id == task_id, Task.user_id == user_id, Task.done == False)
                .values(done=True)
            )
            await session.commit()
            return result.rowcount > 0
