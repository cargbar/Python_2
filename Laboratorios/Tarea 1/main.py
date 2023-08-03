import requests

# Paso 1: Selección de una API y endpoint
API_URL = "https://api.example.com"
ENDPOINT = "/data"

# Paso 2: Crear funciones para consumir datos de la API
def get_data_from_api():
    response = requests.get(API_URL + ENDPOINT)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error al obtener los datos de la API.")
        return None