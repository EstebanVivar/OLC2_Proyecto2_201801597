from Abstract.Instruccion import *
from TablaSimbolos.Generator import *
from Abstract.Retorno import Retorno

class Asignacion_Struct(Instruccion):
    def __init__(self, identificador, atributo, expresion, fila, columna):
        Instruccion.__init__(self, fila, columna)
        self.identificador = identificador
        self.atributo = atributo
        self.expresion = expresion

    def compilar(self, entorno):
        genAux = Generator()
        generator = genAux.getInstance()
        generator.agregarComentario("Inicio Asignacion Struct")
        val = self.expresion.compilar(entorno)
        
        var = entorno.obtenerVariable(self.identificador)

        temp = generator.agregarTemporal()

        tempPos = var.posicion
        if(not var.esGlobal):
            tempPos = generator.agregarTemporal()
            generator.agregarExpresion(tempPos, 'P', "+", var.posicion)

        generator.getStack(temp, tempPos)

        if type(var.tipo) == str:
            struct = var.tipo
        else:                
            struct = var.tipoStruct
        if struct != '':
            struct = entorno.obtenerStruct(struct)
            finalAtt = None
            finalAttPos = 0
            for att in struct:
                if att.identificador == self.atributo:
                    finalAtt = att
                    break
                finalAttPos = finalAttPos + 1

            tempAux = generator.agregarTemporal()            
            retTemp = generator.agregarTemporal()

            generator.agregarExpresion(tempAux, temp, '+', finalAttPos)
            generator.setHeap(tempAux, val.valor)
        generator.agregarComentario("Fin Asignacion Struct")
        
        return Retorno(retTemp, finalAtt.tipo, True)
