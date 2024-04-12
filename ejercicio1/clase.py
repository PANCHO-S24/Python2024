class CajaAhorro:
    __nrocuenta =" "
    __cuil=" " 
    __apellido =" "
    __nombre =" "
    __saldo =" "

    def __init__(self, nrocuenta, cuil, apellido, nombre,saldo):  # )constructor recibe comoparametro
        self.__nrocuenta = nrocuenta                                                                                   
        self.__cuil = cuil                              
        self.__apellido = apellido
        self.__nombre = nombre
        self.__saldo = saldo                                                                                    
    def Mostrardatos(self):
        print("holaaaaa mundo ")    

    def Extraer(self,importe):
        if (self.__saldo >= importe):
            self.__saldo = self.__saldo - importe
            print("su saldo actual es de: {self._saldo}")
        else:
            self.__saldo = self.__saldo - importe
            print("saldo insuficiente")
    
    def depositar(self,deposito):
        if (self.__saldo > 0):
            self.__saldo = deposito
            print("deposito hecho!")
        else:
            print("ingrese un numero positivo: ")
    def ValidarCuil(self):
        pass
    
def test():
    lista_cuentas = []
    numcuenta= int(input("ingrese el numero de cuenta "))
    numcuil= int(input("ingrese el numero cuil "))
    ape= str (input("ingrese el apellido "))
    nom= str(input("ingrese el nombre "))
    sald= float(input("ingrese el saldo "))
    caja1=CajaAhorro(numcuenta,numcuil,ape,nom,sald)  
    lista_cuentas.append(caja1)
    return  lista_cuentas
 
        
