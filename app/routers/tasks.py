from fastapi import APIRouter
from typing import List
from app.schema.task import TaskRetrieve,TaskCreate,TaskUpdate
import app.service.task_service as task_service

taskrouter = APIRouter()

@taskrouter.get('/',response_model=List[TaskRetrieve])
async def get_all_tasks():
    return await task_service.get_all_tasks()

@taskrouter.get('/{task_id}',response_model=TaskRetrieve)
async def get_task(task_id:int):
    return await task_service.get_task(task_id)

@taskrouter.post('/',response_model=TaskRetrieve)
async def create_task(task:TaskCreate):
    return await task_service.create_task(task)

@taskrouter.put('/{task_id}',response_model=TaskRetrieve)
async def update_task(task_id:int,task:TaskUpdate):
    return await task_service.update_task(task_id,task)

@taskrouter.delete('/{task_id}',response_model=TaskRetrieve)
async def delete_task(task_id:int):
    return await task_service.delete_task(task_id)