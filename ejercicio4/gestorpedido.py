from clasepedido import Pedido
import csv

class GestorPedidos:
    def __init__(self):
        self.__pedidos = []
    def agregapedidos(self,pedido):
        self.__pedidos.append(pedido)

    def cargar_pedidos(self,archivo):
        archivo = open('datosPedidos.csv')
        reader = csv.reader(archivo,delimiter=",")
        for fila in reader:
            patA= fila[0]
            iden = fila[1]
            comP= fila[2]
            tiempoE = fila[3]
            tiempoR = fila[4]
            precio = fila[5]
            pedido = Pedido(patA,iden,comP,tiempoE,tiempoR,precio)
            self.__pedidos.append(pedido)
        i=0

        while(i<len(self.__pedidos)):
            ped= self.__pedidos[i]
            i+=1

    def get_pedidos(self):
        return self.__pedidos
    
    def agregaPedidoTeclado(self):
        pat= input("ingrese la patente de la moto para asignar el pedido: ")
        i=0
        while i<len(self.__pedidos):
            if pat == self.__pedidos[i].get_patente_Asignada():
                print("La moto con la patente {} tiene asignados los pedidos {}".format(self.__pedidos[i].get_patente_Asignada(),self.__pedidos[i].get_id()))
                idi= input("Ingrese id: ")
                comidaPe=input("ingrese la comida pedida: ")
                timeEntreg= input("Ingrese tiempo de etrega: ")
                timeReal= 0
                precioo= input("Ingrese precio: ")
                pedido65= Pedido(pat,idi,comidaPe,timeEntreg,timeReal,precioo)
                self.__pedidos.append(pedido65)
                print("El nuevo pedido ha sido asignado a la moto")
                return
            i+=1
        print("No se encontro la patente")
    def inciso4a(self,pate,newid,tr):
        i=0
        while i<len(self.__pedidos):
             if pate == self.__pedidos[i].get_patente_Asignada() and newid == self.__pedidos[i].get_id():
                nuevo_tiempo_real = input("Ingrese el nuevo tiempo real de entrega: ")
                self.__pedidos[i].set_tiempo_real(nuevo_tiempo_real)
                print(" Se modifico el tiempo real de entrega ")
             i+=1
        else:(print("------No se encontro la patente y su id------"))
    
    def tiempo_promedio_entrega(self, patt):
        total_tiempo_real = 0
        total_pedidos = 0
        i=0
        while i<len(self.__pedidos):
            pedido= self.__pedidos[i]
            if patt == pedido.get_patente_Asignada():
                total_tiempo_real += pedido.get_tiempo_real()
                total_pedidos = total_pedidos + 1
            i += 1
        if total_pedidos == 0:
            return 0  # En caso de no haber pedidos para esa moto
        return total_tiempo_real / total_pedidos
        





        
        
        
        
        