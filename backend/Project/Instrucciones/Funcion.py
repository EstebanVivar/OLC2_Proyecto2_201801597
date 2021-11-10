from Abstract.Instruccion import *
from TablaSimbolos.Generator import *
from Abstract.Retorno import Tipo
from Instrucciones.RetornoIns import RetornoIns

class Funcion(Instruccion):
    def __init__(self, identificador, parametros, instrucciones,tipo, fila, columna):
        Instruccion.__init__(self, fila, columna)
        self.identificador = identificador
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.tipo=tipo
    
    def compilar(self, entorno):
        entorno.guardarFuncion(self.identificador, self)
        genAux = Generator()
        generator = genAux.getInstance()
        
        entornoFuncion = TablaSimbolos(entorno)

        etiquetaReturn = generator.nuevaEtiqueta()
        entornoFuncion.returnLbl = etiquetaReturn
        entornoFuncion.tamano = 1

        for parametro in self.parametros:
            entornoFuncion.guardarVariable(parametro.identificador, parametro.tipo, (parametro.tipo == Tipo.CADENA or parametro.tipo == Tipo.STRUCT))
        generator.limpiarTemporales()
        generator.agregarInicioFuncion(self.identificador)

        try:
            for instruccion in self.instrucciones:
                
                instruccion.compilar(entornoFuncion)
        except:
            print(f'Error al compilar instrucciones de {self.identificador}')
        
        generator.agregarGoto(etiquetaReturn)
        
        generator.agregarEtiqueta(etiquetaReturn)
            
        generator.agregarFinFuncion()
        generator.limpiarTemporales()