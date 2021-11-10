from Abstract.Expresion import *
from TablaSimbolos.Generator import *
from Abstract.Retorno import Retorno
from Abstract.Retorno import Tipo


class Asignacion_Array(Expresion):
    def __init__(self, identificador, expresiones,valor, fila, columna):
        Expresion.__init__(self, fila, columna)
        self.identificador = identificador
        self.valor = valor
        self.expresiones = expresiones

    def compilar(self, entorno):
        genAux = Generator()
        generator = genAux.getInstance()
        var = entorno.obtenerVariable(self.identificador)
        valor = self.valor.compilar(entorno)
        countPos=0
        for pos in self.expresiones:
            if countPos==0:     
                generator.agregarComentario("Inicio Acceso")           
                etiquetaError = generator.nuevaEtiqueta()
                etiquetaNormal = generator.nuevaEtiqueta()
                etiquetaSalida = generator.nuevaEtiqueta()            
                temporalVariable = generator.agregarTemporal()
                temporalAuxiliar = generator.agregarTemporal()
                temporalIndice = generator.agregarTemporal()
                temporalValor = generator.agregarTemporal()                
                

                
                generator.agregarExpresion(temporalVariable,'P', '+',var.posicion)
                generator.getStack(temporalVariable,temporalVariable)                
                generator.agregarExpresion(temporalIndice, pos.valor, '', '')
                generator.agregarExpresion(temporalValor, temporalVariable, '', '')
                generator.getHeap(temporalAuxiliar,temporalValor)
                generator.agregarIf(temporalIndice, '1', '<', etiquetaError)
                generator.agregarIf(temporalIndice, temporalAuxiliar, '>', etiquetaError)                
                generator.agregarGoto(etiquetaNormal)
                generator.agregarEtiqueta(etiquetaError)
                self.error(generator)
                generator.agregarExpresion(temporalAuxiliar, '0', '', '')
                generator.agregarGoto(etiquetaSalida)                
                generator.agregarEtiqueta(etiquetaNormal)
                generator.agregarExpresion(temporalAuxiliar, temporalValor, '+',temporalIndice)
                if len(self.expresiones)==1:
                    generator.setHeap(temporalAuxiliar,valor.valor)   
                else:
                    generator.getHeap(temporalAuxiliar,temporalAuxiliar)       
                generator.agregarEtiqueta(etiquetaSalida)
                countPos+=1
                generator.agregarComentario("Fin Acceso") 
            else:
                generator.agregarComentario("Inicio Acceso Dos Dimnesion")           
                etiquetaError = generator.nuevaEtiqueta()
                etiquetaNormal = generator.nuevaEtiqueta()
                etiquetaSalida = generator.nuevaEtiqueta()
                temporalIndice = generator.agregarTemporal()
                temporalValor = generator.agregarTemporal()                               
                generator.agregarExpresion(temporalIndice, pos.valor, '', '')
                generator.agregarExpresion(temporalValor, temporalAuxiliar, '', '')
                generator.getHeap(temporalAuxiliar,temporalValor)
                generator.agregarIf(temporalIndice, '1', '<', etiquetaError)
                generator.agregarIf(temporalIndice, temporalAuxiliar, '>', etiquetaError)                
                generator.agregarGoto(etiquetaNormal)
                generator.agregarEtiqueta(etiquetaError)
                self.error(generator)
                generator.agregarExpresion(temporalAuxiliar, '0', '', '')
                generator.agregarGoto(etiquetaSalida)                
                generator.agregarEtiqueta(etiquetaNormal)
                generator.agregarExpresion(temporalAuxiliar, temporalValor, '+',temporalIndice)
                generator.setHeap(temporalAuxiliar,valor.valor)          
                generator.agregarEtiqueta(etiquetaSalida)
                countPos+=1
                generator.agregarComentario("Fin Acceso  Dos Dimnesion") 



        return Retorno(temporalVariable, Tipo.ENTERO, True)
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