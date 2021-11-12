from enum import Enum

class Tipo(Enum):
    
    ENTERO = 1
    FLOTANTE = 2
    BOOLEANO = 3
    CARACTER = 4
    CADENA = 5
    ARREGLO = 6
    STRUCT = 7
    INDEFINIDO = 8
    NULO = 9
    RANGO=10
    NOTHING=11
    RETURN = 30
    CONTINUE = 31
    BREAK = 32

class Retorno:
    def __init__(self, valor, tipo, esTemporal, tipoAuxiliar=""):
        self.valor =valor
        self.tipo=tipo
        self.esTemporal=esTemporal
        self.tipoAuxiliar=tipoAuxiliar
        self.etiquetaTrue=""
        self.etiquetaFalse=""
