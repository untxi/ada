from turtle import  RawTurtle, register_shape

def inicializa():
    screen.title("Mi primer dibujo")

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
    for i in range(3):
        turtle.fd(ancho)
        turtle.rt(120)
        
def casa(ancho):
    cuadrado(ancho)
    turtle.lt(0)
    triangulo(ancho)
    
def doodle(largo):
    turtle.fd(largo)
    turtle.rt(90)
    turtle.fd(largo)
    turtle.rt(90)
    turtle.fd(largo // 2)
    turtle.rt(90)
    turtle.fd(largo // 2)
    turtle.rt(90)
    turtle.fd(largo)
    turtle.rt(90)
    turtle.fd(largo // 4)
    turtle.rt(90)
    turtle.fd(largo // 4)
    turtle.rt(90)
    turtle.fd(largo // 2)

def patron01(largo):
    for i in range(4):
        doodle(largo)

def patron02(largo):
    for i in range(8):
        doodle(largo)
        turtle.rt(45)

def circulo(r):
    for i in range(360):
        turtle.fd(r)
        turtle.rt(1)
   
def petalo(tam):
    turtle.circle(tam,60)
    turtle.lt(120)
    turtle.circle(tam,60)
    turtle.lt(120)

def flor(petalos, tam):
    giro = 360 // petalos
    for i in range(petalos):
        petalo(tam)
        turtle.rt(giro)

def florNoAnimada(petalos, tam):
    screen.tracer(False)
    flor(petalos,tam)
    screen.tracer(True)

def cambioVestido():
    ##screen.tracer true animacion false no animacion
    screen.tracer(False)
    turtle.begin_poly()
    flor(6,100)
    turtle.end_poly()
    screen.register_shape("flor", turtle.get_poly())
    screen.tracer(True)
    turtle.reset()
    turtle.shape("flor")
    turtle.pu()
    turtle.speed(1)
    for i in range(200):
        turtle.rt(3)
    turtle.resizemode("user")
    turtle.turtlesize(10,10)
    screen.colormode(255)
    turtle.color((50,180,10),(255,120,0))
    turtle.seth(0)
    turtle.pd()
    cuadrado(150)

def prueba():
    turtle.speed(1)
    screen.delay(10)
    turtle.begin_poly()
    triangulo(50)
    turtle.end_poly()
    screen.register_shape("uno", turtle.get_poly())
    turtle.reset()
    turtle.speed(1)
    screen.delay(10)

    turtle.shape("uno")
    cuadrado(200)

def trian(angulo, largo):
    turtle.seth(0)
    x0 = turtle.xcor()
    y0 = turtle.ycor()
    turtle.lt(angulo)
    turtle.fd(largo)
    turtle.setpos(turtle.xcor(),y0)
    turtle.setpos(x0,y0)
    turtle.seth(0)

def poly(n, m = 50):
    angulo = 360 // n
    for i in range(n):
        turtle.forward(m)
        turtle.left(angulo)

def getInput():
    return screen.textinput("Figura"," 1. Rectangle\n 2. Square\n 3. Triangle\
    \n 4. House\n 5. Doole\n 6. Pattern 1\n 7. Pattern 2\n 8. Circle\n 9. Petal\
    \n10.Flower\n11.Shape Change\n 0. Exit or <Enter>")

def param(default, n):
    return default if len(ops) == 1 in range(1,n+1) else ops[n]

from turtle import TurtleScreen, RawTurtle, TK

root = TK.Tk()
root.title("cambio de tamaño")
canvas = TK.Canvas(root, width=1000, height=1000,
                        bg="white")
canvas.pack()
screen = TurtleScreen(canvas)
turtle = RawTurtle(screen)

turtle.shape("turtle")
turtle.speed(5)
while True:
    x = getInput()
    if x in ["","0","00"] or x == None:
        break
    turtle.reset()
    ops = [int(y) for y in x.split()]
    x = ops[0]
    if x == 1:
        rectangulo(100, 50)
    elif x == 2:
        cuadrado(200)
    elif x == 3:
        triangulo(150)
    elif x == 4:
        casa(100)
    elif x == 5:
        doodle(100)
    elif x == 6:
        patron01(100)
    elif x == 7:
        patron02(50)
    elif x == 8:
        circulo(1)
    elif x == 9:
        petalo(80)
    elif x == 10:
        flor(10,60)
    elif x == 11:
        cambioVestido()
screen.mainloop()
