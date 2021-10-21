from .routes.users import users_router
from .routes.login import login_router
from .routes.chatrooms import chatroom_router
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

REACT_HOST = os.getenv("REACT_HOST")
REACT_PORT = os.getenv("REACT_PORT")

# React config
origins = [
    f"http://{REACT_HOST}:{REACT_PORT}",
    f"{REACT_HOST}:{REACT_PORT}"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router=login_router)
app.include_router(router=users_router, prefix="/users")
app.include_router(router=chatroom_router, prefix="/chatroom")
