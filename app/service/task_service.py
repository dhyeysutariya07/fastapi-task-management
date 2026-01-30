from app.models.task import Task
from app.schema.task import TaskCreate,TaskUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.task import TaskRepository
from typing import List
from fastapi.exceptions import HTTPException
from fastapi import status


class TaskService:
    @staticmethod
    async def create(db:AsyncSession,task:TaskCreate)->Task:
        task_to_create = Task(
            title = task.title,
            priority = task.priority,
            estimated_hours = task.estimated_hours
        )

        task =await TaskRepository.create(db,task_to_create)
        return task

    @staticmethod
    async def get(db:AsyncSession,task_id:int)->Task:
        task = await TaskRepository.get_task(db,task_id)
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
        return task
    
    @staticmethod
    async def get_all(db:AsyncSession)->List[Task]:
        return await TaskRepository.get_all(db)
    
    @staticmethod
    async def update(
        db: AsyncSession,
        task_id: int,
        payload: TaskUpdate) -> Task:

        task = await TaskRepository.get_task(db, task_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        updates = payload.model_dump(exclude_unset=True)

        return await TaskRepository.update_task(db, task, updates)
    
    @staticmethod
    async def delete(db:AsyncSession,task_id:int)->None:
        task = await TaskRepository.get_task(db,task_id)
        if task is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
        
        await TaskRepository.delete_task(db,task)

        