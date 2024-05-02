class Reparacion:
    __patente=""
    __reparacion=""
    __repuesto=""
    __preciorep=""
    __precioManoOb=""
    __estado=""
    def __init__(self,patente,reparacion,repuesto,preciorep,precioManoOb,estado):
        self.__patente=patente
        self.__reparacion=reparacion    
        self.__repuesto=repuesto
        self.__preciorep=preciorep
        self.__precioManoOb=precioManoOb
        self.__estado=estado
    def getPatente(self):
        return self.__patente
    def getReparacion(self):
        return self.__reparacion
    def getRepuesto(self):
        return self.__repuesto
    def getPrecioRep(self):
        return self.__preciorep
    def getPrecioManoOb(self):
        return self.__precioManoOb
    def getEstado(self):
        return self.__estado