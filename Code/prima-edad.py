##################################
## PROGRAMA:        Rango de Edades
##
## Autor:           Jean Paul Velluti
##
## Fecha:           8/7/13
##
## Seguro de vida por edad de años
##
## Entrada:         Edad de la persona
##
## Salida:          Monto a pagar.
##
## Restricciones:   Edad y Millones son numeros enteros   
##
###################################

## Entrada

x=int(input("Digite la edad: "))
y=int(input("Digite los millones que quiera: "))

## Desarrollo

if (x < 10):
    prima = y * 4200
if (x >= 10) and (x < 16):
    prima = y * 5300
if (x >= 16) and (x < 21):
    prima = y * 7420
if (x >= 21) and (x < 35):
    prima = y * 8400
if (x >= 35) and (x < 45):
    prima = y * 9100
if (x >= 45):
    prima = y * 15100

## Salida    
print ("El monto a pagar es de ",prima)
        
        
    
