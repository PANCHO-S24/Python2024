class Fecha:
    __fecha= ""
    __id_equipo_local=""
    __id_equipo_visitante=""
    __cant_gol_local=""
    __cant_gol_visitante=""

    def __init__(self, fecha, id_equipo_local, id_equipo_visitante, cant_gol_local, cant_gol_visitante):
        self.__fecha = fecha
        self.__id_equipo_local = id_equipo_local
        self.__id_equipo_visitante = id_equipo_visitante
        self.__cant_gol_local = cant_gol_local 
        self.__cant_gol_visitante = cant_gol_visitante
    
    def get_fecha(self):
        return self.__fecha
    def get_id_equipo_local(self):
        return self.__id_equipo_local
    def get_id_equipo_visitante(self):
        return self.__id_equipo_visitante
    def get_cant_gol_local(self):
        return self.__cant_gol_local
    def get_cant_gol_visitante(self):
        return self.__cant_gol_visitante
   