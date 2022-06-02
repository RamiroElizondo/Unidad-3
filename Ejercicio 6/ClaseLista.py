from zope.interface import implementer
from ClaseInterfaz import Interfaz
from ClaseNodo import Nodo
from ClaseArtefacto import Artefacto

@implementer(Interfaz)
class Lista:
    __comienzo: Nodo | None
    
    def __init__(self):
        self.__comienzo = None
        self.__tope = None

    def encuentra(self,posicion:int):
        actual = self.__comienzo
        while actual != None and posicion != 0:
            actual = actual.getSiguiente()
            posicion -= 1
        if actual == None:
            raise Exception("Posicion no valida")
        
        return actual
    
    def insertarElemento(self,artefacto:Artefacto, pos:int):
        nodo = self.encuentra(pos)
        nodo.setSiguiente(Nodo(artefacto,nodo.getSiguiente()))
    
    def agregarElemento(self,elemento):
        if self.__comienzo is None:
            self.__comienzo = Nodo(elemento,None)
            self.__tope = self.__comienzo
        else:
            self.__comienzo.__next(Nodo(elemento,None)) #type: ignore
            self.__tope = self.__tope.__next #type: ignore

    def mostrarElemento(self,pos:int):
        nodo = self.encuentra(pos)
        print('Artefacto: {}'.format(nodo.getDato()))
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self