from clase import Cuenta

def ingresarDatosCuenta():
    cuentas = []
    for i in range(1):
        print("Ingrese los datos para la cuenta", i + 1)
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cuil = input("CUIL: ")
        num_cuenta = input("Número de cuenta: ")
        saldo = float(input("Saldo: "))  
        cuenta = Cuenta(nombre, apellido, cuil, num_cuenta, saldo)
        cuentas.append(cuenta)
    return cuentas

def menu_opciones():
    print("---------------------------------------")
    print("1. Mostrar datos de cuenta")
    print("2. Depositar dinero")
    print("3. Extraer dinero")
    print("4. Salir")
    print("---------------------------------------")
    opcion = input("Ingrese la opción deseada: ")
    
    return opcion

def test(cuentas):
    while True:
        opcion = menu_opciones()
        if opcion == "1":
            for cuenta in cuentas:
                cuenta.Mostrardatos()
        elif opcion == "2":
            for cuenta in cuentas:
                monto = float(input("Ingrese el monto a depositar para la cuenta {}: ".format(cuenta.num_cuenta)))
                cuenta.depositar(monto)
                print("Saldo actual de la cuenta {}: {}".format(cuenta.num_cuenta, cuenta.saldo))
        elif opcion == "3":
            for cuenta in cuentas:
                monto = float(input("Ingrese el monto a extraer para la cuenta {}: ".format(cuenta.num_cuenta)))
                cuenta.Extraer(monto)
                print("Saldo actual de la cuenta {}: {}".format(cuenta.num_cuenta, cuenta.saldo))
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    cuentas = ingresarDatosCuenta()
    test(cuentas)
