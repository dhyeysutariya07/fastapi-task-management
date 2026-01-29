from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from app.models.user import User
from app.schema.user import UserCreate, UserUpdate
from app.repositories.user import UserRepository
from app.core.security import hash_password


class UserService:

    @staticmethod
    async def create_user(db: AsyncSession, user: UserCreate) -> User:
        existing_user = await UserRepository.get_by_username(db, user.username)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists"
            )

        user = User(
            username=user.username,
            password=hash_password(user.password)
        )

        return await UserRepository.create(db, user)

    @staticmethod
    async def get_user_by_id(db: AsyncSession, user_id: int) -> User:
        user = await UserRepository.get_by_id(db, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return user

    @staticmethod
    async def get_all_users(db: AsyncSession):
        return await UserRepository.get_all(db)

    @staticmethod
    async def update_user(
        db: AsyncSession,
        user_id: int,
        user_in: UserUpdate
    ) -> User:

        user = await UserRepository.get_by_id(db, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        if user_in.username is not None:
            user.username = user_in.username

        if user_in.password is not None:
            user.password = hash_password(user_in.password)

        return await UserRepository.update(db, user)

    @staticmethod
    async def delete_user(db: AsyncSession, user_id: int) -> None:
        user = await UserRepository.get_by_id(db, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        await UserRepository.delete(db, user)
