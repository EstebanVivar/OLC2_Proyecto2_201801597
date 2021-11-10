from Abstract.Expresion import *
from Abstract.Retorno import *
from TablaSimbolos.TablaSimbolos import *
from TablaSimbolos.Generator import *


class Llamada(Expresion):
    def __init__(self, identificador, parametros, fila, columna):
        Expresion.__init__(self, fila, columna)
        self.identificador=identificador
        self.parametros = parametros

    def compilar(self,entorno):
        try:
            func = entorno.obtenerFuncion(self.identificador)
            if func != None:
                valores = []

                genAux = Generator()
                generator = genAux.getInstance()
                # size = entorno.tamano
                size = generator.guardarTemporales(entorno)
                for param in self.parametros:
                    valores.append(param.compilar(entorno))
                temp = generator.agregarTemporal()

                generator.agregarExpresion(temp, 'P', '+', entorno.tamano+1)
                

                aux = 0
                for param in valores:
                    aux = aux +1
                    generator.setStack(temp, param.valor)
                    if aux != len(valores):
                        generator.agregarExpresion(temp, temp, '+', '1')
                
                generator.cambioEntorno(entorno.tamano)
                generator.llamadaFuncion(self.identificador)
                generator.getStack(temp, 'P')
                generator.regresoEntorno(entorno.tamano)
                
                generator.recoverTemps(entorno, size)
                # TODO: Verificar tipo de la funcion. Boolean es distinto
                return Retorno(temp, func.tipo, True)
            else:
                # STRUCT
                struct = entorno.obtenerStruct(self.identificador)
                if struct != None:
                    self.tipoStruct = self.identificador

                    genAux = Generator()
                    generator = genAux.getInstance()

                    returnTemp = generator.agregarTemporal()
                    generator.agregarExpresion(returnTemp, 'H', '', '')

                    aux = generator.agregarTemporal()
                    generator.agregarExpresion(aux, returnTemp, '', '')

                    generator.agregarExpresion('H', 'H','+',len(struct))
                    auxParam=0
                    for att in self.parametros:
                        value = att.compilar(entorno)
                        struct[auxParam].tipoStruct=struct[auxParam].tipo
                        struct[auxParam].tipo=value.tipo

                        if value.tipo != Tipo.BOOLEANO:
                            generator.setHeap(aux, value.valor)
                        else:
                            retLbl = generator.nuevaEtiqueta()
                            
                            generator.agregarEtiqueta(value.etiquetaTrue)
                            generator.setHeap(aux, '1')
                            generator.agregarGoto(retLbl)

                            generator.agregarEtiqueta(value.etiquetaFalse)
                            generator.setHeap(aux, '0')

                            generator.agregarEtiqueta(retLbl)
                        generator.agregarExpresion(aux, aux,'+','1')
                        auxParam=auxParam+1
                    return Retorno(returnTemp, Tipo.STRUCT, True)
        except:
            print("Error en llamada a funcion")
