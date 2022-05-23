from ast import Eq
import csv
import numpy
from ClaseEquipo import Equipo


class ManejadorEquipos:
    __arreglo: numpy.ndarray

    def __init__(self):
        self.__arreglo = numpy.empty(0, dtype=Equipo)

    def cargarEquipo(self):
        with open('Ejercicio 3\equipos.csv','r',encoding='utf8')as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader,None)
            for linea in reader:
                objeto = Equipo(linea[0],linea[1])
                self.__flores = numpy.append(self.__flores, objeto) # type: ignore

        for objetoE in self.__arreglo:
            print(objetoE)