from ClasePersonal import Personal
class Docente(Personal):
    __carrera:str = ""
    __cargo:str = ""
    __catedra:str = ""

    def __init__(self,cuil,apellido,nombre,sueldoB,antiguedad,carrera,cargo,catedra):
        super().__init__(cuil,apellido,nombre,sueldoB,antiguedad)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra

    