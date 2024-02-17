from typing import Union
from routes import starships_routes
from fastapi import FastAPI

app = FastAPI()

app.include_router(starships_routes)