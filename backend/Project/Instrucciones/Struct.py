from Abstract.Instruccion import *

class Struct(Instruccion):

    def __init__(self, identificador, atributos,  fila, columna):
        Instruccion.__init__(self, fila, columna)
        self.identificador = identificador
        self.atributos = atributos
    
    def compilar(self, entorno):
        entorno.guardarStruct(self.identificador, self.atributos)