####################################################################
#
# Programa: tiempo de una ciudad a otra
# Autor: 
# Fecha: 14-2-13
#
# El programa indicara con base en velocidad y distancia el tiempo que se tardara de una ciudad a otra.
#
# Entradas: v- velocidad d-distancia
#Salidas: t-tiempo
#restricciones: expresion en km/h
#
###################################################################

#Lectura de valores de entrada

d= int(input ( "distancia " ))
v= int( input ( " velocidad" ))

#Calculo de tiempos

tiempo = ( d / v ) * 60

#imprimiir

print ( " el tiempo transcurrido es de : " , tiempo )

 

 
 
