from ClaseArtefacto import Artefacto


class Televisor(Artefacto):
    __tipoPantalla:str = ""
    __pulgadas:int = 0
    __tipoDefinicion:str = ""
    __conexionI:bool = False

    def __init__(self,marca,modelo,color,pais,precio,tipoPantalla,pulgada,tipoD,conexion):
        super().__init__(marca,modelo,color,pais,precio)
        self.__tipoPantalla = str(tipoPantalla)
        self.__pulgadas = int(pulgada)
        self.__tipoDefinicion = str(tipoD)
        self.__conexionI = bool(conexion)

    def ImporteVentaT(self):
        venta:float = self.__precio
        if self.__tipoDefinicion == "SD":
            venta = venta + (venta * 0.01)
        elif self.__tipoDefinicion == "HD":
            venta = venta + (venta * 0.02)
        elif self.__tipoDefinicion == "FULLHD":
            venta = venta + (venta * 0.03)
        if self.__conexionI == True:
            venta = venta + (venta * 0.10)
        return venta
    