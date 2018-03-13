# coding=utf8 

"""CONVERTIDOR DE CM A KM, M Y CM"""

distancia=(input("Introduzca una distancia en centimetros:"))
cm=distancia
resto= cm % 100
m=distancia % 100000 / 100
km=cm / 100000


if km:
	if m or resto:
		print distancia, "centimetros son:", km, "km"
	else:
		print distancia, "centimetros son:", km, "km"

if m:
	if resto:
		print distancia, "centimetros son:", m, "m"
	else:
		print distancia, "centimetros son:", m, "m"


if cm == 0 or resto:
	print distancia, "centimetros son:", resto, "cm"
		
"""print distancia, "centimetros son:", cm, "cm", m, "m", km, "km" """
