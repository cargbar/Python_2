import requests
import random

def obtener_chiste_aleatorio():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["value"]
    else:
        return "Error al obtener el chiste aleatorio."

def obtener_categorias():
    url = "https://api.chucknorris.io/jokes/categories"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return []

def obtener_chiste_por_categoria(categoria):
    url = f"https://api.chucknorris.io/jokes/random?category={categoria}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["value"]
    else:
        return "Error al obtener el chiste de la categoría especificada."

def mostrar_menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Obtener un chiste aleatorio de Chuck Norris.")
        print("2. Obtener categorías disponibles de chistes.")
        print("3. Obtener un chiste de Chuck Norris por categoría.")
        print("4. Salir.")
        
        opcion = input("Ingrese el número de opción que desea ejecutar: ")
        
        if opcion == "1":
            chiste = obtener_chiste_aleatorio()
            print("\nChiste de Chuck Norris:")
            print(chiste)
        elif opcion == "2":
            categorias = obtener_categorias()
            if categorias:
                print("\nCategorías disponibles:")
                for categoria in categorias:
                    print(categoria)
            else:
                print("\nError al obtener las categorías.")
        elif opcion == "3":
            categorias = obtener_categorias()
            if categorias:
                print("\nCategorías disponibles:")
                for i, categoria in enumerate(categorias, 1):
                    print(f"{i}. {categoria}")
                
                num_categoria = input("\nIngrese el número de categoría que desea: ")
                if num_categoria.isdigit() and 1 <= int(num_categoria) <= len(categorias):
                    categoria_seleccionada = categorias[int(num_categoria) - 1]
                    chiste = obtener_chiste_por_categoria(categoria_seleccionada)
                    print(f"\nChiste de Chuck Norris en la categoría '{categoria_seleccionada}':")
                    print(chiste)
                else:
                    print("\nOpción inválida.")
            else:
                print("\nError al obtener las categorías.")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    mostrar_menu()
