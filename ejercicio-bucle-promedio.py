#coding=utf8

# Inicializaciones
salir = "N"
total= 0
contador= 0
promedio= 0
numero=(input("Introduzca un numero:"))

while ( salir=="N" ):
    # Hago cosas
    if (numero != -1):
        numero=(input("Introduzca otro numero:"))
        total= total + numero
        contador= contador + 1
        promedio= total/contador
        
    
    
    # Incremento
    
    
    
    
    # Activo indicador de salida si toca
    if ( numero == -1 ): # Condición de salida
        salir = "S"
print "El promedio de los numeros es= ", promedio

