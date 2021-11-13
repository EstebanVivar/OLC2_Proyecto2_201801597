from backend.Project.TablaSimbolos.TablaSimbolos import TablaSimbolos


from .TablaSimbolos import TablaSimbolos

class Generator:
    generator = None

    def __init__(self):

        self.contadorTemporal = 0
        self.contadorEtiqueta = 0

        self.C3D = ''
        self.funciones = ''
        self.nativas = ''
        self.dentroFuncion = False
        self.dentroNativa = False
        self.tempsRecover = {}
        self.temporales = []

        self.printString = False
        self.potencia = False
        self.upper = False        
        self.lower = False               
        self.length = False
        self.potS=False
        self.concatenarS=False
        self.math=False

    def cleanAll(self):

        self.contadorTemporal = 0
        self.contadorEtiqueta = 0

        self.C3D = ''
        self.funciones = ''
        self.nativas = ''
        self.dentroFuncion = False
        self.dentroNativa = False
        self.tempsRecover = {}
        self.temporales = []

        self.printString = False
        Generator.generator = Generator()

    #############
    # CODE
    #############
    def Header(self):
        if self.math:
            header = 'package main;\n\nimport (\n\t"fmt"\n\t"math"\n)\n\n'
        else:
            header = 'package main;\n\nimport (\n\t"fmt"\n)\n\n'
        if len(self.temporales) > 0:
            header += 'var '
            for temporal in range(len(self.temporales)):
                header += self.temporales[temporal]
                if temporal != (len(self.temporales) - 1):
                    header += ", "
            header += " float64\n"
        header += "var P, H float64;\nvar stack[3000000]float64;\nvar heap [3000000]float64;\n\n"
        return header

    def CodigoC3D(self):
        return f'{self.Header()}{self.nativas}\n{self.funciones}\nfunc main(){{\n{self.C3D}\n}}'


    def codigoInterno(self, codigo, tab="\t"):
        if(self.dentroNativa):
            if(self.nativas == ''):
                self.nativas = self.nativas 
            self.nativas = self.nativas + tab + codigo
        elif(self.dentroFuncion):
            if(self.funciones == ''):
                self.funciones = self.funciones 
            self.funciones = self.funciones + tab + codigo
        else:
            self.C3D = self.C3D + '\t' + codigo

    def agregarComentario(self, comment):
        pass
        # self.codigoInterno(f'/* {comment} */\n')

    def getInstance(self):
        if Generator.generator == None:
            Generator.generator = Generator()
        return Generator.generator

    def agregarSaltoLinea(self):
        self.codigoInterno("\n")

    ########################
    # Manejo de Temporales
    ########################
    def agregarTemporal(self):
        temporal = f't{self.contadorTemporal}'
        self.contadorTemporal += 1
        self.temporales.append(temporal)
        self.tempsRecover[temporal] = temporal
        return temporal

    def limpiarTemporales(self):
        self.tempsRecover = {}

    def freeTemp(self, temp):
        if(temp in self.tempsRecover):
            self.tempsRecover.pop(temp, None)

    def guardarTemporales(self, entorno):
        tamano = 0
        if len(self.tempsRecover) > 0:
            temp = self.agregarTemporal()
            self.freeTemp(temp)

            self.agregarComentario('Guardado de temporales')
            self.agregarExpresion(temp, 'P', '+', entorno.tamano)
            for valor in self.tempsRecover:
                tamano += 1
                self.setStack(temp, valor, False)
                if tamano != len(self.tempsRecover):
                    self.agregarExpresion(temp, temp, '+', '1')
            self.agregarComentario('Fin Guardado de temporales')
        ptr = entorno.tamano
        entorno.tamano = ptr + tamano
        return ptr

    def recoverTemps(self, entorno, pos):
        if len(self.tempsRecover) > 0:
            temp = self.agregarTemporal()
            self.freeTemp(temp)

            tamano = 0

            self.agregarComentario('Recuperacion de temporales')
            self.agregarExpresion(temp, 'P', '+', pos)
            for value in self.tempsRecover:
                tamano += 1
                self.getStack(value, temp)
                if tamano != len(self.tempsRecover):
                    self.agregarExpresion(temp, temp, '+', '1')
            entorno.tamano = pos
            self.agregarComentario('Fin Recuperacion de temporales')
    #####################
    # Manejo de Etiquetas
    #####################
    def nuevaEtiqueta(self):
        etiqueta = f'L{self.contadorEtiqueta}'
        self.contadorEtiqueta += 1
        return etiqueta

    def agregarEtiqueta(self, etiqueta):
        self.codigoInterno(f'{etiqueta}:\n')

    ###################
    # GOTO
    ###################
    def agregarGoto(self, etiqueta):
        self.codigoInterno(f'goto {etiqueta};\n')

    ###################
    # IF
    ###################
    def agregarIf(self, opIzq, opDer, operador, etiqueta):
        self.freeTemp(opIzq)
        self.freeTemp(opDer)
        self.codigoInterno(
            f'if {opIzq} {operador} {opDer} {{goto {etiqueta};}}\n')

    ###################
    # EXPRESIONES
    ###################
    def agregarExpresion(self, resultado, opIzq, operador,opDer):
        self.freeTemp(opIzq)
        self.freeTemp(opDer)
        self.codigoInterno(f'{resultado}={opIzq}{operador}{opDer};\n')

    ###################
    # FUNCIONES
    ###################
    def agregarInicioFuncion(self, identificador):
        if(not self.dentroNativa):
            self.dentroFuncion = True
        self.codigoInterno(f'func {identificador}(){{\n', '')

    def agregarFinFuncion(self):
        self.codigoInterno('return;\n}\n')
        if(not self.dentroNativa):
            self.dentroFuncion = False

    ###############
    # STACK
    ###############
    def setStack(self, posicion, valor,FreeValue = True):
        self.freeTemp(posicion)
        if FreeValue:
            self.freeTemp(valor)
        self.codigoInterno(f'stack[int({posicion})]={valor};\n')

    def getStack(self, temporal, posicion):
        self.freeTemp(posicion)
        self.codigoInterno(f'{temporal}=stack[int({posicion})];\n')

    #############
    # ENVS
    #############
    def cambioEntorno(self, tamano):
        self.codigoInterno(f'P=P+{tamano};\n')

    def llamadaFuncion(self, identificador):
        self.codigoInterno(f'{identificador}();\n')

    def regresoEntorno(self, tamano):
        self.codigoInterno(f'P=P-{tamano};\n')

    ###############
    # HEAP
    ###############
    def setHeap(self, posicion, valor):
        self.freeTemp(posicion)
        self.freeTemp(valor)
        self.codigoInterno(f'heap[int({posicion})]={valor};\n')

    def getHeap(self, temporal, posicion):
        self.freeTemp(posicion)
        self.codigoInterno(f'{temporal}=heap[int({posicion})];\n')

    def nextHeap(self):
        self.codigoInterno('H=H+1;\n')

    # INSTRUCCIONES
    def agregarImprimir(self, tipo, valor):
        if tipo =="f":
            self.codigoInterno(f'fmt.Printf("%{tipo}", {valor});\n')
        else:
            self.codigoInterno(f'fmt.Printf("%{tipo}", int({valor}));\n')

    def printTrue(self):
        self.agregarImprimir("c", 116)
        self.agregarImprimir("c", 114)
        self.agregarImprimir("c", 117)
        self.agregarImprimir("c", 101)

    def printFalse(self):
        self.agregarImprimir("c", 102)
        self.agregarImprimir("c", 97)
        self.agregarImprimir("c", 108)
        self.agregarImprimir("c", 115)
        self.agregarImprimir("c", 101)

    ##############
    # NATIVAS
    ##############
    def fPrintString(self):
        if(self.printString):
            return
        self.printString = True
        self.dentroNativa = True

        self.agregarInicioFuncion('printString')
        # Label para salir de la funcion
        etiquetaRetorno = self.nuevaEtiqueta()
        # Label para la comparacion para buscar fin de cadena
        etiquetaComparacion = self.nuevaEtiqueta()

        # Temporal puntero a Stack
        tempSP = self.agregarTemporal()

        # Temporal puntero a Heap
        tempHP = self.agregarTemporal()

        self.agregarExpresion(tempSP, 'P', '+', '1')

        self.getStack(tempHP, tempSP)

        # Temporal para comparar
        tempCompara = self.agregarTemporal()

        self.agregarEtiqueta(etiquetaComparacion)

        self.getHeap(tempCompara, tempHP)

        self.agregarIf(tempCompara, '-1', '==', etiquetaRetorno)

        self.agregarImprimir('c', tempCompara)

        self.agregarExpresion(tempHP, tempHP,  '+','1')

        self.agregarGoto(etiquetaComparacion)

        self.agregarEtiqueta(etiquetaRetorno)
        self.agregarFinFuncion()
        self.dentroNativa = False
        self.freeTemp(tempSP)
        self.freeTemp(tempHP)
        self.freeTemp(tempCompara)

    def fPotencia(self):
        
        if(self.potencia):
            return
        self.potencia = True
        self.dentroNativa = True
        self.agregarInicioFuncion('Potencia')
        
        t0 = self.agregarTemporal()
        self.agregarExpresion(t0, 'P', '+', '1')

        t1 = self.agregarTemporal()
        self.getStack(t1, t0)

        self.agregarExpresion(t0, t0, '+', '1')

        t2 = self.agregarTemporal()
        self.getStack(t2, t0)
        self.agregarExpresion(t0, t1, '', '')

        L0 = self.nuevaEtiqueta()
        L1 = self.nuevaEtiqueta()

        self.agregarEtiqueta(L0)
        self.agregarIf(t2, '1', '<=', L1)
        self.agregarExpresion(t1, t1, '*',t0 )
        self.agregarExpresion(t2, t2, '-','1')
        self.agregarGoto(L0)
        self.agregarEtiqueta(L1)
        self.setStack('P', t1)
        
        self.agregarFinFuncion()
        self.dentroNativa = False
        self.freeTemp(t0)
        self.freeTemp(t1)
        self.freeTemp(t2)

    
    def fUpper(self):
        if(self.upper):
            return
        self.upper = True
        self.dentroNativa = True

        self.agregarInicioFuncion('upper')
        # Label para salir de la funcion
        etiquetaRetorno = self.nuevaEtiqueta()
        # Label para la comparacion para buscar fin de cadena
        etiquetaComparacion = self.nuevaEtiqueta()
        # Label para la comparacion para buscar fin de cadena   
        etiquetaIgnorar = self.nuevaEtiqueta()
        # Temporal puntero a Stack
        t1 = self.agregarTemporal()

        # Temporal puntero a Heap
        t2 = self.agregarTemporal()
        
        t3 = self.agregarTemporal()
        
        t4= self.agregarTemporal()

        self.agregarExpresion(t1, 'H', '', '')
        
        self.agregarExpresion(t2, 'P', '+', '1')
        self.getStack(t3, t2)

        # Temporal para comparar
        
        self.agregarEtiqueta(etiquetaComparacion)

        self.getHeap(t4, t3)

        self.agregarIf(t4, '-1', '==', etiquetaRetorno)
        self.agregarIf(t4, '97', '<', etiquetaIgnorar)
        self.agregarIf(t4, '122', '>', etiquetaIgnorar)
        self.agregarExpresion(t4, t4,  '-','32')
        
        self.agregarEtiqueta(etiquetaIgnorar)
        self.setHeap('H', t4)        
        self.agregarExpresion('H', 'H', '+', '1')        
        self.agregarExpresion(t3, t3, '+', '1')
        self.setStack('P',t1)
        self.agregarGoto(etiquetaComparacion)

        self.agregarEtiqueta(etiquetaRetorno)
        self.setHeap('H',-1)        
        self.agregarExpresion('H', 'H', '+', '1')            
        self.setStack('P',t1)
        self.agregarFinFuncion()
        self.dentroNativa = False
        self.freeTemp(t1)
        self.freeTemp(t2)
        self.freeTemp(t3)        
        self.freeTemp(t4)
        

    def fLower(self):
        if(self.lower):
            return
        self.lower = True
        self.dentroNativa = True

        self.agregarInicioFuncion('lower')
        etiquetaRetorno = self.nuevaEtiqueta()
        etiquetaComparacion = self.nuevaEtiqueta()
        etiquetaIgnorar = self.nuevaEtiqueta()
        t1 = self.agregarTemporal()
        t2 = self.agregarTemporal()        
        t3 = self.agregarTemporal()        
        t4= self.agregarTemporal()
        self.agregarExpresion(t1, 'H', '', '')        
        self.agregarExpresion(t2, 'P', '+', '1')
        self.getStack(t3, t2)        
        self.agregarEtiqueta(etiquetaComparacion)
        self.getHeap(t4, t3)
        self.agregarIf(t4, '-1', '==', etiquetaRetorno)
        self.agregarIf(t4, '65', '<', etiquetaIgnorar)
        self.agregarIf(t4, '90', '>', etiquetaIgnorar)
        self.agregarExpresion(t4, t4,  '+','32')        
        self.agregarEtiqueta(etiquetaIgnorar)
        self.setHeap('H', t4)        
        self.agregarExpresion('H', 'H', '+', '1')        
        self.agregarExpresion(t3, t3, '+', '1')
        self.setStack('P',t1)
        self.agregarGoto(etiquetaComparacion)
        self.agregarEtiqueta(etiquetaRetorno)
        self.setHeap('H',-1)        
        self.agregarExpresion('H', 'H', '+', '1')            
        self.setStack('P',t1)
        self.agregarFinFuncion()
        self.dentroNativa = False
        self.freeTemp(t1)
        self.freeTemp(t2)
        self.freeTemp(t3)        
        self.freeTemp(t4)

    def fLength(self):
        if(self.lower):
            return
        self.length = True
        self.dentroNativa = True

        self.agregarInicioFuncion('length')
        etiquetaRetorno = self.nuevaEtiqueta()        
        
        t1 = self.agregarTemporal()

        self.agregarExpresion(t1, 'P', '+', '1')
        self.getStack(t1, t1)        
        self.getHeap(t1, t1)
        self.agregarGoto(etiquetaRetorno)
        
        self.agregarEtiqueta(etiquetaRetorno)
        
        self.setStack('P',t1)
        self.agregarFinFuncion()
        self.dentroNativa = False
        self.freeTemp(t1)
    
    def potenciaS(self):
        if self.potS:
            return
        self.potS=True
        self.dentroNativa=True
        self.agregarInicioFuncion("potenciaS")
        inicio=self.agregarTemporal()
        self.agregarExpresion(inicio,'H','','')
        numero=self.agregarTemporal()
        self.agregarExpresion(numero,'P','+','2')
        obtNum=self.agregarTemporal()
        self.getStack(obtNum,numero)
        self.agregarExpresion(obtNum,obtNum,'+','1')
        cadena=self.agregarTemporal()
        self.agregarExpresion(cadena,'P','+','1')
        obtS=self.agregarTemporal()
        repetir=self.nuevaEtiqueta()
        self.agregarEtiqueta(repetir)
        self.getStack(obtS,cadena)
        self.agregarExpresion(obtNum,obtNum,'-','1')
        salir=self.nuevaEtiqueta()
        self.agregarIf(obtNum,'0','<=',salir)
        repetir2=self.nuevaEtiqueta()
        self.agregarEtiqueta(repetir2)
        caracter=self.agregarTemporal()
        self.getHeap(caracter,obtS)
        self.agregarIf(caracter,'-1','==',repetir)
        self.setHeap('H',caracter)
        self.nextHeap()
        self.agregarExpresion(obtS,obtS,'+','1')
        self.agregarGoto(repetir2)
        self.agregarEtiqueta(salir)
        self.setHeap('H','-1')
        self.nextHeap()
        self.setStack('P',inicio)
        self.agregarFinFuncion()
        self.dentroNativa=False
        self.freeTemp(inicio)
        self.freeTemp(numero)
        self.freeTemp(obtNum)
        self.freeTemp(cadena)
        self.freeTemp(obtS)
        self.freeTemp(caracter)

    def concatenar(self):
        if(self.concatenarS):
            return
        self.concatenarS = True
        self.dentroNativa = True
        self.agregarInicioFuncion('concatenar')
        inicio=self.agregarTemporal()
        self.agregarExpresion(inicio,'H','','')
        primero=self.agregarTemporal()
        self.agregarExpresion(primero,'P','+','1')
        segundo=self.agregarTemporal()
        obtP=self.agregarTemporal()
        self.getStack(obtP,primero)
        self.agregarExpresion(segundo,'P','+','2')
        conP=self.nuevaEtiqueta()
        self.agregarEtiqueta(conP)
        obtPH=self.agregarTemporal()
        self.getHeap(obtPH,obtP)
        compareLbl1=self.nuevaEtiqueta()
        self.agregarIf(obtPH,'-1',"==",compareLbl1)
        self.setHeap('H',obtPH)
        self.nextHeap()
        self.agregarExpresion(obtP,obtP,'+','1')
        self.agregarGoto(conP)
        self.agregarEtiqueta(compareLbl1)
        self.getStack(obtP,segundo)
        conS=self.nuevaEtiqueta()
        self.agregarEtiqueta(conS)
        self.getHeap(obtPH,obtP)
        salir=self.nuevaEtiqueta()
        self.agregarIf(obtPH,'-1','==',salir)
        self.setHeap('H',obtPH)
        self.nextHeap()
        self.agregarExpresion(obtP,obtP,'+','1')
        self.agregarGoto(conS)
        self.agregarEtiqueta(salir)
        self.setHeap('H','-1')
        self.nextHeap()
        self.setStack('P',inicio)
        self.agregarFinFuncion()
        self.dentroNativa = False
        self.freeTemp(inicio)
        self.freeTemp(primero)
        self.freeTemp(segundo)
        self.freeTemp(obtP)
        self.freeTemp(obtPH)