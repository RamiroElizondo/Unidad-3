from ManejadorAparato import ManejadorAparato
from ClaseHeladera import Heladera
from ClaseLavarropa import Lavarropa
from ClaseTelevisor import Televisor


class Menu:
    __manejador: ManejadorAparato

    def __init__(self):
        self.__manejador = ManejadorAparato()
    
    def crearAparatos(self):

    def mostrar(self):
        print('Menu Opciones'.center(30,'-'))
        print('0- Salir')
        print('1- Insertar Aparato')
        print('2- Agregar Aparato')
        print('3- Mostrar Aparato de una posicion')
        print('4- Mostrar Cantidad de cada Aparato')
        print('5- Mostrar Marca de todos los Aparatos')
        print('6- Mostrar Aparatos en venta')
        print('7- Almacenar Objetos')
    
    def opcion1(self):
        posicion = int(input('Ingrese la posicion: '))
        objetoA = self.crearAparatos(posicion)
        self.__manejador.insertarA(objetoA,posicion)


    def opcion2(self):
        print('Aun No Programado')

    def opcion3(self):
        print('Aun No Programado')

    def opcion4(self):
        print('Aun No Programado')

    def opcion5(self):
        print('Aun No Programado')

    def opcion6(self):
        print('Aun No Programado')
    
    def opcion7(self):
        print('Aun No Programado')

    def menuOpciones(self,opcion):
        if opcion == 1:
            self.opcion1()
        elif opcion == 2:
            self.opcion2()
        elif opcion == 3:
            self.opcion3()
        elif opcion == 4:
            self.opcion4()
        elif opcion == 5:
            self.opcion5()
        elif opcion == 6:
            self.opcion6()
        elif opcion == 7:
            self.opcion7()
        elif opcion != 0 and opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5 and opcion != 6 and opcion != 7:
            print('Opcion Invalida')

