from src.domain.usecases.starships_list_colector import StarshipsListColectorInterface
from src.infra.swapi_api_consumer import SwapiApiConsumer
from typing import List, Dict, Type

class StarshipsListColector(StarshipsListColectorInterface):
    '''  StarshipsListColector usecase '''
    
    def __init__(self, api_consumer: Type[SwapiApiConsumer]) -> None:
        self.__api_consumer = api_consumer
        
    def list(self, page: int) -> List[Dict]:
        api_response = self.__api_consumer.get_starships(page)
        starships_formated_list = self.__format_api_response(api_response.response["results"])
        #print(response)
        return starships_formated_list
        
        
    @classmethod
    def __format_api_response(cls, results: List[Dict]):
        starships_formated_list = []
        
        
        for starship in results:
            starships_formated_list.append(
                {
                    "id": starship["url"].split("/")[-2],
                    "name": starship["name"],
                    "model":starship["model"],
                    "manufacturer":starship["manufacturer"] ,
                    "cost_in_credits": starship["cost_in_credits"],
                    "length":starship["length"],
                    "max_atmosphering_speed":starship["max_atmosphering_speed"],
                    "cargo_capacity": starship["cargo_capacity"],
                    "hyperdrive_rating":starship["hyperdrive_rating"],
                    "MGLT":starship["MGLT"],
                }
            )
    
        return starships_formated_list
        

    