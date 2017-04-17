from turtle import TurtleScreen, RawTurtle, TK
pos = 0
XDIS = 9   ## Distancia entre puntos.
alto = False ## Control del ciclo por siempre
estado = True

def anime():
    """ Función genérica que permite encender o apagar un led.
        Utiliza las siguiente variables globales
            estado   : indica si el led debe encenderse o apagarse.
            pos      : número de led.
            pizarra  : pizarra electrónica.
        Entradas:
            ninguna.
        Salidas:
            ninguna.
    """

    ## Determina la posición del led a encender
    x = (pos + 47) * 9
    y = (9) * (-9)
    fondo_tablero.tracer(False)
    ## Se posiciona en el centro del led.
    pizarra.pu() ## Levanta el lápiz
    pizarra.goto(x, y)

    ## Dibuja el led
    ##pizarra.dot(25, "red")
    if estado: pizarra.dot(5, "orange")
    else: pizarra.dot(5, "black")
    fondo_tablero.tracer(True)


def dibuja_leds():
    """ Dibuja los leds apagados.
        Entradas:
            Ninguna.
        Salidas:
            Ninguna.
        Restricciones:
            pizarra es una variable global que corresponde a una tortuga.
    """

    global pizarra
    
    ## Limpia la pantalla y oculta la tortuga
    pizarra.reset()
    pizarra.ht()

    ## El siguiente código es dummy.
    ## Permite dibujar 9 leds muy grandes apagados.
    ## Solo para fines ilustrativos !!!

    screen = pizarra.getscreen() ## Primero obtiene el
                                 ## turtle screen de la tortuga

    screen.tracer(False) ## Apaga la animación
    
    for x in range(-47,48):
        pizarra.pu()  ## Levanta el lápiz
        pizarra.setx(x*XDIS)
        pizarra.pd()  ## Baja el lápiz 
        for y in range(-9, 10):
            pizarra.pu()  ## Levanta el lápiz
            pizarra.sety(y*XDIS)
            pizarra.pd()  ## Baja el lápiz

        
            ## Dibuja un led apagado
            pizarra.dot(8, "red")  
            pizarra.dot(5, "black")

    screen.tracer(True) ## Enciende la animación

def detiene():
    global alto
    alto = True
    print("Fin !!")

def por_siempre():
    global pos, estado
    if not alto:
        anime()
        estado = not estado
        if estado: pos = (pos - 1) % -95
        fondo_tablero.ontimer(por_siempre, 1)


def crea_tablero(titulo, alto, ancho):
    """ Crea una pizarra electrónica.
        Entradas:
            titulo : título de la ventana que contendrá la
                     pizarra electrónica.
            alto   : alto de la ventana en pixeles.
            ancho  : ancho de la ventna en pixeles.
        Salidas:
            Ninguna.
        Restricciones:
            titulo es una tira, alto y ancho son enteros positivos.
    """
    assert isinstance(titulo, str)
    assert isinstance(alto, int) and alto > 0
    assert isinstance(ancho, int) and ancho > 0

    ## Crea la ventana y un canvas para dibujar
    root = TK.Tk()
    root.title(titulo)
    canvas = TK.Canvas(root, width=ancho, height=alto)
    canvas.pack()
    
    ## Crea un TurtleScreen y la tortuga para dibujar
    global fondo_tablero
    fondo_tablero = TurtleScreen(canvas)

    ## Establece el fondo de la pizarra electrónica
    canvas["bg"] = "black"
    canvas.pack()
    global pizarra
    pizarra = RawTurtle(fondo_tablero)

    dibuja_leds()

    ## Establece las funciones para capturar las teclas
    fondo_tablero.onkeypress(lambda : detiene(), "Escape")

    por_siempre()
    fondo_tablero.listen()
    print("terminó")    
    root.mainloop()
    

if __name__ == '__main__':
    crea_tablero("Pizarra Electrónica", 300, 900)
