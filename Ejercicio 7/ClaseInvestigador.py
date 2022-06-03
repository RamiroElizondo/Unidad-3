from ClasePersonal import Personal
class Investigacion(Personal):
    __areaInvestigacion:str = ""
    __tipoInvestigacion:str = ""


    def __init__(self,cuil,apellido,nombre,sueldoB,antiguedad,areaInvestigacion,tipoInvestigacion):
        super().__init__(cuil,apellido,nombre,sueldoB,antiguedad)
        self.__areaInvestigacion = areaInvestigacion
        self.__tipoInvestigacion = tipoInvestigacion
