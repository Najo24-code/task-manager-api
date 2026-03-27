from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

class TaskBase(BaseModel):
    title: str
    description: str
    state: str
    deadline: datetime

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    owner: UserResponse

    class Config:
        from_attributes = True

class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    state: Optional[str]
    deadline: Optional[datetime]