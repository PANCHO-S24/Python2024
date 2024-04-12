from clase import CajaAhorro
from clase import test

if __name__ == "__main__":
  lista_cuenta = test()
  print(f"[1],consultar saldo: ")
  print(f"[2],Extraer: ")
  print(f"[3],Depositar: ")
  print(f"[5],test: ")
  
  
  opcion=int(input("ingrese operacion"))
  while opcion !=0:
    if opcion == 1:
       for elemento in lista_cuenta:
           print(elemento.Mostrardatos())
    if opcion == 2:
       CajaAhorro.Extraer()
    if opcion == 3:
       CajaAhorro.depositar()
    if opcion == 5:
       CajaAhorro.test()
       