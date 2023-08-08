import requests

BASE_URL = 'https://www.thesportsdb.com/api/v1/json/3/all_sports.php'

def get_teams(sport):
    url = BASE_URL + f'search_all_teams.php?s={sport}'
    response = requests.get(url)
    return response.json()

# Puedes agregar más funciones para acceder a otros datos de la API

if __name__ == '__main__':
    sport = 'Soccer'
    teams_data = get_teams(sport)
    
    print(f"Teams in {sport}:")
    for team in teams_data['teams']:
        print(team['strTeam'])

