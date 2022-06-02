from ClaseLista import Lista
from ClaseArtefacto import Artefacto

class ManejadorAparato:
    __lista: Lista

    def __init__(self):
        self.__lista = Lista()
    
    def insertarA(self,objetoA: Artefacto,pos):
        self.__lista.insertarElemento(objetoA,pos)
    
    def agregarA(self,objetoA):
