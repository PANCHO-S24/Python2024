from clientes import Cliente
import csv

class GestorCliente:
    __listacliente = []
    
    def __init__(self):
        self.__listacliente=[]

    def agregacliente(self,cli):
        self.__listacliente.append(cli)
    
    def cargarcliente(self):
        archivo = open('clientes.csv')
        reader = csv.reader(archivo,delimiter=";")
        for fila in reader:
            dni = fila[0]
            nom = fila[1]
            ape = fila[2]
            tel = fila[3]
            pate = fila[4]
            vehi = fila[5]
            est = fila[6]
            cli = Cliente(dni,nom,ape,tel,pate,vehi,est)
            self.__listacliente.append(cli)
        i=0

        while i<len(self.__listacliente):
            self.__listacliente[i]
            i+=1
    
    def get_cliente(self):
        return self.__listacliente