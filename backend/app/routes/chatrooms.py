from fastapi import APIRouter, status, Form
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ..models.chatroom import Chatroom
from ..models.user import User

from ..db.connect import db

chatroom_router = APIRouter()


@chatroom_router.post("/", response_description="Add new chatroom", tags=["Chatroom"])
async def create_chatroom(chatroom: Chatroom) -> JSONResponse:
    """
    Create a chatroom linked to a User.
    """
    created_chatroom = jsonable_encoder(chatroom)
    new_chatroom = await db["chatroom"].insert_one(created_chatroom)
    created_chatroom = await db["chatroom"].find_one(new_chatroom.inserted_id, {"_id": 0})
    print(created_chatroom)
    return JSONResponse(content=created_chatroom, status_code=status.HTTP_201_CREATED)
