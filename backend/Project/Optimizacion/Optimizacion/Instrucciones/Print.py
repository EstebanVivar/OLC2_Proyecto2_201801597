from Optimizacion.Optimizacion.CodigoTresDirecciones import CodigoTresDirecciones as c3d

class Print(c3d):

    def __init__(self, str, exp, fila, colum):
        self.str = str
        self.exp = exp
        super().__init__(fila, colum)
    
    def getCode(self):
        if self.deleted:
            return ''
        elif self.str != '%f':
            return f'fmt.Printf("{self.str}", int({self.exp.getCode()}));'
        else:
            return f'fmt.Printf("{self.str}", {self.exp.getCode()});'