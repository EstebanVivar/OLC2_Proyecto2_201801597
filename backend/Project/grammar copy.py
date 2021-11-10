
   
from Abstract.NodoReporteArbol import NodoReporteArbol
import os
import re
import sys
import ply.yacc as yacc
import ply.lex as lex

from TablaSimbolos.TablaSimbolos import TablaSimbolos
from TablaSimbolos.Arbol import Arbol
from TablaSimbolos.Tipo import Nativa, OperadorAritmetico, OperadorLogico, OperadorRelacional
from TablaSimbolos.Excepcion import Excepcion

from Instrucciones.Llamada import Llamada
from Instrucciones.Funcion import Funcion
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue

from Instrucciones.AsignacionArray import AsignacionArray
from Instrucciones.While import While
from Instrucciones.If import If
from Instrucciones.For import For
from Instrucciones.Asignacion import Asignacion
from Instrucciones.Struct import Struct
from Instrucciones.Asignacion_Struct import Asignacion_Struct
from Instrucciones.Imprimir import Imprimir

from Expresiones.Identificador import Identificador
from Expresiones.Array import Array
from Expresiones.Logica import Logica
from Expresiones.Rango import Rango
from Expresiones.Relacional import Relacional
from Expresiones.Aritmetica import Aritmetica
from Expresiones.Nativa_Conv import Nativa_Conv
from Expresiones.Nativa_String import Nativa_String
from Expresiones.Nativa_Mate import Nativa_Mate
from Expresiones.Constante import Constante

from Objeto.Primitivo import Primitivo

from Abstract.Objeto import TipoObjeto


sys.setrecursionlimit(10000)


reservadas = {
    'Int64': 'RINT',
    'Float64': 'RFLOAT',
    'String': 'RSTRING',
    'Char': 'RCHAR',
    'Bool': 'RBOOL',
    'println': 'RPRINTLN',
    'print': 'RPRINT',
    'log10': 'RLOG10',
    'log': 'RLOG',
    'for': 'RFOR',
    'in': 'RIN',
    'sin': 'RSIN',
    'cos': 'RCOS',
    'tan': 'RTAN',
    'sqrt': 'RSQRT',
    'parse': 'RNPARSE',
    'trunc': 'RNTRUNC',
    'float': 'RNFLOAT',
    'string': 'RNSTRING',
    'typeof': 'RNTYPEOF',
    'lowercase': 'RLOWER',
    'uppercase': 'RUPPER',
    'struct': 'RSTRUCT',
    'mutable': 'RMUTABLE',
    'if': 'RIF',
    'else': 'RELSE',
    'elseif': 'RELSEIF',
    'while': 'RWHILE',
    'false': 'RFALSE',
    'true': 'RTRUE',
    'break': 'RBREAK',
    'continue': 'RCONTINUE',
    'length': 'RLENGTH',
    'function': 'RFUNC',
    'return': 'RRETURN',
    'end': 'REND',
}

tokens = [
    'PUNTOCOMA',
    'P_IZQ',
    'P_DER',
    'C_IZQ',
    'C_DER',
    'COMA',
    'DOT',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'MODULO',
    'POTENCIA',
    'NEGACION',
    'MENOR',
    'MENORIGUAL',
    'MAYOR',
    'MAYORIGUAL',
    'COMPARACION',
    'DISTINTO',
    'IGUAL',
    'RANGO',
    'TIPO',
    'AND',
    'OR',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'CARACTER',
    'ID'
] + list(reservadas.values())

t_PUNTOCOMA = r';'
t_P_IZQ = r'\('
t_P_DER = r'\)'
t_C_IZQ = r'\['
t_C_DER = r']'
t_COMA = r','
t_DOT = r'\.'
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_MODULO = r'%'
t_POTENCIA = r'\^'
t_NEGACION = r'!'
t_MENOR = r'<'
t_MENORIGUAL = r'<='
t_MAYOR = r'>'
t_MAYORIGUAL = r'>='
t_COMPARACION = r'=='
t_DISTINTO = r'!='
t_IGUAL = r'='
t_RANGO = r':'
t_TIPO = r'::'
t_AND = r'\&\&'
t_OR = r'\|\|'


def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)    
    return t


def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)    
    return t


def t_CADENA(t):
    r'(\".*?\")'
    t.value = t.value
    return t


def t_CARACTER(t):
    r'(\'.?\')'
    t.value = t.value
    return t


def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

def t_COMENTARIO_MULTI(t):
    r'\#\=(.|\n)*?\=\#'
    t.lexer.lineno += t.value.count("\n")

def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1

t_ignore = "\t\r"

def t_NUEVA_LINEA(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    errores.append(Excepcion("Lexico", "Error lexico: " +
                   t.value[0], t.lexer.lineno, ENCONTRAR_COL(input, t)))
    t.lexer.skip(1)


def ENCONTRAR_COL(inp, token):
    LINEA_INICIO = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - LINEA_INICIO) + 1


lexer = lex.lex()

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'MENOR', 'MAYOR', 'MAYORIGUAL',
     'MENORIGUAL', 'DISTINTO', 'COMPARACION'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO'),
    ('right', 'UMENOS'),
    ('left', 'POTENCIA'),
)

def p_INICIO(t):
    'start                      : instrucciones'
    t[0] = t[1]
    


def p_LISTA_INSTRUCCIONES(t):
    'instrucciones              : instrucciones  instruccion PUNTOCOMA'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_INSTRUCCIONES(t):
    'instrucciones              : instruccion PUNTOCOMA'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

# ///////////////////////////////////////INSTRUCCION//////////////////////////////////////////////////


def p_INSTRUCCION(t):
    '''instruccion              : instruccion_imprimir
                                | instruccion_if
                                | instruccion_asignacion 
                                | instruccion_while
                                | instruccion_break
                                | instruccion_return
                                | instruccion_funcion
                                | instruccion_llamada
                                | instruccion_continue
                                | instruccion_for
                                | instruccion_struct
                                | nativas
                                '''
    t[0] = t[1]

def p_error(t):
    errores.append(Excepcion("Sintáctico", "Error Sintáctico:" +
                   str(t.value), t.lexer.lineno, ENCONTRAR_COL(input, t)))

def p_NATIVAS(t):
    '''nativas                  : RLOG10 P_IZQ expresion P_DER
                                | RLOG P_IZQ expresion COMA expresion P_DER 
                                | RSIN P_IZQ expresion P_DER
                                | RCOS P_IZQ expresion P_DER
                                | RTAN P_IZQ expresion P_DER
                                | RSQRT P_IZQ expresion P_DER
                                | RNFLOAT P_IZQ expresion P_DER 
                                | RNSTRING P_IZQ expresion P_DER
                                | RLOWER P_IZQ expresion P_DER
                                | RUPPER P_IZQ expresion P_DER 
                                | RNTYPEOF P_IZQ expresion P_DER 
                                | RNTRUNC P_IZQ expresion P_DER '''
    if t[1] == 'log10':
        t[0] = Nativa_Mate(Nativa.LOG10, t[3], None, t.lineno(
            2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[1] == 'log':
        t[0] = Nativa_Mate(Nativa.LOG, t[3], t[5], t.lineno(
            2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[1] == 'sin':
        t[0] = Nativa_Mate(Nativa.SIN, t[3], None, t.lineno(
            2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[1] == 'cos':
        t[0] = Nativa_Mate(Nativa.COS, t[3], None, t.lineno(
            2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[1] == 'tan':
        t[0] = Nativa_Mate(Nativa.TAN, t[3], None, t.lineno(
            2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[1] == 'sqrt':
        t[0] = Nativa_Mate(Nativa.SQRT, t[3], None, t.lineno(
            2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[1] == 'float':
        t[0] = Nativa_Conv(Nativa.FLOAT, t[3], None, t.lineno(
            2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[1] == 'string':
        t[0] = Nativa_Conv(Nativa.STRING, t[3], None, t.lineno(
            2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[1] == 'typeof':
        t[0] = Nativa_Conv(Nativa.TYPEOF, t[3], None, t.lineno(
            2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[1] == 'uppercase':
        t[0] = Nativa_Conv(Nativa.UPPER, t[3], None, t.lineno(
            2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[1] == 'lowercase':
        t[0] = Nativa_Conv(Nativa.LOWER, t[3], None, t.lineno(
            2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[1] == 'trunc':
        t[0] = Nativa_Conv(Nativa.TRUNC, t[3], None, t.lineno(
            2), ENCONTRAR_COL(input, t.slice[2]))
            

def p_INSTRUCCION_PARSE(t):
    'nativas                    : RNPARSE P_IZQ tipo_dato COMA expresion P_DER'
    if t[1] == 'parse':
        t[0] = Nativa_String(Nativa.PARSE, t[5], t[3], t.lineno(
            2), ENCONTRAR_COL(input, t.slice[2]))


def p_IMPRIMIR_SALTO(t):
    'instruccion_imprimir       : RPRINTLN P_IZQ parametros_print P_DER'
    t[0] = Imprimir(t[3], t.lineno(1), ENCONTRAR_COL(input, t.slice[1]))


def p_IMPRIMIR(t):
    'instruccion_imprimir       : RPRINT P_IZQ parametros_print P_DER'
    t[0] = Imprimir(t[3], t.lineno(1), ENCONTRAR_COL(input, t.slice[1]))


def p_LISTA_PARAMETROS_PRINT(t):
    'parametros_print           : parametros_print COMA parametro_print'
    t[1].append(t[3])
    t[0] = t[1]


def p_PARAMETROS_PRINT(t):
    'parametros_print           : parametro_print'
    t[0] = [t[1]]


def p_PARAMETRO_PRINT(t):
    'parametro_print            : expresion'
    t[0] = t[1]



def p_INSTRUCCION_FOR(t):
    'instruccion_for       : RFOR ID RIN rango instrucciones REND'
    t[0] = For(t[2], t[4], t[5], t.lineno(1), ENCONTRAR_COL(input, t.slice[2]))


def p_RANGO(t):
    '''rango                    : expresion RANGO expresion                                
                                '''
    t[0] = Rango(t[1], t[3], t.lineno(1), ENCONTRAR_COL(input, t.slice[2]))


def p_RANGO_CADENA(t):
    'rango                      : expresion'
    t[0] = Rango(t[1], None, t.lineno(1),  t[1].fila)


def p_ASIGNACION(t):
    'instruccion_asignacion     : ID IGUAL expresion'
    t[0] = Asignacion(t[1], t[3], None, t.lineno(1),
                      ENCONTRAR_COL(input, t.slice[1]))


def p_ASIGNACION_TIPO(t):
    'instruccion_asignacion     : ID IGUAL expresion TIPO tipo_dato'
    t[0] = Asignacion(t[1], t[3], t[5], t.lineno(1),
                      ENCONTRAR_COL(input, t.slice[1]))


def p_ASIGNACION_STRUCT(t):
    'instruccion_asignacion     : ID DOT ID IGUAL   expresion'
    t[0] = Asignacion_Struct(t[1], t[3], t[5], t.lineno(
        1), ENCONTRAR_COL(input, t.slice[2]))


def p_TIPO_DATO(t):
    '''tipo_dato                : RINT
                                | RFLOAT
                                | RSTRING
                                | RCHAR
                                | RBOOL
                                '''
    if t[1] == "Int64":
        t[0] = TipoObjeto.ENTERO
    elif t[1] == "Float64":
        t[0] = TipoObjeto.DECIMAL
    elif t[1] == "String":
        t[0] = TipoObjeto.CADENA
    elif t[1] == "Char":
        t[0] = TipoObjeto.CARACTER
    elif t[1] == "Bool":
        t[0] = TipoObjeto.BOOLEANO

def p_CUERPO_IF(t):
    'instruccion_if             : RIF cuerpo_if'
    t[0] = t[2]


def p_IF_SIMPLE(t):
    'cuerpo_if                  : expresion  instrucciones REND'
    t[0] = If(t[1], t[2], None, None, t.lineno(
        1), ENCONTRAR_COL(input, t.slice[3]))


def p_IF_ELSE(t):
    'cuerpo_if                  : expresion instrucciones RELSE  instrucciones REND'
    t[0] = If(t[1], t[2], t[4], None, t.lineno(
        1), ENCONTRAR_COL(input, t.slice[3]))


def p_ELSEIF(t):
    'cuerpo_if                  : expresion instrucciones RELSEIF  cuerpo_if'
    t[0] = If(t[1], t[2], None, t[4], t.lineno(
        1), ENCONTRAR_COL(input, t.slice[3]))


def p_WHILE(t):
    'instruccion_while          : RWHILE expresion  instrucciones REND'
    t[0] = While(t[2], t[3], t.lineno(1), ENCONTRAR_COL(input, t.slice[1]))


def p_BREAK(t):
    'instruccion_break          : RBREAK'
    t[0] = Break(t.lineno(1), ENCONTRAR_COL(input, t.slice[1]))

def p_CONTINUE(t):
    'instruccion_continue          : RCONTINUE'
    t[0] = Continue(t.lineno(1), ENCONTRAR_COL(input, t.slice[1]))


def p_FUNCION_SIMPLE(t):
    'instruccion_funcion        : RFUNC ID P_IZQ parametros P_DER instrucciones REND'
    t[0] = Funcion(t[2], t[4], t[6], t.lineno(1),
                   ENCONTRAR_COL(input, t.slice[1]))


def p_FUNCION_PARAMETROS(t):
    'instruccion_funcion        : RFUNC ID P_IZQ P_DER instrucciones REND'
    t[0] = Funcion(t[2], [], t[5], t.lineno(1), ENCONTRAR_COL(input, t.slice[1]))

# ///////////////////////////////////////paramETROS//////////////////////////////////////////////////


def p_LISTA_PARAMETROS_FUNCION(t):
    'parametros                 : parametros COMA parametro'
    t[1].append(t[3])
    t[0] = t[1]


def p_PARAMETROS_FUNCION(t):
    'parametros                 : parametro'
    t[0] = [t[1]]


def p_LISTA_PARAMETROS_STRUCT(t):
    'datos_struct                 : datos_struct  parametro PUNTOCOMA'
    t[1].append(t[2])
    t[0] = t[1]


def p_PARAMETROS_STRUCT(t):
    'datos_struct                 : parametro PUNTOCOMA'
    t[0] = [t[1]]


def p_PARAMETRO_TIPO(t):
    'parametro                  : ID TIPO tipo_dato'
    t[0] = {'identificador': t[1], 'tipo': t[3]}


def p_PARAMETRO(t):
    'parametro                  : ID TIPO tipo_dato ID'
    t[0] = {'identificador': t[1]}


def p_STRUCT(t):
    'instruccion_struct      : RSTRUCT ID datos_struct REND'
    t[0] = Struct(t[2], t[3], False, t.lineno(1),
                  ENCONTRAR_COL(input, t.slice[1]))


def p_MUTABLE_STRUCT(t):
    'instruccion_struct      : RMUTABLE RSTRUCT ID datos_struct REND'
    t[0] = Struct(t[3], t[4], True, t.lineno(1),
                  ENCONTRAR_COL(input, t.slice[1]))


def p_ACCESO_STRUCT(t):
    'expresionStruct            : ID DOT ID'
    t[0] = Struct(t[1], t[3], t.lineno(
        2), ENCONTRAR_COL(input, t.slice[1]))

# ///////////#Incluye STRUCT//////////////////////////


def p_LLAMADA(t):
    'instruccion_llamada        : ID P_IZQ P_DER'
    t[0] = Llamada(t[1], [], t.lineno(1), ENCONTRAR_COL(input, t.slice[3]))


def p_LLAMADA_PARAMETROS(t):
    'instruccion_llamada        : ID P_IZQ parametros_llamada P_DER'
    t[0] = Llamada(t[1], t[3], t.lineno(1), ENCONTRAR_COL(input, t.slice[1]))


def p_LISTA_PARAMETROS_LLAMADA(t):
    'parametros_llamada         : parametros_llamada COMA parametro_llamada'
    t[1].append(t[3])
    t[0] = t[1]


def p_PARAMETROS_LLAMADA(t):
    'parametros_llamada         : parametro_llamada'
    t[0] = [t[1]]


def p_PARAMETRO_LLAMADA(t):
    'parametro_llamada          : expresion'
    t[0] = t[1]

# ///////////////////////////////////////LLAMADA A FUNCION//////////////////////////////////////////////////


def p_RETURN(t):
    'instruccion_return         : RRETURN expresion'
    t[0] = If(t[2], t.lineno(1), ENCONTRAR_COL(input, t.slice[1]))

# ///////////////////////////////////////EXPRESION//////////////////////////////////////////////////


def p_EXPRESION_BINARIA(t):
    '''
    expresion                   : expresion MAS expresion
                                | expresion MENOS expresion
                                | expresion POR expresion
                                | expresion DIVIDIDO expresion
                                | expresion MODULO expresion
                                | expresion POTENCIA expresion
                                | expresion MENOR expresion
                                | expresion MENORIGUAL expresion
                                | expresion MAYOR expresion
                                | expresion MAYORIGUAL expresion
                                | expresion COMPARACION expresion
                                | expresion DISTINTO expresion
                                | expresion AND expresion
                                | expresion OR expresion
    '''
    if t[2] == '+':
        t[0] = Aritmetica(OperadorAritmetico.MAS, t[1], t[3],
                          t.lineno(2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[2] == '-':
        t[0] = Aritmetica(OperadorAritmetico.MENOS, t[1], t[3],
                          t.lineno(2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[2] == '*':
        t[0] = Aritmetica(OperadorAritmetico.POR, t[1], t[3],
                          t.lineno(2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[2] == '%':
        t[0] = Aritmetica(OperadorAritmetico.MOD, t[1], t[3],
                          t.lineno(2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[2] == '^':
        t[0] = Aritmetica(OperadorAritmetico.POT, t[1], t[3],
                          t.lineno(2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[2] == '>':
        t[0] = Relacional(OperadorRelacional.MAYOR, t[1], t[3],
                          t.lineno(2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[2] == '<':
        t[0] = Relacional(OperadorRelacional.MENOR, t[1], t[3],
                          t.lineno(2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[2] == '>=':
        t[0] = Relacional(OperadorRelacional.MAYORIGUAL, t[1],
                          t[3], t.lineno(2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[2] == '<=':
        t[0] = Relacional(OperadorRelacional.MENORIGUAL, t[1],
                          t[3], t.lineno(2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[2] == '==':
        t[0] = Relacional(OperadorRelacional.COMPARACION, t[1],
                          t[3], t.lineno(2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[2] == '!=':
        t[0] = Relacional(OperadorRelacional.DIFERENTE, t[1],
                          t[3], t.lineno(2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[2] == '&&':
        t[0] = Logica(OperadorLogico.AND, t[1], t[3],
                      t.lineno(2), ENCONTRAR_COL(input, t.slice[2]))
    elif t[2] == '||':
        t[0] = Logica(OperadorLogico.OR, t[1], t[3], t.lineno(2),
                      ENCONTRAR_COL(input, t.slice[2]))
    else:
        t[0] = Aritmetica(OperadorAritmetico.DIV, t[1], t[3],
                          t.lineno(2), ENCONTRAR_COL(input, t.slice[2]))


def p_EXPRESION_MENOS(t):
    '''expresion                : MENOS expresion %prec UMENOS'''
    t[0] = Aritmetica(OperadorAritmetico.NEG, t[2], None,
                      t.lineno(2), ENCONTRAR_COL(input, t.slice[1]))


def p_EXPRESION_PARENTESIS(t):
    'expresion                  : P_IZQ expresion P_DER'
    t[0] = t[2]


def p_EXPRESION_LONGITUD(t):
    'expresion                  : RLENGTH P_IZQ  expresion P_DER'
    t[0] = If(t[3], t.lineno(2), ENCONTRAR_COL(input, t.slice[4]))


def p_EXPRESION_ACCESO_STRUCT(t):
    'expresion                  : expresionStruct'
    t[0] = t[1]


def p_EXPRESION_LLAMADA(t):
    'expresion                  : instruccion_llamada'
    t[0] = t[1]


def p_EXPRESION_NATIVAS(t):
    'expresion                  : nativas'
    t[0] = t[1]

def p_EXPRESION_ASIGNACION_ARRAY(t):
    'instruccion_asignacion                  : ID accesos IGUAL expresion'
    t[0] = AsignacionArray(t[1], t[2],t[4], t.lineno(
        1), ENCONTRAR_COL(input, t.slice[1]))

def p_EXPRESION_ACCESO_ARRAY(t):
    'expresion                  : ID accesos'
    # t[0] = Acceso_Array(t[1], t[2], t.lineno(
    #     1), ENCONTRAR_COL(input, t.slice[1]))
    


def p_EXPRESION_LISTA_ACCESOS(t):
    'accesos                    : accesos acceso'
    t[1].append(t[2])
    t[0] = t[1]


def p_EXPRESION_ACCESOS(t):
    'accesos                    : acceso'
    t[0] = [t[1]]


def p_EXPRESION_ACCESO(t):
    'acceso                     : C_IZQ expresion C_DER'
    t[0] = t[2]


def p_EXPRESION_CONTENIDO_ARRAY(t):
    'expresion                  : C_IZQ parametros_print C_DER'
    t[0] = Array(t[2], t.lineno(1), ENCONTRAR_COL(input, t.slice[1]))


def p_EXPRESION_IDENTIFICADOR(t):
    'expresion                  : ID'
    t[0] = Identificador(t[1], t.lineno(1), ENCONTRAR_COL(input, t.slice[1]))


def p_EXPRESION_ENTERO(t):
    'expresion                  : ENTERO'
    t[0] = Constante(Primitivo(TipoObjeto.ENTERO, t[1]),
                     t.lineno(1), ENCONTRAR_COL(input, t.slice[1]))


def p_EXPRESION_DECIMAL(t):
    'expresion                  : DECIMAL'
    t[0] = Constante(Primitivo(TipoObjeto.DECIMAL, t[1]),
                     t.lineno(1), ENCONTRAR_COL(input, t.slice[1]))


def p_EXPRESION_CADENA(t):
    'expresion                  : CADENA'
    t[0] = Constante(Primitivo(TipoObjeto.CADENA, str(t[1]).replace(
        '\\n', '\n')), t.lineno(1), ENCONTRAR_COL(input, t.slice[1]))


def p_EXPRESION_CARACTER(t):
    'expresion                  : CARACTER'
    t[0] = Constante(Primitivo(TipoObjeto.CARACTER, str(t[1])),
                     t.lineno(1), ENCONTRAR_COL(input, t.slice[1]))


def p_EXPRESION_TRUE(t):
    'expresion                  : RTRUE'
    t[0] = Constante(Primitivo(TipoObjeto.BOOLEANO, True),
                     t.lineno(1), ENCONTRAR_COL(input, t.slice[1]))


def p_EXPRESION_FALSE(t):
    'expresion                  : RFALSE'
    t[0] = Constante(Primitivo(TipoObjeto.BOOLEANO, False),
                     t.lineno(1), ENCONTRAR_COL(input, t.slice[1]))


def p_EXPRESION_NEGATIVO(t):
    'expresion                  : NEGACION expresion'
    t[0] = Logica(OperadorLogico.NOT, None, t[2],
                  t.lineno(2), ENCONTRAR_COL(input, t.slice[1]))


parser = yacc.yacc()


def getErrores():
    return errores


def parse(inp):
    global errores
    global lexer
    global parser
    errores = []
    lexer = lex.lex()
    parser = yacc.yacc()
    global input
    input = inp
    instrucciones = parser.parse(inp)
    ast = Arbol(instrucciones)
    TSGlobal = TablaSimbolos()
    ast.setTSglobal(TSGlobal)
    nodo = NodoReporteArbol("raiz")
    for instruccion in ast.getInstrucciones():
        if isinstance(instruccion, Funcion):
            ast.addFuncion(instruccion)
            
        elif isinstance(instruccion, Struct):
            ast.addStruct(instruccion)
        else:
            instruccion.ejecutar(ast, TSGlobal)
        nodo.agregarHijoNodo(instruccion.obtenerNodo())
    TS=ast.getTSGlobal()
    listaSimbolos=list()
    getTabla(ast,TS.tabla,TS.ambito,listaSimbolos)
    print(listaSimbolos)

   
    return ast,ast.getDot(nodo),listaSimbolos
    
def getTabla(ast,tabla,ambito,listaSimbolos):
    for x in tabla.values():  
        if isinstance(x,TablaSimbolos): 
            listaSimbolos.append({"id": x.id,"ambito":x.ambito,"tipo":x.tipo,"fila":str(x.fila),"columna":str(x.columna)})      
            # print(x.id+ " - "+x.ambito+" - "+x.tipo+" - "+str(x.fila)+" - "+str(x.columna)  )   
            getTabla(ast,x.tabla,x.id,listaSimbolos)
        else:
            try:
                listaSimbolos.append({"id":x.id,"ambito":ambito,"tipo":tabla[x.id].valor.tipo.name,"fila":str(x.fila),"columna":str(x.columna)})
            except:
                listaSimbolos.append({"id":x.id,"ambito":ambito,"tipo":"STRUCT","fila":str(x.fila),"columna":str(x.columna)})
            
      
            
