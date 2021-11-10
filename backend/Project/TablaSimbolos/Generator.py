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
        header = '/*----HEADER----*/\npackage main;\n\nimport (\n\t"fmt"\n)\n\n'
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
                self.nativas = self.nativas + '/*-----NATIVAS-----*/\n'
            self.nativas = self.nativas + tab + codigo
        elif(self.dentroFuncion):
            if(self.funciones == ''):
                self.funciones = self.funciones + '/*-----FUNCIONES-----*/\n'
            self.funciones = self.funciones + tab + codigo
        else:
            self.C3D = self.C3D + '\t' + codigo

    def agregarComentario(self, comment):
        self.codigoInterno(f'/* {comment} */\n')

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
