
class Pedido:
    __identificador=""
    __patenteAsig=""
    __comidaped=""
    __tiempoEntrega=""
    __tiempoReal=""
    __precio=""

    def __init__(self,patenteAsig,identificador,comidaped,tiempoEntrega,tiempoReal,precio):
       self.__identificador= identificador
       self.__patenteAsig= patenteAsig
       self.__comidaped= comidaped
       self.__tiempoEntrega= tiempoEntrega
       self.__tiempoReal= tiempoReal
       self.__precio= precio
    
    def get_id(self):
        return self.__identificador
    def get_patente_Asignada(self):
        return self.__patenteAsig
    def get_comida_pedida(self):
        return self.__comidaped
    def get_tiempo_entrega(self):
        return self.__tiempoEntrega
    def get_tiempo_real(self):
        return int(self.__tiempoReal)
    def set_tiempo_real(self,tiempR):
        self.__tiempoReal = tiempR
    def get_precio(self):
        return self.__precio
    

    