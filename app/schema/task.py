from pydantic import BaseModel, Field, model_validator
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

    @model_validator(mode="after")
    def at_least_one_field(cls, values):
        if not any(values.model_dump().values()):
            raise ValueError("At least one field must be provided for update")
        return values


class TaskRetrieve(BaseModel):
    id: int
    title: str
    priority: str
    estimated_hours: float
    actual_hours: Optional[float]
    created_at: datetime
    updated_at: datetime
