from passlib.context import CryptContext
from datetime import datetime,timedelta
from jose import jwt

SECRET_KEY = "SUPER_SECRET_KEY"   
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    to_encode["exp"] = datetime.now() + expires_delta
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_access_token(user_id: int):
    return create_token(
        {"sub": str(user_id)},
        timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

def create_refresh_token(user_id: int):
    return create_token(
        {"sub": str(user_id)},
        timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    )
