from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.deps import get_db
from app.service.auth_service import AuthService

authrouter = APIRouter()

@authrouter.post("/auth/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    return await AuthService.login(
        db=db,
        username=form_data.username,
        password=form_data.password,
        scopes=form_data.scopes,
    )
