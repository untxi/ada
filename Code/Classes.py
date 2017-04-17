##CLASES

class Rectangulo:
    def __init__(self, a, b):
        self.ancho = a
        self.largo = b
    def deme_area(self):
        return self.ancho * self.largo

##Herencia
    
#superclase
class Base:
    def __init__(self, a):
        self.nombre = a
    def deme_nombre(self):
        return self.nombre
    
#clase con herencia
class Subclase(Base):
    def __init__(self, a, b):
        Base.__init__(self, a)
        self.apellido = b
    def deme_completo(self):
        return self.nombre + "  " + self.apellido
    

##Jererquias

class ClaseA:
    def __init__(self,a,b):
        self.x1 = a
        self.x2 = b
    def m1(self):
        return self.x1 + self.x2
    def m2(self):
        return self.x1 * self.x2
    
class ClaseB(ClaseA):
    def __init__(self,a,b,c,d):
        ClaseA.__init__(self,a,b)
        self.x3 = c
        self.x4 = d
    def m2(self):
        s = 0
        for x in range(1,5):
            s+= getattr(self, "x%d" % x)
        return s
    def m3(self):
        m = 1
        for x in range(1,5):
            m*= getattr(self, "x%d" % x)
        return m
class ClaseC(ClaseB):
    def __init__(self, a,b,c,d,e,f):
        ClaseB.__init__(self, a,b,c,d)
        self.x5 = e
        self.x6 = f
    def m3(self):
        s = 0
        for x in range(1,7):
            s += getattr(self, "x%d" % x)
        return s
    def m4(self):
        m = 1
        for x in range(1,7):
            m *= getattr(self, "x%d" % x)
        return m

class Mi:
    mi = 20
    def __init__(self,a):
        self.x = a
    def suma(self):
        Mi.mi += self.x
    def deme(self):
        return Mi.mi
  #a.mi = crea una instancia del atributo.      
    
