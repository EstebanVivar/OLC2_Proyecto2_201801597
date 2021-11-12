from Optimizacion.Optimizacion.CodigoTresDirecciones import CodigoTresDirecciones as c3d

class If(c3d):

    def __init__(self,condicion,label, fila, colum):
        self.condicion = condicion
        self.etiqueta = label
        super().__init__(fila, colum)
    
    def getCode(self):
        return f'if {self.condicion.getCode()} {{goto {self.etiqueta};}}'