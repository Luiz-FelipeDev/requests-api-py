from fastapi import APIRouter, Request as RequestFastApi

starships_routes = APIRouter()

starships_routes.get("/api/starships/list")
def get_starships_in_pagination(request: RequestFastApi):
    return {'Ola': 'Mundo'}