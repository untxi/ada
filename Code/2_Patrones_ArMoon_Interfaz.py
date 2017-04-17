## ========================================================================== ##
## 
## Programa: 2_Patrones_ArMoon_Interfaz.py
## Autores : Arburola León, Samantha P.
##           Rojas Alfaro,  Luis A.
## Fecha   : 07.05.2014
##
##  Dibujar Patrones ArMoon con una tortuga en una ventana. Con fun-
## cionalidad de suma, guardando los operando y representandolos, así
## como el resultados final, habilitando la limpieza de la ventana para
## una nueva operación y el cierre del programa desde un menú con botones.
##
## Entradas:
##      Operandos, valores enteros positivos a sumar.
## Salidas:
##      Dibujos de los Patrones ArMoon de los operandos y resultado de la suma.
## Restricciones:
##      Los valores de los operandos deben ser enteros positivos, en caso de no  
##      reconocer el valor el programa presentará un cero. 
## ========================================================================== ##

""" ======================= IMPORTACIÓN DE RECURSOS ======================== """
## Importar Recursos
import turtle
from turtle import *
import tkinter
from tkinter import *
import time
from tkinter import messagebox
""" ======================================================================== """

""" =================== DEFINICIÓN DE VARIABLES GLOBALES =================== """
## Lista en la que se van a incluir los sumandos.
lista_sumandos = []
## Posición inicial de X.
x = 435
## Posición Inicial de Y.
y = 300
""" ======================================================================== """

""" ==================== OPERACIONES DE SUMA ARMOON ======================== """
## Operador
def sumando(sumando):
    """ Retorna el operando a partir de la revisión de las restricciones.
        En caso de ser un dígito válido retorna el valor correpondiente,
        de lo contrario la salida será 0.

        Entrada:
            Número correspondiente al operando.

        Salida :
            Dibujo del PAtrón ArMoon.

        Restricciones:
            La entrada debe ser un entero positivo.
    """
    ## Restricciones
    assert isinstance(sumando, str)
    ## Revisión
    sumando = int(sumando)if sumando.isdigit() else 0
    ## Agrega los valores de los operandos a la lista para la suma general
    lista_sumandos.append (sumando)
    ## Salida/ Dibujo
    dibuja_patron (sumando)

## Función de Verificación para listas
def esNumerica(lista_sumandos):
    """ Verifica si todos los elementos de una lista son valores numéricos
        enteros positivos.
        
        Entrada:
            lista_sumandos, lista por verificar.
        Salida:
            True,  Para una lista con todos las instancias numéricas >= 0.
            False, En caso de encontrar una instancia no numérica.
        Restricción:
            La entrada debe ser una instancia de listas.
    """
    ## Restriccioines
    assert isinstance(lista_sumandos, list)
    ## Proceso
    i = 0
    while i < len(lista_sumandos):
        if not(isinstance(lista_sumandos[i], int)):
            lista_sumandos[i] = 0
        i += 1
    ## Salida
    return lista_sumandos

## Suma ArMoon de 2 valores
def suma2_ArMoon(sumando1, sumando2):
    """ Suma dos sumandos decimales en ArMoon
        Entrada:
            sumando1 y sumando2
        Salidas:
            resultado, resultado de la sumar ArMoon en decimal
        Restricciones:
            las entradas son enteros postivo
    """
    ## Restriciones
    assert isinstance(sumando1, int) ##and sumando1 >= 0
    assert isinstance(sumando2, int) ##and sumando2 >= 0
    ## Ciclo para obtener la concatenación del resultado de la sumas
    resultado = ""
    while sumando1 or sumando2:
        result = ((sumando1 % 64) + (sumando2 % 64)) % 64
        result = bin(result)
        i, s = 2, ""
        while i < len(result):
            s += result[i]
            i += 1
        resultado = s.zfill(6) + resultado
        sumando1 //= 64
        sumando2 //= 64
    resultado = resultado if str(resultado).isdigit() else "000000"
    ## Salida
    if resultado == "":
        resultado = "0"
    return int(resultado, 2)

## Suma ArMoon de valores multiples
def suma_ArMoon(lista_sumandos):
    """ Suma en formato ArMoon los valores numéricos de una lista
        con instancias decimales.

        Entrada:
            lista_sumandos, una lista con todos los sumandos por procesar.
        Salidas:
            Dibuja el Patrón Armoon del resultado de toda la suma.
        Restricciones:
            - La entrada debe ser una lista donde cada instancia sea un valor
            numérico decimal entero positivo.
            - Si no lo es sustituirá el error con un cero.
    """
    ## Restriciones
    assert isinstance(lista_sumandos, list) #and lista_sumandos != []
    ## Globales
    global x, y
    ## Revisión de la lista
    if lista_sumandos == []:
        lista_sumandos.append(0)
    lista_sumandos = esNumerica(lista_sumandos)
    ## Ciclo para obtener la concatenación del resultado de la sumas
    i = 0
    resultado = 0
    while i < len(lista_sumandos):
        resultado = (suma2_ArMoon(resultado, lista_sumandos[i]))
        i += 1
    ## Dibuja línea divisora
    lienzo.tracer(False)
    tod.pu()
    tod.goto(x-870, y+17)
    tod.pd()
    tod.pensize(2)
    tod.color("green")
    tod.fd(890)
    lienzo.tracer(True)    
    ## Salida
    dibuja_patron(resultado)
""" ======================================================================== """

""" ===================== DIBUJAR EL LIENZO DE TRABAJO ===================== """
## Dibuja el lienzo
""" Crear Ventana de Dibujo """
turtle.setup(1000, 650)
lienzo = turtle.Screen()
lienzo.bgcolor("darkgray")
lienzo.title("Patrones ArMoon")
# Crea la tortuga tod y sus atributos
tod = turtle.Turtle()
tod.color("#ffffff")
tod.pensize(1)
""" ======================================================================== """

""" ==== FUNCIÓN: LIMPIAR EL LIENZO Y RESTABLECER LOS VALORES GLOBALES ===== """
## Clear Screen
def clear_screen(ventana):
    """ Limpia la ventana y posiciona la tortuga en 0,0.
        Entrada:
            ventana, el nombre de la ventana para limpiar
        Salida:
            Ninguna.
        Restricciones:
            Ninguna.
    """
    ## Limpiar el lienzo
    tod.reset()
    ## Restablacer los valores de las variables globales
    global lista_sumandos, x, y
    lista_sumandos = []
    x = 450
    y = 310
""" ======================================================================== """

""" ==== FUNCIÓN: DIRECCIONES DE LOS PATRONES ============================== """
## Hexágono
def hexagono(_6bits):
    """ Dibuja un hexágono codificado en ArMoon a partir de una tira de 6bits.
        Entrada:
            _6bits, una tira con 6 bits para reconocer
        Salida:
            Dibuja el hexágono.
        Restricciones:
            La entrada debe ser un string de largo 6.
    """
    ## Restricción
    if not(isinstance(_6bits, str)):
        _6bits = "000000"
    elif len(_6bits) < 6:
        _6bits.zfill(6)
    ## Colores respectivos a 0 y 1
    rellena1 = "turquoise" ## Color para 0
    rellena0 = "gray"      ## Color para 1
    ## Asignación de colores
    colores = []
    i = 0
    while i < len(_6bits):
        if _6bits[i] == "0":
            colores.append(rellena0)
        elif _6bits[i] == "1":
            colores.append(rellena1)
        i += 1
            
    ## Dibujo
    lienzo.tracer(False) ## Desactiva la visualización del dibuja
    tod.speed(10000)         ## Velocidad de la tortuga para dibujar
    ## Triángulo 0
    tod.color("white", colores[5]) 
    tod.begin_fill()
    tod.forward(15)
    tod.left(120)
    tod.forward(15)
    tod.left(120)
    tod.forward(15)
    tod.left(120)
    tod.end_fill()
    tod.fd(15)
    ## Triángulo 1
    tod.color("white",colores[4])
    tod.begin_fill()
    tod.left(120)
    tod.forward(15)
    tod.right(120)
    tod.forward(15)
    tod.right(120)
    tod.fd(15)
    tod.end_fill()
    ## Triángulo 2
    tod.color("white",colores[3])
    tod.begin_fill()
    tod.left(120)
    tod.forward(15)
    tod.left(120)
    tod.forward(15)
    tod.left(120)
    tod.forward(15)
    tod.end_fill()
    ## Triángulo 3
    tod.color("white",colores[2])
    tod.begin_fill()
    tod.fd(15)
    tod.right(120)
    tod.fd(15)
    tod.right(120)
    tod.fd(15)
    tod.end_fill()
    ## Triángulo 4
    tod.color("white",colores[1])
    tod.begin_fill()
    tod.right(120)
    tod.forward(15)
    tod.left(120)
    tod.forward(15)
    tod.left(120)
    tod.forward(15)
    tod.end_fill()
    ## Triángulo 5
    tod.color("white",colores[0])
    tod.begin_fill()
    tod.right(120)
    tod.forward(15)
    tod.right(120)
    tod.forward(15)
    tod.right(120)
    tod.forward(15)
    tod.end_fill()
    lienzo.tracer(True) ## Activa la visualización del dibuja
    tod.pu()  ## Sube lapiz
    ## La traslada al punto para iniciar el siguiente patrón
    tod.left(60)
    tod.fd(30)
    tod.pd()  ## Baja lapiz
    
## Reloj
def reloj(_6bits):
    """ Dibuja un Patrón de tipo 2 ArMoon codificado en ArMoon a
        partir de una tira de 6 bits.        
        Entrada:
            6bits, una tira con 6 bits para reconocer
        Salida:
            Dibuja el hexágono.
        Restricciones:
            La entrada debe ser un string de largo 6.
    """
    ## Restricción
    if not(isinstance(_6bits, str)):
        _6bits = "000000"
    elif len(_6bits) < 6:
        _6bits.zfill(6)
    ## Colores respectivos a 0 y 1
    rellena1 = "turquoise" ## Color para 0
    rellena0 = "gray"      ## Color para 1
    ## Asignación de colores
    colores = []
    i = 0
    while i < len(_6bits):
        if _6bits[i] == "0":
            colores.append(rellena0)
        elif _6bits[i] == "1":
            colores.append(rellena1)
        i += 1
    ## Dibujo
    # Arena
    lienzo.tracer(False)
    tod.speed(10000)
    ## Triángulo 0
    tod.color("white",colores[5])
    tod.begin_fill()
    tod.left(120)
    tod.back(15)
    tod.left(60)
    tod.fd(15)
    tod.right(120)
    tod.fd(15)
    tod.end_fill()
    ## Triángulo 1
    tod.color("white",colores[4])
    tod.begin_fill()
    tod.right(180)
    tod.fd(15)
    tod.right(120)
    tod.fd(15)
    tod.left(60)
    tod.back(15)
    tod.end_fill()
    ## Triángulo 2
    tod.color("white",colores[3])
    tod.begin_fill()
    tod.fd(15)
    tod.left(120)
    tod.fd(15)
    tod.right(120)
    tod.fd(15)
    tod.right(120)
    tod.fd(15)
    tod.end_fill()
    tod.right(60)
    tod.fd(15)
    ## Triángulo 3
    tod.color("white",colores[2])
    tod.begin_fill()
    tod.left(120)
    tod.fd(15)
    tod.right(120)
    tod.fd(15)
    tod.right(120)
    tod.fd(15)
    tod.end_fill()
    ## Triángulo 4
    tod.color("white",colores[1])
    tod.begin_fill()
    tod.right(60)
    tod.fd(15)
    tod.right(120)
    tod.fd(15)
    tod.right(120)
    tod.fd(15)
    tod.end_fill()
    tod.back(15)
    tod.right(120)
    tod.fd(15)
    ## Triángulo 5
    tod.color("white",colores[0])
    tod.begin_fill()
    tod.left(120)
    tod.fd(15)
    tod.left(120)
    tod.fd(15)
    tod.end_fill()
    lienzo.tracer(True)  ## Mostrar reloj

    ## Acomodo siguiente par patron
    tod.pu()
    tod.right(120)
    tod.fd(15)
    tod.left(60)
    tod.fd(30)
    tod.right (60)
    tod.left (240)
    tod.pd()
""" ======================================================================== """

""" === FUNCIÓN: DIBUJAR PATRONES ARMOON =================================== """
def dibuja_patron(operando):
    global master
    """ Recibe un número decimal para el cual va a realizar la
        concatenación de bits los cuales formaran el patrón ArMoon.

        Entrada:
            número decimal 
        Salida :
            Dibujo del Patrón ArMoon.
        Restricciones:
            La entrada debe ser entero positivo.
    """
    ## Restriciones
    assert isinstance(operando, int)
    # Dirección de la posición Inicial
    global x, y
    tod.pu()
    tod.tiltangle(180)
    tod.goto(x,y)
    tod.pd()
    ## Ciclo para dibujar los patrones del operando 
    if operando == 0:
        hexagono("000000")
        tod.pu()
        tod.fd(30)
        tod.left(180)
    elif operando < 0:
        operando = abs(operando)
    ## Dibujar los partones
    i = 0  
    while operando > 0:
        _6bits = operando % 64
        _6bits = bin(_6bits)[2:].zfill(6)
        ## Dibujo 
        if i % 2 == 0:
            hexagono(_6bits)
        elif i % 2 == 1:
            reloj(_6bits)
        operando = operando // 64
        i += 1
    ## Posicionnar la tortuga para el próximo Patrón
    if i % 2 == 1:
        tod.pu()
        tod.fd(30)
        tod.left(180)
    
    tod.pu()
    y -= 30
    x = 435
    tod.goto(x, y)
    ventana_general()
""" ======================================================================== """

""" ================== FUNCIONES AUXILIARES PARA EL MENÚ =================== """
def con_suma(ventan):
    suma_ArMoon(lista_sumandos)
    ventan.iconify()
    time.sleep(2)
    ventan.deiconify()

def contra_general(ventana):
    """ Función para quitar la ventana general
    """
    ventana.destroy()

def limpieza(ventana,ventanas):
    """ Función para ejecutar la limpieza del lienzo de trabajo
    """
    clear_screen(ventanas)
    ventana.withdraw()

def ocultar(ventana,ventana2):
    ventana.withdraw() # Oculta una ventana
    ventana2.withdraw()
    global lienzo
    lienzo.bye() 
""" ======================================================================== """

""" === FUNCIÓN: VENTANA MENÚ GENERAL INTERACTIVA ========================== """
def ventana_general():
    """ Presenta la ventana del Menú Principal.
        Muestra los botones correspondientes a:
            Operandos
            Suma
            Limpiar
            Salir
            
        Entradas:
            Ninguna.
        Salidas:
            Ninguna.
        Restricciones:
            Ninguna.
            
    """
    global general
    general = tkinter.Tk()
    general.config(bg = "black")
    general.geometry ("225x160+600+300") ## Ancho, Largo, X Y (posiciona ventana pantalla)
    general.title ("Patrones Armoon")
    ############  MENU   ############
    bienvenida = tkinter.Label(general,text = "Bienvenido a Patrones Armoon", font = "Century 11")
    bienvenida.config(bg = "black")
    bienvenida.config(fg = "white")
    bienvenida.pack()

    bienvenida1 = tkinter.Label(general,text = "▲▼▲▼▲▼▲▼▲▼▲▼▲▼", font = "Century 11")
    bienvenida1.place(x = 10, y = 40)
    bienvenida1.config(bg = "black")
    bienvenida1.config(fg = "white")
    bienvenida1.pack()

    verifica = tkinter.Label(general,text = "Elija una de las siguientes opciones:", font = "Constantia 10")
    verifica.config(bg = "black")
    verifica.config(fg = "white")
    verifica.pack()

    opc1 = tkinter.Button(general, text = "► Operandos ◄", font = "Rockwell 10", relief = "ridge", command = ventana_operando)
    opc1.place(x = 5, y = 80)
    opc1.config(bg = "black")
    opc1.config(fg = "white")

    opc2 = tkinter.Button(general, text = "►       Suma      ◄", font = "Rockwell 10", relief = "ridge", command=lambda: con_suma(general))
    opc2.place(x = 117, y = 80)
    opc2.config(bg = "black")
    opc2.config(fg = "white")

    opc3 = tkinter.Button(general, text = "►     Limpiar    ◄", font = "Rockwell 10", relief = "ridge", command= ventana_alerta)
    opc3.place(x = 5, y = 118)
    opc3.config(bg = "black")
    opc3.config(fg = "white")

    opc4 = tkinter.Button(general, text = "►      Salir         ◄", font = "Rockwell 10", relief = "ridge",command= ventana_salida )
    opc4.place(x = 117, y = 118)
    opc4.config(bg = "black")
    opc4.config(fg = "white")
""" ======================================================================== """

""" === FUNCIÓN: VENTANA INGRESO DE OPERANDO =============================== """
def ventana_operando ():
    global num_op
    global general

    contra_general(general)
    
    def show_entry_fields():
        master.withdraw()
        sumando (e1.get())

    master = Tk()
    master.title("Patrones ArMoon")
    master.config(bg = "black")
    master.geometry("200x150+600+300")


    bienvenida = Label(master, text = "Bienvenido a Patrones Armoon", font = "Century 10")
    bienvenida.config(bg = "black")
    bienvenida.config(fg = "white")
    bienvenida.pack()

    verifica = Label(master, text = "Opción 1. Operandos de Suma.", font = "Centaur 12")
    verifica.config(bg = "black")
    verifica.config(fg = "white")
    verifica.pack()

    intro =Label(master, text = "Digite un número", font = "Constantia 10")
    intro.place(x = 75, y = 58)
    intro.config(bg = "black")
    intro.config(fg = "white")

    operando = Label(master, text = ("Patrón:"), font = "Century 10")
    operando.place(x = 10, y = 80)
    operando.config(bg = "black")
    operando.config(fg = "white")


    e1 = Entry(master)
    e1.place(x = 65, y = 80)


    botonaceptar = Button(master,text = "      Aceptar      ", font = "Rockwell 10", command = show_entry_fields)
    botonaceptar.place(x = 8, y = 115)
    botonaceptar.config(bg = "black")
    botonaceptar.config(fg = "white")

    botonsalir = Button (master, text = "       Menú        ", font = "Rockwell 10", command=  master.destroy)
    botonsalir.place(x = 106, y = 115)
    botonsalir.config(bg = "black")
    botonsalir.config(fg = "white")   
""" ======================================================================== """

""" === FUNCIÓN: ALERTA PARA BORRAR ======================================== """
def ventana_alerta():
    global lienzo
    global general
    
    alerta= tkinter.Tk()
    alerta.config(bg = "black")
    alerta.geometry("225x100+600+300") ## Ancho, Largo, X Y (posiciona ventana pantalla)
    alerta.title("Patrones Armoon")
    ############  MENU   ############
    aviso = tkinter.Label(alerta,text = "¿Esta seguro que desea borrar los datos?",font = "Century 8")
    aviso.place(x = 4, y = 25)
    aviso.config(bg = "black")
    aviso.config(fg = "white")

    botonacepta = tkinter.Button(alerta,text = "     Aceptar     ", font = "Rockwell 10", command= lambda: limpieza(alerta,lienzo))
    botonacepta.place(x = 17, y = 60)
    botonacepta.config(bg = "black")
    botonacepta.config(fg = "white")

    botoncancela = tkinter.Button (alerta, text = "    Cancelar    ", font = "Rockwell 10",command= lambda: alerta.withdraw())
    botoncancela.place(x = 125, y = 60)
    botoncancela.config(bg = "black")
    botoncancela.config(fg = "white")
""" ======================================================================== """

""" === FUNCIÓN: ALERTA DE SALIDA ========================================== """
def ventana_salida():
    global general
    
    salida = tkinter.Tk()
    salida.config(bg = "black")
    salida.geometry("225x100+600+300") ## Ancho, Largo, X Y (posiciona ventana pantalla)
    salida.title("Patrones Armoon")
    ############  MENU   ############
    avisalida = tkinter.Label(salida, text = "¿Esta seguro que desea salir?", font = "Century 10")
    avisalida.place(x = 25, y = 25)
    avisalida.config(bg = "black")
    avisalida.config(fg = "white")

    botonacepta = tkinter.Button(salida, text = "     Aceptar     ", font = "Rockwell 10",command=lambda: ocultar(salida,general))
    botonacepta.place(x = 25, y = 60)
    botonacepta.config(bg = "black")
    botonacepta.config(fg = "white")

    botoncancela = tkinter.Button(salida, text = "    Cancelar    ", font = "Rockwell 10", command = salida.destroy)
    botoncancela.place(x = 125,y = 60)
    botoncancela.config(bg = "black")
    botoncancela.config(fg = "white")
    
""" ======================================================================== """

""" -  -  -  -  -  -  -  -  -  - Menú Principal -  -  -  -  -  -  -  -  -  - """
ventana_general()
