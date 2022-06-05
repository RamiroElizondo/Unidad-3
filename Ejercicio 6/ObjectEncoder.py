import json
from ClaseLista import ListaEnlazada
from ClaseTelevisor import Televisor
from ClaseLavarropa import Lavarropa
from ClaseHeladera import Heladera

class ObjectEncoder:
    def leerJSON(self,archivo):
        with open(archivo,'r',encoding='utf8')as docjson:
            datos = json.load(docjson)
        return datos

    def cargarObjetos(self,lista:ListaEnlazada):
        dicc = self.leerJSON("aparatos.json")
        for elem in dicc:
            if "__class__" not in elem:
                raise Exception("No hay Objetos")
            else:
                class_name = elem["__class__"]
                if class_name == "Heladera":
                    atributos = elem["__atributos__"]
                    heladera = Heladera(**atributos)
                    lista.agregarElemento(heladera)
                elif class_name == "Lavarropa":
                    atributos = elem["__atributos__"]
                    lavarropa= Lavarropa(**atributos)
                    lista.agregarElemento(lavarropa)
                elif class_name == "Televisor":
                    atributos = elem["__atributos__"]
                    televisor = Televisor(**atributos)
                    lista.agregarElemento(televisor)

    def escribirJSON(self,archivo,datos):
        with open(archivo,'w',encoding='utf8')as docjson:
            json.dump(datos,docjson)
        return True