## Clases
### Disponibles
class Disponible:
    def __init__(self, blocks):
        ## Cantidad de Bloques disponibles
        assert isinstance(blocks, int) and 1 <= blocks
        self.cant_bloq = blocks
        ## Bloques Disponibles
        lista = []
        for x in range(0,blocks):
            lista.append(x)
        self.bloq_disp = lista

    def lista(self):
        return self.bloq_disp

    def asignaEspacio(self, bloq_sol):
        ## Bloques solicitados
        assert isinstance(bloq_sol, int) and 1 <= bloq_sol <= self.cant_bloq
        self.bloq_sol = bloq_sol
        dis = len(self.bloq_disp)
        sol = self.bloq_sol
        if sol > dis:
            raise AssertionError ("NOT ENOUGH MEMORY BLOCKS")
        else:
            lista_sol = self.bloq_disp[0:sol]
            self.bloq_disp = self.bloq_disp[sol:]
        return lista_sol

    def devolver(self, bloq_dev):
        ## Devolución de Bloques
        assert isinstance(bloq_dev, list)
        self.bloq_dev = bloq_dev
        for x in self.bloq_dev:
            self.bloq_disp.append(x)
        ##return self.bloq_disp

    def reiniciar(self):
        self.cant_bloq = 0
        self.bloq_disp = []
        

### Archivo
class Archivo:
    def __init__(self, nombre, tamaño, blocks, color):
        assert isinstance(nombre, str)
        assert isinstance(tamaño, int)
        assert isinstance(blocks, list) and len(blocks) == tamaño
        assert isinstance(color, str) 
        self.nombre = nombre
        self.tamaño = tamaño
        self.blocks = blocks
        self.color = color

    def aumentarEspacio(self, addblocks):
        assert isinstance(addblocks, list)
        self.blocks.append(addblocks)

    def obtenerNombre(self):
        return self.nombre

    def obtenerBloques(self):
        return self.blocks

    def obtenerColor(self):
        return self.color

    def obtenerTamaño(self):
        return self.tamaño

### Directorio
    
class Directorio:
    def __init__(self):
        self.directorio = []

    def agregarArchivo(self, a_archivo):
        assert isinstance(a_archivo, Archivo)
        ## Propiedades del archivo
        self.directorio.append(a_archivo)

    def list_direc(self):
        return self.directorio

    def existeArchivo(self, e_archivo):
        for archi in self.directorio:
            if e_archivo in archi:
                return True
            else:
                return False

    def borrarArchivo(self, b_archivo):
        if b_archivo in self.directorio:
            self.directorio.remove(b_archivo)
        else:
            return "Archivo sin coincidencia o no existente"


##==========================================================================##
instrucciones = "Los mandatos que puede ejecutar son las siguientes:\n" + \
          "Tenga en cuenta que el simbolo "'_'" representa un espacio en blanco,\n" +\
          ""'nnn'" representa un número entero, "'nom'" el nombre del archivo,\n" +\
          ""'tam'" el tamaño en bloques y el color debe ingresarlo en el formato #RRGGBB\n"+\
          "- Digite             --> Para \n" +\
          "    F_nnn                nnn debe ser un multiplo de 5\n" +\
          "    L                    Muestra una lista de archivos existentes\n" +\
          "    C_nom_tam_color      Crear un archivo\n" +\
          "    E_nom_tam            Expandir el tamaño del archivo\n" +\
          "    R_nom                Borrar el archivo\n" +\
          "    M                    Muestra el mapa de uso del espacio\n"

ejm  =  "   COMANDOS         EJEMPLO\n" +\
        "    F_nnn           --> F_100\n" +\
        "    L               --> L\n" +\
        "    C_nom_tam_color --> C_libro_34_#RRGGBB\n" +\
        "    E_nom_tam       --> E_libro_34\n" +\
        "    R_nom           --> R_libro\n" +\
        "    M               --> M\n"

titulo = "="*70 + "\n" + " " * 33 + "2013" + "\n" + " " * 22 +\
         "Administrador de Archivos" + "\n" + "="*70 + "\n" +\
         "="*70 + "\n" + "Para   recibir   asistencia   digite:   INSTRUCCIONES    ó    EJEMPLOS\n"+\
         "="*70 + "\n" + "="*70 + "\n"


##=========================================================================##
memoria = Disponible(200)
blk_d = memoria.lista()
directorio = Directorio()
t =Archivo("nom", 3, [1,2,3], "#445566")
list_direc = [t]

def Format(blocks):
    global memoria, blk_d, directorio
    memoria = Disponible(blocks)
    blk_d = memoria.lista()
    directorio = Directorio()

def lista_archivos():
    lista = list_direc
    print("=" * 12 + "||" + "=" * 8 + "||" + "=" * 9 + "\n" +\
          "---NOMBRE---||-TAMAÑO-||--COLOR--\n")
    if lista == []:
        print("SIN ARCHIVOS EN MEMORIA")
    else:
        for x in lista:
            print("%-12s||" % x.obtenerNombre(), " %-6d||" % x.obtenerTamaño(), "%s" % x.obtenerColor())

def crear(nom, tam, color):
    global blk_d
    blk_d = memoria.lista()
    if tam <= len(blk_d):
        blocks = blk_d[:len(tam)-1]
        nom = Archivo(nom, tam, blocks, color)
        directorio.agregarArchivo(nom)
    else:
        return "MEMORIA INSUFICIENTE"
    

def expand(nom, tam):
    global blk_d, directorio
    blk_d = memoria.lista()
    if tam <= len(blk_d):
        for x in directorio:
            if x == nom:
                x[0].tamaño += tam
                x[0].blocks += blk_d[:len(tam)-1]
            else:
                return "ARCHIVO NO ENCONTRADO"
    else:
        return "MEMORIA INSUFICIENTE"
    

def remove(nom):
    for x in directorio:
            if x == nom:
                directorio.remove(nom)
            else:
                return "ARCHIVO NO ENCONTRADO"

def Mapa():
    pass


def principal():
    """ Función que evalua cual mandato se ejecutará
        Entradas      : mandato
        Salidas       : Ninguna
        Restricciones : Ninguna
    """
    print(titulo)

    comando = str(input("--> "))
    while comando:
        ini = comando[0]
        if comando == "EJEMPLOS":
            print(ejm)
            
        elif comando == "INSTRUCCIONES":
            print(instrucciones)
            
        elif ini == "F":
            blocks = int(comando[1:])
            if blocks%5 != 0:
                print("Cantidad no Aceptable. Ingrese un multiplo de 5")
                comando
            else:
                Format(blocks)
            
        elif ini == "L":
            lista_archivos()

        elif ini == "C":

            linea = str(comando)
            linea = list(linea.split())

            nom   = linea[1]
            tam   = linea[2]
            color = linea[3]
            
            tam = int(tam)
            crear(nom, tam, color)
            
        elif ini == "E":
            
            linea = str(comando)
            linea = list(linea.split())

            nom   = linea[1]
            tam   = linea[2]
                
            tam = int(tam)
            expand(nom, tam)
                        
        elif ini == "R":
            nom = comando[1:]
            assert isinstance(nom, Archivo)
            remove(nom)
        
        elif ini == "M":
            Mapa()
           
        else:
            print("ERROR DE COMANDO")
        
        comando = str(input("--> "))
    print("Fin de la edición")

    
if __name__ == "__main__":
	principal()
