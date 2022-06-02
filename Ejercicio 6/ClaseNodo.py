from __future__ import annotations
from ClaseArtefacto import Artefacto

class Nodo:
    __artefacto = None
    __siguiente = None

    def __init__(self,artefacto:Artefacto,siguente: Nodo | None):
        self.__artefacto = artefacto
        self.__siguiente = siguente
    
    def setSiguiente(self,siguiente:Nodo | None):
        self.__siguiente = siguiente
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__artefacto
