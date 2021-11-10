from Abstract.Instruccion import *
from Abstract.Retorno import *
from TablaSimbolos.Generator import Generator


class Imprimir(Instruccion):
    def __init__(self, expresion, fila, columna,saltoLinea=False):
        Instruccion.__init__(self, fila, columna)
        self.expresion= expresion
        self.saltoLinea = saltoLinea

    def compilar(self, entorno):
        for exp in self.expresion:
            expresion = exp.compilar(entorno)
            newGenerator = Generator()
            generador = newGenerator.getInstance()

            if(expresion.tipo == Tipo.ENTERO):
                generador.agregarImprimir("d", expresion.valor)
            elif(expresion.tipo == Tipo.FLOTANTE):
                generador.agregarImprimir("f", expresion.valor)
            elif expresion.tipo == Tipo.BOOLEANO:
                etiquetaTemporal = generador.nuevaEtiqueta()
                
                generador.agregarEtiqueta(expresion.etiquetaTrue)
                generador.printTrue()
                
                generador.agregarGoto(etiquetaTemporal)
                
                generador.agregarEtiqueta(expresion.etiquetaFalse)
                generador.printFalse()

                generador.agregarEtiqueta(etiquetaTemporal)
            elif expresion.tipo == Tipo.CADENA:
                generador.fPrintString()

                paramTemp = generador.agregarTemporal()
                
                generador.agregarExpresion(paramTemp, 'P','+', entorno.tamano )
                generador.agregarExpresion(paramTemp, paramTemp, '+', '1')
                generador.setStack(paramTemp, expresion.valor)
                
                generador.cambioEntorno(entorno.tamano)
                generador.llamadaFuncion('printString')

                temp = generador.agregarTemporal()
                generador.getStack(temp, 'P')
                generador.regresoEntorno(entorno.tamano)
            elif(expresion.tipo == Tipo.CARACTER):
                paramTemp = generador.agregarTemporal()
                
                heapTemp = generador.agregarTemporal()
                
                generador.getHeap(heapTemp,expresion.valor)
                
                generador.agregarImprimir("c", heapTemp)
            elif(expresion.tipo == Tipo.RANGO):
                paramTemp = generador.agregarTemporal()
                
                heapTemp = generador.agregarTemporal()
                
                generador.getHeap(heapTemp,expresion.valor)
                
                generador.agregarImprimir("d", heapTemp)
            else:                
                generador.agregarComentario("NO CONTEMPLADO")

            if self.saltoLinea:
                generador.agregarImprimir("c", 10)