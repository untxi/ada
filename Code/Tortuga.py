from turtle import Screen, RawTurtle

screen = Screen()
turtle = RawTurtle(screen)

### Traje
turtle.shape("turtle")


## Tamaño del punto y color
turtle.dot(5, "green")
turtle.fd(50)

turtle.dot(5, "red")
turtle.lt(120)## Gira a la izquierda
turtle.fd(100)## Avanza 100

turtle.dot(5, "blue")
turtle.lt(170)
turtle.fd(150)

turtle.lt(170)

screen.mainloop() ## La pantalla espera un evento...
