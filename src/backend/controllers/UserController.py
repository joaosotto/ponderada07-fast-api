from fastapi import APIRouter
from ..Repository.UserRepository import UserRepository
from ..Entity.User import User

user_router = APIRouter()
user_repo = UserRepository()

@user_router.get("/user")
async def GetAllUsers():
    return await user_repo.GetAllUsers()

@user_router.get("/user/{userId}")
async def GetAllUsers():
    return await user_repo.GetAllUsers()

@user_router.post("/user")
async def PostUser(userData: User):
    return await user_repo.PostUser(userData)