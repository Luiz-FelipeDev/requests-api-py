from abc import ABC, abstractmethod
from typing import List, Dict


class StarshipsListColectorInterface(ABC):
    ''' Starships Colector Interface '''
    
    @abstractmethod
    def list(self, page:int) -> List[Dict]:
        ''' Must implement '''
        raise Exception('Must implement list method')
    