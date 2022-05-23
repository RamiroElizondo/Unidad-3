from this import d


class Equipo:
    __nombre: str = ""
    __cuidad: str = ""
    __jugadores: None
    
    def __init__(self,nom,cuidad):
        self.__nombre = str(nom)
        self.__cuidad = str(cuidad)
        self.__jugadores = []
    
    def agregarJugador(self,jugador):
        

    def __str__(self):
        return ('Nombre: {} Ciudad: {}'.format(self.__nombre,self.__cuidad))