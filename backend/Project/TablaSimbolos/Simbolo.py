from Abstract.Retorno import *

class Simbolo:

    def __init__(self, identificador, tipo, posicion, esGlobal, enHeap,tipoStruct):
        self.identificador = identificador
        self.tipo = tipo
        self.posicion = posicion
        self.esGlobal = esGlobal
        self.enHeap = enHeap
        self.tipoStruct=tipoStruct
        self.valor = None

