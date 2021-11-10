import math
from Objeto.Primitivo import Primitivo
from Abstract.Objeto import TipoObjeto
from enum import Enum
from Abstract.NodoReporteArbol import NodoReporteArbol
from Abstract.Expresion import Expresion
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tipo import TIPO, Nativa


class Nativa_Conv(Expresion):
    def __init__(self, funcion, expresion, conversion, fila, columna):
        print("a")
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
            dato_conversion = self.conversion.compilar(tree,table)
            
            if(dato_conversion.tipo == TipoObjeto.ERROR):
                Excepcion(TipoObjeto.ERROR, f"Operador desconocido: {self.funcion}",self.fila,self.columna);       
        
        
        
        if (self.funcion==Nativa.UPPER):
            return Primitivo(TipoObjeto.CADENA, str(dato.getValue()).upper());
        elif (self.funcion==Nativa.LOWER):
            return Primitivo(TipoObjeto.CADENA, str(dato.getValue()).lower());
        elif (self.funcion==Nativa.FLOAT):
            return Primitivo(TipoObjeto.DECIMAL, float(dato.getValue()));
        elif (self.funcion==Nativa.STRING):
            return Primitivo(TipoObjeto.CADENA, str(dato.getValue()));
        elif (self.funcion==Nativa.TRUNC):
            return Primitivo(TipoObjeto.ENTERO, math.floor(dato.getValue()));
        elif (self.funcion==Nativa.TYPEOF):
            if type(dato.getValue())==int:
                return Primitivo(TipoObjeto.CADENA,"Int64" );
            elif type(dato.getValue())==float:
                return Primitivo(TipoObjeto.CADENA,"Float64" );
            elif type(dato.getValue())==str and dato.getValue()[0]=="'" and dato.getValue()[-0]=="'":
                return Primitivo(TipoObjeto.CADENA,"Char" );
            elif type(dato.getValue())==str:
                return Primitivo(TipoObjeto.CADENA,"String" );
            elif type(dato.getValue())==bool:
                return Primitivo(TipoObjeto.CADENA,"Bool" );
        
                

        
        return Excepcion(TipoObjeto.ERROR, f"Operador desconocido: {self.funcion}",self.fila,self.columna);

    
    def obtenerNodo(self):
        nodo = NodoReporteArbol("NATIVA_CONVERSION")
        if self.conversion != None:
            nodo.agregarHijoNodo(self.expresion.obtenerNodo())
            nodo.agregarHijo(str(self.funcion))
            nodo.agregarHijoNodo(self.conversion.obtenerNodo())
        else:
            nodo.agregarHijo(str(self.funcion))
            nodo.agregarHijoNodo(self.expresion.obtenerNodo())
        
        return nodo