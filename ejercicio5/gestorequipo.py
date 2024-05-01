from claseEquipo import Equipo
import csv

class GestorEquipo:
    def __init__(self):
        self.__Equipo = []
    
    def agregaequipo(self, unequipo):
        self.__Equipo.append(unequipo)

    def cargar_equipo(self,archivo):
        archivo = open('equipos2024.csv')
        reader = csv.reader(archivo, delimiter=",")
        next(reader)
        for fila in reader:
            id_equipo = fila[0]
            nombre = fila[1]
            golFavor = fila[2]
            gol_encontra = fila[3]
            diferencia = fila[4]
            punto = fila[5]
            unequipo = Equipo(id_equipo, nombre, golFavor, gol_encontra, diferencia, punto)
            self.__Equipo.append(unequipo)

    def get_equipo(self):
        return self.__Equipo
    
    def mostrar_datos(self):
        print("-----------------------------")
        for equipo in self.__Equipo:
            print("ID equipo:", equipo.get_id_equipo())
            print("Nombre:", equipo.get_nombre())
            print("Gol a Favor:", equipo.get_gol_afavor())
            print("Gol en contra:", equipo.get_gol_encontra())
            print("Diferencia gol:", equipo.get_diferenciaGol())
            print("Puntos:", equipo.get_punto())
            print("-----------------------------")

    def Busca_equipo(self,nombre):
        i=0
        while i < len(self.__Equipo):
            if self.__Equipo[i].get_nombre() == nombre:
                return self.__Equipo[i]
            i+=1