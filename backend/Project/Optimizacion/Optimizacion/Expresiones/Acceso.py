from Optimizacion.Optimizacion.CodigoTresDirecciones import *

class Acceso(CodigoTresDirecciones):
    def __init__(self, StackHeap, position, fila, colum):
        self.StackHeap = StackHeap
        self.position = position
        super().__init__(fila, colum)
    
    def getCode(self):
        return f'{self.StackHeap}[int({self.position.getCode()})]' 