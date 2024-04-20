class Moto:
    __nombre=" " 
    __apellido=" "  
    __patente=" " 
    __marca =" "
    __kilometraje= ""

    def __init__(self,patente,marca,nombre,apellido,kilometraje):
      self.__nombre= nombre
      self.__apellido= apellido
      self.__patente= patente
      self.__marca= marca
      self.__kilometraje= kilometraje
    
    def get_patente(self):
        return self.__patente
    def get_marca(self):
        return self.__marca
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_kilometraje(self):
        return self.__kilometraje
    