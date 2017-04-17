## Programa: Menú. tiras
## Autor   : Dennisse Rojas
## Fecha   : Abril, 2013
##
## Muestra un menú y permite que el usuario seleccione una
## opción.  Si el usuario no selecciona ninguna o digita
## la palabra fin el programa termina.
## Si el usuario teclea ? el programa muestra la lista de
## opciones.
##
## Entradas:
##      opcion.
##
## Salidas:
##      Mensaje con la opción seleccionada.
##
## Restricciones:
##      Ninguna.
##
## ***********************************************

# Definición de variables globales:
tira = ""

## Funciones que implementan las opciones
## que procesa el programa

def asignar():
    """ *** Asigna una valor a la tira ***
    """
    global tira
    tira = input ("Digite su tira: ") 

def invertir():
    """ *** Invierte el orden de los caracteres de la tira ***
    """
    global tira 
    tira = tira[::-1]
    
def concatenar():
    """ *** une dos tiras ***
    """

def largo():
    """ *** Permite obtener el largo de la tira***
    """
    print ("Largo: ", len (tira))
def imprimir():
    """ *** Imprime la tira ***
    """
    print (tira)


def control_principal():
    """ Procedimiento que implementa el control principal
        basado en un menu básico de opciones.

        Entradas:
            Ninguna.

        Salidas:
            Ninguna.

        Restricciones:
            Ninguna.
    """
        
    ## Presentación del programa

    print("Menu. Tiras")
    print("--------------------")
    instrucciones = """a. Asignar\nb. Invertir\nc. Concatenar\nd. Largo\ne. Imprimir"""
    print(instrucciones)

     ## Lectura de la opción

    opcion = input("opción > ")

    while opcion:

        if opcion == "?":
            print(instrucciones)
        elif opcion == "fin":
            break
        elif opcion in ["a", "b", "c", "d", "e"]:
        
            if opcion == "a":
                asignar()
            elif opcion == "b":
                invertir()
            elif opcion == "c":
                concatenar()
            elif opcion == "d":
                largo()
            elif opcion == "e":
                imprimir()

        opcion = input("opción > ")

    print("Fin !!!")

if __name__ == "__main__":
    control_principal()
