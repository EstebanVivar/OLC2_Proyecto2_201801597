from Abstract.Instruccion import *
from Abstract.Retorno import *
from TablaSimbolos.Generator import Generator
from Expresiones.Relacional import OperadorRelacional, Relacional
from Expresiones.Constante import Constante, Tipo


class If(Instruccion):
    def __init__(self, condicion, instruccionesIf, fila, columna, instruccionesElse=None):
        Instruccion.__init__(self, fila, columna)
        self.condicion = condicion
        self.instruccionesIf = instruccionesIf
        self.instruccionesElse = instruccionesElse

    def compilar(self, entorno):
        # ARREGLAR CONDICION IGUAL A WHILE
        genAux = Generator()
        generator = genAux.getInstance()
        generator.agregarComentario("INICIO IF")
        # if isinstance(self.condicion, Relacional):
        #     generator.agregarIf(self.condicion.OperacionIzq.valor,
        #                         self.condicion.OperacionDer.valor,
        #                         self.getOp(),
        #                         etiquetaTrue)
        # if isinstance(self.condicion, Constante) and self.condicion.tipo == Tipo.BOOLEANO:
        #     generator.agregarIf(str(self.condicion.valor).lower(),
        #                         "",
        #                         "",
        #                         etiquetaTrue)

        cond = self.condicion.compilar(entorno)
        etiquetaTrue = cond.etiquetaTrue
        etiquetaFalse = cond.etiquetaFalse

        generator.agregarComentario("INSTRUCCIONES SI IF VERDADERO")
        generator.agregarEtiqueta(etiquetaTrue)
        for instruccion in self.instruccionesIf:
            instruccion.compilar(entorno)
        
        if self.instruccionesElse != None:
            exitIf = generator.nuevaEtiqueta()
            generator.agregarGoto(exitIf)
            
    
        generator.agregarEtiqueta(etiquetaFalse)
        if self.instruccionesElse != None:
            if isinstance(self.instruccionesElse, If):
                 self.instruccionesElse.compilar(entorno)
            else:
                for instruccion in self.instruccionesElse:
                        instruccion.compilar(entorno)
            generator.agregarEtiqueta(exitIf)