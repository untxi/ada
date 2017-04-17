def multiplicarmatrices(A,B):

    m = len(A)
    n = len(A[0])
    R = []
    i =0
    while i < m :
        fila_r = []
        j = 0
        while j < n:
            fila_r.append(A[i][j]*B[i][j])
            j+= 1
        R.append(fila_r)
        i+= 1
    return(R)

def multiplicarmatrices2(A,B):

    """La matriz A posee m * n y B es n*l, desarrollar la matriz C m*l"""

    c = []
    m = len(A)
    n = len(B)
    l = len(B[0])
    i =0


    while i < m :
        
        fila_i = []
        j = 0
        
        while j < l:

            s = 0
            k = 0
            while k < n:

                s+= A[i][k]+B[k][j]
                k+= 1
                
            fila_i.append(s)
            j+= 1

        c.append(fila_i)
        i+= 1
    return(c)
    

mat= [[2,5],[8,4]]
mat2= [[6,9],[7,14]]
mat3= [[2,3,5],[8,2,9]]
mat4= [[2,3],[0,4],[1,2]]
print(multiplicarmatrices(mat,mat2))
print(multiplicarmatrices2(mat3,mat4))
