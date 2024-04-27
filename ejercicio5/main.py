from gestorequipo import GestorEquipo
from gestorfecha import GestorFecha
gestor_equipo = GestorEquipo()
gestor_fecha = GestorFecha()


def main():
    gestor_equipo.cargar_equipo('archivo')
    gestor_fecha.cargar_fecha('archivo')
    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Mostrar datos de Equipos")
        print("2. Mostrar datos de Fechas")
        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
           gestor_equipo.mostrar_datos()
        elif opcion == "2":
           gestor_fecha.mostrar_datos()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()