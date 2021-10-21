from pydantic import BaseModel
from datetime import datetime

from fastapi import Field


class Message(BaseModel):
    username: str = Field(...)
    content: str = Field(...)
    message_sent: datetime = datetime.now()
    created_by: str = Field(...)
