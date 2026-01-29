from fastapi import FastAPI
from app.routers.tasks import taskrouter
from app.routers.users import userrouter

app = FastAPI(title="Task Management API")

app.include_router(taskrouter,prefix='/api/task',tags=["Tasks"])
app.include_router(userrouter)