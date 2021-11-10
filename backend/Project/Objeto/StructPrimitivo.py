from Abstract.Objeto import Objeto,TipoObjeto
from abc import ABC, abstractmethod

class StructPrimitivo(Objeto):
    def __init__(self,nombre,valor):
        self.nombre=nombre
        self.tipo = TipoObjeto.STRUCT
        self.valor = valor

    def toString(self):
        return str(self.valor)

    def getValue(self):
        return self.valor
    
    def setValue(self,value):
        self.valor=value
    
    def getName(self):
        return self.nombre
