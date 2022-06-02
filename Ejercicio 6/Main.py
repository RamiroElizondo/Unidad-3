from Menu import Menu


if __name__ == '__main__':
    menu = Menu()
    opcion = None
    while opcion != 0:
        menu.mostrar()
        opcion = int(input('Tu Opcion: '))
        menu.menuOpciones(opcion)
    else:
        print('Fin del Programa')