## Clases
### Disponibles
class Disponible:
    def __init__(self, bloq_asig):
        
        ## Cantidad de Bloques disponibles
        assert isinstance(bloq_asig, int) and 1 <= bloq_asig <= 75
        self.cant_bloq = bloq_asig
        
        ## Bloques Disponibles
        lista = []
        for x in range(0,bloq_asig):
            lista.append(x)
        self.bloq_disp = lista

        
    def asignaEspacio(self, bloq_sol):
        ## Bloques solicitados
        assert isinstance(bloq_sol, int) and 1 <= bloq_sol <= 75
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
        assert isinstance(tamaño, int)  and 1 <= tamaño <= 75
        assert isinstance(blocks, list) and len(blocks) == tamaño
        #assert color
        self.nombre = nombre
        self.tamamaño = tamaño
        self.blocks = blocks
        self.color = color

        
    def aumentarEspacio(self, addblocks):
        assert isinstance(addblocks, list)
        self.blocks.append(addblocks)

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
        self.directorio.append(a_archivo)

    def existeArchivo(self, e_archivo):
        if e_archivo in self.directorio:
            return True
        else:
            return False

    def borrarArchivo(self, b_archivo):
        if b_archivo in self.directorio:
            self.directorio.remove(b_archivo)
        else:
            return "Archivo sin coincidencia o no existente"

        

        

