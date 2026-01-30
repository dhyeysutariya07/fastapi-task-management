from fastapi import APIRouter, Depends
from app.db.deps import get_db
from app.schema.auth import LoginRequest, TokenResponse
from app.service.auth_service import AuthService
from sqlalchemy.ext.asyncio import AsyncSession 

authrouter = APIRouter(prefix='/auth',tags=["Auth"])

@authrouter.post('/login',response_model=TokenResponse)
async def login(data: LoginRequest, db: AsyncSession = Depends(get_db)):
    return await AuthService.login(db, data)