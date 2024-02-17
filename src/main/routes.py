from fastapi import APIRouter, Request

starships_routes = APIRouter()

@starships_routes.get("/")
def get_starships_pagination(request: Request):
    return {"hello":"world"}