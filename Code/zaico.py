
def inicio():
    var = input('ingrese su nombre:')
    comparar_num(var)
    
def comparar_num(numero):
    if int(numero) == 1:
        print ('Uno')
    elif int(numero) == 2:
        print ('Dos')
    elif int(numero) == 3:
        print ('Tres')
    elif int(numero) == 4:
        print ('Cuatro') 
    elif int(numero) == 5:
        print ('Cinco')
    else:
        print ('no conozco ese numero')
	
finalizar()
	
	
def finalizar():
	var_terminar =input('terminar? 1.si 2.no')
	if(var_terminar	== 2):
		inicio()
 
inicio() 
