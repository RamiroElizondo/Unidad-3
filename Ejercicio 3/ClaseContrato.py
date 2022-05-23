from datetime import date
from ClaseJugador import Jugador
from ClaseEquipo import Equipo



class Contrato:
    __fechaI: date
    __fechaF: date
    __pagoM: float
    __jugador: Jugador
    __equipo: Equipo

    def __init__(self, fI, fF, pago,jugador,equipo):
        self.__fechaI = date(fI)
        self.__fechaF = date(fF)
        self.__pagoM = float(pago)
        self.__jugador = jugador
        self.__equipo = equipo
        self.__jugador = jugador
        self.__equipo = equipo
        