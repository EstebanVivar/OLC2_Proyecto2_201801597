from Abstract.Instruccion import *
from Abstract.Retorno import *
from TablaSimbolos.Generator import Generator

class Break(Instruccion):
    def __init__(self, fila, columna):
        Instruccion.__init__(self, fila, columna)

    def compilar(self, entorno):
        if entorno.breakLbl == '':
            print("Break fuera de ciclo")
            return
        genAux = Generator()
        generator = genAux.getInstance()

        generator.agregarGoto(entorno.breakLbl)