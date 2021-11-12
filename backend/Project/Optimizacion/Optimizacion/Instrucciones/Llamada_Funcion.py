from Optimizacion.Optimizacion.CodigoTresDirecciones import CodigoTresDirecciones as c3d

class Llamada_Funcion(c3d):

    def __init__(self, id, fila, colum):
        self.id = id
        super().__init__(fila, colum)
    
    def getCode(self):
        return f'{self.id}();'
    