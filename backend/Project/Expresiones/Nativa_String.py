from Abstract.Instruccion import *
from Abstract.Retorno import *
from TablaSimbolos.TablaSimbolos import *

from TablaSimbolos.Tipo import *
from TablaSimbolos.Generator import *
from backend.Project.Abstract.Expresion import Expresion


class Nativa_String(Instruccion):
    def __init__(self, funcion, expresion, fila, columna):    
        Instruccion.__init__(self, fila, columna)    
        self.funcion = funcion
        self.expresion = expresion
        

    def compilar(self, entorno):
        genAux = Generator()
        generador = genAux.getInstance()
        if (self.funcion==Nativa.UPPER):
            
            generador.agregarComentario("upper begin")
            exp = self.expresion.compilar(entorno)
            generador.fUpper()
            paramTemp = generador.agregarTemporal()
                
            generador.agregarExpresion(paramTemp, 'P','+', entorno.tamano )
            generador.agregarExpresion(paramTemp, paramTemp, '+', '1')
            generador.setStack(paramTemp, exp.valor)
            
            generador.cambioEntorno(entorno.tamano)
            generador.llamadaFuncion('upper')

            temp = generador.agregarTemporal()
            generador.getStack(temp, 'P')
            generador.regresoEntorno(entorno.tamano)  
            generador.agregarComentario("upper end")
            return Retorno(temp, Tipo.CADENA, True) 
        elif (self.funcion==Nativa.LOWER):
            exp = self.expresion.compilar(entorno)
            generador.agregarComentario("lower begin")
            generador.fLower()
            paramTemp = generador.agregarTemporal()
                
            generador.agregarExpresion(paramTemp, 'P','+', entorno.tamano )
            generador.agregarExpresion(paramTemp, paramTemp, '+', '1')
            generador.setStack(paramTemp, exp.valor)
            
            generador.cambioEntorno(entorno.tamano)
            generador.llamadaFuncion('lower')

            temp = generador.agregarTemporal()
            generador.getStack(temp, 'P')
            generador.regresoEntorno(entorno.tamano)  
             
            generador.agregarComentario("lenght end")
            return Retorno(temp, Tipo.CADENA, True)
        elif (self.funcion==Nativa.LENGTH):
            exp = self.expresion.compilar(entorno)
            generador.fLength()
            paramTemp = generador.agregarTemporal()
                
            generador.agregarExpresion(paramTemp, 'P','+', entorno.tamano )
            generador.agregarExpresion(paramTemp, paramTemp, '+', '1')
            generador.setStack(paramTemp, exp.valor)
            
            generador.cambioEntorno(entorno.tamano)
            generador.llamadaFuncion('length')

            temp = generador.agregarTemporal()
            generador.getStack(temp, 'P')
            generador.regresoEntorno(entorno.tamano)  
             
            generador.agregarComentario("lenght end")
            return Retorno(temp, Tipo.ENTERO, True)
            
           
        

    
    