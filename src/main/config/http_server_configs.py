from fastapi import FastAPI
from src.main.routes.starships_routes import starships_routes

app = FastAPI()

app.include_router(starships_routes)