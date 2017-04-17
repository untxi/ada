from fuente import *
abc=[]

def p_chr(x):
    global abc
    abc+=x
    return abc

    
def lee():
    global abc
##    fondo_tablero.tracer(False)
##    pizarra.pu()
##    x = (pos ) * 9

    for c in range(0,len(abc)):
        for bit in range(20):
            if bit == 0:
                print("black")
            elif bit == 1:
                print("orange")

##    pizarra.pd()
##    fondo_tablero.tracer(True)





##    if color == "blue":
##        lista.insert(0,color)
##    elif color == "green":
##        lista.insert(0,color)
##    elif color == "white":
##        lista.insert(0,color)
##    elif color == "orange":
##        lista.insert(0,color)
##    return lista

##def muestra(abc):
##    global abc
##    fondo_tablero.tracer(False)
##    pizarra.pu()
##    x = (pos ) * 9
##    for y1 in range((-9),10):
##        y = y1 * 9
##        for c in range(0,len(abc)):
##            for bit in c:
##                if abc[c][bit] == False:
##                    pizarra.goto(x, y)
##                    pizarra.dot(5, "black")
##                elif  abc[c][bit] == True:
##                    if abc[0] == "orange":
##                        pizarra.goto(x, y)
##                        pizarra.dot(5, "orange")
##                    else:
##                        pizarra.goto(x, y)
##                        pizarra.dot(5, "orange")
##    print(abc)
##    pizarra.pd()
##    fondo_tablero.tracer(True)
