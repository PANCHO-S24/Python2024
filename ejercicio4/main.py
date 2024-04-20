
from gestormoto import GestorMotos
from gestorpedido import GestorPedidos
gestor_motos = GestorMotos()
gestor_pedidos = GestorPedidos()


def main():
    

    gestor_motos.cargar_motos('archivo')
    gestor_pedidos.cargar_pedidos('datosPedidos.csv')
    
    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Cargar nuevos pedidos desde teclado")
        print("2. Mostrar datos de motos")
        print("3. Mostrar datos de pedidos")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            gestor_pedidos.agregar_pedido_teclado()
        elif opcion == "2":
             mostrar_datos_motos()
        elif opcion == "3":
             mostrar_datos_pedidos()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")
    
def mostrar_datos_motos():
        print("------Datos de las motos:------")
        motos = gestor_motos.get_motos()
        for moto in motos:
            print("Patente:", moto.get_patente())
            print("Marca:", moto.get_marca()) 
            print("Nombre:", moto.get_nombre())
            print("Apellido:", moto.get_apellido()) 
            print("Kilometraje:", moto.get_kilometraje())
            print("-------------------------------------")
def mostrar_datos_pedidos():
       print("-----Datos de los pedidos:-----")
       pedidos = gestor_pedidos.get_pedidos()
       for pedido in pedidos:
            print("ID Pedido:",pedido.get_id()) 
            print("Patente:",pedido.get_patente_Asignada())
            print("Comidas:",pedido.get_comida_pedida())
            print("Tiempo Estimado:",pedido.get_tiempo_entrega()) 
            print("Tiempo Real:",pedido.get_tiempo_real())
            print("Precio Pedido:",pedido.get_precio())
            print("-------------------------------------")

if __name__ == "__main__":
    main()
