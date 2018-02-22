# coding=utf8 

"""Preguntamos al usuario que tipo de gasolina quiere:
-Super: Normal(1.5€), Turbo(1.55€)
-Sin plomo: Normal(1.6€), Con aditivos(sabor naranja)(1.65€)
-Diesel: Normal(1.7€), Fast&Furius(1.75€)
Luego peguntamos cuantos litros.
Le decimos el importe
gasolinera.py"""

print"""
1) Super
2) Sin plomo
3) Diesel
"""

gasolina=input("Introduzca que tipo de gasolina quieres:")



if gasolina == 1:
	
	Normal_Super=1.5
	Turbo_Super=1.55
	
	print"""
	1) Super normal
	2) Super turbo
	"""
	tipo=input("Introduzca que tipo de gasolina quieres:")
	if tipo==1:
		print "Ha selecionado gasolina Super, Normal de 1.5€ cada litro"
		Litros=input("Introduzca cuantos litros quiere de gasolina:")
		print "EL importe es:", Litros * Normal_Super,"€"		    		        
	elif tipo==2:
		print "Ha selecionado gasolina Super, Turbo de 1.55€ cada litro"
		Litros=input("Introduzca cuantos litros quiere de gasolina:")
		print "El importe es:", Litros * Turbo_Super,"€"
	else: 
		print "Opción incorrecta"
		
elif gasolina == 2:
	
	Sin_plomo=1.6
	Aditivos_Sin=1.65
	
	print"""
	1) Sin plomo
	2) Sin aditivos
	"""
	tipo_1=input("Introduzca que tipo de gasolina quieres:")	
	if tipo==1:
		print "Ha selecionado gasolina Sin plomo, Normal de 1.6€ cada litro"
		Litros=input("Introduzca cuantos litros quiere de gasolina:")
		print "El importe es:", Litros * Sin_plomo,"€"
	elif tipo==2:
	   	print "Ha selecionado gasolina Sin plomo, Aditivos de 1.65€ cada litro"
		Litros=input("Introduzca cuantos litros quiere de gasolina:")
	        print "El importe es:", Litros * Normal_Sin,"€"
	else:
	 	print "Ha cancelado su compra de gasolina"
	 	

elif gasolina == 3:
	
	Normal_Diesel=1.7
	Fast_Furius=1.75
	
	print"""
	1) Normal Diesel
	2) Fast and Furius
	"""
	tipo_2=input("Introduzca que tipo de gasolina quieres:")
	if tipo==1:
		print "Ha selecionado gasolina Diesel, Normal de 1.7€ cada litro"
		Litros=input("Introduzca cuantos litros quiere de gasolina:")
	        print "El importe es:", Litros * Normal_Diesel,"€"
	elif tipo==2:
		print "Ha selecionado gasolina Diesel, Fast&Furius de 1.75€ cada litro"
		Litros=input("Introduzca cuantos litros quiere de gasolina:")
	        print "El importe es:", Litros * Fast&Furius,"€"
	else:
		print "Ha cancelado su compra de gasolina"


else:
	print "Opción incorrecta"
