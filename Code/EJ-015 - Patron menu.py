## ***********************************************
##
## Programa: EJ-015 Patrón Menú.py
## Autor   : JCGP
## Fecha   : Marzo, 2013
##
## Muestra un menú y permite que el usuario seleccione una
## opción.  Si el usuario no selecciona ninguna o digita
## la palabra fin el programa termina.
## Si el usuario teclea ? el programa muestra la lista de
## opciones.
## Luego que el usuario selecciona una opción el programa
## le pide al usuario que digite un valor entero, con el
## cual realizará el procesamiento.
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

## Funciones que implementan las opciones
## que procesa el programa

def Rectángulo(alto, ancho):
    """ *** Entrada: alto y ancho

            Salida:

            Restricciones: Las entradas son valores numericos ***
    """
    
    return ("\n+" + (ancho - 2) * "=" + "+\n" + \
           (alto - 2) * ("|" + " " * (ancho - 2) + "|\n") + \
            


def ÁrboldeNavidad(alto):
    """ *** Construir un árbol de navidad ***
    """
    return alto

def Cruz(n):
    """ *** Comentarios de fc ***
    """
    return n

## flecha hacia derecha
def flecha_der(n):
    assert isinstance(n, int) and n > 0

    flecha = ""

    # Se genera la parte superior
    for i in range(1, n):
        flecha += " " * n + "*" * i + "\n"
        
    # Se gerena el medio
    flecha += "=" * n +  "*" * n + "\n" 

    # Se genera la parte inferior
    for i in range(n-1, 0, -1):
        flecha += " " * n + "*" * i + "\n"
     
    # Ilustra
    return flecha

    #### USO
        # t = flecha_der(n)
        # print(t)


## diamante
def diamante(n):
    diamante = ""
    
    # Se genera la parte superior
    for i in range(1, n):
        diamante += " " * (n-i) + "*" * (2*i-1) + "\n"

    # Se gerena el medio
    diamante += "*" * (2*n-1) + "\n"

    # Se genera la parte inferior
    for i in range(n-1,0, -1):
        diamante += " " * (n-i) + "*" * (2*i-1) + "\n"

    # Ilustra
    return diamante

#### diamante 2
##    # Se genera la parte superior
##    blancos = n-1
##    aster = 1
##    
##    for i in range(1, n):
##        diamante += " " * blancos + "*" * aster + "\n"
##        blancos -= 1
##        aster   += 2
            
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

    print("Menu. Versión 1.0")
    print("--------------------")
    instrucciones = """a. Dibujer 1\nb. Opción 2\nc. Opción 3\nd. Opción 4"""
    print(instrucciones)

    ## Lectura de la opción

    opcion = input("opción > ")

    while opcion:

        if opcion == "?":
            print(instrucciones)
        elif opcion == "fin":
            break
        elif opcion in ["a", "b", "c", "d"]:
            
            n_str = input(".... n > ")
            n = int(n_str)if n_str.isdigit() else 0

            if opcion == "a":

                ## Lee alto y ancho
                
                alto_str =  input("....alto > ")
                ancho_str = input("....ancho > ")
                alto = int(alto_str)if alto_str.isdigit() else 0
                ancho = int(ancho_str) if ancho_str.isdigit() else 0

                ## Imprima el Rectángulo
                
                print("op-a >>>", Rectángulo(alto,ancho))
                
            elif opcion == "b":

                ##Lee alto

                alto_str = int("....alto > ")
                alto = int(alto_str)if alto_str.isdigit() else 0
                print("op-b >>>", ÁrboldeNavidad(alto))
            elif opcion == "c":
                print("op-c >>>", Cruz(orden))
         

        opcion = input("opción > ")

    print("Fin !!!")

if __name__ == "__main__":
    control_principal()


