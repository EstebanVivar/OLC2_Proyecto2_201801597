

from TablaSimbolos.Simbolo import *
from TablaSimbolos.Excepcion import Excepcion


class TablaSimbolos:
    def __init__(self, anterior=None):
        self.anterior = anterior
        self.tamano = 0
        self.breakLbl = ''
        self.continueLbl = ''
        self.returnLbl = ''
        if(anterior != None):
            self.tamano = self.anterior.tamano
            self.breakLbl = self.anterior.breakLbl
            self.continueLbl = self.anterior.continueLbl
            self.returnLbl = self.anterior.returnLbl
        self.variables = {}
        self.funciones = {}
        self.structs = {}

    def guardarVariable(self, idVariable, tipo, enHeap,tipoStruct=''):
        if idVariable in self.variables.keys():
            print("Variable repetida")
        else:
            nuevoSimbolo = Simbolo(
                idVariable, tipo, self.tamano, self.anterior == None, enHeap,tipoStruct)
            self.tamano += 1
            self.variables[idVariable] = nuevoSimbolo
        return self.variables[idVariable]

    def guardarFuncion(self, idFuncion, funcion):
        if idFuncion in self.funciones.keys():
            print("Función repetida")
        else:
            self.funciones[idFuncion] = funcion

    def guardarStruct(self, idStruct, atributos):
        if idStruct in self.structs.keys():
            print("Struct repetido")
        else:
            self.structs[idStruct] = atributos

    def obtenerVariable(self, idVariable):
        entorno = self
        while entorno != None:
            if idVariable in entorno.variables.keys():
                return entorno.variables[idVariable]
            entorno = entorno.anterior
        return None

    def obtenerFuncion(self, idFuncion):
        entorno = self
        while entorno != None:
            if idFuncion in entorno.funciones.keys():
                return entorno.funciones[idFuncion]
            entorno = entorno.anterior
        return None

    def obtenerStruct(self, idStruct):
        entorno = self
        while entorno != None:
            if idStruct in entorno.structs.keys():
                return entorno.structs[idStruct]
            entorno = entorno.anterior
        return None

    def obtenerGlobal(self):
        entorno = self
        while entorno.anterior != None:
            entorno = entorno.anterior
        return entorno
