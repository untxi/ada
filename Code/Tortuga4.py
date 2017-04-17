from turtle import Screen, RawTurtle

def inicializa():

    global screen, turtle
    screen= Screen()
    screen.title("Mi dibujito")
    turtle = RawTurtle(screen)

def rectangulo(largo, ancho):

    turtle.fd(largo)
    turtle.rt(90)
    turtle.fd(ancho)
    turtle.rt(90)

    turtle.fd(largo)
    turtle.rt(90)
    turtle.fd(ancho)
    turtle.rt(90)

def cuadrado(ancho):

    for i in range(4):
        turtle.fd(ancho)
        turtle.rt(90)

def triangulo(ancho):
    for i in range (3):
        turtle.fd(ancho)
        turtle.rt(120)

def casa(ancho):
    cuadrado(ancho)
    turtle.lt(60)
    triangulo(ancho)

def poly(n,angulo, m=50):
    for i in range(n):
        turtle.forward(n)
        turtle.left(angulo)
def petalo(tam=60):
    turtle.circle(tam,60)
    turtle.lt(120)
    turtle.circle(tam,60)
    turtle.lt(120)

def flor(petalos=8, tam=60):
    giro = 360 // petalos
    for i in range(petalos):
        petalo(tam)
        turtle.rt(giro)

def florNoAnimada(petalos=8, tam=60):
    screen.tracer(False)
    flor(petalos,tam)
    screen.tracer(True)
    
inicializa()
"""rectangulo(60,30)"
cuadrado(30)

"""
"""triangulo(30)

casa(30)"""
florNoAnimada(500,5)
screen.exitonclick()
    
    
    




