from gestorventas import GestorVentas

def menu():
    gestor_ventas = GestorVentas()
    while True:
        print("\nMenú de opciones:")
        print("1. Registrar venta")
        print("2. Total facturación por sucursal")
        print("3. Sucursal que más facturó en un día")
        print("4. Sucursal con menos facturación en la semana")
        print("5. Total facturación de todas las sucursales")
        print("6. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            dia = int(input("Ingrese el día de la semana (1-7): "))
            sucursal = int(input("Ingrese el número de sucursal (1-5): "))
            importe = float(input("Ingrese el importe de la factura: "))
            gestor_ventas.registrar_venta(dia, sucursal, importe)
            print("Venta registrada con éxito.")
        elif opcion == 2:
            sucursal = int(input("Ingrese el número de sucursal (1-5): "))
            total = gestor_ventas.total_facturacion_sucursal(sucursal)
            print(f"Total facturado por la sucursal {sucursal}: ${total}")
        elif opcion == 3:
            dia = int(input("Ingrese el día de la semana (1-7): "))
            sucursal = gestor_ventas.sucursal_mas_facturo_dia(dia)
            print(f"La sucursal que más facturó en el día {dia} es la sucursal {sucursal}.")
        elif opcion == 4:
            sucursal = gestor_ventas.sucursal_menos_facturacion_semana()
            print(f"La sucursal con menos facturación en la semana es la sucursal {sucursal}.")
        elif opcion == 5:
            total = gestor_ventas.total_facturacion_semana()
            print(f"Total facturado por todas las sucursales en la semana: ${total}")
        elif opcion == 6:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__== '__main__':
  menu()