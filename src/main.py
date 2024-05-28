from fastapi import FastAPI
from src.User.Controller import user_router

app = FastAPI()

app.include_router(user_router, prefix="/api")

@app.get("/")
async def root():
    return "API rodando"
