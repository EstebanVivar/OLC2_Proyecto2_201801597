import re
import ply.lex as lex

errores = []


reserved = {
    'float64'   :   'RFLOAT',
    'int'       :   'RINT',
    'fmt'       :   'RFMT',
    'func'      :   'RFUNC',
    'return'    :   'RRETURN',
    'if'        :   'RIF',
    'goto'      :   'RGOTO',
    'Printf'    :   'RPRINTF',
    'package'   :   'RPACKAGE',
    'import'    :   'RIMPORT',
    'var'       :   'RVAR',
    'math'      :   'RMATH',
    'Mod'       :   'RMOD'
}

tokens  = [
    'COMA',
    'PTCOMA',
    'PUNTO',
    'DPUNTOS',
    'PARI',
    'PARD',
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'POT',
    'MOD',
    'IGUAL',
    'IGUALDAD',
    'DIFERENTE',
    'MAYOR',
    'MENOR',
    'MAYORI',
    'MENORI',
    'OR',
    'AND',
    'ENTERO',
    'DECIMAL',
    'CADENA',
    'ID',
    'CORI',
    'CORD',
    'LLI',
    'LLD'
]+ list(reserved.values())

# Tokens
t_COMA          = r','
t_PTCOMA        = r';'
t_DPUNTOS       = r':'
t_PUNTO         = r'\.'
t_PARI          = r'\('
t_PARD          = r'\)'
t_MAS           = r'\+'
t_MENOS         = r'\-'
t_POR           = r'\*'
t_DIV           = r'\/'
t_POT           = r'\^'
t_MOD           = r'\%'
t_IGUALDAD      = r'\=='
t_IGUAL         = r'\='
t_DIFERENTE     = r'\!='
t_MAYOR         = r'\>'
t_MENOR         = r'\<'
t_MAYORI        = r'\>='
t_MENORI        = r'\<='
t_OR            = r'\|\|'
t_AND           = r'&&'
t_CORI          = r'\['
t_CORD          = r'\]'
t_LLI           = r'\{'
t_LLD           = r'\}'

#Decimal
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t


#Entero
def t_ENTERO(n):
    # 12341234
    r'\d+'
    try:
        if(n.value != None):
            n.value = int(n.value)
        else:
            n.value = 'nothing'
    except ValueError:
        print("Valor del entero demasiado grande %d", n.value)
        n.value = 0
    return n


#Identificador
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')# Check for reserved words
    return t

#Cadena
def t_CADENA(t):
    # 13ashd8127126?2\n
    r'(\".*?\")'
    t.value = t.value[1:-1] #Se remueven las comillas de la entrada
    t.value = t.value.replace('\\t','\t')
    t.value = t.value.replace('\\n','\n')
    t.value = t.value.replace('\\"','\"')
    t.value = t.value.replace("\\'","\'")
    t.value = t.value.replace('\\\\','\\')
    return t

#Comentario Multilinea
def t_Com_Multiple(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    
#Nueva Linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caracteres ignorados
t_ignore = " \t"

#Error
def t_error(t):
    t.lexer.skip(1)

def find_column(inp, tk):
    line_start = inp.rfind('\n', 0, tk.lexpos) + 1
    return (tk.lexpos - line_start) + 1

lexer = lex.lex(reflags = re.IGNORECASE)