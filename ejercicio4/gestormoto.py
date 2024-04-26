from clasemoto import Moto
import csv

class GestorMotos:
    def __init__(self):
        self.__motos = []
    
    def agregamotos(self,unamoto):
        self.__motos.append(unamoto)

    def cargar_motos(self,archivo):
        archivo = open('datosMotos.csv')
        reader = csv.reader(archivo,delimiter=",")
        for fila in reader:
            patente = fila[0]
            marca = fila[1]
            nombre = fila[2]
            apellido = fila[3]
            kilometraje = fila[4]
            unamoto = Moto(patente,marca,nombre,apellido,kilometraje)
            self.__motos.append(unamoto)
        i=0

        while(i<len(self.__motos)):
            Mot= self.__motos[i]
            i+=1

    def get_motos(self):
        return self.__motos
    
    def mostrar_datos_moto(self,patt):
        i=0
        while i<len(self.__motos):
            if patt == self.__motos[i].get_patente():
                print("-----Datos del conductor -----")
                print("Nombre: ",self.__motos[i].get_nombre())
                print("Apellido: ",self.__motos[i].get_apellido())
                print("------------------------------")
                return # Sale del método después de encontrar la patente
            i+=1     
        print("-----No se encontro la patente------")