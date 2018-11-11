import ply.yacc as yacc
import Lex_Python
tokens= Lex_Python.tokens
precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIME','DIVIDED')
)
# lazo while
def p_loop_while(p):
    ''' loop_while : WHILE '''
def lazo_for ():
    b=1+1
    print("b")



'''def p_error(p):
    print("Syntax error!")
    file = open('res', 'a')
    file.write('Syntax error!\n')
    file.close()
'''
def p_error(p):
    raise Exception("Syntax error.")
i=0
while i<3:
    print(i)
    i=1+i
print(i)

for il in "hugo":
    print(il)
hugo= "12.3"
print(int(12.3))