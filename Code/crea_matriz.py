def sonenteros(mat):

    """    La función son enteros permite determinar si la matriz
           posee numeros enteros.

           Entradas:

               mat : Matriz declarada por el usuario.
          Salida:

              La función retorna true si todos los elementos son enteros.

          Restricciones:

              Ninguna.
    """
    
    m = len(mat)
    
    i=0
    while i < m:
        j = 0
        n= len(mat[i])
        while j < n and isinstance(mat[i][j],int) :

            j+= 1
           

        i+= 1
    return(i == m and j == n )

def matrizordenn(n):
    
    assert isinstance(n,int) and n >= 1
    matr = []
    x = 0

    for x in range(n):

        fila = [0 for j in range(n)]
        matr.append(fila)
        
            
    return(matr)
def mat_0(n):

    mat= []
    for i in range(n):
        mat.append([0 for j in range(n)])
    return mat

def mat_00(n):

    mat= []
    fila = [0 for j in range(n)]
    for i in range(n):
        mat.append(fila)
    return mat

mat= [[1,2,3],["1","2","3"]]
print(sonenteros(mat))
n = int(input("Digite un numero."))
n = n if isinstance(n,int) and n >= 1 else 1

print(matrizordenn(n))



def identidad(n):
    m  = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(m if i == j else 0)
        m.append(fila)
    return m


def sumacolumnas(mat):
    """    La función suma columnas permite determinar la suma de la matriz.
           Entradas:
               mat : Matriz declarada por el usuario.
          Salida:
              La función retorna true si todos los elementos son enteros.
          Restricciones:
              Ninguna.
    """
    
    m = len(mat)
    s= 0
    lista= []
    j=0
    while j < len(mat[0]):
        s = 0
        i = 0
        while i < m and isinstance(mat[i][j],int) :
            s=  s + mat[i][j]
            i+= 1
        j+= 1
        lista.append(s)   
    return(lista)


def sumafilas(mat):
    """    La función suma filas permite determinar la suma de la matriz.
           Entradas:
               mat : Matriz declarada por el usuario.
          Salida:
              La función retorna true si todos los elementos son enteros.
          Restricciones:
              Ninguna.
    """
    
    m = len(mat)
    s= 0
    lista= []
    i=0
    while i < m:
        j = 0
        s = 0
        n= len(mat[i])
        while j < n and isinstance(mat[i][j],int) :
            s= s+ mat[i][j]
            j+= 1
        lista.append(s)
        i+= 1
    return(lista)

def sumafilas2(mat):
    lista = []
    for i in range (len(mat)):
        lista.append(sum(mat[i]))
    return(lista)

def sumafilas3(mat):
    return[sum(x) for x in mat]


def sumamatrices(mat, mat2):
    """    La función suma matrices permite determinar la suma de dos matrices.
           Entradas:
               mat : Matriz declarada por el usuario.
          Salida:
              La función retorna true si todos los elementos son enteros.
          Restricciones:
              Ninguna.
    """
    
    m = len(mat)
    n = len (mat[0])
    s= 0
    matriz= []
    lista = []
    for i in range(m):
        for j in range(n):
            s = mat[i][j] + mat2[i][j]
            lista.append(s)
        matriz.append(lista)      
    return(matriz)

def sumamatrices2(A,B):
    m = len(A)
    n = len(A[0])
    R = []
    i =0
    while i < m :
        fila_r = []
        j = 0
        while j < n:
            fila_r.append(A[i][j]+B[i][j])
            j+= 1
        R.append(fila_r)
        i+= 1
    return(R)
