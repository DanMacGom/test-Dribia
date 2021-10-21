from pydantic import BaseModel
from datetime import datetime

from pydantic import Field


class Message(BaseModel):
    """Message class."""
    username: str = Field(...)
    content: str = Field(...)
    message_sent_datetime: datetime = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "username": "John",
                "content": "What are you up to?"
            }
        }
