from abc import ABC, abstractmethod

class Expresion(ABC):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.etiquetaTrue=""
        self.etiquetaFalse=""
        self.tipoStruct = ''    

    @abstractmethod
    def compilar(self,entorno):
        pass
   