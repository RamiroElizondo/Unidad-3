from ClaseDocente import Docente
from ClaseInvestigador import Investigacion

class DocenteInvestigador(Docente,Investigacion):
    __categoria:str = ""
    __importe:float = 0.0

    def __init__(self, cuil, apellido, nombre, sueldoB, antiguedad, carrera, cargo, catedra,area,tipoI,cate,importe):
        super().__init__(self,cuil, apellido, nombre, sueldoB, antiguedad, carrera, cargo, catedra)
        super().__init__(self,cuil, apellido, nombre, sueldoB, antiguedad,area,tipoI)
        self.__categoria = cate
        self.__importe = float(importe)
        