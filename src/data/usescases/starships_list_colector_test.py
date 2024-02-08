from .starships_list_colector import StarshipsListColector
from src.infra.swapi_api_consumer import SwapiApiConsumer
from src.infra.test.swapi_api_consumer import SwapiApiConsumerSpy


def test_list():
    api_consumer = SwapiApiConsumerSpy()
    starship_list_colector = StarshipsListColector(api_consumer=api_consumer)
    page = 1
    
    response = starship_list_colector.list(page)
    
    assert api_consumer.get_starships_attributes == {"page": page}
    assert isinstance(response, list)
    assert "id" in response[0]
    assert "name" in response [0]
    
    
    
    