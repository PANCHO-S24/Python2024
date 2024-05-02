from ManejadorClientes import GestorCliente
a = GestorCliente()
def menu():
    
    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Mostrar datos de clientes")
        print("2. Mostrar datos de reparaciones")
        print("3. Salir")
        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
           a.cargarcliente()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()