class Personal:
    __cuil:str = ""
    __apellido:str = ""
    __nombre:str = ""
    __sueldoB:float = 0.0
    __antiguedad:int = 0

    def __init__(self,cuil,apellido,nombre,sueldoB,antiguedad):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldoB = float(sueldoB)
        self.__antiguedad = antiguedad