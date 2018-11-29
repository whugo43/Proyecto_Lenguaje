from Lex_Python import *

def plagio(data1, data2):
    tokens1=tokens_arbol(data1)
    tokens2 = tokens_arbol (data2)
    i=0
    suma=0
    total=len (tokens2)
    temp=len(tokens1)
    while (i < len(tokens2)-1) or (temp!=0):
        contador=0
        if (tokens2[i]in tokens1):
            tokens1.remove(tokens2[i])
            contador=1
        suma=suma+contador
        temp=len(tokens1)
        i=i+1
        round ((suma/total)*100, 2)

    retorno= "El % de coincidencia es: " + str(round ((suma/total)*100, 2))+" %"
    return (retorno)
