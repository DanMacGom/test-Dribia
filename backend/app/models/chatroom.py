from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

from .message import Message


class Chatroom(BaseModel):
    """Chatroom class."""
    chatroom_name: str = Field(...)
    messages: List[Message]
    username: str = Field(..., min_length=2, max_length=50)
    password: str = Field(..., min_length=2, max_length=50)
    creation_date: datetime = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "username": "Batman",
                "password": "DCrules"
            }
        }
