from ClaseArtefacto import Artefacto


class Heladera(Artefacto):
    __capacidad:int = 0
    __freezer:bool = False
    __ciclica:bool = False

    def __init__(self,marca,modelo,color,pais,precio,cap,freezer,ciclica):
        super().__init__(marca,modelo,color,pais,precio)
        self.__capacidad = int(cap)
        self.__freezer = bool(freezer)
        self.__ciclica = bool(ciclica)
    
    def ImporteVentaH(self):
        venta:float = self.__precio
        if self.__freezer == False:
            venta = venta + (venta * 0.01)
        elif self.__freezer == True:
            venta = venta + (venta * 0.05)
        if self.__ciclica == True:
            venta = venta + (venta * 0.10)
