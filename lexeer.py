import ply.lex as lex

tokens = [
	'PLUS', 'MINUS', 'TIMES', 'DIVIDED', 'LPAREN', 'RPAREN', # )
	'ID', # variable names
	'NUMBER','COMILLA_DOBLE','TEXT','DECIMAL', 'COMMENT'
	'EQUAL','GT','LT','GEQT','LEQT',
]

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDED = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMILLA_SIMPLE = r"\'"
t_COMILLA_DOBLE = r'\"'
t_TEXT = r"(\'[\w\s\.]*\'|\"[\w\s\.]*\")"
t_EQUAL = r'\='
t_GT = r'>'
t_LT = r'<'
t_GEQT = r'>='
t_LEQT = r'<='

reserved_words = {
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
  'yield'	:	"YIELD"
}

tokens = tokens + list(reserved_words.values())

t_ignore = '\t'

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
	r'[a-zA-Z_ ][a-zA-Z0-9_]*'
	if t.value in reserved_words:
		t.type = reserved_words[t.value]
	else:
		t.type = 'SYMBOL'
	return t

def t_COMMENT(t):
    r '^#[\w\W]+'
    pass

#PRUEBAS
lexer = lex.lex()
data = """
	Hola=4
	"""

lexer.input(data)

while True:
	tok = lexer.token()
	if not tok:
		break
	print(tok)
