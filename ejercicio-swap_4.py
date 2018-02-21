# coding=utf8

""""
cajon1=1     cajon1=3     ///cajon1=3   cajon3=1  cajon_extra=3
cajon2=2     cajon2=4     ///cajon2=4   cajon4=2  cajon_extra=2
cajon3=3     cajon3=1
cajon4=4     cajon4=2
"""


cajon1=(input("Introduzca un numero:"))
cajon2=(input("Introduzca un numero diferente al primero:"))
cajon3=(input("Introduzca un numero diferente al primero y al segundo:"))
cajon4=(input("Introduzca un numero diferente al resto:"))

cajon_extra=cajon3
cajon3=cajon1
cajon1=cajon_extra
cajon_extra=cajon4
cajon4=cajon2
cajon2=cajon_extra

print cajon1
print cajon2
print cajon3
print cajon4
