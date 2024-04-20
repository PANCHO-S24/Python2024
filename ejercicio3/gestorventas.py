class GestorVentas:
    __ventas= " "
    
    def __init__(self):
        self.__ventas= [[0 for _ in range(7)] for _ in range(5)]

    def registrar_venta(self, dia, sucursal, importe):
        self.__ventas[sucursal - 1][dia - 1] += importe

    def total_facturacion_sucursal(self, sucursal):
        total = sum(self.__ventas[sucursal - 1])
        return total

    def sucursal_mas_facturo_dia(self, dia):
        max_facturacion = max(self.__ventas, key=lambda x: x[dia - 1])
        sucursal = self.__ventas.index(max_facturacion) + 1
        return sucursal

    def sucursal_menos_facturacion_semana(self):
        total_sucursales = [sum(sucursal) for sucursal in self.__ventas]
        sucursal_menos_facturacion = total_sucursales.index(min(total_sucursales)) + 1
        return sucursal_menos_facturacion

    def total_facturacion_semana(self):
        total = sum(sum(sucursal) for sucursal in self.__ventas)
        return total
