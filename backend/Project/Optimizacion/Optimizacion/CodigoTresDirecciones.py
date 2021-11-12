from abc import ABC, abstractmethod

class CodigoTresDirecciones(ABC):
    
    def __init__(self, fila, colum):
        self.fila = fila
        self.colum = colum
        self.haveInt = False
        self.deleted = False
    
    @abstractmethod
    def getCode(self):
        pass