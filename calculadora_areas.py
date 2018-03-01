# coding=utf8 
from math import pi

print"""Calculadora de areas"""
print"""
1) Triangulo
2) Circulo
"""
menu=(input("Introduzca que area quieres saber de una de las opciones que hay disponibles:"))

if menu == 1:
    base=(input("Introduzca la base del triangulo:"))
    altura=(input("Introduzca la altura del triangulo:"))    
    print "El area del triangulo es:", base * altura/2
    
if menu == 2:
	radio=(input("Introduzca el radio del circulo:"))
	print "El area del triangulo es:", round (pi*radio**2)
