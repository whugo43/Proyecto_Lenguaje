import ply.yacc as yacc
from Lex_Python import tokens

file = open('res', 'a')
file.close
def p_main(p):
    """ main : body
            | body main
    """
    print("Correct!")
    file = open('res.txt', 'a')
    file.write("Correct!\n")
    file.close()

def p_body (p):
    """ body : for
            | while
            | if
            | variables
            | operation_mathematic
            | operation_logic
            | operator_arithmetic
    """

def p_condicion_FOR (t):
    """ for : FOR SYMBOL IN RANGE LPAREN NUMBER RPAREN
                        | FOR SYMBOL IN CORIZ NUMBER COMA NUMBER COMA NUMBER CORDER
                        | FOR SYMBOL IN RANGE LPAREN NUMBER COMA NUMBER LPAREN
                        """

def p_condition_while (p):
    """ while : WHILE operation_logic DOBLE_PUNTO variables
               | WHILE operation_logic DOBLE_PUNTO if
               | WHILE operation_logic DOBLE_PUNTO while"""

def p_condicion_if (p):
    """ if : IF operation_logic  DOBLE_PUNTO variables
        | IF operation_logic DOBLE_PUNTO  variables ELSE variables
        | IF operation_logic DOBLE_PUNTO variables ELIF operation_logic DOBLE_PUNTO variables ELSE variables"""

def p_variables (p):
    """ variables : SYMBOL EQUAL SYMBOL
    | SYMBOL EQUAL type_number
    | SYMBOL EQUAL operation_mathematic"""


def p_operation_mathematic (p):
    """ operation_mathematic : type_number operator_arithmetic type_number
                              | SYMBOL operator_arithmetic type_number

    """

def p_operation_logic (p):
    """operation_logic : operation_log
                    | operation_log  AND operation_logic
                    | operation_log  OR operation_logic

    """


def p_operation_log (p):
    """ operation_log : SYMBOL operator_logic SYMBOL
                        | SYMBOL operator_logic type_number
                        | type_number operator_logic SYMBOL
                        | type_number operator_logic type_number
    """

def p_type_number(p):
    """ type_number : NUMBER
                     | DECIMAL """

def p_operator_arithmetic(p):
    """ operator_arithmetic : PLUS
                 | MINUS
                 | TIMES
                 | DIVIDED """

def p_operator_logic(p):
    """ operator_logic : DOUBLE_EQUAL
                 | GT
                 | LT
                 | GEQT
                 | LEQT """

def p_booleans(p):
    """ booleans : TRUE
                 | FALSE"""

def p_error(p):
        print ("Syntax error!")
        file = open ('res.txt', 'a')
        file.write ('Syntax error!\n')
        file.close ()

parser=yacc.yacc()

def validate(expr):
    return parser.parse(expr)

validate(''' a=5
             b=a
            IF a > b: a=10''')
