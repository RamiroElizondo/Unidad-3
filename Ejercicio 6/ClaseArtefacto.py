class Artefacto:
    __marca:str = ""
    __modelo:str = ""
    __color:str = ""
    __pais:str = ""
    __precio:float = 0.0

    def __init__(self,marca,modelo,color,pais,precio):
        self.__marca = str(marca)
        self.__modelo = str(modelo)
        self.__color = str(color)
        self.__pais = str(pais)
        self.__precio = float(precio)