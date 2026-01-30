from fastapi import FastAPI
from app.routers.tasks import taskrouter
from app.routers.users import userrouter
from app.routers.auth import authrouter

app = FastAPI(title="Task Management API")

app.include_router(taskrouter)
app.include_router(userrouter)
app.include_router(authrouter)