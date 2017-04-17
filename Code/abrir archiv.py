
##    f = open("Tablap.txt")
##    linea = f.readline()
##    elements = []
##    while linea:
##        #print(linea)
##        elements.append([linea[:-1]])
##        linea = f.readline()
##    f = f.close()
##    return elements,

##elements = info_elements()
##i=0
##while i <= len(elements)-1:
##    if "Oro" == elements[i][-1]:
##        print(elements[i][-1], ":)")
##    else :
##        print(":(", elements[i][-1])
##    i += 1

#p[i][-1][-1]
def info_elements():
    f = open("Tablap.txt")
    lista = f.readlines()
    self.tabla = {}
    for linea in lista:
        if linea:
            linea = linea[:-1].split(";")
            e = Elemento(linea[0], linea[1], int(linea[2]), float(linea[3]),
                            int(linea[4]), int(linea[5]), int(linea[6]))

            self.tabla[linea[1]] = e
