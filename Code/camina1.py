from turtle import TurtleScreen, RawTurtle, TK
pos = 47
XDIS = 9  
alto = False 
estado = True

def anime():
    ## Determina la posición del led a encender
    fondo_tablero.tracer(False)
    pizarra.pu()
    x = (pos ) * 9
    for y1 in range((-9),10):
        y = y1 * 9
        pizarra.goto(x, y)
        if estado: pizarra.dot(5, "orange")
        else: pizarra.dot(5, "black")
    fondo_tablero.tracer(True)


def dibuja_leds():
    global pizarra

    pizarra.reset()
    pizarra.ht()
    screen = pizarra.getscreen() 
    screen.tracer(False)     
    pizarra.pu()
    for x in range(-47,48):
        pizarra.setx(x*XDIS)
        for y in range((-9), 10):
            pizarra.sety(y*XDIS)
            pizarra.dot(8, "red")  
            pizarra.dot(5, "black")
    pizarra.pu()
    screen.tracer(True) 

def detiene():
    global alto
    alto = True
    print("Fin !!")

def por_siempre():
    global pos, estado
    if not alto:
        anime()
        estado = not estado
        if estado:
            if pos == (-47):
                pos += 94
            else:
                pos -= 1 
        fondo_tablero.ontimer(por_siempre, 150)


def crea_tablero(titulo, alto, ancho):
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
    crea_tablero("Pizarra Electrónica", 250, 900)
