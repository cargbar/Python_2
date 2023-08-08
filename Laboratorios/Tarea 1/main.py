import covid_api

def main_menu():
    print("1. Mostrar resumen global COVID-19")
    print("2. Salir")

if __name__ == '__main__':
    while True:
        main_menu()
        choice = input("Elija una opción: ")
        
        if choice == '1':
            summary = covid_api.get_summary()
            global_summary = summary['Global']
            print("Global COVID-19 Summary:")
            print("Total confirmed:", global_summary['TotalConfirmed'])
            print("Total deaths:", global_summary['TotalDeaths'])
        elif choice == '2':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


