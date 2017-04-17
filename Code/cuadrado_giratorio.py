from turtle import TurtleScreen, RawTurtle, TK

root = TK.Tk()
root.title("Ejemplo 1")
canvas = TK.Canvas(root, width=500, height=500)
canvas.pack()
    
turtle = RawTurtle(screen)

turtle.shape("turtle")

turtle.left(20)

turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
delay(1000)
turtle.left(30)

turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)

turtle.left(40)

turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)

screen.mainloop()
