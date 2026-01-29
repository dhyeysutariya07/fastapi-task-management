from app.schema.task import TaskCreate, TaskRetrieve, TaskUpdate
from app.storage.memory import tasks_db,next_id
from datetime import datetime
from fastapi.exceptions import HTTPException
from fastapi import status

async def create_task(task:TaskCreate):
    global next_id
    new_task = TaskRetrieve(
    id=next_id,
    title=task.title,
    priority=task.priority,
    estimated_hours=task.estimated_hours,
    actual_hours=None,
    created_at=datetime.now(),
    updated_at=datetime.now()
    )


    tasks_db.append(new_task)
    next_id+=1

    return new_task

async def get_all_tasks():
    return tasks_db

async def get_task(task_id:int)->TaskRetrieve:
    for task in tasks_db:
        if task.id == task_id:
            return task
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")

async def update_task(task_id:int,task:TaskUpdate):
    task_to_update = await get_task(task_id)
    if task.title is not None:
        task_to_update.title = task.title
    if task.priority is not None:
        task_to_update.priority = task.priority
    if task.estimated_hours is not None:
        task_to_update.estimated_hours = task.estimated_hours
    if task.actual_hours is not None:
        task_to_update.actual_hours = task.actual_hours

    task_to_update.updated_at = datetime.now()

    return task_to_update

async def delete_task(task_id:int):
    task_to_delete = await get_task(task_id)
    tasks_db.remove(task_to_delete)
    return task_to_delete