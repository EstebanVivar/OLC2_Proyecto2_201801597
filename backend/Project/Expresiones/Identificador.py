from TablaSimbolos.Generator import *
from Abstract.Expresion import *
from Abstract.Retorno import *


class Identificador(Expresion):
    def __init__(self, identificador, fila, columna):        
        Expresion.__init__(self, fila, columna)
        self.identificador = identificador

    def compilar(self, entorno):
        genAux = Generator()
        generator = genAux.getInstance()

        generator.agregarComentario("Compilacion de Acceso")
        
        var = entorno.obtenerVariable(self.identificador)
        if(var == None):
            print("Error, no existe la variable: "+self.identificador)
            return

        # Temporal para guardar variable
        temp = generator.agregarTemporal()

        # Obtencion de posicion de la variable
        tempPos = var.posicion
        if(not var.esGlobal):
            tempPos = generator.agregarTemporal()
            generator.agregarExpresion(tempPos, 'P',"+", var.posicion )
        generator.getStack(temp, tempPos)

        if var.tipo != Tipo.BOOLEANO:
            generator.agregarComentario("Fin compilacion acceso")
            generator.agregarSaltoLinea()
            return Retorno(temp, var.tipo, True)
        if self.etiquetaTrue == '':
            self.etiquetaTrue = generator.nuevaEtiqueta()
        if self.etiquetaFalse == '':
            self.etiquetaFalse = generator.nuevaEtiqueta()
        
        generator.agregarIf(temp, '1', '==', self.etiquetaTrue)
        generator.agregarGoto(self.etiquetaFalse)

        generator.agregarComentario("Fin compilacion acceso")
        generator.agregarSaltoLinea()

        ret = Retorno(None, Tipo.BOOLEANO, False)
        ret.etiquetaTrue = self.etiquetaTrue
        ret.etiquetaFalse = self.etiquetaFalse
        return ret