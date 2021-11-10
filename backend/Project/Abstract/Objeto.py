from abc import ABC, abstractmethod
from enum import Enum

class TipoObjeto(Enum):
    ENTERO = 1
    DECIMAL = 2
    BOOLEANO = 3
    CADENA = 4
    CARACTER = 5
    POTENCIA = 6
    MODULO = 7
    STRUCT = 8    
    RANGO = 9
    ARREGLO=10
    ENTORNO = 11
    
    ERROR = 100


class Objeto(ABC):
    def __init__(self, tipo):
        self.tipo = tipo
        super().__init__()

    @abstractmethod
    def toString(self):
        pass

    @abstractmethod
    def getValue(self):
        pass