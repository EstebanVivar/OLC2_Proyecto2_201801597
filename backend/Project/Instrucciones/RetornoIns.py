from Abstract.Expresion import *
from Abstract.Retorno import *
from TablaSimbolos.Generator import *

class RetornoIns(Expresion):

    def __init__(self, expresion, fila, columna):
        Expresion.__init__(self, fila, columna)
        self.expresion = expresion
    
    def compilar(self, entorno):
        
        if(entorno.returnLbl == ''):
            print("Return fuera de funcion")
            return
        genAux = Generator()
        generator = genAux.getInstance()
        generator.agregarComentario("inicio return")
        value = self.expresion.compilar(entorno)
        if(value.tipo == Tipo.BOOLEANO):
            tempLbl = generator.nuevaEtiqueta()
            
            generator.agregarEtiqueta(value.etiquetaTrue)
            generator.setStack('P', '1')
            generator.agregarGoto(tempLbl)

            generator.agregarEtiqueta(value.etiquetaFalse)
            generator.setStack('P', '0')

            generator.agregarEtiqueta(tempLbl)
        else:
            generator.setStack('P', value.valor)
        generator.agregarComentario("fin return")