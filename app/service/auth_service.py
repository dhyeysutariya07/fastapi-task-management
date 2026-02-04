from fastapi import HTTPException
from app.core.security import create_access_token, create_refresh_token, verify_password
from app.repositories.user import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession


class AuthService:

    @staticmethod
    async def login(db: AsyncSession, username: str, password: str, scopes: list[str]):
        user = await UserRepository.get_by_username(db, username)
        if not user or not verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        return {
            "access_token": create_access_token(user_id=user.id),
            "refresh_token": create_refresh_token(user.id),
            "token_type": "bearer",
        }
