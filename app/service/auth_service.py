from fastapi import HTTPException
from app.core.security import create_access_token, create_refresh_token, verify_password
from app.repositories.user import UserRepository
from app.schema.auth import LoginRequest
from sqlalchemy.ext.asyncio import AsyncSession


class AuthService:

    @staticmethod
    async def login(db: AsyncSession, data: LoginRequest):
        user = await UserRepository.get_by_username(db, data.username)
        if not user or not verify_password(data.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        return {
            "access_token": create_access_token(user.id),
            "refresh_token": create_refresh_token(user.id)
        }
