from re import A
from Optimizacion.Optimizacion.Gotos.Goto import *
from Optimizacion.Optimizacion.Gotos.If import *
from Optimizacion.Optimizacion.Instrucciones.Asignacion import *
from Optimizacion.Optimizacion.Instrucciones.Label import Label

class Optimizador:

    def __init__(self, packages, temporales, codigo):
        self.packages = packages
        self.temps = temporales
        self.code = codigo
        self.optimizacion = []
    
    def getCode(self):
        ret = f'package main;\n\n'
        if self.packages:
            var = ''
            for pk in self.packages:
                var += '"'+ pk + '";\n\t'
            var = var[:-3]
            ret += f'import(\n\t{var}\n);\n'
        for temp in self.temps:
            ret += f'var {temp}\n'
        
        ret += '\n'
        
        for func in self.code:
            ret += func.getCode() + '\n\n'
            
        return ret
    
    def reporteMirilla(self,regla, expresion, optimizada, fila):
        self.optimizacion.append(f'{regla}, {expresion}, {optimizada}, {fila}')
    
    def getReporte(self):
        return self.optimizacion
        

    def Mirilla(self):
        # Por cada funcion
        for func in self.code:
            tam = 20
            if len(func.instr)<tam:
                tam=len(func.instr)
            yaentro=False
            
            while tam <= len(func.instr):
                opt = False
                # 10 pasadas al codigo de la mirilla
                for i in range(10):
                    aux = 0
                    if i==8:
                        self.extraMirilla(func.instr[0 + aux: tam + aux])
                    # pasada completa
                    while (tam + aux) <= len(func.instr):
                        opt = opt or self.Regla1(func.instr[0 + aux: tam + aux])
                        opt = opt or self.Regla2(func.instr[0 + aux: tam + aux])
                        opt = opt or self.Regla3(func.instr[0 + aux: tam + aux])
                        opt = opt or self.Regla4(func.instr[0 + aux: tam + aux])
                        opt = opt or self.Regla5(func.instr[0 + aux: tam + aux])
                        opt = opt or self.Regla6(func.instr[0 + aux: tam + aux])
                        opt = opt or self.Regla7(func.instr[0 + aux: tam + aux])
                        opt = opt or self.Regla8(func.instr[0 + aux: tam + aux])
                        aux = aux + 1        
                # Si no hubo optimizacion en la pasada, subir el tamaño
                if not opt:
                    tam = tam + 20
                    if len(func.instr)<tam and yaentro==False:
                        ls =tam-len(func.instr)
                        tam=tam-ls 
                        yaentro=True
                      
    def extraMirilla(self,array):
        # puntero actual
        i=0
        while i<len(array):
            actual = array[i]
            if isinstance(actual, Label) and not actual.deleted:
                label=actual.id
                bandera=False
                x=0
                while x<len(array):
                    gotoo=array[x]
                    if isinstance(gotoo, Goto) and not gotoo.deleted:
                        if (gotoo.etiqueta==label):
                            bandera=True
                    elif isinstance(gotoo, If) and not gotoo.deleted:
                        if (gotoo.etiqueta==label):
                            bandera=True
                    x=x+1
                if bandera==False:
                    self.reporteMirilla('Regla Extra', f'{actual.getCode()}', '//Expresion eliminada para evitar errores de Goto y Labels', actual.fila)
                    actual.deleted=True
            i=i+1

    def Regla1(self, array):
        opt = False

        # puntero actual
        i=0
        while i<len(array):
            actual = array[i]
            if isinstance(actual, Asignacion) and not actual.deleted:
                if isinstance(actual.exp, Variable):
                    x=i+1
                    while x<len(array):
                        siguiente=array[x]
                        if isinstance(siguiente, Asignacion) and not siguiente.deleted:
                            if isinstance(siguiente.exp, Variable):
                                if siguiente.place.getCode()==actual.exp.getCode() and siguiente.exp.getCode()==actual.place.getCode():
                                    bandera=False
                                    y=i+1
                                    while y<x:
                                        instr=array[y]
                                        if isinstance(instr, Asignacion) and not instr.deleted:
                                            if instr.place.getCode()==actual.place.getCode():
                                                bandera=True
                                        y=y+1
                                    
                                    if bandera==False:
                                        opt = True
                                        self.reporteMirilla('Regla 1',f'{actual.getCode()}\n{siguiente.getCode()}',f'{actual.getCode()}', siguiente.fila)
                                        siguiente.deleted = True
                                        break
                        x=x+1
            i=i+1
        return opt 
                                
    def Regla2(self, array):
        opt = False
        # puntero actual
        i=0
        while i<len(array):
            actual = array[i]
            if isinstance(actual, Goto) and not actual.deleted:
                lbl1=actual.etiqueta
                x=i+1
                while x<len(array):
                    siguiente=array[x]
                    if not isinstance(siguiente, Label) and not siguiente.deleted:
                        self.reporteMirilla('Regla 2',f'{actual.getCode()}\n{siguiente.getCode()}',lbl1, siguiente.fila)
                        siguiente.deleted = True
                        opt =True
                    elif isinstance(siguiente, Label) and not siguiente.deleted:
                        lbl2=siguiente.id
                        if lbl1 == lbl2:
                            self.reporteMirilla('Regla 2',f'{actual.getCode()}',lbl1, siguiente.fila)
                            actual.deleted=True
                            opt =True 
                        break
                    x=x+1
            i=i+1
        return opt 
                                
    def Regla3(self, array):
        opt = False
        # Recorrer el arreglo de instrucciones C3D
        for i in range(len(array)):
            actual = array[i]
            # Si la instruccion es un If
            if isinstance(actual, If) and not actual.deleted:
                if i<len(array)-2:
                    siguiente = array[i+1]
                    lbl=array[i+2]
                    # Si el siguiente es un Goto
                    if isinstance(siguiente, Goto) and not siguiente.deleted:
                        if isinstance(lbl, Label) and not lbl.deleted:
                            if lbl.id==actual.etiqueta:
                                original = f'{actual.getCode()}\n{siguiente.getCode()}'
                                actual.condicion.signoContrario() # agarra signo contrario
                                actual.etiqueta = siguiente.etiqueta # cambia la etiqueta del if
                                siguiente.deleted = True # elimina goto de la etiqueta del else
                                self.reporteMirilla('Regla 3', original,f'{actual.getCode()}', actual.fila)
                                lbl.deleted = True # elimina la etiqueta del if anterior
                                opt = True  
        return opt 
    
    def Regla4(self,array):
        opt = False

        # puntero actual
        i=0
        while i<len(array):
            actual = array[i]
            if isinstance(actual, Goto) and not actual.deleted:
                lbl1=actual.etiqueta
                x=i+1
                while x<len(array):
                    siguiente=array[x]
                    if isinstance(siguiente, Label) and not siguiente.deleted:
                        lbl2=siguiente.id
                        if lbl1 == lbl2:
                            if x<len(array)-1:
                                goto1=array[x+1]
                                if isinstance(goto1, Goto) and not goto1.deleted:
                                    original = f'{actual.etiqueta}'
                                    actual.etiqueta=goto1.etiqueta
                                    self.reporteMirilla('Regla 4', original,f'{actual.getCode()}', actual.fila)
                                    siguiente.deleted=True
                                    goto1.deleted=True
                                    opt =True  
                                    break
                    x=x+1
            i=i+1
        return opt 
    
    def Regla5(self, array):
        opt = False
        # puntero actual
        i=0
        while i<len(array):
            actual = array[i]
            if isinstance(actual, If) and not actual.deleted:
                lbl1=actual.etiqueta
                x=i+1
                while x<len(array):
                    lbl2=array[x]
                    if isinstance(lbl2, Label) and not lbl2.deleted:
                        id_etiqueta=lbl2.id
                        if lbl1==id_etiqueta:
                            if x<len(array)-1:
                                goto1=array[x+1]
                                if isinstance(goto1, Goto) and not goto1.deleted:
                                    hay_instr=False
                                    y=i+1
                                    while y<x:
                                        hay_instr=True
                                        y=y+1
                                    if hay_instr:
                                        original = actual.getCode()
                                        actual.etiqueta=goto1.etiqueta
                                        self.reporteMirilla('Regla 5', original,f'{actual.getCode()}', actual.fila)
                                        opt =True  
                                        break
                    x=x+1
            i=i+1

        return opt 

    def Regla6(self, array):
        opt = False
        # Recorrer el arreglo de instrucciones C3D
        for i in range(len(array)):
            actual = array[i]
            if isinstance(actual, Asignacion) and not actual.deleted:
                if(actual.selfAsignacion()): # Si se esta asignando a si mismo en alguna posicion de exp
                    if actual.exp.Redu6():# verrificar +0 -0 *1 /1
                        opt = True
                        self.reporteMirilla('Regla 6',f'{actual.getCode()}','//Se ha eliminado', actual.fila)
                        actual.deleted = True
        return opt 
    
    def Regla7(self, array):
        opt = False
        # Recorrer el arreglo de instrucciones C3D
        for i in range(len(array)):
            actual = array[i]
            if isinstance(actual, Asignacion) and not actual.deleted:
                if(not actual.selfAsignacion()): # Si no esta asignando a si mismo en alguna posicion de exp
                    if not isinstance(actual.exp, Variable) and not isinstance(actual.exp, Acceso) and not actual.deleted:
                        original = actual.getCode()
                        if actual.exp.Redu7():# Si si cambio la expresion
                            self.reporteMirilla('Regla 7',original,f'{actual.getCode()}', actual.fila)
                            opt = True
        return opt 

    def Regla8(self, array):
        opt = False
        # Recorrer el arreglo de instrucciones C3D
        for i in range(len(array)):
            actual = array[i]
            if isinstance(actual, Asignacion) and not actual.deleted:
                if isinstance(actual.exp, Expresion):
                    original = actual.getCode()
                    if actual.exp.Redu8():# Si si cambio la expresion
                        self.reporteMirilla('Regla 8',original,f'{actual.getCode()}', actual.fila)
                        opt = True
        return opt 