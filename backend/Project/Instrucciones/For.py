from Abstract.Instruccion import *
from Abstract.Retorno import *
from TablaSimbolos.Generator import Generator
from TablaSimbolos.TablaSimbolos import TablaSimbolos


class For(Instruccion):
    def __init__(self, identificador, expresion, instrucciones, fila, columna):
        Instruccion.__init__(self, fila, columna)
        self.identificador = identificador
        self.expresion = expresion
        self.instrucciones = instrucciones

    def compilar(self, entorno):

        genAux = Generator()
        generator = genAux.getInstance()

        generator.agregarComentario("INICIO FOR")

        nuevoEntorno = TablaSimbolos(entorno)
        rango = self.expresion.compilar(nuevoEntorno)      
        nuevoEntorno.guardarVariable(self.identificador, rango.tipo, False)

        EtiquetaFor = generator.nuevaEtiqueta()
        EtiquetaSalida = generator.nuevaEtiqueta()

        temporalSimulado= generator.agregarTemporal()
        temporalGetStack=generator.agregarTemporal() 
        temporalHeap=generator.agregarTemporal()              
         

        nuevoEntorno.breakLbl = EtiquetaSalida
        nuevoEntorno.continueLbl = EtiquetaFor
         
        generator.agregarExpresion(temporalSimulado,'P','+',entorno.tamano)
        generator.setStack(temporalSimulado,rango.valor)        
        generator.agregarExpresion(temporalSimulado,'P','+',entorno.tamano)        
        generator.getStack(temporalGetStack,temporalSimulado)
        
        generator.agregarEtiqueta(EtiquetaFor)

        generator.getHeap(temporalHeap,temporalGetStack)
        generator.setStack(temporalSimulado,temporalGetStack)
        generator.agregarExpresion(temporalGetStack,temporalGetStack,'+',1)
        generator.agregarIf(temporalHeap,'-1','==',EtiquetaSalida)
        # generator.agregarExpresion(temporalSimulado2,'P','+',entorno.tamano)
        # generator.getStack(temporalStack,temporalSimulado2)
        # generator.agregarIf(temporalGetStack,'-1','==',EtiquetaSalida)

        generator.agregarComentario("INSTRUCCIONES FOR")
        for instruccion in self.instrucciones:
            instruccion.compilar(nuevoEntorno)
        generator.agregarComentario("FIN INSTRUCCIONES FOR")
        generator.agregarGoto(EtiquetaFor)
        generator.agregarEtiqueta(EtiquetaSalida)
