from turtle import Screen, RawTurtle

screen = Screen()
turtle = RawTurtle(screen)

### Traje
turtle.shape("turtle")


## Tamaño del punto y color
turtle.pu()
turtle.dot(7, "red")
turtle.fd(40)

turtle.pd()
turtle.rt(90)
turtle.fd(40)
turtle.dot(5, "red")

turtle.rt(90)
turtle.fd(80)
turtle.dot(5, "red")

turtle.rt(90)
turtle.fd(80)
turtle.dot(5, "red")

turtle.rt(90)
turtle.fd(80)
turtle.dot(5, "red")

turtle.rt(90)
turtle.fd(40)


turtle.pu()
turtle.rt(90)
turtle.fd(40)





"""
turtle.dot(5, "red")
turtle.dot(5, "blue")
turtle.lt(170)
turtle.fd(150)

turtle.lt(170)

screen.mainloop() ## La pantalla espera un evento...
"""
