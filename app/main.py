from fastapi import FastAPI
from app.routers.tasks import taskrouter

app = FastAPI(title="Task Management API")

app.include_router(taskrouter,prefix='/api/task',tags=["Tasks"])