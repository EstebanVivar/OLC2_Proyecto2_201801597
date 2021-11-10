
import math
from Objeto.Primitivo import Primitivo
from Abstract.Objeto import TipoObjeto
from enum import Enum
from Abstract.NodoReporteArbol import NodoReporteArbol
from Abstract.Expresion import Expresion
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO, Nativa


class Nativa_Mate(Expresion):
    def __init__(self, funcion, expresion, base, fila, columna):
        self.funcion = funcion
        self.expresion = expresion
        self.base = base
        self.fila = fila
        self.columna = columna

    def compilar(self, tree, table):
        dato = self.expresion.compilar(tree, table)
      
        if self.base!=None:
            dato_base = self.base.compilar(tree,table)
            if(dato_base.tipo == TipoObjeto.ERROR):
                return dato_base;  

        if(dato.tipo == TipoObjeto.ERROR):
            return dato;
        
        

        if (self.funcion==Nativa.LOG10):
            if(dato.tipo==TipoObjeto.ENTERO or dato.tipo==TipoObjeto.DECIMAL):
                return Primitivo(TipoObjeto.DECIMAL, float(math.log10(dato.getValue())));            

        elif (self.funcion==Nativa.LOG):
            if((dato.tipo==TipoObjeto.ENTERO or dato.tipo==TipoObjeto.DECIMAL)
            and(dato_base.tipo==TipoObjeto.ENTERO or dato_base.tipo==TipoObjeto.DECIMAL)):
                return Primitivo(TipoObjeto.ENTERO, float(math.log(dato_base.getValue(),dato.getValue())));           
        
        elif (self.funcion==Nativa.SIN):
            if(dato.tipo==TipoObjeto.ENTERO or dato.tipo==TipoObjeto.DECIMAL):
                return Primitivo(TipoObjeto.DECIMAL, math.sin(dato.getValue()));

        elif (self.funcion==Nativa.COS):
            if(dato.tipo==TipoObjeto.ENTERO or dato.tipo==TipoObjeto.DECIMAL):
                return Primitivo(TipoObjeto.DECIMAL, float(math.cos(dato.getValue())));  

        elif (self.funcion==Nativa.TAN):
            if(dato.tipo==TipoObjeto.ENTERO or dato.tipo==TipoObjeto.DECIMAL):
                return Primitivo(TipoObjeto.DECIMAL, float(math.tan(dato.getValue()))); 

        elif (self.funcion==Nativa.SQRT):
            if(dato.tipo==TipoObjeto.ENTERO or dato.tipo==TipoObjeto.DECIMAL):
                return Primitivo(TipoObjeto.DECIMAL, float(math.sqrt(dato.getValue())));             

        return Excepcion(TipoObjeto.ERROR, f"Operador desconocido: {self.funcion}",self.fila,self.columna);

    
    def obtenerNodo(self):
        nodo = NodoReporteArbol("NATIVA_ARITMETICA")
        if self.base != None:
            nodo.agregarHijoNodo(self.expresion.obtenerNodo())
            nodo.agregarHijo(str(self.funcion))
            nodo.agregarHijoNodo(self.base.obtenerNodo())
        else:
            nodo.agregarHijo(str(self.funcion))
            nodo.agregarHijoNodo(self.expresion.obtenerNodo())
        
        return nodo