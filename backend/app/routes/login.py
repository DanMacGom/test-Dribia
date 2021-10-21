from fastapi import APIRouter, status, Form
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ..models.user import User
from .users import create_user

from ..db.connect import db

login_router = APIRouter()


@login_router.post("/", response_description="Check if credentials match", tags=["Login"])
async def check_login(username: str = Form(...), password: str = Form(...)):
    """
    Checks whether the user with the given username and password exists in the database.
    """
    user_in_db = await db["users"].find_one({"username": username, "password": password}, {"username": 1, "_id": 0})

    if user_in_db is not None:
        return JSONResponse(content=user_in_db, status_code=status.HTTP_200_OK)
    else:
        new_user = User(username=username, password=password)
        create_user_response = await create_user(new_user)
        return create_user_response
