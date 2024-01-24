from src.infra.swapi_api_consumer import SwapiApiConsumer
from src.errors.http_request_error import HttpRequestError

def test_get_starships():
    ''' Criando teste do método associado as informações das naves '''
    
    #requests_mock.get('https://swapi.dev/api/starships/', status_code=200, json= {'requesicao':'sucesso'})
    
    starship = SwapiApiConsumer()
    page = 1
    get_starships_response = starship.get_starships(page=page)
    
    assert get_starships_response.request.method == 'GET'
    assert get_starships_response.request.url == 'https://swapi.dev/api/starships/'
    assert get_starships_response.request.params == {'page': page}
    assert get_starships_response.request.status_code == 200
    
    # TODO serve para saber se a instância pertence a uma determinada classe
    assert isinstance(get_starships_response.request.response['results'], list) 
    
''' 
def test_get_starships_http_error():
    starship = SwapiApiConsumer()
    page = 100
    try:
        starship.get_starships(page=page)
        assert True is False
    except HttpRequestError as error:
        assert error.message is not None 
        assert error.status_code is not None
        print(error.message)
        print(error.status_code)
    
'''   
    
    
    