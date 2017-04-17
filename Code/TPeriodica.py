class Elemento:

    """ Esta clase permite crear elementos de la
        tabla periódica.

        Las atributos de las instancias de esta
        clase son los siguientes:

               nombre    : nombre del elemento
               simbolo   : símbolo del elemento
               nAtomico  : número atómico
               masa      : masa atómica
               grupo     : grupo a que pertenece el elemento
               periodo   : periodo del elemento
               nsQuimica : número de la serie química

        El siguiente es un ejemplo de como crear una
        instancia de esta clase.

        p = Elemento("Selenio", "Se", 34, 78.96, 16, 4, 4)

        El último argumento corresponde al número de la serie
        química.  El atributo de clase SerieQuimica asocia el
        número de la serie con el nombre respectivo.  Por lo
        tanto el Selenio es un Halógeno.

    """
    
    

    def __init__(self, nombre, simbolo, nAtomico, masa,
                 grupo, periodo, sQuimica):
        """ Constructor que permite definir un elemento
            de la tabla periodica.
            Entradas:
               nombre    : nombre del elemento
               simbolo   : símbolo del elemento
               nAtomico  : número atómico
               masa      : masa atómica
               grupo     : grupo a que pertenece el elemento
               periodo   : periodo del elemento
               nsQuimica : número de la serie química
            Salidas:
               Instancia de la clase.
            Restricciones:
               1. nombre es un string diferente de nulo.
               2. simbolo es un string de letras de tamaño máximo 3 que no puede ser
                  nulo, en donde la primera letra debe ser mayúscula.
               3. nAtomico es un entero de 1 a 117.
               4. masa atómica es un valor numérico (entero o flotante)
               5. Grupo es un entero de 0 a 18.
               6. periodo es un entero de 1 a 7.
               7. nsQuimica es un entero 0 a 9
        """
        ##1 <>
        assert isinstance(nombre, str) and nombre != "", \
               "==> Nombre del símbolo es inválido."
        ##2
        assert isinstance(simbolo, str) and 3 >= len(simbolo) >= 1 and simbolo != "" and 90 >= ord(simbolo[0]) >= 65
        ##3
        assert isinstance(nAtomico, int) and 117 >= nAtomico >= 1
        ##4
        assert isinstance(masa, int) or isinstance(masa, float)
        ##5
        assert isinstance(grupo, int) and 18 >= grupo >= 0
        ##6
        assert isinstance(periodo, int) and 7 >= periodo >= 1
        ##7
        assert isinstance(sQuimica, int) and 9 >= sQuimica >= 0

        
        self.nombre   = nombre
        self.simbolo  = simbolo
        self.nAtomico = nAtomico
        self.masa     = masa
        self.grupo    = grupo
        self.periodo  = periodo
        self.sQuimica = sQuimica

    def __repr__(self):
        """ Este método se invoca en forma automática
            cuando se imprimen instancias de esta clase o
            cuando se digita una instancia directamente en
            el shell de Python.

            El método retorna la tira que muestra el estatuto
            print o el shell.

            Ejemplos:
            En los siguientes ejemplos suponga que la variable e
            apunta a una instancia que tiene la información del
            hidrógeno.  Entonces se produce el siguiente efecto.
            
                >>> e
                Elemento -------> [Hidrógeno] 
                Símbolo  -------> [H  ] 
                Número Atómico -> [1] 
                Masa -----------> [1.0079] 
                Grupo, Periodo -> [1, 1]

                >>> print(e)
                Elemento -------> [Hidrógeno] 
                Símbolo  -------> [H  ] 
                Número Atómico -> [1] 
                Masa -----------> [1.0079] 
                Grupo, Periodo -> [1, 1]
            
        """
        tira = "Elemento -------> [%s] \n" % self.nombre + \
               "Símbolo  -------> [%-3s] \n" % self.simbolo + \
               "Número Atómico -> [%d] \n" % self.nAtomico + \
               "Masa -----------> [%3.4f] \n" % self.masa + \
               "Grupo, Periodo -> [%d, %d] \n" % (self.grupo, self.periodo) +\
               "Serie Química --> [%s] \n" % self.SerieQuimica.get(self.sQuimica)
        return tira 


    SerieQuimica = { 0 : "Actínidos",
                     1 : "Alcalino",
                     2 : "Alcalinotérreos",
                     3 : "Gases Nobles",
                     4 : "Halógenos",
                     5 : "Lantánidos",
                     6 : "Metales de transición",
                     7 : "Metales del bloque p",
                     8 : "Metaloides",
                     9 : "No metales" }
    
    def perteneceSerie(self, sQuimica):
        """ Verifica si la instancia pertenece a la serie
            química indicada por sQuimica.
            Entradas:
                sQ : número de serie química para la cual
                     se desea verificar si el elemento
                     pertenece o no.
            Salidas:
                True si pertenece, False en caso contrario.
            Restricciones:
                sQ es un entero en el rango de 0 a 9.
        """
        assert isinstance(self.sQuimica, int) and 9 >= self.sQuimica >= 0

        f = open("Tablap1.txt")
        lista = f.readlines()
        self.tabla = {}
        for linea in lista:
            if linea:
                linea = linea[:-1].split(";")
                e = (linea[1], int(linea[2]), float(linea[3]),
                             int(linea[4]), int(linea[5]), int(linea[6]))
                self.tabla = {linea[0]: e}
                
        return self.tabla
        
    
class TablaElementos:
    """ Esta clase permite implementar un diccionario de elementos
        químicos.
        La instancia se crea a partir de un archivo por medio del
        constructor de la clase.
        Las instancias solo tienen un atributo que corresponde al diccionario.
        Este diccionario tiene como llave el símbolo de un elemento y
        como valor una instancia de la clase Elemento.
    """

    def __init__(self, archivo):
        """ Constructor de la clase.
            Entradas:
                archivo : nombre del archivo que contiene
                          información de elementos de la tabla
                          periodica.

                El formato de este archivo es el siguiente:
                - Por cada elemento de la tabla periodica se
                  incluye una línea.
                - La información de los elementos viene separada
                  por punto y coma.
                - Los campos son:
                       nombre    : nombre del elemento
                       simbolo   : símbolo del elemento
                       nAtomico  : número atómico
                       masa      : masa atómica
                       grupo     : grupo a que pertenece el elemento
                       periodo   : periodo del elemento
                       nsQuimica : número de la serie química

            Salidas :
                instancia de la clase.
            Restricciones:
                archivo es un string y existe un archivo
                con ese nombre.
            Supuestos:
                El archivo tiene extensión .csv y los valores
                vienen separados por punto y coma.
        """
        assert isinstance(archivo, str)

        try:
            f = open(archivo)
        except:
            raise FileNotFoundError("El archivo [" + archivo + "] no existe.")

        lista = f.readlines()

        self.tabla = {}
        for linea in lista:
            if linea:
                linea = linea[:-1].split(";")
                e = Elemento(linea[0], linea[1], int(linea[2]), float(linea[3]),
                             int(linea[4]), int(linea[5]), int(linea[6]))
                self.tabla[linea[1]] = e
            
    def imprima(self, sQuimica):
        """ Imprime los elementos de la tabla periodica pertenecientes
            a una serie química.
            Entradas:
                sQuima : número de la serie química.
            Salidas:
                Reporte con los elementos de la serie química.
            Restricciones:
                sQuimica es un entero entre 0 y 9. 
        """
        SerieQuimica = { 0 : "Actínidos",
                     1 : "Alcalino",
                     2 : "Alcalinotérreos",
                     3 : "Gases Nobles",
                     4 : "Halógenos",
                     5 : "Lantánidos",
                     6 : "Metales de transición",
                     7 : "Metales del bloque p",
                     8 : "Metaloides",
                     9 : "No metales" }
        
        print("SERIE QUÍMICA : ", SerieQuimica.get(sQuimica))
        print("No.  Nombre               Simbolo   #Atómico   Masa Atómica  Grupo   Periodo")
        print("---  ---------------      -------   --------   ------------  -----   -------")

        i = 0
        for x in self.tabla.keys():
            if self.tabla[x].sQuimica == sQuimica:
                print("0" * (3 - len(str(i))) + str(i), "  %-15s" % self.tabla[x].nombre,\
                      "       %-3s  " % self.tabla[x].simbolo,\
                      "   %-3d   " % self.tabla[x].nAtomico,\
                      "       %-3d     " % self.tabla[x].masa,\
                      "  %d" % self.tabla[x].grupo,\
                      "      %d" % self.tabla[x].periodo)
                i += 1

    def deme_tabla(self):
        return self.tabla
        

def seleccione(l_elem, sQuimica, ms):
    """ Retorna una lista con todos los símbolos de los
        elementos químicos que pertenecen a una serie 
        química y cuya masa sea mayor a un valor particular.
        Entradas:
            l_elem   : lista de instancias de la clase Elemento.
            sQuimica : número de la serie química.
            ms       : valor a considera para la masa.
        Salidas:
            La lista.
        Supuestos:
            Todos los parámetros son correctos.
            Esto significa que no tiene que incluir asserts.
    """
    return []

def caso(nn, param = None):
    """ Función que define los casos de
        prueba que se aplican en el examen.
    """
    if nn == 1:    

        #------------------------------------------------------------#
        print("Caso de Prueba No. 1")
        if (isinstance(param, Elemento) and param.nombre == "Oro" and \
            param.simbolo == "Au" and param.nAtomico == 79 and \
            param.masa == 196.9660 and param.grupo == 11 and \
            param.periodo == 6 and param.sQuimica == 6):
            print("==> Caso Exitoso / Obtuvo 5 puntos del examen")
        else:
            print("==> Caso Fallido / Revise que haya indicado los argumentos correctos")
        #------------------------------------------------------------#

    elif nn == 2:  
        
        #------------------------------------------------------------#
        print("Caso de Prueba No. 2")
        ## Crea un elemento - el Selenio indicando su
        ## símbolo, número atómico (34), masa atómica (78.96),
        ## grupo (16), periodo (4) y número de serie química (5)

        p = Elemento("Selenio", "Se", 34, 78.96, 16, 4, 9)

        ## Se supone que el estudiante modificó el código
        ## del método __repr__.  Ahora la impresión incluye el
        ## nombre de la serie química.
        ## Llame el profesor para que vea el resultado del print.

        print(p)
        #------------------------------------------------------------#
        
    elif nn == 3:

        #------------------------------------------------------------#
        print("Caso de Prueba No. 3")
        Elemento("Plata",1,47,107.8682,11,5,6)
        #------------------------------------------------------------#

    elif nn == 4:

        #------------------------------------------------------------#
        print("Caso de Prueba No. 4")
        Elemento("Plata","ag",47,107.8682,11,5,6)
        #------------------------------------------------------------#

    elif nn == 5:

        #------------------------------------------------------------#
        print("Caso de Prueba No. 5")
        Elemento("Plata","Argentum",47,107.8682,11,5,6)
        #------------------------------------------------------------#

    elif nn == 6:

        #------------------------------------------------------------#
        print("Caso de Prueba No. 6")
        Elemento("Plata","Ag",47,107.8682,20,5,6)
        #------------------------------------------------------------#

    elif nn == 7:

        #------------------------------------------------------------#
        print("Caso de Prueba No. 7")
        Elemento("Plata","Ag",147,107.8682,11,5,6)
        #------------------------------------------------------------#

    elif nn == 8:

        #------------------------------------------------------------#
        print("Caso de Prueba No. 8")
        p = Elemento("Selenio", "Se", 34, 78.96, 16, 4, 9)
        if p.perteneceSerie(9):
            print("==> Caso Exitoso / Obtuvo 5 puntos del examen")
        else:
            print("==> Caso Fallido / Revise su código")
        #------------------------------------------------------------#

    elif nn == 9:    

        #------------------------------------------------------------#
        print("Caso de Prueba No. 9")
        if isinstance(param, TablaElementos):
            print("==> Caso Exitoso / Obtuvo 5 puntos del examen")
            param.imprima(0)
        else:
            print("==> Caso Fallido / Revise que haya indicado el argumento correcto")
        #------------------------------------------------------------#

    elif nn == 10:

        #------------------------------------------------------------#
        print("Caso de Prueba No. 10")
        if isinstance(param, TablaElementos) and \
           param.tabla["Ac"].nombre == "Actinio" and \
           param.tabla["Ac"].nAtomico == 89:
            print("==> Caso Exitoso / Obtuvo 5 puntos del examen")
        else:
            print("==> Caso Fallido / Revise que haya modificado bien el archivo")
        #------------------------------------------------------------#

    elif nn == 11:

        #------------------------------------------------------------#
        print("Caso de Prueba No. 11")
        print("Debe imprimir los Gases Nobles !! - El argón es uno de ellos ...")
        param.imprima(3)
        #------------------------------------------------------------#

    elif nn == 12:

        #------------------------------------------------------------#
        print("Caso de Prueba No. 12")
        print(seleccione(param, 6, 270))  ## ["Hs", "Rg", "Uup"]
        #------------------------------------------------------------#
        

                    
        



    
