from pydantic import BaseModel, ConfigDict, Field, model_validator
from typing import Optional, Literal
from datetime import datetime


class TaskCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Short title of the task"
    )
    priority: Literal["low", "medium", "high"] = Field(
        ...,
        description="Priority level of the task"
    )
    estimated_hours: float = Field(
        ...,
        gt=0,
        description="Estimated hours to complete the task"
    )
    owner_id:int



class TaskUpdate(BaseModel):
    title: Optional[str] = Field(
        None,
        min_length=3,
        max_length=100
    )
    priority: Optional[Literal["low", "medium", "high"]] = None
    estimated_hours: Optional[float] = Field(
        None,
        gt=0
    )
    actual_hours: Optional[float] = Field(
        None,
        ge=0
    )
    owner_id:int


    @model_validator(mode="after")
    def at_least_one_field(cls, values):
        if not any(values.model_dump().values()):
            raise ValueError("At least one field must be provided for update")
        return values


class TaskRetrieve(BaseModel):
    id: int
    title: str
    priority: str
    owner_id:int
    estimated_hours: float
    actual_hours: Optional[float]
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True) # this data might come from ORM objects, not dicts.
