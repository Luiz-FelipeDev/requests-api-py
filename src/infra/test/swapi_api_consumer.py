from faker import Faker 

fake = Faker()


def mock_starships():
    '''
    mock data for starships
        :return - dict with startships infomation
    
    '''
    
    return {
        
            "name": fake.name(),
            "model": fake.name(),
            "manufacturer": fake.name(),
            "cost_in_credits": fake.random_int(),
            "length": fake.random_int(),
            "max_atmosphering_speed":fake.random_int(),
            "cargo_capacity": fake.random_int(),
            "hyperdrive_rating": fake.random_int(),
            "MGLT": fake.random_int(),
            "url": "https://swapi.dev/api/starships/{}/".format(fake.random_int())
        
    }