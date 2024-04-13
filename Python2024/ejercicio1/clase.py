class Cuenta:
    __num_cuenta =" "
    __cuil=" " 
    __apellido =" "
    __nombre =" "
    __saldo =" "

    def __init__(self, nombre, apellido, cuil, numero_cuenta, saldo_inicial):
        self.nombre = nombre
        self.apellido = apellido
        self.cuil = cuil
        self.num_cuenta = numero_cuenta
        self.saldo = float(saldo_inicial)                                                                                    
    
    def Mostrardatos(self):
        print("Nombre: ",self.nombre)    
        print("Apellido: ",self.apellido)  
        print("Cuil: ",self.cuil)  
        print("Numero de cuenta: ",self.num_cuenta)  
        print("saldo: ",self.saldo)  
    
    def Extraer(self,importe):
        if (self.saldo >= importe):
            self.saldo = self.saldo - importe
            print("Su saldo actual es de:",self.saldo)
            return self.saldo
        else:
            print("Saldo insuficiente")
            return -1
    
    def depositar(self,importe):
        if (importe > 0):
            self.saldo += importe
            print("deposito hecho! , Nuevo Saldo :",self.saldo)
        else:
            print("El importe debe ser positivo: ")
    
    def ValidarCuil(self):
        pass
    
 
        
