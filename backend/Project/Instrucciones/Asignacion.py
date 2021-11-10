
from Abstract.Instruccion import *
from Abstract.Retorno import *
from TablaSimbolos.Generator import *


class Asignacion(Instruccion):
    def __init__(self, identificador, expresion,fila, columna,tipo = None):        
        Instruccion.__init__(self, fila, columna)
        self.identificador = identificador
        self.expresion = expresion
        self.tipo = tipo

    def compilar(self, entorno):
        genAux = Generator()
        generator = genAux.getInstance()

        generator.agregarComentario("Compilacion de valor de variable")
        # Compilacion de valor que estamos asignando
        val = self.expresion.compilar(entorno)

        generator.agregarComentario("Fin de valor de variable")

        # Guardado y obtencion de variable. Esta tiene la posicion, lo que nos sirve para asignarlo en el heap
        nuevaVariable=entorno.obtenerVariable(self.identificador)
        if nuevaVariable == None:
            nuevaVariable = entorno.guardarVariable(self.identificador, val.tipo, (val.tipo == Tipo.CADENA or val.tipo == Tipo.STRUCT),self.expresion.tipoStruct)
        nuevaVariable.tipo = val.tipo
        
        # Obtencion de posicion de la variable
        tempPos = nuevaVariable.posicion
        if(not nuevaVariable.esGlobal):
            tempPos = generator.agregarTemporal()
            generator.agregarExpresion(tempPos, 'P', "+", nuevaVariable.posicion)
        
        if(val.tipo == Tipo.BOOLEANO):
            tempLbl = generator.nuevaEtiqueta()
            
            generator.agregarEtiqueta(val.etiquetaTrue)
            generator.setStack(tempPos, "1")
            
            generator.agregarGoto(tempLbl)

            generator.agregarEtiqueta(val.etiquetaFalse)
            generator.setStack(tempPos, "0")

            generator.agregarEtiqueta(tempLbl)
        else:
            generator.setStack(tempPos, val.valor)
        generator.agregarSaltoLinea()