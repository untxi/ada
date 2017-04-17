def decimal_entero(numero):
    if numero == int(numero):
        return numero
    else:
        if numero > int(numero):
            numero= numero * 10
        return decimal_entero(numero)
    
def cuenteDigitos(n):
    if n <10:
        return 1
    else:
        return 1 + cuenteDigitos(n//10)
    
from math import *

def invierte(numero):
    return invertir(numero,cuenteDigitos(numero))


def invertir(numero,cantidadDigitos):
        if numero  < 10:
            return numero
        else:
            return numero % 10 * 10**(cantidadDigitos-1)+invertir(numero//10,cantidadDigitos-1)

def inv_num(x):
    x=int(input("digite el numero que quiera invertir: " ) )
    y = str(x%10)+str(x//10%10)+str(x//100)
    return(int(y))

def uso_raiz():
    from math import*
    a = float(input("digite el valor a : "))
    b = float(input("digite el valor b : "))
    c = float(input("digite el valor c : "))
    x1 = -b+(sqrt(b**2)-((4*a)*c))/2*a

    return ("el resultado de x1 es: ", x1)

def MCM(m,n):
    fp = (m if m < n else n)
    p, r = next(fp), 1
    while p != 1:
        while m % p == 0 and n % p == 0:
            m //= p
            n //= p
            r *= p
        p = next(fp)
    return r



## potencia mas pequeña o igual a N

n=int(input("Digite el numero "))
p=1
bits=0
while p<=n:
    p*=2
    bits+=1

print(bits)

