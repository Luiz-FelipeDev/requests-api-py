from src.infra.swapi_api_consumer import SwapiApiConsumer
from src.errors.http_request_error import HttpRequestError

def test_get_starships(requests_mock):
    ''' Testing get_startships method '''
    
    requests_mock.get('https://swapi.dev/api/starships/', status_code=200, json= {'requesicao':'sucesso', 'results' : [{}]})
    starship = SwapiApiConsumer()
    page = 1
    get_starships_response = starship.get_starships(page=page)
    
    assert get_starships_response.request.method == 'GET'
    assert get_starships_response.request.url == 'https://swapi.dev/api/starships/'
    assert get_starships_response.request.params == {'page': page}
    assert get_starships_response.status_code == 200
    
    assert isinstance(get_starships_response.response['results'], list) 
 


def test_get_starships_http_error(requests_mock): 
    ''' Testing error in get_starships method'''
    
    requests_mock.get('https://swapi.dev/api/starships/', status_code=400, json= {'detail': 'something'})
    
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
    

    
    
    