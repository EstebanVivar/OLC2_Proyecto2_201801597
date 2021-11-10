from Abstract.Expresion import *
from Abstract.Retorno import *
from TablaSimbolos.Generator import Generator
from enum import Enum

class OperadorLogico(Enum):
    AND = 0
    OR = 1
    NOT = 2

class Logica(Expresion):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        Expresion.__init__(self, fila, columna)
        self.operador = operador
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer
    
    def compilar(self, entorno):
        genAux = Generator()
        generator = genAux.getInstance()

        generator.agregarComentario("INICIO EXPRESION LOGICA")

        self.verificarEtiquetas()
        etiquetaAux = ''

        if self.operador == OperadorLogico.AND:
            etiquetaAux = self.OperacionIzq.etiquetaTrue = generator.nuevaEtiqueta()
            self.OperacionDer.etiquetaTrue = self.etiquetaTrue
            self.OperacionIzq.etiquetaFalse = self.OperacionDer.etiquetaFalse = self.etiquetaFalse
        elif self.operador == OperadorLogico.OR:
            self.OperacionIzq.etiquetaTrue = self.OperacionDer.etiquetaTrue = self.etiquetaTrue
            etiquetaAux = self.OperacionIzq.etiquetaFalse = generator.nuevaEtiqueta()
            self.OperacionDer.etiquetaFalse = self.etiquetaFalse
        else:
            print("NOT")
        left = self.OperacionIzq.compilar(entorno)
        if left.tipo != Tipo.BOOLEANO:
            print("No se puede utilizar en expresion booleana")
            return
        generator.agregarEtiqueta(etiquetaAux)
        right = self.OperacionDer.compilar(entorno)
        if right.tipo != Tipo.BOOLEANO:
            print("No se puede utilizar en expresion booleana")
            return
        generator.agregarComentario("FINALIZO EXPRESION LOGICA")
        generator.agregarSaltoLinea()
        ret = Retorno(None, Tipo.BOOLEANO, False)
        ret.etiquetaTrue = self.etiquetaTrue
        ret.etiquetaFalse = self.etiquetaFalse
        return ret
    
    def verificarEtiquetas(self):
        genAux = Generator()
        generator = genAux.getInstance()
        if self.etiquetaTrue == '':
            self.etiquetaTrue = generator.nuevaEtiqueta()
        if self.etiquetaFalse == '':
            self.etiquetaFalse = generator.nuevaEtiqueta()