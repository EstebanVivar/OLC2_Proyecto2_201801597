from Optimizacion.Optimizacion.CodigoTresDirecciones import CodigoTresDirecciones

class Variable(CodigoTresDirecciones):

    def __init__(self,value, line, column, constante = False):
        self.value = value
        self.contante = constante
        super().__init__(line, column)
    
    def getCode(self):
        return str(self.value)
    
    def cambiar_a (self, valor):
        self.value = valor