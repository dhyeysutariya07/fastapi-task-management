from app.db.deps import get_current_user
from app.models.task import Task
from app.models.user import User
from app.schema.task import TaskCreate,TaskUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.task import TaskRepository
from typing import List
from fastapi.exceptions import HTTPException
from fastapi import Depends, status


class TaskService:
    @staticmethod
    async def create(db:AsyncSession,task:TaskCreate,user:User)->Task:
        task_to_create = Task(**task.model_dump())

        task =await TaskRepository.create(db,task_to_create)
        return task

    @staticmethod
    async def get(db:AsyncSession,task_id:int,user:User)->Task:
        task = await TaskRepository.get_task(db,task_id)
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
        return task
    
    @staticmethod
    async def get_all(db:AsyncSession,user:User)->List[Task]:
        return await TaskRepository.get_all(db)
    
    @staticmethod
    async def update(
        db: AsyncSession,
        task_id: int,
        payload: TaskUpdate,
        user:User) -> Task:

        task = await TaskRepository.get_task(db, task_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        updates = payload.model_dump(exclude_unset=True)

        return await TaskRepository.update_task(db, task, updates)
    
    @staticmethod
    async def delete(db:AsyncSession,task_id:int,user:User)->None:
        task = await TaskRepository.get_task(db,task_id)
        if task.owner_id != user.id:
            raise HTTPException(status_code=403, detail="Not allowed")

        if task is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
        
        await TaskRepository.delete_task(db,task)

    @staticmethod
    async def get_tasks_by_user(db:AsyncSession,user_id:int):
        tasks = await TaskRepository.list_by_user(db,user_id)
        return tasks

        