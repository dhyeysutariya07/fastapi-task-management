from pydantic import BaseModel, model_validator
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username:str
    password:str

class UserRetrieve(BaseModel):
    id:int
    username:str
    created_at:datetime

class UserUpdate(BaseModel):
    username:Optional[str]
    password:Optional[str]

    @model_validator(mode='after')
    def at_least_one_field(cls,values):
        if not any(values.model_dump().values()):
            raise ValueError("At least one field must be provided for update")
        return values
    
class User(BaseModel):
    id:int
    username:str
    password:str
    created_at:datetime