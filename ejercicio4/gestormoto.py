from clasemoto import Moto
import csv

class GestorMotos:
    def __init__(self):
        self.__motos = []
    
    def agregamotos(self,moto):
        self.__motos.append(moto)

    def cargar_motos(self,archivo):
        archivo = open('datosMotos.csv')
        reader = csv.reader(archivo,delimiter=",")
        for fila in reader:
            patente = fila[0]
            marca = fila[1]
            nombre = fila[2]
            apellido = fila[3]
            kilometraje = fila[4]
            moto = Moto(patente,marca,nombre,apellido,kilometraje)
            self.__motos.append(moto)
        i=0

        while(i<len(self.__motos)):
            Mot= self.__motos[i]
            i+=1

    def get_motos(self):
        return self.__motos
