from pydantic import BaseModel
from datetime import datetime
from pydantic import Field


class User(BaseModel):
    """User class."""
    username: str = Field(..., min_length=4, max_length=12)
    password: str = Field(..., min_length=4, max_length=12)
    creation_date: datetime = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "username": "Batman",
                "password": "DCrules"
            }
        }
