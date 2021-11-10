from Abstract.Expresion import *
from Abstract.Retorno import *
from TablaSimbolos.Generator import Generator

class Array(Expresion):
    def __init__(self,  expresiones, fila, columna):        
        Expresion.__init__(self, fila, columna)
        self.expresiones = expresiones

    def compilar(self, entorno):
        newGenerator = Generator()
        generador = newGenerator.getInstance()
        generador.agregarComentario("INICIO ARRAY")
        retTemp = generador.agregarTemporal()
        generador.agregarExpresion(retTemp, 'H', '', '')
        
        temp2 = generador.agregarTemporal()        
        generador.agregarExpresion(temp2,retTemp, '', '')
        tamanio=len(self.expresiones)
        
        generador.agregarExpresion('H','H', '+', tamanio+1)
        generador.setHeap(temp2,tamanio)
        generador.agregarExpresion(temp2,temp2,'+',1)

        coutExp=0
        for var in self.expresiones:
            coutExp+=1
            if isinstance(var,Array):
                var=var.compilar(entorno)
                generador.setHeap(temp2, var.valor)
            elif var.tipo==Tipo.CADENA:
                var = var.compilar(entorno)
                generador.setHeap(temp2, var.valor)
            else:
                generador.setHeap(temp2, var.valor)
            if coutExp != tamanio:
                generador.agregarExpresion(temp2,temp2,'+',1)
        generador.agregarComentario("FIN ARRAY")
        return Retorno(retTemp, var.tipo, True)
    