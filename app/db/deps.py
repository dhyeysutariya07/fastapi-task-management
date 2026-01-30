from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError,jwt
from app.core.security import ALGORITHM, SECRET_KEY
from app.db.session import AsyncSessionLocal
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator

from app.repositories.user import UserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = await UserRepository.get_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user