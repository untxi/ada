def pruebaMenor(lista):
    ## RESTRICCIÓN: lista de números enteros
    for x in lista:
        if not isinstance(x, int):
            return False

    ## RESTRICCIÓN: orden ascendente
    m = i = 0
    while i <= len(lista)-1:
        if m > lista[i]:
            return False
        else:
            m = lista[i]
            fin = True
        i += 1
    return fin
