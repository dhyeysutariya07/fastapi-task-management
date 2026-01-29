from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User
from typing import List


class UserRepository:
    @staticmethod
    async def create(db:AsyncSession,user:User)->User:
        db.add(user)
        await db.commit()
        await db.refresh(user)

        return user
    
    @staticmethod
    async def get_by_id(db:AsyncSession,user_id:int)->User|None:
        result=await db.execute(
            select(User).where(User.id==user_id)
        )

        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_all(db:AsyncSession)->List[User]:
        result =await db.execute(select(User))
        return result.scalars().all()
    
    @staticmethod
    async def get_by_username(db:AsyncSession,username:str)->User|None:
        result = await db.execute(
            select(User).where(User.username==username)
        )

        return result.scalar_one_or_none()
    
    @staticmethod
    async def update(db:AsyncSession,user:User)->User:
        db.add(user)
        await db.commit()
        await db.refresh(user)

        return user
    
    @staticmethod
    async def delete(db:AsyncSession,user:User)->None:
        await db.delete(user)
        await db.commit()