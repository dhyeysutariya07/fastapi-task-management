from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.deps import get_db
from typing import List
from app.schema.task import TaskRetrieve,TaskCreate,TaskUpdate
from app.service.task_service import TaskService

taskrouter = APIRouter(prefix='/tasks',tags=['Tasks'])

@taskrouter.get('/',response_model=List[TaskRetrieve])
async def get_all_tasks(db:AsyncSession=Depends(get_db)):
    return await TaskService.get_all(db)

@taskrouter.get('/{task_id}',response_model=TaskRetrieve)
async def get_task(task_id:int,db:AsyncSession=Depends(get_db)):
    return await TaskService.get(db,task_id)

@taskrouter.post('/',response_model=TaskRetrieve)
async def create_task(task:TaskCreate,db:AsyncSession=Depends(get_db)):
    return await TaskService.create(db,task)

@taskrouter.put('/{task_id}',response_model=TaskRetrieve)
async def update_task(task_id:int,task:TaskUpdate,db:AsyncSession=Depends(get_db)):
    return await TaskService.update(db,task_id,task)

@taskrouter.delete('/{task_id}')
async def delete_task(task_id:int,db:AsyncSession=Depends(get_db)):
    await TaskService.delete(db,task_id)
    return {"detail":"Task Deleted Successfully"}