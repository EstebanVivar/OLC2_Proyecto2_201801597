from Abstract.Expresion import *
from Abstract.Retorno import *
from TablaSimbolos.Generator import Generator
from enum import Enum
import uuid

class OperadorAritmetico(Enum):
    MAS = 0
    MENOS = 1
    MULTIPLICACION = 2
    DIVISION = 3
    POTENCIA = 4


class Aritmetica(Expresion):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        Expresion.__init__(self, columna, columna)
        self.operador = operador
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer

    
    def compilar(self, entorno):
        genAux = Generator()
        generator = genAux.getInstance()
        izquierdo = self.OperacionIzq.compilar(entorno)
        derecho = self.OperacionDer.compilar(entorno)
        
        temp = generator.agregarTemporal()
       
        operador = ''
        
        if(self.operador == OperadorAritmetico.MAS):
            operador = '+'
        elif(self.operador == OperadorAritmetico.MENOS):
            operador = '-'
        elif(self.operador == OperadorAritmetico.MULTIPLICACION):
            operador = '*'
        elif (self.operador == OperadorAritmetico.DIVISION):
            operador = '/'
        if  derecho.tipo == Tipo.RANGO:      
            heapTemp=generator.agregarTemporal()
            generator.getHeap(heapTemp,derecho.valor)
            if operador=='/':
                generator.agregarExpresion(temp, f'float64({izquierdo.valor})', '/',f'float64({heapTemp})')
                return Retorno(temp, Tipo.FLOTANTE, True)
            else:
                generator.agregarExpresion(temp, izquierdo.valor,operador,heapTemp)  
            return self.retorno(izquierdo,derecho,temp) 
        if izquierdo.tipo == Tipo.RANGO:
            heapTemp=generator.agregarTemporal()
            generator.getHeap(heapTemp,izquierdo.valor)   
            if operador=='/':
                generator.agregarExpresion(temp, f'float64({heapTemp})', '/',f'float64({derecho.valor})')
                return Retorno(temp, Tipo.FLOTANTE, True)
            else:         
                generator.agregarExpresion(temp, heapTemp,operador,derecho.valor)
            return self.retorno(izquierdo,derecho,temp)
        elif(self.operador == OperadorAritmetico.DIVISION):
            
            trueLbl = generator.nuevaEtiqueta()
            falseLbl = generator.nuevaEtiqueta()
            exitLbl = generator.nuevaEtiqueta()
            generator.agregarComentario("hola")
            generator.agregarIf(derecho.valor, 0, '==', trueLbl)
            generator.agregarGoto(falseLbl)
            generator.agregarEtiqueta(trueLbl)
            # generator.printMathError()
            generator.agregarGoto(exitLbl)
            generator.agregarEtiqueta(falseLbl)
            generator.agregarExpresion(temp, f'float64({izquierdo.valor})', '/',f'float64({derecho.valor})')
            generator.agregarEtiqueta(exitLbl)
            generator.agregarComentario("fin")
            return Retorno(temp, Tipo.FLOTANTE, True)
        elif self.operador == OperadorAritmetico.POTENCIA:
            # generator.fPower()
            paramTmp = generator.agregarTemporal()

            generator.agregarExpresion(paramTmp, 'P', entorno.tamano, '+')
            generator.agregarExpresion(paramTmp, paramTmp, '1', '+')
            generator.setStack(paramTmp, izquierdo.valor)

            generator.agregarExpresion(paramTmp, paramTmp, '1', '+')
            generator.setStack(paramTmp, derecho.valor)

            generator.cambioEntorno(entorno.tamano)
            generator.llamadaFuncion('Potencia')

            tmp = generator.agregarTemporal()
            generator.getStack(tmp, 'P')
            generator.regresoEntorno(entorno.tamano)
            if izquierdo.tipo == Tipo.FLOTANTE or derecho.tipo == Tipo.FLOTANTE:
                return Retorno(tmp, Tipo.FLOTANTE, True)
            else:
                return Retorno(tmp, Tipo.ENTERO, True)
        
        elif izquierdo.tipo == Tipo.RANGO or derecho.tipo == Tipo.RANGO:
            generator.agregarExpresion(temp, izquierdo.valor,operador, derecho.valor)
            # return Retorno(temp, Tipo.RANGO, True)
        else:
            generator.agregarExpresion(temp, izquierdo.valor,operador, derecho.valor)
        
        return self.retorno(izquierdo,derecho,temp)
          
    def retorno(self,izquierdo,derecho,temp):
        if izquierdo.tipo == Tipo.FLOTANTE or derecho.tipo == Tipo.FLOTANTE:
            return Retorno(temp, Tipo.FLOTANTE, True)
        else:
            return Retorno(temp, Tipo.ENTERO, True)