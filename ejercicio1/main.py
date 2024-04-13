from clase import Cuenta

def ingresarDatosCuenta():
    cuentas = []
    for i in range(2):
        print("Ingrese los datos para la cuenta", i + 1)
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cuil = input("CUIL: ")
        num_cuenta = input("Número de cuenta: ")
        saldo = float(input("Saldo: "))  # Convertimos a float
        print("---------------------------------------")
        cuenta = Cuenta(nombre, apellido, cuil, num_cuenta, saldo)
        cuentas.append(cuenta)
    return cuentas

def test(cuentas):
    for cuenta in cuentas:
        print("\nInformación de la cuenta de", cuenta.nombre, cuenta.apellido)
        print("CUIL:", cuenta.cuil)
        print("Número de cuenta:", cuenta.numero_cuenta)
        print("Saldo actual:", cuenta.saldo)
        cuenta.depositar(float(input("Ingrese el monto a depositar: ")))
        cuenta.Extraer(float(input("Ingrese el monto a extraer: ")))

if __name__ == "__main__":
    cuentas = ingresarDatosCuenta()
    test(cuentas)
