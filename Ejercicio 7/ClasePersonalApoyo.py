from ClasePersonal import Personal
class PersonalApoyo(Personal):
    __categoria:str = ""


    def __init__(self,cuil,apellido,nombre,sueldoB,antiguedad,categoria):
        super().__init__(cuil,apellido,nombre,sueldoB,antiguedad)
        self.__categoria = categoria
