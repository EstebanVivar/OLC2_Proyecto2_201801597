
import sys
import ply.yacc as yacc
import ply.lex as lex

from Instrucciones.Llamada import Llamada
from Instrucciones.Funcion import Funcion
from Instrucciones.Break import Break
from Instrucciones.Struct import Struct
from Instrucciones.AccesoStruct import AccesoStruct
from Instrucciones.Continue import Continue
from Instrucciones.For import For

from Instrucciones.RetornoIns import RetornoIns


from Instrucciones.Imprimir import Imprimir

from Expresiones.Identificador import Identificador
from Expresiones.Logica import Logica, OperadorLogico
from Expresiones.Relacional import Relacional, OperadorRelacional
from Expresiones.Aritmetica import Aritmetica, OperadorAritmetico
from Expresiones.Constante import Constante
from Expresiones.Rango import Rango

from Abstract.Retorno import Tipo


from Instrucciones.If import If
from Instrucciones.Asignacion import Asignacion
from Instrucciones.While import While
from Instrucciones.Parametro import Parametro
from Expresiones.Array import Array
from Instrucciones.AccesoArray import Acceso_Array
from Instrucciones.Asignacion_Array import Asignacion_Array


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
    'elseif': 'RELSEIF',
    'else': 'RELSE',
    'while': 'RWHILE',
    'false': 'RFALSE',
    'true': 'RTRUE',
    'break': 'RBREAK',
    'continue': 'RCONTINUE',
    'length': 'RLENGTH',
    'function': 'RFUNC',
    'end': 'REND',
    'return': 'RRETURN',
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
t_AND = r'&&'
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
    t.value = t.value[1:-1]
    return t


def t_CARACTER(t):
    r'(\'.?\')'
    t.value = t.value[1:-1]
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


t_ignore = " \t\r"


def t_NUEVA_LINEA(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character ", ord(t.value[0]))
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
    ('left', 'POTENCIA'),
)


def p_INICIO(t):
    'start                      : instrucciones'
    t[0] = t[1]
    return t[0]


def p_LISTA_INSTRUCCIONES(t):
    '''instrucciones            : instrucciones  instruccion PUNTOCOMA
                                |  instruccion PUNTOCOMA'''
    if len(t) == 3:
        t[0] = [t[1]]
    else:
        t[1].append(t[2])
        t[0] = t[1]


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
                                '''
    t[0] = t[1]


# //////////////////////////////////////////IMPRIMIR///////////////////////////////////////////////////


def p_IMPRIMIR_SALTO(t):
    'instruccion_imprimir       : RPRINTLN P_IZQ parametros_print P_DER'
    t[0] = Imprimir(t[3], t.lineno(1), t.lexpos(0), True)


def p_IMPRIMIR(t):
    'instruccion_imprimir       : RPRINT P_IZQ parametros_print P_DER'
    t[0] = Imprimir(t[3], t.lineno(1), t.lexpos(0))


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


# ////////////////////////////////////////// IF ////////////////////////////////////////////////////////


def p_CUERPO_IF(t):
    '''instruccion_if           : RIF expresion instrucciones REND
                                | RIF expresion instrucciones RELSE  instrucciones REND
                                | RIF expresion instrucciones listaELSEIF REND
                                '''
    if len(t) == 5:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0))
    elif len(t) == 6:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[4])
    elif len(t) == 7:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[5])


def p_ELSEIF(t):
    '''listaELSEIF              : RELSEIF expresion instrucciones 
                                | RELSEIF expresion instrucciones RELSE instrucciones 
                                | RELSEIF expresion instrucciones listaELSEIF 
                                '''
    if len(t) == 4:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0))
    elif len(t) == 5:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[4])
    elif len(t) == 6:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[5])


# ////////////////////////////////// ASIGNACION ///////////////////////////////////////////////


def p_ASIGNACION(t):
    '''instruccion_asignacion : ID IGUAL expresion
                                | ID accesos IGUAL expresion'''
    if len(t) == 4:
        t[0] = Asignacion(t[1], t[3], t.lineno(2), t.lexpos(2))
    else:
        t[0] = Asignacion_Array(t[1], t[2],t[4], t.lineno(
        1), t.lexpos(3))

# /////////////////////////////////////// WHILE //////////////////////////////////////////////////


def p_WHILE(t):
    'instruccion_while          : RWHILE expresion  instrucciones REND'
    t[0] = While(t[2], t[3], t.lineno(1), t.lexpos(1))


# /////////////////////////////////////BREAK///////////////////////////


def p_BREAK(t):
    'instruccion_break : RBREAK'
    t[0] = Break(t.lineno(1), t.lexpos(1))


# /////////////////////////////////////CONTINUE/////////////////////////


def p_CONTINUE(t):
    'instruccion_continue          : RCONTINUE'
    t[0] = Continue(t.lineno(1), t.lexpos(1))


# /////////////////////////////////////RETURN///////////////////////////
def p_RETURN(t):
    '''instruccion_return   : RRETURN
                            | RRETURN expresion'''
    if len(t) == 2:
        t[0] = RetornoIns(None, t.lineno(1), t.lexpos(1))
    else:
        t[0] = RetornoIns(t[2], t.lineno(1), t.lexpos(1))
# //////////////////////////////////// FUNCION ////////////////////////


def p_FUNCION(t):
    '''instruccion_funcion      : RFUNC ID P_IZQ parametros P_DER TIPO tipo_dato instrucciones REND
                                | RFUNC ID P_IZQ P_DER TIPO tipo_dato instrucciones REND'''
    if len(t) == 10:
        t[0] = Funcion(t[2], t[4], t[8], t[7], t.lineno(1), t.lexpos(1))
    else:
        t[0] = Funcion(t[2], [], t[7], t[6], t.lineno(1), t.lexpos(1))


# /////////////////////////////////////// PARAMETROS //////////////////////////////////////////////////

def p_PARAMETROS(t):
    '''parametros               : parametros COMA parametro
                                | parametro'''
    if len(t) == 4:
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]


def p_PARAMETRO_TIPO(t):
    '''parametro                    : ID TIPO tipo_dato'''
    t[0] = Parametro(t[1],t[3], t.lineno(1), t.lexpos(1))

def p_PARAMETRO_TIPO_STRUCT(t):
    '''parametro                    : ID TIPO ID'''
    t[0] = Parametro(t[1],t[3], t.lineno(1), t.lexpos(1))




# /////////////////////////////////////// TIPO DATO ////////////////////////////////////////////////


def p_TIPO_DATO(t):
    '''tipo_dato                : RINT
                                | RFLOAT
                                | RSTRING
                                | RCHAR
                                | RBOOL
                                '''
    if t[1] == "Int64":
        t[0] = Tipo.ENTERO
    elif t[1] == "Float64":
        t[0] = Tipo.FLOTANTE
    elif t[1] == "String":
        t[0] = Tipo.CADENA
    elif t[1] == "Char":
        t[0] = Tipo.CARACTER
    elif t[1] == "Bool":
        t[0] = Tipo.BOOLEANO


# ////////////////////////////////////////////  LLAMADA FUNCION ///////////////////////////////////////

def p_LLAMADA(t):
    '''instruccion_llamada : ID P_IZQ P_DER
                | ID P_IZQ expresiones P_DER'''
    if len(t) == 4:
        t[0] = Llamada(t[1], [], t.lineno(1), t.lexpos(1))
    else:
        t[0] = Llamada(t[1], t[3], t.lineno(1), t.lexpos(1))

# CALL PARAMS


def p_PARAMETROS_LLAMADA(t):
    '''expresiones :  expresiones COMA expresion
                    | expresion'''
    if len(t) == 4:
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]


# //////////////////////////////////////STRUCT///////////////////////////////////////////////


def p_STRUCT(t):
    'instruccion_struct      : RSTRUCT ID atributos REND'
    t[0] = Struct(t[2], t[3],t.lineno(1), t.lexpos(1))


def p_LISTA_PARAMETROS_STRUCT(t):
    '''atributos            : atributos  parametro PUNTOCOMA
                            | parametro PUNTOCOMA'''
    if len(t) == 4:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

# ///////////////////////////////////////FOR//////////////////////////////////////////////////

def p_INSTRUCCION_FOR(t):
    'instruccion_for       : RFOR ID RIN range instrucciones REND'
    t[0] = For(t[2], t[4], t[5], t.lineno(1), t.lexpos(1))


def p_RANGO(t):
    '''range                    : expresion RANGO expresion                                
                                '''
    t[0] = Rango(t[1], t[3], t.lineno(1), t.lexpos(1))


def p_RANGO_CADENA(t):
    'range               : expresion'
    t[0] = Rango(t[1], None, t.lineno(1),  t[1].fila)


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
        t[0] = Aritmetica(OperadorAritmetico.MAS, t[1],
                          t[3], t.lineno(2), t.lexpos(0))
    elif t[2] == '-':
        t[0] = Aritmetica(OperadorAritmetico.MENOS, t[1],
                          t[3], t.lineno(2), t.lexpos(0))
    elif t[2] == '*':
        t[0] = Aritmetica(OperadorAritmetico.MULTIPLICACION, t[1],
                          t[3], t.lineno(2), t.lexpos(0))
    elif t[2] == '/':
        t[0] = Aritmetica(OperadorAritmetico.DIVISION, t[1],
                          t[3], t.lineno(2), t.lexpos(0))
    elif t[2] == '>':
        t[0] = Relacional(OperadorRelacional.MAYOR, t[1],
                          t[3], t.lineno(2), t.lexpos(0))
    elif t[2] == '<':
        t[0] = Relacional(OperadorRelacional.MENOR, t[1],
                          t[3], t.lineno(2), t.lexpos(0))
    elif t[2] == '>=':
        t[0] = Relacional(OperadorRelacional.MAYOR_IGUAL,
                          t[1], t[3], t.lineno(2), t.lexpos(0))
    elif t[2] == '<=':
        t[0] = Relacional(OperadorRelacional.MENOR_IGUAL,
                          t[1], t[3], t.lineno(2), t.lexpos(0))
    elif t[2] == '==':
        t[0] = Relacional(OperadorRelacional.COMPARA,
                          t[1], t[3], t.lineno(2), t.lexpos(0))
    elif t[2] == '!=':
        t[0] = Relacional(OperadorRelacional.DISTINTO, t[1],
                          t[3], t.lineno(2), t.lexpos(0))
    elif t[2] == '&&':
        t[0] = Logica(OperadorLogico.AND, t[1], t[3],
                      t.lineno(2), t.lexpos(0))
    elif t[2] == '||':
        t[0] = Logica(OperadorLogico.OR, t[1], t[3], t.lineno(2),
                      t.lexpos(0))


def p_EXPRESION_IDENTIFICADOR(t):
    'expresion                  : ID'
    t[0] = Identificador(t[1], t.lineno(1), t.lexpos(1))


def p_EXPRESION_LLAMADA(t):
    'expresion                  : instruccion_llamada'
    t[0] = t[1]


def p_ACCESO_STRUCT(t):
    '''expresion                : expresion DOT ID
                                | ID DOT ID'''   
    t[0] = AccesoStruct(t[1], t[3], t.lineno(1), t.lexpos(1))

# def p_EXPRESION_MENOS(t):
#     '''expresion                : MENOS expresion %prec UMENOS'''
#     t[0] = Aritmetica(OperadorAritmetico.NEG, t[2], None,
#                       t.lineno(2), t.lexpos(0))


def p_EXPRESION_ACCESO_ARRAY(t):
    'expresion                  : ID accesos'
    t[0] = Acceso_Array(t[1], t[2], t.lineno(1), t.lexpos(0))
    


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



def p_EXPRESION_ENTERO(t):
    'expresion                  : ENTERO'
    t[0] = Constante(int(t[1]), Tipo.ENTERO, t.lineno(1), t.lexpos(0))


def p_EXPRESION_PARENTESIS(t):
    'expresion                  : P_IZQ expresion P_DER'
    t[0] = t[2]


def p_EXPRESION_ARRAY(t):
    'expresion                  : C_IZQ parametros_print C_DER'
    t[0] = Array(t[2], t.lineno(1), t.lexpos(0))


def p_EXPRESION_DECIMAL(t):
    'expresion                  : DECIMAL'
    t[0] = Constante(float(t[1]), Tipo.FLOTANTE,
                     t.lineno(1), t.lexpos(0))


def p_EXPRESION_CADENA(t):
    'expresion                  : CADENA'
    t[0] = Constante(str(t[1]), Tipo.CADENA, t.lineno(1), t.lexpos(0))


def p_EXPRESION_CARACTER(t):
    'expresion                  : CARACTER'
    t[0] = Constante(t[1], Tipo.CARACTER, t.lineno(1), t.lexpos(0))


def p_EXPRESION_TRUE(t):
    'expresion                  : RTRUE'
    t[0] = Constante(True, Tipo.BOOLEANO, t.lineno(1), t.lexpos(0))


def p_EXPRESION_FALSE(t):
    'expresion                  : RFALSE'
    t[0] = Constante(False, Tipo.BOOLEANO, t.lineno(1), t.lexpos(0))


# def p_EXPRESION_NEGATIVO(t):
#     'expresion                  : NEGACION expresion'
#     t[0] = Logica(OperadorLogico.NOT, None, t[2],
#                   t.lineno(2), t.lexpos(0))


parser = yacc.yacc()


def parserX(input):
    return parser.parse(input)
