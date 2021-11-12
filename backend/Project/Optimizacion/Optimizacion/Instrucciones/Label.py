from Optimizacion.Optimizacion.CodigoTresDirecciones import CodigoTresDirecciones as c3d

class Label(c3d):

    def __init__(self,lbl, fila, colum):
        self.id = lbl
        super().__init__(fila, colum)
    
    def getCode(self):
        if self.deleted:
            return ''
        return f'{self.id}:'
    