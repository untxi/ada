##--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.-##
##
## Programa: Menú_ArMoon.py
## Autores : Arburola León, Samantha
##           Rojas Alfaro,  Luis
## Fecha   : 02.04.2014
##
##     Los  Patrones Armoon  son representaciones mediante figuras
## especiales de números en binario (1`s y 0`s). Se rellenan según
## a  la  especificación  numeral  del  usuario  y  mediante  este
## programa también se permite la suma de ellos.
##
##--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.-##

## Función: 
def sumando(num):
    """ Retorna el operando a partir de la revisión de las restricciones
        En caso de ser un dígito válido retorna el valor correpondiente,
        de lo contrario la salida será 0

        Entrada:
            número correspondiente al operando

        Salida :
            operando

        Restricciones:
            la entrada debe ser un entero positivo
    """
    assert isinstance(num, int) and num >= 0
    op = input("Ingrese el operando %d: " % num)
    op = int(op)if op.isdigit() else 0
    return op

## Función: Dibujo tipo 1 (hexagono) Patrones ArMoon    
def hexagono(contador, _6bits):
    """ Dibuja el simbolo del Patrón ArMoon
              *-----*
             ***---***
            *****-*****
            -----*-----
             ---***---
              -*****-

        Entradas:
            contador, tira de bits
        Salida  :
            impresión del patron
        Restricciones:
            contador debe ser entero positivo,
            el largo de la tira de binario debe ser 6
    """
    ## Restriciones
    assert isinstance(contador, int) and contador >= 0
    assert isinstance(_6bits, str) and len(_6bits) == 6
    
    ## Encabezado de Patrón ArMoon para cada sección de 6 binarios
    print("Patrón ArMoon No. %d  - Dec: %d  - Bin: %s" % (contador, int(_6bits, 2), _6bits))

    ## Ordenamiento de bits ArMoon
    b = ""
    i = 0
    while i <= len(_6bits)-1:
        b = _6bits[i] + b
        i += 1
    _6bits = b
        
    ## Líneas del Patrón ArMoon
    L1 = L2 = L3 = L4 = L5 = L6 = ""
    for j in range(0, 6):
        bit = _6bits[j]
        if 0 <= j <= 2:
            if j % 2 == 1:
                if bit == "0":
                    L1 += "-----"
                    L2 += "---"
                    L3 += "-"
                elif bit == "1":
                    L1 += "*****"
                    L2 += "***"
                    L3 += "*"
            elif j % 2 == 0:
                if bit == "0":
                    L1 += "-"
                    L2 += "---"
                    L3 += "-----"
                elif bit == "1":
                    L1 += "*"
                    L2 += "***"
                    L3 += "*****"
        elif 3 <= j <= 5:
            if j % 2 == 1:
                if bit == "0":
                    L4 += "-----"
                    L5 += "---"
                    L6 += "-"
                elif bit == "1":
                    L4 += "*****"
                    L5 += "***"
                    L6 += "*"
            elif j % 2 == 0:
                if bit == "0":
                    L4 += "-"
                    L5 += "---"
                    L6 += "-----"
                elif bit == "1":
                    L4 += "*"
                    L5 += "***"
                    L6 += "*****"
                    
    ## Impresión de las líneas
    print( L1.center(11, " ") + "\n" + L2.center(11, " ") + "\n" +
           L3.center(11, " ") + "\n" + L4.center(11, " ") + "\n" +
           L5.center(11, " ") + "\n" + L6.center(11, " ") + "\n")

## Función: Dubujo tipo 2 (reloj de arena) Patrones ArMoon
def arena(contador, _6bits):
    """ Dibuja el simbolo del Patrón ArMoon
              -----*-----
               ---***---
                -*****-
                *-----*
               ***---***
              *****-*****

        Entradas:
            contador, tira de bits
        Salida  :
            impresión del patron
        Restricciones:
            contador debe ser entero positivo,
            el largo de la tira de binario debe ser 6
    """
    ## Restriciones
    assert isinstance(contador, int) and contador >= 0
    assert isinstance(_6bits, str) and len(_6bits) == 6
    
    ## Encabezado de Patrón ArMoon para cada sección de 6 binarios
    print("Patrón ArMoon No. %d  - Dec: %d  - Bin: %s" % (contador, int(_6bits, 2), _6bits))

    ## Ordenamiento de bits ArMoon
    b = ""
    i = 0
    while i <= len(_6bits)-1:
        b = _6bits[i] + b
        i += 1
    _6bits = b
    
    ## Líneas del Patrón ArMoon
    L1 = L2 = L3 = L4 = L5 = L6 = ""
    for j in range(0, 6):
        bit = _6bits[j]
        if 0 <= j <= 2:
            if j % 2 == 0:
                if bit == "0":
                    L1 += "-----"
                    L2 += "---"
                    L3 += "-"
                elif bit == "1":
                    L1 += "*****"
                    L2 += "***"
                    L3 += "*"
            elif j % 2 == 1:
                if bit == "0":
                    L1 += "-"
                    L2 += "---"
                    L3 += "-----"
                elif bit == "1":
                    L1 += "*"
                    L2 += "***"
                    L3 += "*****"
        elif 3 <= j <= 5:
            if j % 2 == 0:
                if bit == "0":
                    L4 += "-----"
                    L5 += "---"
                    L6 += "-"
                elif bit == "1":
                    L4 += "*****"
                    L5 += "***"
                    L6 += "*"
            elif j % 2 == 1:
                if bit == "0":
                    L4 += "-"
                    L5 += "---"
                    L6 += "-----"
                elif bit == "1":
                    L4 += "*"
                    L5 += "***"
                    L6 += "*****"
                    
    ## Impresión de las líneas
    print( L1.center(11, " ") + "\n" + L2.center(11, " ") + "\n" +
           L3.center(11, " ") + "\n" + L4.center(11, " ") + "\n" +
           L5.center(11, " ") + "\n" + L6.center(11, " ") + "\n")
    
## Función: Impresión de Patrones ArMoon
def imprime_patron(operando):
    """ Recibe un número decimal para el cual va a realizar la
        concatenación de simbolos los cuales formaran el patrón ArMoon

        Entrada:
            número decimal 
        Salida :
            Impresión del patrón ArMoon
        Restricciones:
            la entrada debe ser entero positivo
    """
    ## Restriciones
    assert isinstance(operando, int) and operando >= 0
    
    ## Encabezado
    print("SECUENCIA S = %d  B = %s\n" % (operando, str(bin(operando))[2:]))

    ## Ciclo para imprimir los patrones del operando      
    if operando == 0:
        hexagono(1, "000000")
    else:
        i = 1
        while operando != 0:
            _6bits = operando % 64
            b, c = "", 2
            bin_bit = str(bin(_6bits))
            while c <= len(bin_bit)-1:
                b += bin_bit[c]
                c += 1
            _6bits = b
            _6bits = _6bits.zfill(6) if len(_6bits) < 6 else _6bits
               
        ## Encabezado
            print("Patrón No. %d  - Bin: %s  Dec: %d" % (i, _6bits, int(_6bits,2)))
        ## Dibujo 
            if i % 2 == 0:
                arena(i, _6bits)
            elif i % 2 != 0:
                hexagono(i, _6bits)
            operando = operando // 64
            i += 1

## Función: Sumador ArMoon
def suma_ArMoon(sumando1, sumando2):
    """ Suma dos sumandos decimales en ArMoon
        Entrada:
            sumando1 y sumando2
        Salidas:
            resultado de la sumar ArMoon en decimal
        Restricciones:
            las entradas son enteros postivo
    """
    ## Restriciones
    assert isinstance(sumando1, int) and sumando1 >= 0
    assert isinstance(sumando2, int) and sumando2 >= 0

    ## Ciclo para obtener la concatenación del resultado de la sumas
    resultado = ""
    while sumando1 or sumando2:
        result = ((sumando1 % 64) + (sumando2 % 64)) % 64
        result = bin(result)
        i, s = 2, ""
        while i <= len(result)-1:
            s += result[i]
            i += 1
        resultado = s.zfill(6) + resultado
        sumando1 //= 64
        sumando2 //= 64
    resultado = resultado if str(resultado).isdigit() else "000000"
    return int(resultado, 2)


## Función: Menú Principal
def menu():
    """ Implementar el menú para que el usuario pueda elegir la acción a realizar

        Entradas:
            Ninguna
            
        Salidas:
            Ninguna
            
        Restricciones:
            Ninguna
    """
    
    ## Presentación del programa
    print(":=" * 37)
    print(" Mosaico ArMoon ".center(74, "|"))
    print(":=" * 37 + "\n")
    instrucciones = "Para esta versión de Mosaica ArMoon tiene disponibles estos comandos\n" +\
          "1. Ingresar primer  operando\n2. Ingresar segundo operando\n" +\
          "3. Imprimir primer  operando\n4. Imprimir segundo operando\n" +\
          "5. Imprimir suma\n6. Terminar\n  ?: para ver las Instrcciones\n"
    print(instrucciones)
    
    ## Lectura de la opción
    opcion = input("OPCIÓN > ")

    ## Difinición de operandos
    operando1 = 0
    operando2 = 0

    ## Evaluación de instruacciones
    while opcion:
        if opcion == "?":        ## Mostrar las intruciones
                print("?" * 73)
                print(" Instrucciones ".center(73, "·"))
                print("?" * 73)
                print(instrucciones + "\n") 
            
        elif opcion == "6":      ## Terminar
            break

        elif opcion in ["1", "2", "3", "4", "5"]:  ## Escoger la opción del menú

            if opcion == "1":    ## Opción No. 1
                print("=:" * 37)
                print(" Primer Sumando ".center(73, "="))
                print("=:" * 37)
                num = 1
                operando1 = sumando(num)
                
            elif opcion == "2":  ## Opción No. 2
                print("=:" * 37)
                print(" Segundo Sumando ".center(73, "="))
                print("=:" * 37)
                num = 2
                operando2 = sumando(num)
                
            elif opcion == "3":  ## Opción No. 3
                print("**=" * 24)
                print(" Armoon Sumando 1 ".center(73, "-"))
                print("**=" * 24)
                imprime_patron(operando1)
                
            elif opcion == "4":  ## Opción No. 4
                print("**=" * 24)
                print(" Armoon Sumando 2 ".center(73, "-"))
                print("**=" * 24)
                imprime_patron(operando2)
                
            elif opcion == "5":  ## Opción No. 5
                print(":-" * 37)
                print(" Suma Armoon ".center(73, "·"))
                print(":-" * 37)
                resultado = suma_ArMoon(operando1, operando2)
                imprime_patron(resultado)

        opcion = input("\nOPCIÓN > ")

    print("¡Fin!")

## Programa Principal
if __name__ == "__main__":
    menu()
