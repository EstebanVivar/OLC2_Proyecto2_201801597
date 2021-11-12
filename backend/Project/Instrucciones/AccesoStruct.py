from Abstract.Expresion import *
from TablaSimbolos.Generator import *
from Abstract.Retorno import Retorno
from Abstract.Retorno import Tipo

class AccesoStruct(Expresion):

    def __init__(self, identificador, atributo, fila, columna):
        Expresion.__init__(self, fila, columna)
        self.identificador = identificador
        self.atributo = atributo
    
    def compilar(self, entorno):
        genAux = Generator()
        generator = genAux.getInstance()
        generator.agregarComentario("Inicio Acceso Struct")

        overStruct=False
        if isinstance(self.identificador,AccesoStruct):
            var = self.identificador.compilar(entorno)
            overStruct=True     
        else:
            var = entorno.obtenerVariable(self.identificador)
        finalAttPos = 0
        finalAtt = None
        temp = generator.agregarTemporal()
        if  overStruct:
            struct = entorno.obtenerStruct(var.tipoAuxiliar)   
                     
            for att in struct:              

                if att.identificador == self.atributo:
                    finalAtt = att
                    break
                finalAttPos = finalAttPos + 1
        else:
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
                for att in struct:              

                    if att.identificador == self.atributo:
                        finalAtt = att
                        break
                    finalAttPos = finalAttPos + 1

        tempAux = generator.agregarTemporal()
        retTemp = generator.agregarTemporal()

        generator.agregarExpresion(tempAux, temp, '+', finalAttPos)
        generator.getHeap(retTemp, tempAux)
        generator.agregarComentario("Fin Acceso Struct")
        return Retorno(retTemp, finalAtt.tipo, True,finalAtt.tipoStruct)
       