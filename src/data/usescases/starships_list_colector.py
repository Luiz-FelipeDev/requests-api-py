from src.domain.usecases.starships_list_colector import StarshipsListColectorInterface
from src.infra.swapi_api_consumer import SwapiApiConsumer
from typing import List, Dict, Type

class StarshipsListColector(StarshipsListColectorInterface):
    '''  StarshipsListColector usecase '''
    
    def __init__(self, api_consumer: Type[SwapiApiConsumer]) -> None:
        self.__api_consumer = api_consumer
        
    def list(self, page: int) -> List[Dict]:
        response = self.__api_consumer.get_starships(page)
        print(response)
        

    