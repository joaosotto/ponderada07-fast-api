from fastapi import APIRouter
from ..Repository.UserRepository import UserRepository
from ..Entity.User import User

user_router = APIRouter()
user_repo = UserRepository

@user_router.get("/user")
async def GetAllUsers():
    return 'GetAllUsers'

@user_router.post("/user")
async def PostUser(userData: User):
    return await user_repo.PostUsers(userData)

@user_router.post("/user")
async def UpdateUser(userId: int, userData: User):
    return await user_repo.UpdateUser(userId, userData)

@user_router.delete("/user")
async def DeleteUser(userId: int):
    return await user_repo.DeleteUser(userId)