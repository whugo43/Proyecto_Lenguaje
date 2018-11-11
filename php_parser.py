
import ply.yacc as yacc
import php_lex
tokens = php_lex.tokens

precedence = (
    ('left','SUMA','RESTA'),
    ('left','MULTIPLICACION','DIVISION')
)
# lazo while
def p_loop_while(p):
    ''' loop_while : WHILE PARENTESIS_IZQ NOMBRE comparador num_var PARENTESIS_DER LLAVE_IZQ LLAVE_DER '''

# lazo for
def p_loop_for(p):
    ''' loop_for : FOR PARENTESIS_IZQ for_condicion PARENTESIS_DER LLAVE_IZQ LLAVE_DER''' 

def p_for_condicion(p):
    ''' for_condicion : NOMBRE ASIGNACION NUMERO PUNTO_COMA NOMBRE comparador num_var PUNTO_COMA for_final'''

def p_for_final(p):
    ''' for_final : SUMA SUMA num_var
                  | num_var SUMA SUMA 
                  | RESTA RESTA num_var
                  | num_var RESTA RESTA 
                  | MULTIPLICACION MULTIPLICACION num_var
                  | num_var MULTIPLICACION MULTIPLICACION '''

# condicional
def p_expression_condicional(p):
    ''' expression_condicional : IF PARENTESIS_IZQ expression_logica PARENTESIS_DER LLAVE_IZQ LLAVE_DER ELSE LLAVE_IZQ LLAVE_DER PUNTO_COMA
                   | IF PARENTESIS_IZQ expression_logica PARENTESIS_DER LLAVE_IZQ LLAVE_DER PUNTO_COMA''' 

# operacion logica 
def p_expression_logica(p):
    ''' expression_logica : expression op_logico expression
                   | NOT NOMBRE '''

# operaciones matematicas
def p_expression_matematica(p):
    ''' expression_matematica : num_var signo num_var'''

# asignar una variable
def p_asign(p):
    '''asign : NOMBRE ASIGNACION expression PUNTO_COMA'''

def p_expression(p):
    '''expression : NUMERO
                  | NOMBRE
                  | NOMBRE signo num_var'''

def p_num_var(p):
    ''' num_var : NUMERO 
                | NOMBRE '''

def p_signo(p):
    ''' signo : SUMA
              | RESTA
              | MULTIPLICACION
              | DIVISION '''

def p_comparador(p):
    ''' comparador : IGUAL
                   | DIFERENTE
                   | MAYOR_QUE
                   | MENOR_QUE
                   | MAYOR_IGUAL_QUE 
                   | MENOR_IGUAL_QUE'''

def p_op_logico(p):
    ''' op_logico : IGUAL
                  | DIFERENTE
                  | MAYOR_QUE
                  | MENOR_QUE
                  | MAYOR_IGUAL_QUE 
                  | MENOR_IGUAL_QUE
                  | IDENTICO
                  | DIFERENT
                  | NO_IDENTICO '''

def p_error(p):
    raise Exception("Syntax error.")

yacc.yacc()