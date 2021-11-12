from Optimizacion.Optimizacion.CodigoTresDirecciones import CodigoTresDirecciones as c3d
from Optimizacion.Optimizacion.Expresiones.Acceso import Acceso
from Optimizacion.Optimizacion.Expresiones.Expresion import Expresion
from Optimizacion.Optimizacion.Expresiones.Variable import *

class Asignacion(c3d):

    def __init__(self, place, exp, fila, colum):
        self.place = place
        self.exp = exp
        super().__init__(fila, colum)
    
    def getCode(self):
        if self.deleted:
            return ''
        
        return f'{self.place.getCode()} = {self.exp.getCode()};'
    
    def selfAsignacion(self):
        if isinstance(self.exp, Variable):
            aux = self.place.getCode() == self.exp.getCode()
        elif isinstance(self.exp, Acceso):
            aux = self.place.getCode() == self.exp.getCode()
        else:
            aux = self.place.getCode() == self.exp.der.getCode() or self.place.getCode() == self.exp.izq.getCode()
        return aux

    def getPlace(self):
        return self.place.getCode()
    
    def getExp(self):
        return self.exp.getCode()