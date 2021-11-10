from Abstract.Instruccion import *

class Parametro(Instruccion):

    def __init__(self, identificador,tipo, fila, columna):
        Instruccion.__init__(self, fila, columna)
        self.identificador = identificador
        self.tipo = tipo
    
    def compilar(self, entorno):
        return self