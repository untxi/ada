## ****************************************************************************
##
## Programa: Tablero_Electronico_Num.py
## Autores : Samantha Arburola, Jean Paul Velluti
## Fecha   : 30.09.2013
##
## Mostrar en una pizarra de leds caracteres numericos
##
## Entradas     : Digitacion de los numeros del 0 al 9 y la tecla Esc
##
## Salidas      : Ilustracion de los caracteres numoricos
##
## Restricciones: Las entradas deben ser onicamente las teclas numoricas
##                  y la tecla Esc
##
## ****************************************************************************

## Importacion para el grafico
from turtle import TurtleScreen, RawTurtle, TK

## Definicion de variables globales
pos = -29
yxdis = 20
xxdis = 20
    
## Funcion determinante de la posicion de los led
##     para el envio del caracter a la pizarra  
def envie(digito, pizarra):
    """ Funcion generica que envia un digito a la pizarra electronica

        Entradas:
            digito  : digito que se enviara a la pizarra
            pizarra : pizarra electronica a la se enviara el digito
            
        Salidas      : Ilustra el digito
        
        Restricciones: digito es un valor entero entre 0 y 9
    """

    global pos
    ## Determina la posicion del led a encender
    x = (pos - 29) * 10
    y = 3   
    ## Actualiza la posicion del siguiente led a encender
    if pos == 24:
        pos -= 53
    else:
        pos += 7

## Funcion para ilustrar el numero  CERO         
def envie_0(pizarra):
    """ Envia a la pizarra el digito 0

        Entradas:
            pizarra : tortuga que se utilizara para dibujar

        Salidas: Referencias para la ilustracion del digito
        
        Restricciones: pizarra corresponde a una tortuga
    """
    
    ## Posicion del led a encender y preparacion de la pizarra
    global pos
    screen = pizarra.getscreen()
    screen.tracer(False)
    pizarra.pu()
    for x1 in range((pos),(pos + 5)):
        x = x1* 10
        for y1 in range((-3),4):
            y = y1 * 10
            pizarra.goto(x,y) 
            pizarra.dot(5, "black")
    ## Ilustracion del numero
    ## Superior y Base
    for x1 in range(1,4):
        x = (pos + x1) * 10
        for y1 in [3, (-3)]:
            y = y1 * 10
            pizarra.goto(x, y)
            pizarra.dot(8, "red")  
            pizarra.dot(5, "orange")
    ## Extremos
    for x1 in [pos,(pos + 4)]:
        x = x1 * 10
        for y1 in range((-3),2):
            y = y1 * 10 + 10
            pizarra.goto(x, y)
            pizarra.dot(8, "red")  
            pizarra.dot(5, "orange")    
    ## Medio
    for x,y in  [(pos+1, -1), (pos+2, 0), (pos+3, 1)]:
        x *= 10
        y *= 10
        pizarra.goto(x, y)
        pizarra.dot(8, "red")  
        pizarra.dot(5, "orange")
    ## Impresion del numero
    pizarra.pd()
    pos += -1
    screen.tracer(True)
    print("CERO")
    envie(0, pizarra)


## Funcion para ilustrar el numero  UNO
def envie_1(pizarra):
    """ Envia a la pizarra el digito 1

        Entradas:
            pizarra : tortuga que se utilizara para dibujar

        Salidas: Referencias para la ilustracion del digito
        
        Restricciones: pizarra corresponde a una tortuga
    """
    
    ## Posicion del led a encender y preparacion de la pizarra
    global pos
    screen = pizarra.getscreen()
    screen.tracer(False)
    pizarra.pu()
    for x1 in range((pos),(pos + 5)):
        x = x1* 10
        for y1 in range((-3),4):
            y = y1 * 10
            pizarra.goto(x,y) 
            pizarra.dot(5, "black")
    ## Ilustracion del numero 
    ## Superior 
    x = (pos + 1) * 10
    y = 2 * 10 
    pizarra.goto(x, y)
    pizarra.dot(8, "red")  
    pizarra.dot(5, "orange")
    ## Medio
    x = (pos + 2) * 10
    for y1 in range(-3, 4):
        y = y1 * 10
        pizarra.goto(x, y)
        pizarra.dot(8, "red")  
        pizarra.dot(5, "orange")
    ## Base       
    for x1 in [1,2,3]:
            x = (pos + x1) * 10
            y = -3 * 10
            pizarra.goto(x, y)
            pizarra.dot(8, "red")  
            pizarra.dot(5, "orange")
    ## Impresion del numero
    pizarra.pd()
    pos += -1
    screen.tracer(True)
    print("UNO")
    envie(1, pizarra)   


## Funcion para ilustrar el numero  DOS 
def envie_2(pizarra):
    """ Envia a la pizarra el digito 2

        Entradas:
            pizarra : tortuga que se utilizara para dibujar

        Salidas: Referencias para la ilustracion del digito
        
        Restricciones: pizarra corresponde a una tortuga
    """
    
    ## Posicion del led a encender y preparacion de la pizarra
    global pos
    screen = pizarra.getscreen()
    screen.tracer(False)
    pizarra.pu()
    for x1 in range((pos),(pos + 5)):
        x = x1* 10
        for y1 in range((-3),4):
            y = y1 * 10
            pizarra.goto(x,y) 
            pizarra.dot(5, "black")
    ## Ilustracion del numero
    ## Superior
    for x1 in range(1,4):
        x = (pos + x1) * 10
        y = 3 * 10
        pizarra.goto(x, y)
        pizarra.dot(8, "red")  
        pizarra.dot(5, "orange")
    ## Medio
    for x, y in [(pos, 2), ((pos + 4), 2), ((pos + 4), 1), ((pos+2), 0),
                 ((pos + 3), 0), ((pos+1), (-1)), (pos,(-2))]:
        x *= 10
        y *= 10
        pizarra.goto(x, y)
        pizarra.dot(8, "red")  
        pizarra.dot(5, "orange")
    ## Base
    for x1 in range(0,5):
        x = (pos + x1) * 10
        y = -3 * 10
        pizarra.goto(x, y)
        pizarra.dot(8, "red")  
        pizarra.dot(5, "orange")
    ## Impresion del numero
    pizarra.pd()
    pos += -1
    screen.tracer(True)
    print("DOS")
    envie(2, pizarra)


## Funcion para ilustrar el numero  TRES 
def envie_3(pizarra):
    """ Envia a la pizarra el digito 3

        Entradas:
            pizarra : tortuga que se utilizara para dibujar

        Salidas: Referencias para la ilustracion del digito
        
        Restricciones: pizarra corresponde a una tortuga
    """
     
    ## Posicion del led a encender y preparacion de la pizarra
    global pos
    screen = pizarra.getscreen()
    screen.tracer(False)
    pizarra.pu()

    for x1 in range((pos),(pos + 5)):
        x = x1* 10
        for y1 in range((-3),4):
            y = y1 * 10
            pizarra.goto(x,y) 
            pizarra.dot(5, "black")
    ## Ilustracion del numero
    ## Superior
    for x1 in range(0,5):
        x = (pos + x1) * 10
        y = 3 * 10
        pizarra.goto(x, y)
        pizarra.dot(8, "red")  
        pizarra.dot(5, "orange")
    ## Medio    
    for x, y in [((pos + 4), 2), ((pos+2), 0),((pos + 3), 1), ((pos+3), 0),
                 ((pos+4),(-1)) ,((pos+4), (-2)),((pos+1), (-3)),
                 ((pos+3), (-3)),((pos+2), (-3)),(pos,(-2))]:
        x *= 10
        y *= 10
        pizarra.goto(x, y)
        pizarra.dot(8, "red")  
        pizarra.dot(5, "orange")
    ## Impresion del numero
    pizarra.pd()
    pos += -1
    screen.tracer(True)
    print("TRES")
    envie(3, pizarra)


## Funcion para ilustrar el numero  CUATRO 
def envie_4(pizarra):
    """ Envia a la pizarra el digito 4

        Entradas:
            pizarra : tortuga que se utilizara para dibujar

        Salidas: Referencias para la ilustracion del digito
        
        Restricciones: pizarra corresponde a una tortuga
    """
        
    ## Posicion del led a encender y preparacion de la pizarra
    global pos
    screen = pizarra.getscreen()
    screen.tracer(False)
    pizarra.pu()
    for x1 in range((pos),(pos + 5)):
        x = x1* 10
        for y1 in range((-3),4):
            y = y1 * 10
            pizarra.goto(x,y) 
            pizarra.dot(5, "black")
    ## Ilustracion del numero
    ## Columna
    for x1 in range(0,5):
        x = (pos + x1) * 10
        y = -1 * 10
        pizarra.goto(x, y)
        pizarra.dot(8, "red")  
        pizarra.dot(5, "orange")
    ## Diagonales
    for x, y in [((pos + 3), 1),((pos + 3), 2),((pos + 3), -3),((pos + 3), -2),
                 ((pos + 3), 0),((pos + 3), 3),((pos + 2), 2),((pos + 1), 1),
                 (pos, 0)]:
        x *= 10
        y *= 10
        pizarra.goto(x, y)
        pizarra.dot(8, "red")  
        pizarra.dot(5, "orange")
    ## Impresion del numero
    pizarra.pd()
    pos += -1
    screen.tracer(True)
    print("CUATRO")
    envie(4, pizarra)


## Funcion para ilustrar el numero  CINCO 
def envie_5(pizarra):
    """ Envia a la pizarra el digito 5

        Entradas:
            pizarra : tortuga que se utilizara para dibujar

        Salidas: Referencias para la ilustracion del digito
        
        Restricciones: pizarra corresponde a una tortuga
    """
    
    ## Posicion del led a encender y preparacion de la pizarra
    global pos
    screen = pizarra.getscreen()
    screen.tracer(False)
    pizarra.pu()
    for x1 in range((pos),(pos + 5)):
        x = x1* 10
        for y1 in range((-3),4):
            y = y1 * 10
            pizarra.goto(x,y) 
            pizarra.dot(5, "black")
    ## Ilustracion del numero
    ## Superior
    for x1 in range(0,5):
        x = (pos + x1) * 10
        y = 3 * 10
        pizarra.goto(x, y)
        pizarra.dot(8, "red")  
        pizarra.dot(5, "orange")
    ## Medio
    for x, y in[(pos, 2), (pos, 1),((pos + 1), 1),((pos + 2), 1),
                ((pos + 3), 1),(pos + 4, 0),((pos + 4), -1),((pos + 4), -2),
                ((pos + 3), -3),((pos + 2), -3),((pos + 1), -3),(pos, -3)]:
        x *= 10
        y *= 10
        pizarra.goto(x, y)
        pizarra.dot(8, "red")  
        pizarra.dot(5, "orange") 
    ## Impresion del numero
    pizarra.pd()
    pos += -1
    screen.tracer(True)
    print("CINCO")
    envie(5, pizarra)


## Funcion para ilustrar el numero  SEIS 
def envie_6(pizarra):
    """ Envia a la pizarra el digito 6

        Entradas:
            pizarra : tortuga que se utilizara para dibujar

        Salidas: Referencias para la ilustracion del digito
        
        Restricciones: pizarra corresponde a una tortuga
    """
    
    ## Posicion del led a encender y preparacion de la pizarra
    global pos
    screen = pizarra.getscreen()
    screen.tracer(False)
    pizarra.pu()
    for x1 in range((pos),(pos + 5)):
        x = x1* 10
        for y1 in range((-3),4):
            y = y1 * 10
            pizarra.goto(x,y) 
            pizarra.dot(5, "black")
    ## Ilustracion del numero
    ## Superior
    for x1 in range(2,5):
        x = (pos + x1) * 10
        y = 3 * 10
        pizarra.goto(x, y)
        pizarra.dot(8, "red")  
        pizarra.dot(5, "orange")
    ## Medio
    for x1, y1 in [(1, 2), (0, 1)]:
        x = (pos + x1) * 10
        y = y1 * 10
        pizarra.goto(x, y)
        pizarra.dot(8, "red")  
        pizarra.dot(5, "orange")
    ## Extremos a
    for x1 in range(0, 4):
        x = (pos + x1) * 10
        for y1 in [0, (-3)]:
            y = y1 * 10
            pizarra.goto(x, y)
            pizarra.dot(8, "red")  
            pizarra.dot(5, "orange")
    ## Extremos b
    for x1 in [0, 4]:
        x = (pos + x1) * 10
        for y1 in [(-1), (-2)]:
            y = y1 * 10
            pizarra.goto(x, y)
            pizarra.dot(8, "red")  
            pizarra.dot(5, "orange")
    ## Impresion del numero
    pizarra.pd()
    pos += -1
    screen.tracer(True)
    print("SEIS")
    envie(6, pizarra)

## Funcion para ilustrar el numero  SIETE
def envie_7(pizarra):
    """ Envia a la pizarra el digito 7

        Entradas:
            pizarra : tortuga que se utilizara para dibujar

        Salidas: Referencias para la ilustracion del digito
        
        Restricciones: pizarra corresponde a una tortuga
    """

    ## Posicion del led a encender y preparacion de la pizarra
    global pos
    screen = pizarra.getscreen()
    screen.tracer(False)
    pizarra.pu()
    for x1 in range((pos),(pos + 5)):
        x = x1* 10
        for y1 in range((-3),4):
            y = y1 * 10
            pizarra.goto(x,y) 
            pizarra.dot(5, "black")

    ## Fila uno
    for x1 in range(0,5):
        x = (pos + x1) * 10
        y = 3 * 10
        pizarra.goto(x, y)
        pizarra.dot(8, "red")  
        pizarra.dot(5, "orange")

    ## El resto de la parte del 7
    for x, y in[(pos + 4, 2), (pos + 3, 1), (pos + 2, 0), (pos + 1, -1),
                (pos + 1, -2), (pos + 1, -3)]:
        x *= 10
        y *= 10
        pizarra.goto(x, y)
        pizarra.dot(8, "red")  
        pizarra.dot(5, "orange")

    ## Impresion del numero
    pizarra.pd()
    pos += -1
    screen.tracer(True)
    print("SIETE")
    envie(7, pizarra)

## Funcion para ilustrar el numero  OCHO 
def envie_8(pizarra):
    """ Envia a la pizarra el digito 8

        Entradas:
            pizarra : tortuga que se utilizara para dibujar

        Salidas: Referencias para la ilustracion del digito
        
        Restricciones: pizarra corresponde a una tortuga
    """
        
    ## Posicion del led a encender y preparacion de la pizarra
    global pos
    screen = pizarra.getscreen()
    screen.tracer(False)
    pizarra.pu()
    for x1 in range((pos),(pos + 5)):
        x = x1* 10
        for y1 in range((-3),4):
            y = y1 * 10
            pizarra.goto(x,y) 
            pizarra.dot(5, "black")
    ## Ilustracion del numero
    ## Medios
    for x1 in range(1,4):
        x = (pos + x1) * 10
        for y1 in [-3, 0, 3]:
            y = y1 * 10
            pizarra.goto(x, y)
            pizarra.dot(8, "red")  
            pizarra.dot(5, "orange")
    ## Extremos
    for x1 in [0, 4]:
        x = (pos + x1) * 10
        for y1 in [-1, -2, 1, 2]:
            y = y1 * 10
            pizarra.goto(x, y)
            pizarra.dot(8, "red")  
            pizarra.dot(5, "orange")
    ## Impresion del numero
    pizarra.pd()
    pos += -1
    screen.tracer(True)
    print("OCHO")
    envie(8, pizarra)

## Funcion para ilustrar el numero  NUEVE
def envie_9(pizarra):
    """ Envia a la pizarra el digito 9

        Entradas:
            pizarra : tortuga que se utilizara para dibujar

        Salidas: Referencias para la ilustracion del digito
        
        Restricciones: pizarra corresponde a una tortuga
    """

    ## Posicion del led a encender y preparacion de la pizarra
    global pos
    screen = pizarra.getscreen()
    screen.tracer(False)
    pizarra.pu()
    for x1 in range((pos),(pos + 5)):
        x = x1* 10
        for y1 in range((-3),4):
            y = y1 * 10
            pizarra.goto(x,y) 
            pizarra.dot(5, "black")

    ## Fila uno
    for x1 in range(1,4):
        x = (pos + x1) * 10
        y = 3 * 10
        pizarra.goto(x, y)
        pizarra.dot(8, "red")  
        pizarra.dot(5, "orange")
    ## Leds diagonales y laterales
    for x, y in[(pos, 2), (pos, 1), (pos + 4, 2), (pos + 4, 1), (pos + 4, -1),
                (pos + 3, - 2)]:
        x *= 10
        y *= 10
        pizarra.goto(x, y)
        pizarra.dot(8, "red")  
        pizarra.dot(5, "orange")
        ## Fila 4
        for x1 in range(1, 5):
            x = (pos + x1) * 10
            y =  0 * 10
            pizarra.goto(x, y)
            pizarra.dot(8, "red")  
            pizarra.dot(5, "orange")
            ## Fila 7
            for x1 in range(0, 3):      
                x = (pos + x1) * 10
                y =  -3 * 10
                pizarra.goto(x, y)
                pizarra.dot(8, "red")  
                pizarra.dot(5, "orange")

    ## Impresion del numero
    pizarra.pd()
    pos += -1
    screen.tracer(True)
    print("NUEVE")
    envie(9, pizarra)


## Funcion para dibujar la pizarra       
def dibuja_leds(pizarra):
    """ Dibuja los leds apagados

        Entradas:
            pizarra : tortuga que se utiliza para dibujar
            
        Salidas: Ninguna

        Restricciones: pizarra corresponde a una tortuga.
    """
    
    global pos
    global xxdis
    global yxdis
    
    ## Limpia la pantalla y oculta la tortuga
    pos = -29
    pizarra.reset()
    pizarra.ht()
    screen = pizarra.getscreen() 
    screen.tracer(False)
    ## Dibuja los led apagados
    y = 0
    x = 0
    pizarra.pu()  
    for x1 in range((-29),30):
        pizarra.setx(x1*10)
        pizarra.dot(8, "red")  
        pizarra.dot(5, "black")
        x1 += xxdis
        for y1 in range((-3),4):
            pizarra.sety(y1*10)
            pizarra.dot(8, "red")  
            pizarra.dot(5, "black")
            y1 += yxdis
            pizarra.pd()
 
    ## Presenta los led  
    screen.tracer(True) 


## Funcion para crear el tablero
def crea_tablero(titulo, alto, ancho):
    """ Crea una pizarra electronica

        Entradas:
            titulo : titulo de la ventana que contendra la pizarra electronica
            alto   : alto de la ventana en pixeles
            ancho  : ancho de la ventna en pixeles
            
        Salidas: Ninguna
        
        Restricciones: titulo es una tira, alto y ancho son enteros positivos
    """

    ## Restricciones
    assert isinstance(titulo, str)
    assert isinstance(alto, int) and alto > 0
    assert isinstance(ancho, int) and ancho > 0

    ## Crea la ventana y un canvas para dibujar
    root = TK.Tk()
    root.title(titulo)
    canvas = TK.Canvas(root, width=ancho, height=alto)
    canvas.pack()

    ## Crea un TurtleScreen y la tortuga para dibujar
    fondo_tablero = TurtleScreen(canvas)

    ## Establece el fondo de la pizarra electronica
    canvas["bg"] = "black"
    canvas.pack()
    pizarra = RawTurtle(fondo_tablero)
    dibuja_leds(pizarra)

    ## Establece las funciones para capturar las teclas
    fondo_tablero.onkeypress(lambda : envie_0(pizarra), "0")
    fondo_tablero.onkeypress(lambda : envie_1(pizarra), "1")
    fondo_tablero.onkeypress(lambda : envie_2(pizarra), "2")
    fondo_tablero.onkeypress(lambda : envie_3(pizarra), "3")
    fondo_tablero.onkeypress(lambda : envie_4(pizarra), "4")
    fondo_tablero.onkeypress(lambda : envie_5(pizarra), "5")
    fondo_tablero.onkeypress(lambda : envie_6(pizarra), "6")
    fondo_tablero.onkeypress(lambda : envie_7(pizarra), "7")
    fondo_tablero.onkeypress(lambda : envie_8(pizarra), "8")
    fondo_tablero.onkeypress(lambda : envie_9(pizarra), "9")
    fondo_tablero.onkeypress(lambda : dibuja_leds(pizarra), "Escape")
    fondo_tablero.listen()
    
    root.mainloop()
    

if __name__ == '__main__':
    crea_tablero("Pizarra Electronica Numerica", 150, 650)
