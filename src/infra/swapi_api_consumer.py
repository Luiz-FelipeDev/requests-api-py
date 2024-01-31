import requests
from requests import Request
from typing import Type, Tuple, Dict
from collections import namedtuple
from src.errors.http_request_error import HttpRequestError
from src.data.interfaces.swapi_api_consumer import SwapiApiConsumerInterface

class SwapiApiConsumer(SwapiApiConsumerInterface):
    
    ''' Class to consumer swapi API with http resquests '''
    
    def __init__(self) -> None:
        self.get_starships_response = namedtuple('GET_Starship', 'status_code request response')
    
    
    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        '''
        request starships in pagination
        :parm - page: int with page of navegation 
        :return - Tuple with status-code, request, response attrributes
        
        '''
          
           #TODO Essa classe pode lidar com várias instâncias. Talvez seja por isso que tenha o decoretor classmethod(um método da class em si)
            
        
        req = requests.Request(
            method='GET',
            url = 'https://swapi.dev/api/starships/',
            params = {'page': page}
        )
        
        req_prepare = req.prepare() # Preparando requisição
        response = self.__send_http_request(req_prepare=req_prepare)
        status_code = response.status_code
        
        # Em caso de sucesso
        if ((status_code >= 200) and (status_code <= 299)):
            return self.get_starships_response(
                status_code= status_code, request = req, response = response.json()
            )
        # Em caso de error retorno a excessão personalizada
        else:
            raise HttpRequestError(
                message = response.json()["detail"], status_code = status_code
            )
          
    @classmethod  
    def __send_http_request(cls, req_prepare: Type[Request]) -> any:
        ''' Preparando a requisição para ser enviada '''
        
        http_session = requests.Session()
        response =  http_session.send(req_prepare)        
        return response
            