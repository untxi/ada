from turtle import Screen, RawTurtle, register_shape

def inicializa():
    screen.title("Mi primer dibujo")

def rectangulo(largo=100, ancho=50):

    turtle.fd(largo)
    turtle.rt(90)
    turtle.fd(ancho)
    turtle.rt(90)
    
    turtle.fd(largo)
    turtle.rt(90)
    turtle.fd(ancho)
    turtle.rt(90)

def cuadrado(ancho=200):
    for i in range(4):
        turtle.fd(ancho)
        turtle.rt(90)

def triangulo(ancho=150):
    for i in range(3):
        turtle.fd(ancho)
        turtle.rt(120)
        
def casa(ancho=200):
    cuadrado(ancho)
    turtle.lt(60)
    triangulo(ancho)
    
def doodle(largo=100):
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

def patron01(largo=100):
    for i in range(4):
        doodle(largo)

def patron02(largo=100):
    for i in range(8):
        doodle(largo)
        turtle.rt(45)

def circulo(r=1):
    for i in range(360):
        turtle.fd(r)
        turtle.rt(1)
   
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

def cambioVestido():
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

def polyI(n, angulo, m = 50):
    for i in range(n):
        turtle.forward(m)
        turtle.left(angulo)
        
def coloque(x, y):
    turtle.pu()
    turtle.setpos(x,y)
    turtle.pd()

def dibuja2():
    trian(15,100)
    coloque(-100,-100)
    trian(35,80)
    coloque(-300,200)
    trian(8,300)

def getInput():
    return screen.textinput("Figura"," 1. Rectangle <lenght> <width>\n 2. Square <width>\n 3. Triangle <size>\
    \n 4. House <size>\n 5. Doole <length>\n 6. Pattern 1 <length>\n 7. Pattern 2 <length>\n 8. Circle <step>\n 9. Petal <size>\
    \n10.Flower <petals> <size>\n11.Inanimate Flower <petals> <size>\n12.Shape Change\n 0. Exit or <Enter>")

def invoca(f, n, ops):
    if len(ops) == 0:
        f()
    elif (len(ops) == 1 and n in (1,2)) or (len(ops) == 2 and n == 1):
        f(ops[0])
    elif len(ops) == 2 and n == 2:
        f(ops[0], ops[1])
    else:
        f()
          
from turtle import TurtleScreen, RawTurtle, TK

root = TK.Tk()
root.title("cambio de tamaño")
canvas = TK.Canvas(root, width=1000, height=1000,
                        bg="white")
canvas.pack()
screen = TurtleScreen(canvas)
turtle = RawTurtle(screen)



while True:
    x = getInput()
    if x in ["","0","00", None]:
        break
    turtle.reset()
    turtle.hideturtle()
    ops = [int(y) for y in x.split()]
    x = ops[0]
    if x == 1:
        invoca(rectangulo, 2, ops[1:])
    elif x == 2:
        invoca(cuadrado, 1, ops[1:])
    elif x == 3:
        invoca(triangulo, 1, ops[1:])
    elif x == 4:
        invoca(casa, 1, ops[1:])
    elif x == 5:
        invoca(doodle, 1, ops[1:])
    elif x == 6:
        invoca(patron01, 1, ops[1:])
    elif x == 7:
        invoca(patron02, 1, ops[1:])
    elif x == 8:
        invoca(circulo, 1, ops[1:])
    elif x == 9:
        invoca(petalo, 1, ops[1:])
    elif x == 10:
        invoca(flor, 2, ops[1:])
    elif x == 11:
        invoca(florNoAnimada, 2, ops[1:])
    elif x == 12:
        cambioVestido()

screen.mainloop()
