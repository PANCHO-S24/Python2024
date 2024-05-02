class Cliente:
    __dni=""
    __nombre=""
    __apellido=""
    __telefono=""
    __patente=""
    __vehiculo=""
    __estado=""

    def __init__(self,dni,nombre,apellido,telefono,patente,vehiculo,estado):
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__telefono=telefono
        self.__patente=patente
        self.__vehiculo=vehiculo
        self.__estado= estado
       
    def getDni(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getTelefono(self):
        return self.__telefono
    def getPatente(self):
        return self.__patente
    def getVehiculo(self):
        return self.__vehiculo
    def getEstado(self):
        return self.__estado

    def mostrarcliente():
        print("---------------------------")
        print("DNI: ",self.__dni)
        print("Nombre: ",self.__nombre)
        print("Apellido:",self.__apellido)
        print("Telefono: ",self.__telefono)
        print("Patente: ",self.__patente)
        print("Vehiculo: ",self.__vehiculo)
        print("Estado: ",self.__estado)
