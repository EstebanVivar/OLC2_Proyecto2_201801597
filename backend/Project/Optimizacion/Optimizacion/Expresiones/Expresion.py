from Optimizacion.Optimizacion.CodigoTresDirecciones import CodigoTresDirecciones

class Expresion(CodigoTresDirecciones):

    def __init__(self, izq, der, tipo, line, column):
        self.izq = izq
        self.der = der
        self.tipo = tipo
        super().__init__(line, column)
    
    def Redu6(self):
        if self.tipo == '+':
            self.deleted = self.der.getCode() == '0' or self.izq.getCode() == '0'
        elif self.tipo == '-':
            self.deleted = self.der.getCode() == '0'
        elif self.tipo == '*':
            self.deleted = self.der.getCode() == '1' or self.izq.getCode() == '1'
        elif self.tipo == '/':
            self.deleted = self.der.getCode() == '1'
        return self.deleted
    
    def Redu7(self):
        ret=False
        if self.tipo=='+' and self.der.getCode() == '0':
            self.tipo=''
            self.der.cambiar_a('')
            ret=True
        elif self.tipo=='+' and self.izq.getCode() == '0':
            self.tipo=''
            self.izq.cambiar_a('')
            ret=True
        elif self.tipo == '-' and self.der.getCode() == '0':
            self.tipo=''
            self.der.cambiar_a('')
            ret=True
        elif self.tipo=='*' and self.der.getCode() == '1':
            self.tipo=''
            self.der.cambiar_a('')
            ret=True
        elif self.tipo=='*' and self.izq.getCode() == '1':
            self.tipo=''
            self.izq.cambiar_a('')
            ret=True
        elif self.tipo == '/' and self.der.getCode() == '1':
            self.tipo=''
            self.der.cambiar_a('')
            ret=True
        return ret
    
    def Redu8(self):
        ret=False
        if self.tipo == '*':
            if self.izq.getCode()=='2':
                self.izq.cambiar_a(self.der.getCode())
                self.tipo='+'
                ret=True
            elif self.der.getCode()=='2':
                self.der.cambiar_a(self.izq.getCode())
                self.tipo='+'
                ret=True
            if self.izq.getCode()=='0':
                self.der.cambiar_a('')
                self.tipo=''
                ret=True
            elif self.der.getCode()=='0':
                self.izq.cambiar_a('')
                self.tipo=''
                ret=True
        elif self.tipo == '/':
            if self.izq.getCode()=='0':
                self.der.cambiar_a('')
                self.tipo=''
                ret=True
        return ret

    def signoContrario(self):
        if self.tipo == '>':
            self.tipo = '<='
        elif self.tipo == '<':
            self.tipo = '>='
        elif self.tipo == '>=':
            self.tipo = '<'
        elif self.tipo == '<=':
            self.tipo = '>'
        elif self.tipo == '==':
            self.tipo = '!='
        elif self.tipo == '!=':
            self.tipo = '=='

    def getCode(self):
        return f'{self.izq.getCode()}{self.tipo}{self.der.getCode()}'