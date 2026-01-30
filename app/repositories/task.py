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

    @staticmethod
    async def get_all(db:AsyncSession)->list[Task]:
        result = await db.execute(select(Task).order_by(Task.created_at))
        return result.scalars().all() 

    
    @staticmethod
    async def get_task(db:AsyncSession,task_id:int)->Task:
        result = await db.execute(select(Task).where(Task.id == task_id))
        return result.scalar_one_or_none()
    
    @staticmethod
    async def update_task(
        db: AsyncSession,
        task: Task,
        updates: dict) -> Task:
        for field, value in updates.items():
            setattr(task, field, value)

        await db.commit()
        await db.refresh(task)
        return task

    
    @staticmethod
    async def delete_task(db:AsyncSession,task:Task)->None:
        await db.delete(task)
        await db.commit()
