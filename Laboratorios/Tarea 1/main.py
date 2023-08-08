import sports_api

def main_menu():
    print("1. Mostrar equipos de un deporte")
    print("2. Salir")

if __name__ == '__main__':
    while True:
        main_menu()
        choice = input("Elija una opción: ")
        
        if choice == '1':
            sport = input("Ingrese el nombre del deporte: ")
            teams_data = sports_api.get_teams(sport)
            print(f"Equipos en {sport}:")
            for team in teams_data['teams']:
                print(team['strTeam'])
        elif choice == '2':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

