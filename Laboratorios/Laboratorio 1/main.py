# importar modulo datetime, obtener fecha y hora#
import datetime
from Trig import Trig


def main():
    trig = Trig()

    while True:
        operation = input("¿Qué valor deseas calcular? (sen/cos/tan): ")
        operation = operation.lower()

        if operation == "sen":
            result = trig.get_sine_of_pi()
        elif operation == "cos":
            result = trig.get_cosine_of_pi()
        elif operation == "tan":
            result = trig.get_tangent_of_pi()
        else:
            print("ERROR. Inténtalo nuevamente.")
            continue

        current_time = datetime.datetime.now()

        # Registrar la operación en el archivo log.txt
        log_entry = (
            f"Fecha y hora: {current_time}\nOperación: {operation} de pi = {result}\n"
        )

        with open("log.txt", "a") as log_file:
            log_file.write(log_entry)

        print(f"El resultado de la {operation} de pi es: {result}\n")

        repeat = input("¿Desea continuar? (si/no): ")
        repeat = repeat.lower()

        if repeat != "si":
            break


if __name__ == "__main__":
    main()