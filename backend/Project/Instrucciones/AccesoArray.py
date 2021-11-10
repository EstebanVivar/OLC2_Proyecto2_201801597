from Abstract.Expresion import *
from TablaSimbolos.Generator import *
from Abstract.Retorno import Retorno
from Abstract.Retorno import Tipo


class Acceso_Array(Expresion):
    def __init__(self, identificador, expresiones, fila, columna):
        Expresion.__init__(self, fila, columna)
        self.identificador = identificador
        self.expresiones = expresiones

    def compilar(self, entorno):
        genAux = Generator()
        generator = genAux.getInstance()
        var = entorno.obtenerVariable(self.identificador)
        countPos=0
        for pos in self.expresiones:
            if countPos==0:
                etiquetaError = generator.nuevaEtiqueta()
                etiquetaNormal = generator.nuevaEtiqueta()
                etiquetaSalida = generator.nuevaEtiqueta()            
                temporalVariable = generator.agregarTemporal()
                temporalIndice = generator.agregarTemporal()
                temporalValor = generator.agregarTemporal()
                generator.agregarExpresion(temporalIndice, pos.valor, '', '')
                generator.getStack(temporalVariable, var.posicion)
                generator.agregarExpresion(temporalValor, temporalVariable, '', '')
                generator.getHeap(temporalVariable,temporalVariable)
                generator.agregarIf(temporalIndice, '1', '<', etiquetaError)
                generator.agregarIf(temporalIndice, temporalVariable, '>', etiquetaError)
                generator.agregarGoto(etiquetaNormal)
                generator.agregarEtiqueta(etiquetaError)
                self.error(generator)
                generator.agregarExpresion(temporalVariable, '0', '', '')
                generator.agregarGoto(etiquetaSalida)
                
                generator.agregarEtiqueta(etiquetaNormal)

                generator.agregarExpresion(temporalValor, temporalValor, '+',temporalIndice)
                generator.getHeap(temporalVariable,temporalValor)          
                generator.agregarEtiqueta(etiquetaSalida)
                countPos+=1
            else:
                etiquetaError = generator.nuevaEtiqueta()
                etiquetaNormal = generator.nuevaEtiqueta()
                etiquetaSalida = generator.nuevaEtiqueta()
                temporalIndice = generator.agregarTemporal()
                temporalValor = generator.agregarTemporal()
                generator.agregarExpresion(temporalIndice, pos.valor, '', '')
                generator.getHeap(temporalValor,temporalVariable)
                generator.agregarIf(temporalIndice, '1', '<', etiquetaError)
                generator.agregarIf(temporalIndice, temporalValor, '>', etiquetaError)
                generator.agregarGoto(etiquetaNormal)
                generator.agregarEtiqueta(etiquetaError)
                self.error(generator)
                generator.agregarExpresion(temporalVariable, '0', '', '')
                generator.agregarGoto(etiquetaSalida)
                
                generator.agregarEtiqueta(etiquetaNormal)

                generator.agregarExpresion(temporalValor, temporalVariable, '+',temporalIndice)
                generator.getHeap(temporalVariable,temporalValor)          
                generator.agregarEtiqueta(etiquetaSalida)
                countPos+=1
        return Retorno(temporalVariable, var.tipo, True)
        
    def error(self,generator):
        generator.agregarImprimir('c',66)
        generator.agregarImprimir('c',111)
        generator.agregarImprimir('c',117)
        generator.agregarImprimir('c',110)
        generator.agregarImprimir('c',100)
        generator.agregarImprimir('c',115)
        generator.agregarImprimir('c',69)
        generator.agregarImprimir('c',114)
        generator.agregarImprimir('c',114)
        generator.agregarImprimir('c',111)
        generator.agregarImprimir('c',114)
        generator.agregarImprimir('c',10)