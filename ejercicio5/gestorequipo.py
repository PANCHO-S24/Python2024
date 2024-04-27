from claseEquipo import Equipo
import csv

class GestorEquipo:
    def __init__(self):
        self.__Equipo = []
    
    def agregaequipo(self, unequipo):
        self.__Equipo.append(unequipo)

    def cargar_equipo(self, archivo):
        archivo = open('equipos2024.csv')
        reader = csv.reader(archivo, delimiter=",")
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
        print("------Datos de los Equipos:------")
        for equipo in self.__Equipo:
            print(f"ID: {equipo.get_id_equipo()}, Nombre: {equipo.get_nombre()}, Goles a favor: {equipo.get_gol_afavor()}, Goles en contra: {equipo.get_gol_encontra()}, Diferencia de goles: {equipo.get_diferenciaGol()}, Puntos: {equipo.get_punto()}")
    