stringLab = "00000000000000\n" + \
            "01111111111110\n" + \
            "00000000000010\n" + \
            "01111111111110\n" + \
            "01111111111110\n" + \
            "01111111111110\n" + \
            "00000000003110"

def creaLaberinto(stringLab) :
    """ Crea un laberinto a partir de una tira de entrada.
        Entradas:
             stringLab : tira que contiene el diseño del
                         laberinto.
        Salidas:
             Laberinto representado por una matriz, tal que
             la entrada i,j contiene: 0 - si la casilla está
             libre, 1 - si hay pared, 3 - posición en donde
             está el queso.
        Restricciones:
             Todas las entradas de la tira son 0, 1 o 3. Las
             filas se representan por un cambio de línea.
             No hay líneas vacías.
    """

    lista = stringLab.split()
    lista = [ x[:-1] if x[-1] == "\n" else x for x in lista]
    lista = [[int(ch) for ch in x] for x in lista]
    return lista

def impLab(laberinto):
    """ Imprime un laberinto.
        Entradas:
             laberinto : laberinto a imprimir.
        Salidas:
             Ninguna.
        Restricciones:
             El laberinto está representado por listas de
             listas, y es una representación consistente. """
        
    for x in laberinto:
        for y in x:
            print(y, end= "")
        print()

def recorrido(i, j):
    """ Dado un laberinto en donde se ubica un queso,
        retorna en una lista de pares ordenados (x,y)
        que indican el camino desde una posición inicial
        (i,j) hasta la posición en que se encuentra el
        queso.
        Entradas:
             (i, j) : posición inicial a partir de donde
                      se realizará la búsqueda de un camino
                      hasta la posición del queso.
        Salidas:
             Lista con las casillas, expresadas como pares
             ordenados, que llevan desde la posición inicial
             hasta la posición en que se encuentra el queso.
             Si no existe un camino retorna la lista vacía.
    """

    if laberinto[i][j] == 3:
        return [(i, j)]

    if laberinto[i][j] == 1:
        return []

    laberinto[i][j] = -1

    if i > 0 and laberinto[i - 1][j] in [0, 3]:                     # Norte
        camino = recorrido(i - 1, j)
        if camino: return [(i, j)] + camino

    if j < len(laberinto[i]) - 1 and laberinto[i][j + 1] in [0, 3]: # Este
        camino = recorrido(i, j + 1)
        if camino: return [(i, j)] + camino

    if i < len(laberinto) - 1 and laberinto[i + 1][j] in [0, 3]:    # Sur
        camino = recorrido(i + 1, j)
        if camino: return [(i, j)] + camino

    if j > 0 and laberinto[i][j - 1] in [0, 3]:                     # Oeste
        camino = recorrido(i, j - 1) 
        if camino: return [(i, j)]+ camino

    return []



    
laberinto = creaLaberinto(stringLab)

impLab(laberinto)

#
for x in recorrido(0,0) : print(x)

