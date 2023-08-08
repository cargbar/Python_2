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