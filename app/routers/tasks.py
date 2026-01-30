from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.deps import get_current_user, get_db
from typing import List
from app.models.user import User
from app.schema.task import TaskRetrieve,TaskCreate,TaskUpdate
from app.service.task_service import TaskService

taskrouter = APIRouter(prefix='/tasks',tags=['Tasks'])

@taskrouter.get('/',response_model=List[TaskRetrieve])
async def get_all_tasks(db:AsyncSession=Depends(get_db),current_user: User = Depends(get_current_user)):
    return await TaskService.get_all(db,current_user)

@taskrouter.get('/{task_id}',response_model=TaskRetrieve)
async def get_task(task_id:int,db:AsyncSession=Depends(get_db),current_user: User = Depends(get_current_user)):
    return await TaskService.get(db,task_id,current_user)

@taskrouter.post('/',response_model=TaskRetrieve)
async def create_task(task:TaskCreate,db:AsyncSession=Depends(get_db),current_user: User = Depends(get_current_user)):
    return await TaskService.create(db,task,current_user)

@taskrouter.put('/{task_id}',response_model=TaskRetrieve)
async def update_task(task_id:int,task:TaskUpdate,db:AsyncSession=Depends(get_db),current_user: User = Depends(get_current_user)):
    return await TaskService.update(db,task_id,task,current_user)

@taskrouter.delete('/{task_id}', response_model=dict)
async def delete_task(task_id:int,db:AsyncSession=Depends(get_db),current_user: User = Depends(get_current_user)):
    await TaskService.delete(db,task_id,current_user)
    return {"detail":"Task Deleted Successfully"}

@taskrouter.get('/user/{user_id}',response_model=List[TaskRetrieve])
async def get_tasks_by_user(user_id:int,db:AsyncSession=Depends(get_db),current_user: User = Depends(get_current_user)):
    return await TaskService.get_tasks_by_user(db,user_id)