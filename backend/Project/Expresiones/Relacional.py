
from Abstract.Expresion import *
from Abstract.Retorno import *
from TablaSimbolos.Generator import Generator
from enum import Enum


class OperadorRelacional(Enum):
    MAYOR = 0
    MENOR = 1
    MAYOR_IGUAL = 2
    MENOR_IGUAL = 3
    COMPARA = 4
    DISTINTO = 5


class Relacional(Expresion):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        Expresion.__init__(self, fila, columna)
        self.operador = operador
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer

    def compilar(self, entorno):
        genAux = Generator()
        generator = genAux.getInstance()

        generator.agregarComentario("INICIO EXPRESION RELACIONAL")

        left = self.OperacionIzq.compilar(entorno)
        right = None

        result = Retorno(None, Tipo.BOOLEANO, False)

        if left.tipo != Tipo.BOOLEANO:
            right = self.OperacionDer.compilar(entorno)
            if (left.tipo == Tipo.ENTERO or left.tipo == Tipo.FLOTANTE) and (right.tipo == Tipo.ENTERO or right.tipo == Tipo.FLOTANTE):
                self.checkLabels()
                generator.agregarIf(left.valor, right.valor,
                                    self.getOp(), self.etiquetaTrue)
                generator.agregarGoto(self.etiquetaFalse)
            elif left.tipo == Tipo.CADENA and right.tipo == Tipo.CADENA:
                print("Comparacion de cadenas")
        else:
            gotoRight = generator.nuevaEtiqueta()
            leftTemp = generator.agregarTemporal()

            generator.agregarEtiqueta(left.etiquetaTrue)
            generator.agregarExpresion(leftTemp, '1', '', '')
            generator.agregarGoto(gotoRight)

            generator.agregarEtiqueta(left.etiquetaFalse)
            generator.agregarExpresion(leftTemp, '0', '', '')

            generator.agregarEtiqueta(gotoRight)

            right = self.OperacionDer.compilar(entorno)
            if right.tipo != Tipo.BOOLEANO:
                print("Error, no se pueden comparar")
                return
            gotoEnd = generator.nuevaEtiqueta()
            rightTemp = generator.agregarTemporal()

            generator.agregarEtiqueta(right.etiquetaTrue)

            generator.agregarExpresion(rightTemp, '1', '', '')
            generator.agregarGoto(gotoEnd)

            generator.agregarEtiqueta(right.etiquetaFalse)
            generator.agregarExpresion(rightTemp, '0', '', '')

            generator.agregarEtiqueta(gotoEnd)

            self.checkLabels()
            generator.agregarIf(leftTemp, rightTemp,
                                self.getOp(), self.etiquetaTrue)
            generator.agregarGoto(self.etiquetaFalse)

        generator.agregarComentario("FIN DE EXPRESION RELACIONAL")
        generator.agregarSaltoLinea()
        result.etiquetaTrue = self.etiquetaTrue
        result.etiquetaFalse = self.etiquetaFalse

        return result

    def checkLabels(self):
        genAux = Generator()
        generator = genAux.getInstance()
        if self.etiquetaTrue == '':
            self.etiquetaTrue = generator.nuevaEtiqueta()
        if self.etiquetaFalse == '':
            self.etiquetaFalse = generator.nuevaEtiqueta()

    def getOp(self):

        if self.operador == OperadorRelacional.MAYOR:
            return '>'
        elif self.operador == OperadorRelacional.MENOR:
            return '<'
        elif self.operador == OperadorRelacional.MAYOR_IGUAL:
            return '>='
        elif self.operador == OperadorRelacional.MENOR_IGUAL:
            return '<='
        elif self.operador == OperadorRelacional.COMPARA:
            return '=='
        elif self.operador == OperadorRelacional.DISTINTO:
            return '!='
