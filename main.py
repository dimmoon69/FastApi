from fastapi import FastAPI
from api import file_router

app = FastAPI()

app.include_router(file_router)
