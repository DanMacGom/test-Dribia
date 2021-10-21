from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

from .message import Message


class Chatroom(BaseModel):
    """Chatroom class."""
    chatroom_name: str = Field(...)
    messages: List[Message]
    created_by: str = Field(...)
    date_created: datetime = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "chatroom_name": "Rockers",
                "messages": [],
                "created_by": "Axl Rose"
            }
        }
