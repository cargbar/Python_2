import requests

BASE_URL = 'https://api.covid19api.com/'

# devuelve un resumen global de datos COVID-19. Puedes mostrar total de confirmados, total de muertes, etc.

def get_summary():
    url = BASE_URL + 'summary'
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    summary = get_summary()
    global_summary = summary['Global']
    print("Global COVID-19 Summary:")
    print("Total confirmed:", global_summary['TotalConfirmed'])
    print("Total deaths:", global_summary['TotalDeaths'])
