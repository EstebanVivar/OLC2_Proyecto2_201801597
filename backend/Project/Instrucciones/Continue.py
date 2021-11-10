from Abstract.Instruccion import *
from Abstract.Retorno import *
from TablaSimbolos.Generator import Generator

class Continue(Instruccion):
    def __init__(self, fila, columna):
        Instruccion.__init__(self, fila, columna)

    def compilar(self, entorno):
        if entorno.continueLbl == '':
            print("Continue fuera de ciclo")
            return
        genAux = Generator()
        generator = genAux.getInstance()

        generator.agregarGoto(entorno.continueLbl)