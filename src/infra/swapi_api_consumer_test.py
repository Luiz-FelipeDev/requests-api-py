from src.infra.swapi_api_consumer import SwapiApiConsumer

def teste_get_starships(requests_mock):
    ''' Criando teste do método associado as informações das naves '''
    
    requests_mock.get('https://swapi.dev/api/starships/', status_code=200, json= {'requesicao':'sucesso'})
    
    starship = SwapiApiConsumer()
    response = starship.get_starships(page=1)
    
    print(response)