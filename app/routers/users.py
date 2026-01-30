from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schema.user import UserCreate, UserRetrieve, UserUpdate
from app.db.deps import get_current_user, get_db
from app.service.user_service import UserService

userrouter = APIRouter(prefix="/users", tags=["Users"],dependencies=[Depends(get_current_user)])

@userrouter.post(
    "/",
    response_model=UserRetrieve,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    return await UserService.create_user(db, user)


@userrouter.get(
    "/",
    response_model=List[UserRetrieve]
)
async def get_users(
    db: AsyncSession = Depends(get_db)
):
    return await UserService.get_all_users(db)


@userrouter.get(
    "/{user_id}",
    response_model=UserRetrieve
)
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await UserService.get_user_by_id(db, user_id)


@userrouter.put(
    "/{user_id}",
    response_model=UserRetrieve
)
async def update_user(
    user_id: int,
    user: UserUpdate,
    db: AsyncSession = Depends(get_db)
):
    return await UserService.update_user(db, user_id, user)


@userrouter.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    await UserService.delete_user(db, user_id)
