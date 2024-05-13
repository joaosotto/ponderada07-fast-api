from dotenv import load_dotenv
load_dotenv
from fastapi import FastAPI
from src.User.Controller.UserController import user_router

app = FastAPI()

app.include_router(user_router, prefix="/api")

@app.get("/")
async def root():
    return "API rodando"
