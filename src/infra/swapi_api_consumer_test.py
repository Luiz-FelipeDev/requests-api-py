from src.infra.swapi_api_consumer import SwapiApiConsumer

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
    