from Abstract.Instruccion import *
from Abstract.Retorno import *
from TablaSimbolos.Generator import Generator
from TablaSimbolos.TablaSimbolos import TablaSimbolos

class While(Instruccion):
    def __init__(self, condicion, instrucciones, fila, columna):
        Instruccion.__init__(self, fila, columna)
        self.condicion = condicion
        self.instrucciones = instrucciones

    def compilar(self, entorno):
        genAux = Generator()
        generator=genAux.getInstance()
        
        generator.agregarComentario("INICIO WHILE")
        EtiquetaRegreso=generator.nuevaEtiqueta()
        generator.agregarEtiqueta(EtiquetaRegreso)
        cond = self.condicion.compilar(entorno)
        nuevoEntorno = TablaSimbolos(entorno)

        nuevoEntorno.breakLbl=cond.etiquetaFalse        
        nuevoEntorno.continueLbl=EtiquetaRegreso

        generator.agregarEtiqueta(cond.etiquetaTrue)
        for instruccion in self.instrucciones:
            instruccion.compilar(nuevoEntorno)
        generator.agregarGoto(EtiquetaRegreso)
        generator.agregarEtiqueta(cond.etiquetaFalse)

        
        

       