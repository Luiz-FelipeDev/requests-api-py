from abc import ABC, abstractmethod
from requests import Request 
from typing import Tuple, Dict, Type


class SwapiApiConsumerInterface(ABC):
    
    @abstractmethod
    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        raise Exception('Must implement get_starships ')
    