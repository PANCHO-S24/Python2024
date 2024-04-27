from claseFecha import Fecha
import csv

class GestorFecha:
    def __init__(self):
        self.__Fecha = []
    
    def agregaequipo(self,unafecha):
        self.__Fecha.append(unafecha)

    def cargar_fecha(self,archivo):
        archivo = open('fechasFutbol.csv')
        reader = csv.reader(archivo,delimiter=",")
        for fila in reader:
            fecha = fila[0]
            id_eq_local= fila[1]
            id_eq_visitante= fila[2]
            cant_gol_local= fila[3]
            cant_gol_visitante= fila[4]
            unafecha= Fecha(fecha, id_eq_local , id_eq_visitante , cant_gol_local , cant_gol_visitante)
            self.__Fecha.append(unafecha)
        i=0

        while(i<len(self.__Fecha)):
            fech= self.__Fecha[i]
            i+=1
        
    def get_fecha(self):
           return self.__Fecha

    def mostrar_datos(self):
        print("------Datos de las fechas:------")
        for fecha in self.__Fecha:
            print(f"Fecha: {fecha.get_fecha()}, id Equipo local: {fecha.get__id_equipo_local()}, Id equipo visitante : {fecha.get_id_equipo_visitante()}, cantidad goles equipo local: {fecha.get_cant_gol_local()},cantidad goles equipo visitante: {fecha.get_cant_gol_visitante()}")
            
         