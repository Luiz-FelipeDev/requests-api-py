from .starships_list_colector import StarshipsListColector
from src.infra.swapi_api_consumer import SwapiApiConsumer


def test_list():
    api_consumer = SwapiApiConsumer()
    starship_list_colector = StarshipsListColector(api_consumer=api_consumer)
    page = 1
    
    starship_list_colector.list(page)
    
    