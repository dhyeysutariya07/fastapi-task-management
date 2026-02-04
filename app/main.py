from fastapi import FastAPI
from app.routers.tasks import taskrouter
from app.routers.users import userrouter
from app.routers.auth import authrouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Task Management API")

app.include_router(taskrouter)
app.include_router(userrouter)
app.include_router(authrouter)

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "https://example.com",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)