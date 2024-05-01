from claseFecha import Fecha
import csv
from gestorequipo import GestorEquipo

class GestorFecha:
    def __init__(self):
        self.__Fecha = []
    
    def agregaequipo(self,unafecha):
        self.__Fecha.append(unafecha)

    def cargar_fecha(self,archivo):
        archivo = open('fechasFutbol.csv')
        reader = csv.reader(archivo,delimiter=",")
        next(reader)
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
        print("-----------------------------")
        for fecha in self.__Fecha:
           print("Fecha:", fecha.get_fecha())
           print("ID Equipo Local:", fecha.get_id_equipo_local())
           print("ID Equipo Visitante:", fecha.get_id_equipo_visitante())
           print("Goles Equipo Local:", fecha.get_cant_gol_local())
           print("Goles Equipo Visitante:", fecha.get_cant_gol_visitante())
           print("-----------------------------")
    
    def mostrar_equipo(self):
        equipo = GestorEquipo()
        equipo.cargar_equipo('archivo')
        nombre= input("Ingrese el nombre del equipo a buscar :")
        eq = equipo.Busca_equipo(nombre)
        print("---------------------------------------")
        print("Equipo", nombre)
        print("Fecha\t\tGoles a Favor\tGoles en contra\t\tDiferencia de Goles\tPuntos")
        for i in range(len(self.__Fecha)):
            if self.__Fecha[i].get_id_equipo_local() == eq.get_id_equipo():
                print("{}\t{}\t\t\t{}\t\t\t{}\t\t{}".format(self.__Fecha[i].get_fecha(),eq.get_gol_afavor(),eq.get_gol_encontra(),eq.get_diferenciaGol(),eq.get_punto()))

    def ActualizarTabla(self):
        equipo_local = None
        equipo_visitante = None
        equipo = GestorEquipo()
        equipo.cargar_equipo('archivo')
        eq = equipo.get_equipo()
        for i in range(len(self.__Fecha)):
            for j in range(len(eq)):
                if self.__Fecha[i].get_id_equipo_local() == eq[j].get_id_equipo():
                    equipo_local = eq[j]
                elif self.__Fecha[i].get_id_equipo_visitante() == eq[j].get_id_equipo():
                    equipo_visitante = eq[j]
            if equipo_local and equipo_visitante:
                print("Partido de la fecha {}: {} vs {}".format(i+1, equipo_local.get_nombre(), equipo_visitante.get_nombre()))
                print()
                if self.__Fecha[i].get_cant_gol_local() > self.__Fecha[i].get_cant_gol_visitante():
                    equipo_local.sumarPuntos(3)
                elif self.__Fecha[i].get_cant_gol_local() < self.__Fecha[i].get_cant_gol_visitante():
                    equipo_visitante.sumarPuntos(3)
                else:
                    equipo_local.sumarPuntos(1)
                    equipo_visitante.sumarPuntos(1)
                
                equipo_local.sumarGolesafavor(int(self.__Fecha[i].get_cant_gol_local()))  # Convertir a entero
                equipo_local.sumarGolencontra(int(self.__Fecha[i].get_cant_gol_visitante()))  # Convertir a entero
                equipo_visitante.sumarGolesafavor(int(self.__Fecha[i].get_cant_gol_visitante()))  # Convertir a entero
                equipo_visitante.sumarGolencontra(int(self.__Fecha[i].get_cant_gol_local()))  # Convertir a entero

              
              

             
