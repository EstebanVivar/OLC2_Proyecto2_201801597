from Abstract.Expresion import *
from Abstract.Retorno import *
from TablaSimbolos.Generator import Generator

class Rango(Expresion):
    def __init__(self,  OperacionIzq, OperacionDer, fila, columna):
        Expresion.__init__(self, fila, columna)
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer

    

    def compilar(self, entorno):   
        newGenerator = Generator()        
        generador = newGenerator.getInstance()
        retTemp = generador.agregarTemporal()
        res_left = self.OperacionIzq.valor
        
        if self.OperacionDer==None:     
            generador.agregarExpresion(retTemp, 'H', '', '')        
            for i in res_left:
                generador.setHeap('H', ord(i))
                generador.nextHeap()
            generador.setHeap('H', '-1')
            generador.nextHeap()
            return Retorno(retTemp, Tipo.CARACTER, True)
        
        res_right = self.OperacionDer.valor
        generador.agregarExpresion(retTemp, 'H', '', '')
        for i in range(res_left, res_right+1):
            generador.setHeap('H', i)
            generador.nextHeap()
        generador.setHeap('H', '-1')
        generador.nextHeap()
        return Retorno(retTemp, Tipo.RANGO, True)

        # retTemp = generador.agregarTemporal()
        # generador.agregarExpresion(retTemp, 'H', '', '')

        # for char in str(self.valor):
        #     generador.setHeap('H', ord(char))   # heap[H] = NUM;
        #     generador.nextHeap()                # H = H + 1;

        # generador.setHeap('H', '-1')            # FIN DE CADENA
        # generador.nextHeap()

     
        
      
     
      