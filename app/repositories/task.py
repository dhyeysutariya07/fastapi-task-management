from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.task import Task


class TaskRepository:

    @staticmethod
    async def create(db: AsyncSession, task: Task) -> Task:
        db.add(task)
        await db.commit()
        await db.refresh(task)
        return task

    @staticmethod
    async def list_by_user(db: AsyncSession, user_id: int) -> list[Task]:
        result = await db.execute(
            select(Task).where(Task.user_id == user_id)
        )
        return result.scalars().all()
