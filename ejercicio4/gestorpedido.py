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