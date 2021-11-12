from Optimizacion.Optimizacion.CodigoTresDirecciones import CodigoTresDirecciones as c3d

class Return(c3d):

    def __init__(self, fila, colum):
        super().__init__(fila, colum)
    
    def getCode(self):
        return 'return;'