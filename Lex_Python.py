import ply.lex as lex

tokens = [
	'PLUS', # +
	'MINUS', # -
	'TIMES', # *
	'DIVIDED', # /
	'LPAREN', # (
	'RPAREN', # )
	'SYMBOL', # variable names
	'NUMBER',
	'COMILLA_SIMPLE',
	'COMILLA_DOBLE',
	'DOBLE_PUNTO',
	'TEXT',
	'DECIMAL',
	'EQUAL',
	'DOUBLE_EQUAL',
	'GT',
	'LT',
	'GEQT',
	'LEQT',
	'COMA',
	'CORIZ',
	'CORDER',
]
t_CORIZ = r'\['
t_CORDER = r'\]'
t_PLUS = r'\+'
t_COMA = r'\,'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDED = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
#t_SYMBOL = r'[a-z]\w*'
t_SYMBOL = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_COMILLA_SIMPLE = r"\'"
t_COMILLA_DOBLE = r'\"'
t_DOBLE_PUNTO= r'\:'
t_TEXT = r"(\'[\w\s\.]*\'|\"[\w\s\.]*\")"
t_EQUAL = r'\='
t_DOUBLE_EQUAL = r'\=='
t_GT = r'>'
t_LT = r'<'
t_GEQT = r'>='
t_LEQT = r'<='


reserved_words = {
	'true':'TRUE',
	'false':'FALSE',
  'and':"AND",
  'as':"AS",
  'assert':"ASSERT",
  'break':"BREAK",
  'class':"CLASS",
  'continue':"CONTINUE",
  'def':"DEF",
  'del':"DEL",
  'elif':"ELIF",
  'else'	:	"ELSE",
  'except'	:	"EXCEPT",
  'exec'	:	"EXEC",
  'finally'	:	"FINALLY",
  'for'	:	"FOR",
  'from'	:	"FROM",
  'global'	:	"GLOBAL",
  'if'	:	"IF",
  'import'	:	"IMPORT",
  'in'	:	"IN",
  'is'	:	"IS" ,
  'lambda'	:	"LAMBDA",
  'not'	:	"NOT",
  'or'	:	"OR",
  'pass'	:	"PASS",
  'print'	:	"PRINT",
  'raise'	:	"RAISE",
  'return'	:	"RETURN",
  'try'	:	"TRY",
  'while'	:	"WHILE",
  'with'	:	"WITH",
  'yield'	:	"YIELD",
  'range'	:  'RANGE',
}

tokens = tokens + list(reserved_words.values())
constants = {
	'true': 'TRUE',
	'false': "FALSE",
	'nil': "NIL",
	'null': "NULL",
}

def t_DECIMAL(t):
	r'\d+\.\d+'
	t.value = float(t.value)
	return t

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_error(t):
    print("Caracter incorrecto '%s'" % t.value[0])
    t.lexer.skip(1)

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value in reserved_words:
		t.type = reserved_words[t.value]
	else:
		t.type = 'SYMBOL'
	return t
t_ignore = ' \t'
lexer = lex.lex()
data =''' a= 5
             b=a
            while a > b: a=10'''
data1= '''hugo=1'''

def recibirtokens(data):
	lexer.input(data)
	l=[]
	while True:
		tok = lexer.token()
		if not tok:
			break
		a=""
		list=tok.__dict__
		l.append([" value: "+ str(list['value']) + ', type: ' + str(list['type'])])
		for i in l:
			a= a+ str(i[0])+ '\n'


	return a
"""
def test(code):
	lexer.input(code)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print(tok)
test(data)
"""
"""
print(recibirtokens(data))

print(recibirtokens(data1))
"""