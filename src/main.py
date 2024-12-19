from fastapi import FastAPI
from src.bot import start_bot

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    start_bot()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Telegram Bot API!"}