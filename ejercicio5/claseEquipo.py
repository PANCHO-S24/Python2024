class Equipo:
    __id_equipo=" "  
    __nombre=""  
    __gol_afavor=""
    __gol_encontra =""
    __diferenciaGol= ""
    __punto= ""
   
   
    def __init__(self, id_equipo, nombre, gol_afavor, gol_encontra, diferenciaGol, punto):
        self.__id_equipo = id_equipo
        self.__nombre = nombre
        self.__gol_afavor = int(gol_afavor) 
        self.__gol_encontra = int(gol_encontra) 
        self.__diferenciaGol = int(diferenciaGol)   
        self.__punto = int(punto) 


    def get_id_equipo(self):
        return self.__id_equipo
    def get_nombre(self):
        return self.__nombre
    def get_gol_afavor(self):
        return self.__gol_afavor
    def get_gol_encontra(self):
        return self.__gol_encontra
    def get_diferenciaGol(self):
        return self.__diferenciaGol
    def get_punto(self):
        return self.__punto
       

    def sumarPuntos(self, puntos):
        self.__punto += puntos

    def sumarGolesafavor(self, goles):
        self.__gol_afavor += goles
        self.__diferenciaGol = self.__gol_afavor  - self.__gol_encontra

    def sumarGolencontra(self, goles):
        self.__gol_encontra += goles
        self.diferencia_goles = self.__gol_afavor - self.__gol_encontra
    