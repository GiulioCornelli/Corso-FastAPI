from Corso2.Custom_Enum import Priority
from pydantic import BaseModel, Field
from typing import Optional



class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length=3, max_length=512, description="name of the todo")
    todo_description: str = Field(..., description="description of the todo")
    priority: Priority = Field(default=Priority.LOW, description="priority of the todo")

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    todo_id: int = Field(..., description="unique identifier of the todo")

class TodoUpdate(BaseModel):
    todo_name: Optional[str] = Field(None, min_length=3, max_length=512, description="name of the todo")
    todo_description: Optional[str] = Field(None, description="description of the todo")
    priority: Optional[Priority] = Field(None, description="priority of the todo")