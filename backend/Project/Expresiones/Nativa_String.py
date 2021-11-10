import math

import locale
from Objeto.Primitivo import Primitivo
from Abstract.Objeto import TipoObjeto
from enum import Enum
from Abstract.NodoReporteArbol import NodoReporteArbol
from Abstract.Expresion import Expresion
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO, Nativa


class Nativa_String(Expresion):
    def __init__(self, funcion, expresion, conversion, fila, columna):        
        self.funcion = funcion
        self.expresion = expresion
        self.conversion = conversion
        self.fila = fila
        self.columna = columna
        

    def compilar(self, tree, table):
        
        if self.expresion!=None:
            dato = self.expresion.compilar(tree, table)
            if(dato.tipo == TipoObjeto.ERROR):
                Excepcion(TipoObjeto.ERROR, f"Operador desconocido: {self.funcion}",self.fila,self.columna);
        
        if self.conversion!=None:
            dato_conversion = self.conversion
            
            if(dato_conversion == TipoObjeto.ERROR):
                Excepcion(TipoObjeto.ERROR, f"Operador desconocido: {self.funcion}",self.fila,self.columna);  
                
       
        
        if (self.funcion==Nativa.PARSE):
            if(dato.tipo==TipoObjeto.CADENA):
                if(dato_conversion==TipoObjeto.ENTERO):                
                    return Primitivo(TipoObjeto.ENTERO, int(float(dato.getValue())));
                elif(dato_conversion==TipoObjeto.DECIMAL):              
                    return Primitivo(TipoObjeto.DECIMAL, float(dato.getValue()));
        
        return Excepcion(TipoObjeto.ERROR, f"Operador desconocido: {self.funcion}",self.fila,self.columna);

    
    def obtenerNodo(self):
        nodo = NodoReporteArbol("NATIVA_CONVERSION")
        if self.conversion != None:
            nodo.agregarHijo(str(self.funcion))
            # nodo.agregarHijoNodo(self.conversion.obtenerNodo())       
            nodo.agregarHijoNodo(self.expresion.obtenerNodo())
        
        return nodo