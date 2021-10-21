from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from typing import List

from ..models.users import User
from ..db.connect import db

users_router = APIRouter()


@users_router.get("/", response_description="List all users", response_model=List[User], tags=["User"])
async def get_users() -> List[User]:
    """
    Gets a list of 50 users.
    """
    users = await db["users"].find().to_list(50)
    return users


@users_router.post("/", response_description="Add new user", tags=["User"])
async def create_user(user: User) -> JSONResponse:
    """
    Create a user in the database.
    """
    user = jsonable_encoder(user)
    new_user = await db["users"].insert_one(user)
    created_user = await db["users"].find_one({"_id": new_user.inserted_id}, {"_id": 0})
    return JSONResponse(content=created_user, status_code=status.HTTP_201_CREATED)
