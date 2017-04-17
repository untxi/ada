tabla={}

def principal ():
    equipo=input("Equipo : ")
    while equipo and equipo != " ":
        tabla[equipo] = {"PJ":0,"PG":0,"PP":0,"Puntos":0}
        equipo=input ("Equipo : ")
    print("*** Resultados ***")
    linea = input(" ")
    while linea and linea != " ":
        proceselinea(linea)
        linea = input (" : ")
    print (tabla)
    

if __name__ == "__main__":
    principal()


def proceselinea(linea):
    if linea == " ":
        print(tabla)
    else:
        partes = descomponga (linea)
        print(partes)


def descompnga(linea):
    lista = linea.split()
    lista[1], lista[3] = int(lista [1]),int(lista[3])
    return lista

def registremarcador(puntos):
    equipo1 = partes[0]
    equipo2 = partes[2]
    golesE1 = partes[1]
    golesE2 = partes[3]

    if golesE1 == golesE2:
        tabla[equipo1]["PJ"]+=1
        tabla[equipo2]["PJ"]+=1
        tabla[equipo1]["PE"]+=1
        tabla[equipo2]["PE"]+=1
        tabla[equipo1]["Puntos"]+=1
        tabla[equipo2]["Puntos"]+=1



    elif golesE1 > golesE2: ##gano equipo 1
        tabla[equipo1]["PJ"]+=1
        tabla[equipo2]["PJ"]+=1
        tabla[equipo1]["PG"]+=1
        tabla[equipo2]["PP"]+=1
        tabla[equipo1]["Puntos"]+=3
        
        

    else:
        tabla[equipo1]["PJ"]+=1
        tabla[equipo2]["PJ"]+=1
        tabla[equipo1]["PP"]+=1
        tabla[equipo2]["PG"]+=1
        tabla[equipo1]["Puntos"]+=3
    
    
    
















##{"Catago":{"PJ":1,"PG":1,"PP":0,"Puntos":3},"Saprissa":{"PJ":1,"PG":1,"PP":7,"Puntos":0}
