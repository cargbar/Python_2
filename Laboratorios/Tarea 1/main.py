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

# Paso 3: Funciones para mostrar partes relevantes de los datos
def show_names(data):
    if data:
        for item in data:
            print(item['name'])

def show_date_ranges(data):
    if data:
        start_dates = [item['start_date'] for item in data]
        end_dates = [item['end_date'] for item in data]
        print("Rangos de fechas:")
        for start_date, end_date in zip(start_dates, end_dates):
            print(f"{start_date} - {end_date}")

# Paso 4: Documentación de la API y funciones
"""
API seleccionada: Example API

Descripción de los datos:
La API proporciona una lista de elementos con sus respectivos nombres y rangos de fechas.

Endpoints utilizados:
- /data: Devuelve una lista de elementos con la siguiente estructura:
    [
        {
            "name": "Nombre del elemento",
            "start_date": "Fecha de inicio",
            "end_date": "Fecha de fin"
        },
        ...
    ]

Funciones creadas:
- get_data_from_api: Realiza una solicitud GET a la API y devuelve los datos en formato JSON.
- show_names: Muestra los nombres de los elementos presentes en los datos.
- show_date_ranges: Muestra los rangos de fechas de los elementos presentes en los datos.
"""

# Paso 5: Documentación de las funciones de exploración
"""
Función show_names(data):
Muestra los nombres de los elementos presentes en los datos.

Parámetros:
- data: Lista de elementos en formato JSON obtenidos de la API.

Función show_date_ranges(data):
Muestra los rangos de fechas de los elementos presentes en los datos.

Parámetros:
- data: Lista de elementos en formato JSON obtenidos de la API.
"""

# Paso 6: Crear un menú básico para acceder a las funciones
def main():
    data = get_data_from_api()
    if data:
        print("1. Mostrar nombres")
        print("2. Mostrar rangos de fechas")
        choice = input("Seleccione una opción: ")
        if choice == "1":
            show_names(data)
        elif choice == "2":
            show_date_ranges(data)
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()

