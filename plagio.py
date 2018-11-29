from Lex_Python import *

def plagio(data1, data2):
    tokens1=tokens_arbol(data1)
    tokens2 = tokens_arbol(data2)
    ltokens1=len(tokens1)
    ltokens2=len(tokens2)
    print(ltokens1,"TOKEN1")
    print(ltokens2,"TOKEN2")

    contador=0
    i=0
    if(ltokens1>ltokens2):
        total=ltokens1
        while(i<ltokens1-1):
            if(tokens1[i] in tokens2):
                tokens2.remove(tokens1[i])
                contador+=1
            i+=1
    elif(ltokens1==ltokens2):
        total=ltokens1
        while(i<ltokens2):
            if (tokens1[i] in tokens2):
                tokens2.remove(tokens1[i])
                contador += 1
            i += 1
    else:
        total=ltokens2
        while (i < ltokens2 - 1):
            if (tokens2[i] in tokens1):
                tokens1.remove(tokens2[i])
                contador += 1
            i += 1
    print(contador,"CONTADOR")
    print(total,"TOTAL")
    round((contador/total)*100,2)

    retorno= "El % de coincidencia es: " + str(round ((contador/total)*100, 2))+" %"
    return (retorno)
