from Abstract.Expresion import *
from Abstract.Retorno import *
from TablaSimbolos.Generator import Generator

class Constante(Expresion):
    def __init__(self, valor,tipo, fila, columna):
        Expresion.__init__(self, fila, columna)
        self.valor = valor
        self.tipo=tipo

    def compilar(self, entorno):  
        newGenerator = Generator()        
        generador = newGenerator.getInstance()
        if(self.tipo == Tipo.ENTERO or self.tipo == Tipo.FLOTANTE):
            return Retorno(str(self.valor), self.tipo, False)
        elif self.tipo == Tipo.BOOLEANO:
            if self.etiquetaTrue == '':
                self.etiquetaTrue = generador.nuevaEtiqueta()
            if self.etiquetaFalse == '':
                self.etiquetaFalse = generador.nuevaEtiqueta()
            
            
            if(self.valor):
                generador.agregarGoto(self.etiquetaTrue)
                generador.agregarComentario("GOTO PARA EVITAR ERROR DE GO1")
                generador.agregarGoto(self.etiquetaFalse)
            else:
                generador.agregarGoto(self.etiquetaFalse)
                generador.agregarComentario("GOTO PARA EVITAR ERROR DE GO2")
                generador.agregarGoto(self.etiquetaTrue)
            
            retorno = Retorno(self.valor, self.tipo, False)
            retorno.etiquetaTrue = self.etiquetaTrue
            retorno.etiquetaFalse = self.etiquetaFalse
            return retorno

        elif self.tipo == Tipo.CADENA:
            retTemp = generador.agregarTemporal()
            generador.agregarExpresion(retTemp, 'H', '', '')

            for char in str(self.valor):
                generador.setHeap('H', ord(char))   # heap[H] = NUM;
                generador.nextHeap()                # H = H + 1;

            generador.setHeap('H', '-1')            # FIN DE CADENA
            generador.nextHeap()

            return Retorno(retTemp, Tipo.CADENA, True)
        else:
            print('Por hacer')
    


   
